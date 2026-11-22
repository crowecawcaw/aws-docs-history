

# Optimizing startup time for GPU-accelerated functions

GPU-accelerated functions typically package GPU libraries such as CUDA alongside ML frameworks, which can add several gigabytes to a container image. Some functions also load artifacts such as model weights, rendering assets, or reference data, often gigabytes in size, before they can serve their first request. Both add time between the moment Lambda provisions an execution environment and the moment your function is ready to handle invocations. This page explains what contributes to that time and how to shorten it by optimizing the container image, lazy-loading it with Seekable OCI, sizing `/tmp`, and loading large artifacts from Amazon S3.

## Startup time breakdown
<a name="lambda-managed-instances-gpu-startup-breakdown"></a>

Before a new execution environment can handle an invocation, Lambda launches a GPU instance if all running GPU instances are at capacity, pulls your container image, and runs your initialization code. As a general best practice, put artifact loading, framework imports, and other one-time setup in your initialization code rather than in the handler. That way, it runs when the execution environment starts and not on every invocation. For the full sequence, see [Understanding the Lambda Managed Instances execution environment](lambda-managed-instances-execution-environment.md). GPU-accelerated functions spend more time than other Event Functions on Lambda Managed Instances in two of these steps:
+ **Container image pull** – Lambda downloads your image layers from Amazon ECR and unpacks them to local storage before it starts the container. GPU images are often several gigabytes, so this step usually dominates startup time. Unpacking is CPU-heavy and can take longer than the download itself. Lambda downloads image layers concurrently and unpacks each one as soon as it arrives, so spreading content across several layers instead of concentrating it in one large layer shortens this step.
+ **Initialization** – Lambda runs your initialization code before the execution environment handles its first invocation. For a GPU workload, this typically includes importing your framework, initializing CUDA, and downloading and loading the artifacts your workload needs, such as model weights into GPU memory or scene assets into `/tmp`.

## Set appropriate timeouts
<a name="lambda-managed-instances-gpu-startup-timeouts"></a>
+ **Account for initialization time.** – On Lambda Managed Instances, the initialization timeout is the maximum of 130 seconds or the configured function timeout, up to 900 seconds (15 minutes). If your initialization code downloads and loads large artifacts, set the function timeout high enough to cover it, and keep the initialization itself under 15 minutes. Publishing a function version starts execution environments, so long initialization also delays the version reaching the `Active` state. The vLLM and SGLang base images apply a second limit: they wait `VLLM_SERVER_TIMEOUT` or `SGLANG_SERVER_TIMEOUT` seconds (600 by default) for the inference server to become ready, independent of the function timeout. For a model that takes longer to load, raise this variable to just under the function timeout. For more information about the execution environment lifecycle, see [Execution environment lifecycle for Lambda Managed Instances](lambda-managed-instances-execution-environment.md).
+ **Configure the function timeout for the first invocation.** – If your handler downloads or loads artifacts on the first invocation instead of in initialization code, set the function timeout high enough to cover that load on top of your normal invocation duration. For the timeout limits by invocation type, see [Configure Lambda Event Function timeout](configuration-timeout.md).

## Optimize your container image
<a name="lambda-managed-instances-gpu-startup-image"></a>

