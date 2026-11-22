

# GPU base images for Lambda Managed Instances

Lambda provides container base images that you can use to build GPU-accelerated functions on Lambda Managed Instances. Each image includes the CUDA runtime libraries, the framework the image is named for (such as PyTorch, vLLM, or SGLang) with its dependencies, and the [Lambda runtime interface client](runtimes-open-source.md#open-source-ric).

**Note**  
Lambda's GPU base images maintain compatibility with the NVIDIA GPU drivers on the instances. We recommend building your GPU-accelerated functions from these images unless your workload uses a language or framework that they do not provide.

## Available images
<a name="lambda-managed-instances-gpu-base-images-available"></a>

Lambda publishes the GPU base images in the [Amazon ECR Public Gallery](https://gallery.ecr.aws/lambda) at `public.ecr.aws/lambda/deep-learning-containers/<framework>:<tag>`.


| Image | Framework : Tag | What's included | 
| --- | --- | --- | 
| Base | base:cuda | CUDA toolkit | 
| CuPy | cupy:cuda | CuPy, CUDA toolkit | 
| PyTorch | pytorch:cuda | PyTorch, cuDNN, torchvision, FFmpeg, s3torchconnector, CUDA toolkit | 
| vLLM | vllm:cuda | vLLM inference server, PyTorch, Transformers, s3torchconnector, CUDA toolkit | 
| SGLang | sglang:cuda | SGLang inference server, PyTorch, Transformers, s3torchconnector, CUDA toolkit | 

## Base
<a name="lambda-managed-instances-gpu-base-images-base"></a>

The `base:cuda` image is a minimal image that includes the CUDA toolkit and the Lambda Python runtime. Use this image when you use custom CUDA kernels or frameworks that Lambda's other base images don't include (such as GROMACS or Blender). The following Dockerfile shows how to add your own packages to `base:cuda`.

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/base:cuda

RUN dnf install -y gcc gcc-c++ cmake make && dnf clean all
RUN pip install --no-cache-dir your-custom-package

WORKDIR /var/task
COPY handler.py .
CMD ["handler.handler"]
```

## CuPy
<a name="lambda-managed-instances-gpu-base-images-cupy"></a>

The `cupy:cuda` image is meant for GPU-accelerated numerical computing with a NumPy-compatible interface. Use the CuPy image for workloads that benefit from GPU-accelerated array operations and don't need a full ML framework. Common use cases include scientific computing, signal processing, and financial modeling. The following Dockerfile shows how you can add a custom handler to this base image.

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/cupy:cuda

WORKDIR /var/task
COPY handler.py .
CMD ["handler.handler"]
```

The following handler code uses CuPy to perform Monte Carlo option pricing.

```python
import cupy as cp
import math

def handler(event, context):
  # Option parameters from the request
  spot = event.get("spot_price", 100.0)
  strike = event.get("strike_price", 105.0)
  rate = event.get("risk_free_rate", 0.05)
  volatility = event.get("volatility", 0.2)
  expiry = event.get("years_to_expiry", 1.0)
  n_simulations = event.get("simulations", 10_000_000)

  # Monte Carlo simulation on GPU
  z = cp.random.standard_normal(n_simulations, dtype=cp.float32)
  price_at_expiry = spot * cp.exp(
      (rate - 0.5 * volatility ** 2) * expiry + volatility * math.sqrt(expiry) * z
  )

  # European call option payoff
  payoffs = cp.maximum(price_at_expiry - strike, 0)
  call_price = float(cp.exp(-rate * expiry) * cp.mean(payoffs))

  # European put option payoff
  put_payoffs = cp.maximum(strike - price_at_expiry, 0)
  put_price = float(cp.exp(-rate * expiry) * cp.mean(put_payoffs))

  return {
      "call_price": round(call_price, 4),
      "put_price": round(put_price, 4),
      "simulations": n_simulations,
      "spot": spot,
      "strike": strike,
  }
```

## PyTorch
<a name="lambda-managed-instances-gpu-base-images-pytorch"></a>

The `pytorch:cuda` image can be used for general-purpose ML inference with PyTorch and CUDA, such as image classification, object detection, speech synthesis, and diffusion models, or for LLM inference where you need full control over the model pipeline. The following example performs image classification using mobilenet. The example Dockerfile installs the model weights at build time. Building the weights into the image suits small models that change infrequently, like the one in this example. For large models, or models that you update often, stream the weights from Amazon S3 at initialization instead of building them into the image, which keeps the image small and lets you change the model without rebuilding it. For more information about optimizing startup time, see [Optimizing startup time for GPU-accelerated functions](lambda-managed-instances-gpu-startup.md).

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/pytorch:cuda

# Download weights at build time so the function has no runtime internet dependency
RUN python3 -c "from torchvision import models; models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)" \
    && cp /tmp/torch/hub/checkpoints/mobilenet_v2-7ebf99e0.pth /var/task/mobilenet_v2.pth
RUN curl -s https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt -o /var/task/imagenet_classes.txt

WORKDIR /var/task
COPY handler.py .
CMD ["handler.handler"]
```

The sample handler code is shown below:

```python
import torch
import io
import base64
import os
from torchvision import models, transforms
from PIL import Image

model = models.mobilenet_v2()
model.load_state_dict(torch.load("/var/task/mobilenet_v2.pth", map_location="cpu", weights_only=True))
model.eval()
preprocess = models.MobileNet_V2_Weights.DEFAULT.transforms()

model.cuda()

with open("/var/task/imagenet_classes.txt") as f:
  labels = f.read().strip().split("\n")

def handler(event, context):
  img_bytes = base64.b64decode(event["image_base64"])
  img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
  tensor = preprocess(img).unsqueeze(0).cuda()

  with torch.inference_mode():
      output = model(tensor)

  probs = torch.softmax(output, dim=1)[0]
  top5 = probs.topk(5)

  return {
      "predictions": [
          {"label": labels[idx], "confidence": round(prob.item(), 4)}
          for prob, idx in zip(top5.values, top5.indices)
      ]
  }
```

## vLLM
<a name="lambda-managed-instances-gpu-base-images-vllm"></a>

### Integration with pre-trained models
<a name="lambda-managed-instances-gpu-base-images-vllm-integration"></a>

The `vllm:cuda` image is meant for serving large language models behind an OpenAI-compatible API. Use it for chat, completion, and embedding workloads where you want the server to handle batching and GPU memory management for you. The image includes the vLLM framework, which you can use to serve models directly without writing code to load the model, batch requests, or manage GPU memory. Configure the `MODEL_ID` environment variable to point to your model on the local file system, in an Amazon S3 bucket, or in a Hugging Face or ModelScope repository. When retrieving models from Hugging Face, we recommend that you authenticate with the `HF_TOKEN` environment variable for higher download rate limits and to access private or gated models. By default, the image serves Qwen/Qwen2.5-0.5B-Instruct.

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/vllm:cuda
```

To use a different model, update the `MODEL_ID` environment variable on the function and publish a new function version. You don't need to rebuild the image.

```bash
aws lambda update-function-configuration \
    --function-name my-gpu-function \
    --environment 'Variables={MODEL_ID=Qwen/Qwen2.5-1.5B-Instruct,HF_TOKEN=<your-hugging-face-token>}'
```

**Note**  
`update-function-configuration` replaces the entire environment-variable map, so include any variables you already set (for example `VLLM_LOAD_FORMAT`).

The image starts the vLLM server during initialization and checks its health while the execution environment runs. If the server exits or fails three consecutive health checks, Lambda replaces the execution environment.

The image automatically handles model downloading, GPU memory management, and serving. Invoke payloads follow an OpenAI-compatible format. For text models, supply an input like the following:

```json
{
  "prompt": "Explain quantum computing in one sentence.",
  "max_tokens": 256
}
```

### Model Streaming and Ephemeral Storage
<a name="lambda-managed-instances-gpu-base-images-vllm-streaming"></a>

For production workloads, we recommend copying models to an S3 bucket in the same Region as your capacity provider and loading them from there. This avoids cross-Region data transfer costs and downloads faster than the Hugging Face Hub.

```bash
huggingface-cli download Qwen/Qwen2.5-1.5B-Instruct --local-dir ./model
aws s3 sync ./model s3://amzn-s3-demo-bucket/models/Qwen2.5-1.5B-Instruct/
```

You can then refer to your S3 prefix in the `MODEL_ID` environment variable. By default, the `vllm:cuda` image downloads models to `/tmp`. We recommend that you stream models directly to memory using an additional environment variable.

```bash
aws lambda update-function-configuration \
    --function-name my-gpu-function \
    --environment 'Variables={MODEL_ID=s3://amzn-s3-demo-bucket/models/Qwen2.5-1.5B-Instruct/,VLLM_LOAD_FORMAT=runai_streamer}'
```

Alternatively, you can increase your `EphemeralStorage` storage setting.

### Custom handlers
<a name="lambda-managed-instances-gpu-base-images-vllm-custom-handlers"></a>

To use a pretrained model with custom business logic, you can provide your own handler code. Your handler code should load the model into memory once while creating multiple Python processes to serve multi-concurrent requests. For more information about customizing request handling, see [Customize request handling with your own handler](lambda-managed-instances-gpu-inference.md#lambda-managed-instances-gpu-inference-custom-handler).

## SGLang
<a name="lambda-managed-instances-gpu-base-images-sglang"></a>

The `sglang:cuda` image, like the `vllm:cuda` image, includes a built-in model serving framework that requires no code. It provides structured generation capabilities and efficient prefix caching via RadixAttention. Use it for LLM workloads that benefit from structured output (JSON mode, regex-constrained generation), multi-turn conversations with prefix sharing, or fine-grained generation control.

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/sglang:cuda
```

Like the vLLM image, configure it with environment variables.

```bash
aws lambda update-function-configuration \
    --function-name my-gpu-function \
    --environment 'Variables={MODEL_ID=Qwen/Qwen2.5-1.5B-Instruct,HF_TOKEN=<your-hugging-face-token>}'
```

**Note**  
`update-function-configuration` replaces the entire environment-variable map, so include any variables you already set.

When overriding the default handler, the same handler pattern applies to the `sglang:cuda` image. The image starts the SGLang server during initialization; your handler forwards requests to `http://127.0.0.1:8000`, the same pattern as the vLLM custom handler. Use the `SGLANG_*` environment variables (`SGLANG_MEM_FRACTION`, `SGLANG_ATTENTION_BACKEND`, `SGLANG_SERVER_ARGS`) in place of the `VLLM_*` ones.

## Build your own base image
<a name="lambda-managed-instances-gpu-base-images-build-your-own"></a>

A GPU-accelerated function can run a container image built from any base image, in any language, as long as the image meets the following requirements:
+ **Runtime interface client** – The image must include a Lambda runtime interface client that supports multi-concurrent execution on Lambda Managed Instances. The image's `ENTRYPOINT` and `CMD` must start it with your handler. For the supported clients and how to add one to an image, see [Lambda Managed Instances runtimes](lambda-managed-instances-runtimes.md) and [Create a Lambda Event Function using a container image](images-create.md).
+ **CUDA runtime libraries** – Install a CUDA 13.x or earlier runtime and framework versions that match it. To use a newer CUDA version, bundle the matching `cuda-compat` package in the image. You do not need to install an NVIDIA driver within your base image as Lambda installs and maintains these on the GPU instances in your capacity provider. For more information about CUDA compatibility, see [CUDA Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/latest/) in the NVIDIA documentation.
+ **Writable paths** – `/tmp` is the only writable directory in the execution environment. Point any cache your framework writes at runtime, such as a kernel cache, to a path under `/tmp`.