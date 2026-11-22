

# Run media and graphics workloads on GPU-accelerated functions

The GPUs in the instance families supported by Lambda Managed Instances include hardware video encode and decode engines (NVENC and NVDEC) and support OpenGL and Vulkan rendering. These engines are separate from the CUDA cores, so a transcoding or rendering function uses the GPU without any CUDA code. This page shows a video transcoding function that uses the hardware encoder and decoder, and a rendering function that uses OpenGL without a display. Each example assumes you already have a GPU capacity provider. The resources you create in these examples might result in charges to your AWS account. For more information about GPU support and base images, see [GPU support for Lambda Managed Instances](lambda-managed-instances-gpu.md) and [GPU base images](lambda-managed-instances-gpu-base-images.md).

A codec is the format in which a video stream is compressed, such as H.264, HEVC, or AV1. NVDEC decodes compressed video into frames and NVENC encodes frames into compressed video. The codecs each engine handles depend on the GPU generation:


| GPU (instance families) | Decode | Encode | 
| --- | --- | --- | 
| T4 (G4dn) | H.264, HEVC | H.264, HEVC | 
| A10G (G5) | H.264, HEVC, AV1 | H.264, HEVC | 
| L4 (G6, Gr6, G6f, Gr6f) | H.264, HEVC, AV1 | H.264, HEVC, AV1 | 
| L40S (G6e) | H.264, HEVC, AV1 | H.264, HEVC, AV1 | 