GPU-accelerated functions support container images up to 32 GB, compared with 10 GB for other Event Functions. The higher limit lets you package the GPU frameworks and CUDA libraries these workloads require. However, a larger image means longer download duration on every new execution environment. Within the image, a single file can be at most 10 GB. If the image contains a larger file, publishing the function version fails during activation. If a model checkpoint or other artifact is larger than 10 GB, split it into multiple files, or keep it out of the image and load it at initialization time. The following practices keep the image pull short.
+ **Keep large artifacts out of the image.** – Package your code, dependencies, and framework in the image. Load model weights, rendering assets, and other large data from Amazon S3 at initialization time instead, either by downloading them into `/tmp` or by streaming them directly into memory with the S3 connector for PyTorch or the Run:ai Model Streamer. This keeps the image small, lets you change artifacts without rebuilding the image, and removes the largest files from the image pull path. The Lambda vLLM and SGLang base images follow this pattern: you set the model with the `MODEL_ID` environment variable, and the image loads the model during initialization, so the load happens when you publish the function version rather than on the first invocation. For more information about loading large artifacts and the GPU base images, see [Load large artifacts from Amazon S3](#lambda-managed-instances-gpu-startup-s3) and [GPU base images](lambda-managed-instances-gpu-base-images.md).
+ **Start from the smallest base image that works for you.** – Choose the smallest Lambda base image that works for your application. For the list of available images, see [GPU base images](lambda-managed-instances-gpu-base-images.md).
+ **Spread content across layers.** – Lambda downloads several image layers concurrently and unpacks each layer, a CPU-heavy step, as soon as its download completes. An image whose content is concentrated in a single very large layer pulls more slowly than the same content split across several layers. This is because the large layer must finish downloading before its unpacking can begin, and no other layer unpacks in the meantime. Every `COPY`, `ADD`, and `RUN` instruction in a Dockerfile produces one layer, so split large instructions rather than combining them. For example, if you package sharded model weights, copy each shard with its own instruction instead of copying the directory in one instruction:

  ```dockerfile
  # One layer that holds every shard
  COPY models/ /opt/models/
  
  # One layer per shard: shards download concurrently, and each unpacks as soon as it arrives
  COPY models/model-00001-of-00004.safetensors /opt/models/
  COPY models/model-00002-of-00004.safetensors /opt/models/
  COPY models/model-00003-of-00004.safetensors /opt/models/
  COPY models/model-00004-of-00004.safetensors /opt/models/
  ```

  Do not flatten the image into a single layer, for example by exporting the container file system and importing it as a new image. Put the content that changes least, such as weights, in earlier layers and your handler code in the last layer. That way, a rebuild reuses the cached layers and pushes only the small top layer.

## Store large artifacts in /tmp
<a name="lambda-managed-instances-gpu-startup-tmp"></a>

GPU-accelerated functions can configure up to 32 GB of ephemeral storage in `/tmp`, compared with 10 GB for other Event Functions. Artifacts that your initialization code downloads, such as rendering assets or a model in a format that no streaming tool reads, are written here. Downloading them at initialization time instead of packaging them in the image keeps the image pull short, and a `/tmp` sized for the artifacts lets you keep them out of the image whatever their size. Model weights that a streaming tool reads directly into memory do not need `/tmp` at all; see [Load large artifacts from Amazon S3](#lambda-managed-instances-gpu-startup-s3).

You configure the size of `/tmp` with the `EphemeralStorage` setting of your function. Size it for the artifacts your initialization code downloads. For more information, see [Configure ephemeral storage for Lambda Event Functions](configuration-ephemeral-storage.md).

**Note**  
`/tmp` is the only writable directory in the execution environment. Its contents persist for the lifetime of the execution environment and are available to every invocation that runs in it. You cannot pre-populate `/tmp` in your Dockerfile, because it is not visible at image build time.

The Lambda PyTorch base image sets `TORCH_HOME` to a path under `/tmp` so that PyTorch's default model cache works without code changes. If you use a different framework or a different base image, set the framework's cache directory yourself. For example:

```dockerfile
ENV TORCH_HOME=/tmp/torch
```

## Use SOCI to lazy-load your image
<a name="lambda-managed-instances-gpu-startup-soci"></a>

Seekable OCI (SOCI) lets an execution environment start before the whole container image has been downloaded. Lambda Managed Instances fetches only the files your function reads, when it reads them, instead of downloading and unpacking the full image first. GPU images often include large libraries and assets that a given function never reads. As a result, lazy loading reduces the time to first invocation and makes startup time much less sensitive to total image size. SOCI applies to all container image functions on Lambda Managed Instances. For how it works, how to create a SOCI index for your image, and its limitations, see [Lazy-load container images with Seekable OCI (SOCI)](lambda-managed-instances-seekable-oci.md).

## Load large artifacts from Amazon S3
<a name="lambda-managed-instances-gpu-startup-s3"></a>

Downloading an artifact to `/tmp` and then loading it into memory adds the write to and read from local storage as overhead on top of the download. For model weights, stream them from Amazon S3 directly into memory instead, using the tools described in this section. Other artifacts, such as rendering assets or reference data, have no streaming tool; download them to `/tmp` with the AWS SDK at initialization time and size `EphemeralStorage` for them as described in the previous section.
+ **Use the S3 connector for PyTorch.** – The Lambda PyTorch base image includes `s3torchconnector`, which streams weights from Amazon S3 into CPU memory using the AWS Common Runtime, with no intermediate write to `/tmp`.

Use streaming when:
+ **Your model is large.** – Streaming avoids the local storage overhead of the download-then-load pattern. The benefit grows with model size.
+ **Your model is larger than your configured `/tmp`.** – Streaming is the only option when the weights do not fit on disk.

### Example: stream model weights at initialization
<a name="lambda-managed-instances-gpu-startup-s3-example"></a>

The following example loads a PyTorch state dictionary from Amazon S3 in the initialization code, outside the handler, and moves the model to the GPU there. Each worker process in the execution environment runs the initialization code and holds its own copy of the model. As a result, the S3 read happens once per worker process rather than on every invocation. For more information, see [Concurrency within an execution environment](lambda-managed-instances-gpu-scaling.md#lambda-managed-instances-gpu-scaling-concurrency).

```python
import os
import torch
from s3torchconnector import S3Checkpoint

MODEL_URI = "s3://amzn-s3-demo-bucket/models/model.pt"

# Initialization code: stream the weights into CPU memory once per worker process.
checkpoint = S3Checkpoint(region="us-west-2")
with checkpoint.reader(MODEL_URI) as reader:
    state_dict = torch.load(reader, map_location="cpu", weights_only=True)

model = MyModel()
model.load_state_dict(state_dict)
model.eval()
model.to("cuda")

def handler(event, context):
    with torch.inference_mode():
        return run_inference(model, event)
```

For comparison, the download-then-load pattern looks like this:

```python
import boto3, torch

s3 = boto3.client("s3", region_name="us-west-2")
s3.download_file("amzn-s3-demo-bucket", "models/model.pt", "/tmp/model.pt")
state_dict = torch.load("/tmp/model.pt", map_location="cpu", weights_only=True)
```

Place the S3 bucket in the same AWS Region as your function to minimize network latency when you load the weights. Your function's execution role needs `s3:GetObject` permission on the objects it reads. If you use the connector's dataset classes to read every object under a prefix, the role also needs `s3:ListBucket` permission on the bucket.
+ **Stream weights into vLLM and SGLang.** – The Lambda vLLM and SGLang base images include the Run:ai Model Streamer, which streams safetensors shards from Amazon S3 directly into GPU memory. By default the images download the model to `/tmp`; streaming removes that copy and the `/tmp` sizing that goes with it.

Stage the model in S3 as safetensors. Put the \*.safetensors shards, `config.json`, and the tokenizer files under an S3 prefix in the same Region as the function:

```bash
huggingface-cli download Qwen/Qwen2.5-1.5B-Instruct --local-dir ./model
aws s3 sync ./model s3://amzn-s3-demo-bucket/models/Qwen2.5-1.5B-Instruct/
```

Set the following environment variables on the function:

```
MODEL_ID=s3://amzn-s3-demo-bucket/models/Qwen2.5-1.5B-Instruct/
VLLM_LOAD_FORMAT=runai_streamer
SERVED_MODEL_NAME=qwen2.5-1.5b-instruct
```

Grant access and a network path. The function's execution role needs `s3:GetObject` and `s3:ListBucket` on the prefix; the streamer uses the function's credentials. The capacity provider's VPC needs a route to Amazon S3 through a gateway VPC endpoint or a NAT gateway.

For more information about streaming into vLLM and SGLang, see the [vLLM documentation](https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer/) on the vLLM website and the [SGLang documentation](https://lmsysorg.mintlify.app/docs/advanced_features/object_storage) on the SGLang website. For more information about the base images, see [GPU base images](lambda-managed-instances-gpu-base-images.md).