For the full list, including VP9 and older codecs, see the [NVIDIA video encode and decode GPU support matrix](https://developer.nvidia.com/video-encode-decode-support-matrix) on the NVIDIA website.

The GPU base images are published in the Lambda public ECR gallery at `public.ecr.aws/lambda/deep-learning-containers/<framework>:<tag>`, for example `public.ecr.aws/lambda/deep-learning-containers/pytorch:cuda-v1`. The examples on this page pin the `cuda-v1` tag of the PyTorch and base images, which tracks the latest 1.x release of each image. For the available images and tags, see [GPU base images](lambda-managed-instances-gpu-base-images.md). The examples push the images you build to your own Amazon ECR repository in us-east-2. Replace it with the Region you build in.

Use non-fractional GPU instance types for media and rendering functions. On fractional GPU instance types (G6f and Gr6f), the encoder, decoder, and graphics engines are shared with the other instances on the same physical GPU, so the throughput of your function varies with their load. On the other supported instance families, each execution environment has the whole GPU and its engines to itself. Both examples request 16 GB of accelerator memory, which places them on a whole GPU.

## Example 1: Transcode video with the GPU encoder and decoder
<a name="lambda-managed-instances-gpu-media-transcode"></a>

In this example, you build a function that downloads a video file from Amazon S3, decodes it with NVDEC, re-encodes it to H.264 with NVENC, and uploads the result. The function runs FFmpeg, which performs the decoding and encoding with the GPU engines selected. The PyTorch base image includes FFmpeg built with NVIDIA hardware acceleration, so no installation is needed. The example expects H.264 or HEVC source video files. For a source codec that NVDEC does not decode, such as ProRes, FFmpeg decodes on the CPU and only the encode runs on the GPU, so the invocation takes longer. For the codecs each GPU decodes, see [the codec support table](#lambda-managed-instances-gpu-media-codec-table).

**Note**  
The function reads from and writes to an Amazon S3 bucket in the same Region, so its execution role needs `s3:GetObject` on the input objects and `s3:PutObject` on the output prefix, and the capacity provider's subnets need a route to Amazon S3 through a gateway endpoint or a NAT gateway.

### Step 1: Build and push the image
<a name="lambda-managed-instances-gpu-media-transcode-step1"></a>

Create a directory with the following two files.

Dockerfile:

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/pytorch:cuda-v1

COPY handler.py /var/task/
CMD ["handler.handler"]
```

handler.py:

```python
import os
import subprocess
import tempfile

import boto3

s3 = boto3.client("s3")

def handler(event, context):
    bucket = event["bucket"]
    key = event["key"]
    output_key = event.get("output_key", "output/" + os.path.basename(key))

    # Concurrent invocations in the same execution environment share /tmp, so each
    # invocation works in its own directory, which is removed when the invocation ends.
    with tempfile.TemporaryDirectory(dir="/tmp") as workdir:
        src = os.path.join(workdir, "input" + os.path.splitext(key)[1])
        dst = os.path.join(workdir, "output.mp4")

        s3.download_file(bucket, key, src)

        subprocess.run(
            [
                "ffmpeg", "-y",
                "-hwaccel", "cuda", "-hwaccel_output_format", "cuda",
                "-i", src,
                "-c:v", "h264_nvenc", "-preset", "p4", "-b:v", "5M",
                "-c:a", "aac",
                dst,
            ],
            check=True,
        )

        s3.upload_file(dst, bucket, output_key)

    return {"bucket": bucket, "output_key": output_key}
```

The handler follows these practices:
+ **Decode and encode on the GPU** – `-hwaccel cuda` decodes the input with NVDEC and `-hwaccel_output_format cuda` keeps the decoded frames in GPU memory. As a result, the frames go straight to the `h264_nvenc` encoder without a round trip through CPU memory.
+ **Use a separate working directory for each invocation** – `/tmp` is the only writable directory in the execution environment, and all concurrent invocations in that execution environment share it. A temporary directory per invocation keeps their files apart and is removed at the end, so repeated invocations do not fill the storage.
+ **Encode audio with AAC** – `-c:a aac` re-encodes the audio on the CPU; audio encoding is not GPU-accelerated. Copying the source audio unchanged with `-c:a copy` skips that work, but it produces a playable MP4 only when the source audio is already in a codec that MP4 players expect, such as AAC. Sources with PCM audio, such as ProRes or MXF masters, need the re-encode.

Build the image and push it to Amazon ECR.

Using AWS CLI:

```bash
aws ecr create-repository --repository-name my-transcode-function --region us-east-2

aws ecr get-login-password --region us-east-2 | \
  docker login --username AWS --password-stdin 111122223333.dkr.ecr.us-east-2.amazonaws.com

docker build -t my-transcode-function .
docker tag my-transcode-function:latest 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-transcode-function:v1
docker push 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-transcode-function:v1
```

### Step 2: Create the function
<a name="lambda-managed-instances-gpu-media-transcode-step2"></a>

Create a function from the image you pushed that uses your GPU capacity provider. Set ephemeral storage large enough for the input and output files, and `PerExecutionEnvironmentMaxConcurrency` to 1, so that each file has the encoder and decoder engines to itself and the first run gives you the transcode time for a single file. Step 4 raises the concurrency to process several files at once; the handler already keeps a separate working directory per invocation, so it works at both settings. The example invokes the function synchronously. For videos that take longer to transcode than a synchronous invocation allows, invoke the function asynchronously, for example from an Amazon S3 event. Set the timeout accordingly. For the timeout limits by invocation type, see [Configure Lambda Event Function timeout](configuration-timeout.md).

Using AWS CLI:

```bash
aws lambda create-function \
  --function-name my-transcode-function \
  --package-type Image \
  --code ImageUri=111122223333.dkr.ecr.us-east-2.amazonaws.com/my-transcode-function:v1 \
  --role arn:aws:iam::111122223333:role/my-transcode-function-role \
  --memory-size 8192 \
  --timeout 900 \
  --ephemeral-storage '{"Size":10240}' \
  --accelerator-config '{"AcceleratorMemorySize":16}' \
  --capacity-provider-config '{"LambdaManagedInstancesCapacityProviderConfig":{"CapacityProviderArn":"arn:aws:lambda:us-east-2:111122223333:capacity-provider:my-gpu-capacity-provider","PerExecutionEnvironmentMaxConcurrency":1,"ExecutionEnvironmentMemoryGiBPerVCpu":4}}'
```

### Step 3: Publish the function and invoke it
<a name="lambda-managed-instances-gpu-media-transcode-step3"></a>

Publish the function to `$LATEST.PUBLISHED` and wait for it to become `Active`.

Using AWS CLI:

```bash
aws lambda publish-version --function-name my-transcode-function --publish-to LATEST_PUBLISHED

aws lambda get-function-configuration \
  --function-name my-transcode-function \
  --qualifier '$LATEST.PUBLISHED' \
  --query State
```

When the state is Active, invoke the function with the bucket and key of your sample video.

```bash
aws lambda invoke \
  --function-name my-transcode-function \
  --cli-binary-format raw-in-base64-out \
  --payload '{"bucket":"amzn-s3-demo-bucket","key":"input/sample.mp4"}' \
  response.json

cat response.json
aws s3 ls s3://amzn-s3-demo-bucket/output/
```

The transcoded file is at output/sample.mp4.

**Note**  
The GPUUtilization and ExecutionEnvironmentGPUUtilization metrics measure activity on the GPU's compute cores. The encoder and decoder are separate engines, so a transcoding function keeps these metrics low even while it is fully using NVENC and NVDEC. Use the function's Duration metric to understand transcoding throughput.

### Step 4: Transcode files in parallel
<a name="lambda-managed-instances-gpu-media-transcode-step4"></a>

Raise `PerExecutionEnvironmentMaxConcurrency` to 4 and republish `$LATEST.PUBLISHED` so that one execution environment processes four files at a time. The encoder and decoder engines take work from concurrent sessions through hardware queues, so concurrency does not multiply encoding throughput linearly. How much it adds depends on the number of encoder engines on the GPU: the T4 (G4dn) and A10G (G5) have one, the L4 (G6, Gr6, G6f, and Gr6f) has two, and the L40S (G6e) has three. Concurrency also overlaps the download, upload, and CPU work of some invocations with the encoding of others. This raises engine utilization and shortens the total time for a batch.

Using AWS CLI:

```bash
aws lambda update-function-configuration \
  --function-name my-transcode-function \
  --capacity-provider-config '{"LambdaManagedInstancesCapacityProviderConfig":{"CapacityProviderArn":"arn:aws:lambda:us-east-2:111122223333:capacity-provider:my-gpu-capacity-provider","PerExecutionEnvironmentMaxConcurrency":4,"ExecutionEnvironmentMemoryGiBPerVCpu":4}}'

aws lambda publish-version --function-name my-transcode-function --publish-to LATEST_PUBLISHED
```

Each concurrent invocation runs its own FFmpeg process, so size MemorySize and ephemeral storage for the number of files processed at once. Every worker also initializes the handler module, including the AWS SDK client, before the version becomes Active. A higher concurrency setting therefore needs more memory for initialization even when the invocations themselves are small.

The GPUs in the supported instance families are data center GPUs, which do not limit the number of concurrent encoder sessions. The ceiling on how many files one execution environment transcodes at a time is the throughput of its encoder and decoder engines and the CPU work around them. The ceiling is not a session count.

### Clean up
<a name="lambda-managed-instances-gpu-media-transcode-cleanup"></a>

Delete the function, then delete the capacity provider if you no longer need it.

Using AWS CLI:

```bash
aws lambda delete-function --function-name my-transcode-function
aws lambda delete-capacity-provider --capacity-provider-name my-gpu-capacity-provider
```

## Example 2: Render an image with OpenGL without a display
<a name="lambda-managed-instances-gpu-media-render"></a>

In this example, you build a function that renders a frame with OpenGL on the GPU and writes it to Amazon S3 as a PNG. The function has no display attached, so it creates its OpenGL context through EGL directly on the GPU device. The same approach applies to any renderer or game engine that can target EGL, and to Vulkan applications, which need no display server either. The function writes to an Amazon S3 bucket in the same Region, so its execution role needs `s3:PutObject` permission on the bucket. The capacity provider's subnets need a route to Amazon S3 through a gateway endpoint or a NAT gateway.

### Step 1: Build and push the image
<a name="lambda-managed-instances-gpu-media-render-step1"></a>

Create a directory with the following two files. The image starts from the base image, which contains the Lambda runtime and CUDA libraries but no ML framework. It adds the OpenGL dispatch library and the Python bindings.

Dockerfile:

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/base:cuda-v1

RUN dnf install -y libglvnd-egl libglvnd-opengl libX11 && dnf clean all
RUN pip install --no-cache-dir PyOpenGL numpy pillow boto3

# PyOpenGL defaults to the GLX platform on Linux. Select EGL so that it resolves
# EGL entry points through eglGetProcAddress and needs no X server.
ENV PYOPENGL_PLATFORM=egl

COPY handler.py /var/task/
CMD ["handler.handler"]
```

handler.py:

```python
import io
import os

import boto3
import numpy as np
from OpenGL import EGL, GL
from OpenGL.EGL.EXT.device_base import eglQueryDevicesEXT
from OpenGL.EGL.EXT.platform_base import eglGetPlatformDisplayEXT
from OpenGL.EGL.EXT.platform_device import EGL_PLATFORM_DEVICE_EXT
from OpenGL.raw.EGL._types import EGLDeviceEXT
from PIL import Image

WIDTH, HEIGHT = 1024, 1024
s3 = boto3.client("s3")
_context_pid = None

def create_context():
    # Enumerate GPUs as EGL devices and open the first one, without a display server.
    devices = (EGLDeviceEXT * 8)()
    num_devices = EGL.EGLint()
    eglQueryDevicesEXT(8, devices, num_devices)
    if num_devices.value == 0:
        raise RuntimeError("No EGL devices found")
    display = eglGetPlatformDisplayEXT(EGL_PLATFORM_DEVICE_EXT, devices[0], None)
    if not EGL.eglInitialize(display, None, None):
        raise RuntimeError(f"eglInitialize failed: {hex(EGL.eglGetError())}")

    config_attribs = np.array([
        EGL.EGL_SURFACE_TYPE, EGL.EGL_PBUFFER_BIT,
        EGL.EGL_RENDERABLE_TYPE, EGL.EGL_OPENGL_BIT,
        EGL.EGL_RED_SIZE, 8, EGL.EGL_GREEN_SIZE, 8, EGL.EGL_BLUE_SIZE, 8,
        EGL.EGL_NONE,
    ], dtype=np.int32)
    configs = (EGL.EGLConfig * 1)()
    num_configs = EGL.EGLint()
    EGL.eglChooseConfig(display, config_attribs, configs, 1, num_configs)
    if num_configs.value == 0:
        raise RuntimeError("No matching EGL config")

    surface_attribs = np.array([EGL.EGL_WIDTH, WIDTH, EGL.EGL_HEIGHT, HEIGHT, EGL.EGL_NONE], dtype=np.int32)
    surface = EGL.eglCreatePbufferSurface(display, configs[0], surface_attribs)
    EGL.eglBindAPI(EGL.EGL_OPENGL_API)
    context = EGL.eglCreateContext(display, configs[0], EGL.EGL_NO_CONTEXT, None)
    if not EGL.eglMakeCurrent(display, surface, surface, context):
        raise RuntimeError(f"eglMakeCurrent failed: {hex(EGL.eglGetError())}")


def ensure_context():
    # An EGL context belongs to the process that created it. Create one in each
    # worker process on its first invocation and reuse it afterwards.
    global _context_pid
    if _context_pid != os.getpid():
        create_context()
        _context_pid = os.getpid()


def handler(event, context):
    ensure_context()

    # Draw a color gradient triangle.
    GL.glViewport(0, 0, WIDTH, HEIGHT)
    GL.glClearColor(0.1, 0.1, 0.1, 1.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glBegin(GL.GL_TRIANGLES)
    GL.glColor3f(1.0, 0.0, 0.0); GL.glVertex2f(-0.8, -0.8)
    GL.glColor3f(0.0, 1.0, 0.0); GL.glVertex2f(0.8, -0.8)
    GL.glColor3f(0.0, 0.0, 1.0); GL.glVertex2f(0.0, 0.8)
    GL.glEnd()
    GL.glFinish()

    pixels = GL.glReadPixels(0, 0, WIDTH, HEIGHT, GL.GL_RGB, GL.GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGB", (WIDTH, HEIGHT), pixels).transpose(Image.FLIP_TOP_BOTTOM)

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    key = event.get("output_key", "renders/frame.png")
    s3.upload_fileobj(buffer, event["bucket"], key)
    return {"bucket": event["bucket"], "output_key": key, "renderer": GL.glGetString(GL.GL_RENDERER).decode()}
```

The handler follows these practices:
+ **Create the OpenGL context once per worker process** – An EGL context belongs to the process that creates it. The handler therefore creates the context on the first invocation in each worker process and reuses it for later invocations. The `_context_pid` check creates a new context if the handler runs in a process that does not own one. With `PerExecutionEnvironmentMaxConcurrency` set to 1 there is a single worker process, and the context is created once per execution environment.
+ **Enumerate the GPU through the EGL device extensions** – EGL\_EXT\_device\_enumeration and EGL\_EXT\_platform\_device give a display for the GPU itself. No X server or Wayland compositor is involved. The EGL pbuffer surface takes the place of a window.
+ **Check the renderer** – The response includes GL\_RENDERER, which names the GPU when hardware rendering is active, for example NVIDIA L4/PCIe/SSE2. If it names a software renderer such as llvmpipe, the GPU is not being used.

Build the image and push it to Amazon ECR.

Using AWS CLI:

```bash
aws ecr create-repository --repository-name my-render-function --region us-east-2

aws ecr get-login-password --region us-east-2 | \
  docker login --username AWS --password-stdin 111122223333.dkr.ecr.us-east-2.amazonaws.com

docker build -t my-render-function .
docker tag my-render-function:latest 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-render-function:v1
docker push 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-render-function:v1
```

### Step 2: Create the function
<a name="lambda-managed-instances-gpu-media-render-step2"></a>

Using AWS CLI:

```bash
aws lambda create-function \
  --function-name my-render-function \
  --package-type Image \
  --code ImageUri=111122223333.dkr.ecr.us-east-2.amazonaws.com/my-render-function:v1 \
  --role arn:aws:iam::111122223333:role/my-render-function-role \
  --memory-size 4096 \
  --timeout 60 \
  --accelerator-config '{"AcceleratorMemorySize":16}' \
  --capacity-provider-config '{"LambdaManagedInstancesCapacityProviderConfig":{"CapacityProviderArn":"arn:aws:lambda:us-east-2:111122223333:capacity-provider:my-gpu-capacity-provider","PerExecutionEnvironmentMaxConcurrency":1,"ExecutionEnvironmentMemoryGiBPerVCpu":4}}'
```

### Step 3: Publish the function and invoke it
<a name="lambda-managed-instances-gpu-media-render-step3"></a>

Using AWS CLI:

```bash
aws lambda publish-version --function-name my-render-function --publish-to LATEST_PUBLISHED

aws lambda get-function-configuration \
  --function-name my-render-function \
  --qualifier '$LATEST.PUBLISHED' \
  --query State
```

When the state is Active, invoke the function and download the rendered frame.

```bash
aws lambda invoke \
  --function-name my-render-function \
  --cli-binary-format raw-in-base64-out \
  --payload '{"bucket":"amzn-s3-demo-bucket"}' \
  response.json

cat response.json
aws s3 cp s3://amzn-s3-demo-bucket/renders/frame.png .
```

The response names the GPU in the renderer field, for example {"bucket": "amzn-s3-demo-bucket", "output\_key": "renders/frame.png", "renderer": "NVIDIA L4/PCIe/SSE2"}, and frame.png shows a color gradient triangle.

### Clean up
<a name="lambda-managed-instances-gpu-media-render-cleanup"></a>

Delete the function, then delete the capacity provider if you no longer need it.

Using AWS CLI:

```bash
aws lambda delete-function --function-name my-render-function
aws lambda delete-capacity-provider --capacity-provider-name my-gpu-capacity-provider
```