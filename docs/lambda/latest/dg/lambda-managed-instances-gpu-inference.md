

# Run inference workloads on GPU-accelerated functions

This page shows how to run model inference on GPU-accelerated functions with the vLLM or SGLang base image. You first deploy a model with the default handler and invoke it through the server's OpenAI-compatible API. The quickest way to try an image is to point it at a model on a third-party source (such as the Hugging Face Hub). The examples then switch to loading the model from Amazon S3, which is the configuration to use for production functions. You then replace the default handler with your own on the same function to add request validation and prompt templating while keeping one inference server per execution environment.

## Prerequisites
<a name="lambda-managed-instances-gpu-inference-prerequisites"></a>

Before you begin, make sure that you have the following:
+ A GPU capacity provider, an execution role for the function, and Docker and the AWS CLI installed. For instructions on creating a capacity provider, see [Getting started](lambda-managed-instances-gpu-getting-started.md).
+ At least one GPU instance type in your capacity provider that can provide the 12 GB of accelerator memory and 16,384 MB of system memory that the examples request, such as `g4dn.2xlarge` or larger (for example, `g6.2xlarge`).
+ The GPU base images, which are published in the Lambda public ECR gallery at `public.ecr.aws/lambda/deep-learning-containers/<framework>:<tag>`, for example `public.ecr.aws/lambda/deep-learning-containers/vllm:cuda`. The examples on this page use the 1.x release of each image, indicated by the `cuda-v1` tag on the image. For the available images and tags, see [GPU base images](lambda-managed-instances-gpu-base-images.md).
+ An Amazon ECR repository in the Region you build in. The examples push the images you build to a repository in `us-east-2`; replace it with the Region you build in.

For more information about GPU-accelerated functions, see [GPU support for Lambda Managed Instances](lambda-managed-instances-gpu.md) and [GPU base images](lambda-managed-instances-gpu-base-images.md).

## Serve a model with vLLM or SGLang
<a name="lambda-managed-instances-gpu-inference-serve"></a>

Use the vLLM or SGLang base image to serve a model using an OpenAI-compatible API without writing handler code. Each image packages the inference server and a default handler. When an execution environment starts, the image starts the server once during initialization, and every worker process forwards its invocations to that server over local HTTP. One copy of the model serves all concurrent invocations in the execution environment, and the server batches them. The image checks the server's health while the execution environment runs; if the server exits or stops answering, Lambda replaces the execution environment. You set the model with one environment variable and deploy.

### Choose where the model loads from
<a name="lambda-managed-instances-gpu-inference-model-source"></a>

The simplest way to use a model is to point `MODEL_ID` at a Hugging Face model ID. The image downloads the model from the Hugging Face Hub to `/tmp` during initialization, which requires outbound internet access from the capacity provider's subnets and enough `EphemeralStorage` for the model:

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/vllm:cuda-v1

ENV MODEL_ID=Qwen/Qwen2.5-1.5B-Instruct
```

If you point `MODEL_ID` at a Hugging Face model ID, we recommend that you also set `HF_TOKEN` to raise your download rate limit and to access private or gated models. `HF_TOKEN` is a secret, so set it as a function environment variable rather than baking it into the image. For production, store it in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) and read it in your initialization code instead of passing it in plaintext.

```bash
aws lambda update-function-configuration \
  --function-name my-gpu-function \
  --environment 'Variables={MODEL_ID=Qwen/Qwen2.5-1.5B-Instruct,HF_TOKEN=<your-hugging-face-token>}'
```

Pointing `MODEL_ID` at a Hugging Face model ID is fine for a first test, but not for a production function. A Hugging Face download crosses the internet, depends on the Hub's speed and your NAT gateway, and repeats on every new execution environment, which slows scale-out. The rest of this page loads the model from an S3 bucket in the same Region as the function instead. Copy the model to your bucket once:

```bash
hf download Qwen/Qwen2.5-1.5B-Instruct --local-dir ./model
aws s3 sync ./model s3://amzn-s3-demo-bucket/models/Qwen2.5-1.5B-Instruct/
```

The function's execution role needs `s3:GetObject` and `s3:ListBucket` on the S3 prefix path, and the capacity provider's VPC needs a route to Amazon S3 through a gateway VPC endpoint or a NAT gateway.

### Configuring your Dockerfile
<a name="lambda-managed-instances-gpu-inference-serve-dockerfile"></a>

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/vllm:cuda-v1
```

The image's entry point starts the Lambda runtime interface client, and its default `CMD` names the image's default handler, so the Dockerfile needs only the `FROM` line. Set `MODEL_ID` and `VLLM_LOAD_FORMAT` as function environment variables ([Step 2](#lambda-managed-instances-gpu-inference-serve-create-function)) rather than baking them into the image, so you can change them without rebuilding. `VLLM_LOAD_FORMAT=runai_streamer` reads a model in safetensors format tensor by tensor into GPU memory. With a model in Amazon S3, the weights go straight from Amazon S3 into GPU memory, no `/tmp` space is needed for the model, and the write to and read from local storage are skipped, which matters for models of several gigabytes. With a model ID from a third-party source, vLLM downloads the repository to `/tmp` first, whatever the load format, so size `EphemeralStorage` for the model. Leave `VLLM_LOAD_FORMAT` unset for a model that is not in safetensors format; vLLM then downloads it to `/tmp` and loads it from there. In both cases the load happens when you publish the function version, before the version becomes `Active`. To switch models, update `MODEL_ID` in the function's environment variables and publish a new version. No image rebuild is needed.

### Step 1: Build and push the image
<a name="lambda-managed-instances-gpu-inference-serve-build-push"></a>

Create your GPU function image as shown below:

Using AWS CLI:

```bash
aws ecr create-repository --repository-name my-gpu-function --region us-east-2

aws ecr get-login-password --region us-east-2 | \
  docker login --username AWS --password-stdin 111122223333.dkr.ecr.us-east-2.amazonaws.com

docker build -t my-gpu-function .
docker tag my-gpu-function:latest 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-gpu-function:v1
docker push 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-gpu-function:v1
```

### Step 2: Create the function
<a name="lambda-managed-instances-gpu-inference-serve-create-function"></a>

Create a function on your GPU capacity provider from the image you pushed to Amazon ECR. Set `AcceleratorMemorySize` to 12 GB in `AcceleratorConfig`, `MemorySize` to 16,384 MB, and `ExecutionEnvironmentMemoryGiBPerVCpu` to 4, and leave `PerExecutionEnvironmentMaxConcurrency` at its default. 12 GB of accelerator memory holds the 1.5-billion-parameter model, about 3 GB in 16-bit precision, and leaves room for the key-value cache that vLLM sizes from the memory it is allowed to use (`VLLM_GPU_MEM_UTIL`, 80 percent by default) to serve concurrent requests. The default concurrency of 4 sends four requests at a time to the one server process, which fits them in that cache. 16,384 MB of memory covers the server process, the CUDA libraries, and the weights while they pass through CPU memory during loading. The vLLM server handles concurrent requests itself, so the default concurrency is appropriate. The ratio matters because the execution environment's vCPUs are carved out of the instance: 16,384 MB at the default ratio of 2 GiB per vCPU asks for 8 vCPUs, which is every vCPU on a `g6.2xlarge`. The version fails to activate with `IncompatibleAcceleratorInstanceTypes`. At 4 GiB per vCPU the same memory needs 4 vCPUs and fits.

Using AWS CLI:

```bash
aws lambda create-function \
  --function-name my-gpu-function \
  --package-type Image \
  --code ImageUri=111122223333.dkr.ecr.us-east-2.amazonaws.com/my-gpu-function:v1 \
  --role arn:aws:iam::111122223333:role/my-gpu-function-role \
  --memory-size 16384 \
  --timeout 900 \
  --environment 'Variables={MODEL_ID=s3://amzn-s3-demo-bucket/models/Qwen2.5-1.5B-Instruct/,VLLM_LOAD_FORMAT=runai_streamer}' \
  --accelerator-config '{"AcceleratorMemorySize":12}' \
  --capacity-provider-config '{"LambdaManagedInstancesCapacityProviderConfig":{"CapacityProviderArn":"arn:aws:lambda:us-east-2:111122223333:capacity-provider:my-gpu-capacity-provider","ExecutionEnvironmentMemoryGiBPerVCpu":4}}'
```

### Step 3: Publish the function and invoke the function
<a name="lambda-managed-instances-gpu-inference-serve-publish-invoke"></a>

Publish the function to `$LATEST.PUBLISHED`. Publishing runs the initialization code: Lambda pulls the image, the image starts the vLLM server, and the server loads the model. The version becomes `Active` when the server is ready. Loading the model from Amazon S3 is faster than downloading it from a third-party source during initialization.

Using AWS CLI:

```bash
aws lambda publish-version --function-name my-gpu-function --publish-to LATEST_PUBLISHED

aws lambda get-function-configuration \
  --function-name my-gpu-function \
  --qualifier '$LATEST.PUBLISHED' \
  --query State
```

When the state is `Active`, invoke the function. The unqualified function name invokes `$LATEST.PUBLISHED`. The event is an OpenAI chat completion request. The handler forwards a request that contains `messages` to the server's `/v1/chat/completions` endpoint, and a request that contains `prompt` to `/v1/completions`.

```bash
aws lambda invoke \
  --function-name my-gpu-function \
  --cli-binary-format raw-in-base64-out \
  --payload '{"messages":[{"role":"user","content":"Explain what a GPU does in one sentence."}],"max_tokens":64}' \
  response.json

cat response.json
```

The response is the server's OpenAI-compatible response. Its `model` field is the value of `MODEL_ID`, here the `s3://` prefix. To return a stable model name instead, set the `SERVED_MODEL_NAME` environment variable; the handler then uses it as the default and the server reports it.

```json
{
  "id": "chatcmpl-...",
  "model": "s3://amzn-s3-demo-bucket/models/Qwen2.5-1.5B-Instruct/",
  "choices": [
    {
      "message": {"role": "assistant", "content": "A GPU performs many simple calculations in parallel, ..."},
      "finish_reason": "stop"
    }
  ],
  "usage": {"prompt_tokens": 17, "completion_tokens": 24, "total_tokens": 41}
}
```

If your request includes tools, the server needs a tool call parser to choose a tool itself. Set `VLLM_SERVER_ARGS` to `--enable-auto-tool-choice --tool-call-parser <parser>` with the parser for your model, and the server accepts `tool_choice` set to `auto` or omitted. Without these flags, set `tool_choice` to `required` or to the name of a tool; requests with `auto` or no `tool_choice` fail.

## Configuration
<a name="lambda-managed-instances-gpu-inference-configuration"></a>

The images expose the server's settings as environment variables prefixed with `VLLM_` for vLLM and `SGLANG_` for SGLang, for example `VLLM_GPU_MEM_UTIL` and `VLLM_MAX_MODEL_LEN`, or `SGLANG_MEM_FRACTION` and `SGLANG_MAX_TOTAL_TOKENS`. The following table lists common variables. For the full list and their defaults, see the vLLM and SGLang sections of [GPU base images](lambda-managed-instances-gpu-base-images.md). For the models tested with each image, see the [vLLM supported models](https://aws.github.io/deep-learning-containers/vllm/models/) and [SGLang supported models](https://aws.github.io/deep-learning-containers/sglang/models/) lists on the GitHub website. Other models supported by vLLM or SGLang, including embedding, audio-language, and vision-language models, should also work.


| Variable | Default | Description | 
| --- | --- | --- | 
| MODEL\_ID | Qwen/Qwen2.5-0.5B-Instruct | Hugging Face model ID, S3 prefix, or local path | 
| SERVED\_MODEL\_NAME | Not set | Stable model name clients use in the response's model field; passed to the server as --served-model-name. Defaults to MODEL\_ID. | 
| VLLM\_LOAD\_FORMAT | Not set | Set to runai\_streamer to stream weights from Amazon S3 into memory | 
| VLLM\_GPU\_MEM\_UTIL | 0.8 | vLLM --gpu-memory-utilization | 
| VLLM\_MAX\_MODEL\_LEN | Not set | vLLM --max-model-len | 
| VLLM\_SERVER\_PORT | 8000 | Local port the vLLM server listens on | 
| VLLM\_SERVER\_TIMEOUT | 600 | Seconds to wait for the server to become ready | 
| VLLM\_SERVER\_ARGS | Not set | Additional vllm serve flags, for example --enable-auto-tool-choice --tool-call-parser hermes | 
| SGLANG\_MEM\_FRACTION | 0.8 | SGLang --mem-fraction-static | 
| SGLANG\_ATTENTION\_BACKEND | flashinfer | SGLang --attention-backend | 
| SGLANG\_MAX\_TOTAL\_TOKENS | Not set | SGLang --max-total-tokens | 
| SGLANG\_SERVER\_TIMEOUT | 600 | Seconds to wait for the server to become ready | 
| SGLANG\_SERVER\_ARGS | Not set | Additional sglang.launch\_server flags, for example --tool-call-parser qwen | 
| ENGINE\_EXTENSION | on | Set to off to keep the image from starting the server, for a handler that starts its own | 
| ENGINE\_HEALTH\_INTERVAL | 10 | Seconds between health checks of the running server | 
| ENGINE\_HEALTH\_TIMEOUT | 10 (vLLM), 30 (SGLang) | Seconds to wait for each health check | 
| ENGINE\_HEALTH\_FAILURES | 3 | Consecutive failed health checks before Lambda replaces the execution environment | 

## Customize request handling with your own handler
<a name="lambda-managed-instances-gpu-inference-custom-handler"></a>

The default handler of the vLLM and SGLang images forwards each event to the inference server as it arrives. To process requests before forwarding them for inference (for example, to inject a system prompt, perform validation, or cap `max_tokens`), replace the default handler with your own `handler.py`, while keeping the server setup unchanged. The image still starts the inference server during initialization; your handler only forwards requests to it over local HTTP, so one copy of the model serves all concurrent invocations in the execution environment. Do not start a server from the handler: it competes with the one the image started for the port and the GPU memory. If your handler must start its own server, set the `ENGINE_EXTENSION` environment variable to `off`. The following steps replace the handler on `my-gpu-function` from the previous section.

### Sample Dockerfile
<a name="lambda-managed-instances-gpu-inference-custom-dockerfile"></a>

```dockerfile
FROM public.ecr.aws/lambda/deep-learning-containers/vllm:cuda-v1

COPY handler.py /var/task/
CMD ["handler.handler"]
```

### Sample Handlers
<a name="lambda-managed-instances-gpu-inference-custom-handler-code"></a>

The handler forwards each request to the server that the image started. Before forwarding it caps `max_tokens` and adds a system prompt when the caller did not send one, and it gives the server until just before the invocation deadline to answer.

```python
import json
import os

import requests

MODEL_ID = os.environ["MODEL_ID"]
SERVED_MODEL_NAME = os.environ.get("SERVED_MODEL_NAME")
PORT = os.environ.get("VLLM_SERVER_PORT", "8000")
BASE_URL = f"http://127.0.0.1:{PORT}"

SYSTEM_PROMPT = "You are a helpful customer support assistant. Be concise."
MAX_TOKENS_LIMIT = 1024


def _request_timeout(context):
    # Give the server until one second before the invocation deadline.
    return max(0.1, context.get_remaining_time_in_millis() / 1000 - 1)


def handler(event, context):
    if isinstance(event, (bytes, bytearray, str)):
        event = json.loads(event or "{}")
    body = dict(event)
    body["max_tokens"] = min(body.get("max_tokens", 256), MAX_TOKENS_LIMIT)
    if "messages" in body:
        messages = body["messages"]
        if not any(m.get("role") == "system" for m in messages):
            messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
    body.setdefault("model", SERVED_MODEL_NAME or MODEL_ID)
    path = "/v1/chat/completions" if "messages" in body else "/v1/completions"
    try:
        response = requests.post(f"{BASE_URL}{path}", json=body, timeout=_request_timeout(context))
    except requests.ConnectionError as e:
        raise RuntimeError(f"vLLM server is not reachable at {BASE_URL}: {e}") from e
    except requests.Timeout as e:
        raise RuntimeError("vLLM server did not answer before the invocation deadline") from e
    if response.status_code >= 400:
        # Surface vLLM's error body instead of a bare HTTPError.
        raise RuntimeError(f"vLLM returned {response.status_code}: {response.text}")
    return response.json()
```

Each worker process imports `handler.py` during initialization and forwards its invocations to the server over local HTTP, so one copy of the model serves every concurrent invocation. The image starts the server before the first invocation and the version does not reach `Active` until the server is ready, so the handler does not wait for it. If the server exits or stops answering health checks while the execution environment runs, Lambda replaces the execution environment; invocations in flight on it fail with the connection error the handler raises. For more information about concurrency, see [Concurrency for Lambda Managed Instances runtimes](lambda-managed-instances-gpu-scaling.md#lambda-managed-instances-gpu-scaling-concurrency).

For the SGLang image, the same handler applies with `SGLANG_SERVER_PORT` in place of `VLLM_SERVER_PORT`. For the variables each image defines, see [GPU base images](lambda-managed-instances-gpu-base-images.md).

### Step 4: Build and push the image containing your custom handler
<a name="lambda-managed-instances-gpu-inference-custom-build-push"></a>

Package the handler shown earlier in your container image and push it to Amazon ECR with a new tag.

Using AWS CLI:

```bash
docker build -t my-gpu-function .
docker tag my-gpu-function:latest 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-gpu-function:v2
docker push 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-gpu-function:v2
```

### Step 5: Update the function and invoke the new handler
<a name="lambda-managed-instances-gpu-inference-custom-update-invoke"></a>

Point the function at the new image and republish `$LATEST.PUBLISHED`. The function configuration, including the capacity provider, accelerator memory, and concurrency, is unchanged. Lambda rolls out the new image in steps: it starts execution environments with the new handler, waits for each to become ready, and then removes the execution environments that run the previous image. The function keeps serving invocations during the rollout.

Using AWS CLI:

```bash
aws lambda update-function-code \
  --function-name my-gpu-function \
  --image-uri 111122223333.dkr.ecr.us-east-2.amazonaws.com/my-gpu-function:v2

aws lambda publish-version --function-name my-gpu-function --publish-to LATEST_PUBLISHED

aws lambda get-function-configuration \
  --function-name my-gpu-function \
  --qualifier '$LATEST.PUBLISHED' \
  --query State
```

When the state is `Active`, send a request with `max_tokens` set to 4096. The handler lowers it to `MAX_TOKENS_LIMIT` (1,024) before forwarding the request, so the server stops after 1,024 tokens:

```bash
aws lambda invoke \
  --function-name my-gpu-function \
  --cli-binary-format raw-in-base64-out \
  --payload '{"messages":[{"role":"user","content":"Write a detailed essay of at least 3000 words on the history of GPU computing, with sections and headings."}],"max_tokens":4096}' \
  response.json

cat response.json
```

In the response, `finish_reason` is `length` and `usage.completion_tokens` is 1,024, which confirms the cap. The system prompt from `SYSTEM_PROMPT` was added to the request as well, because the request had no system message.

```json
{
  "choices": [{"message": {"role": "assistant", "content": "..."}, "finish_reason": "length"}],
  "usage": {"prompt_tokens": 38, "completion_tokens": 1024, "total_tokens": 1062}
}
```

The custom handler changes how requests are processed, not how the model is loaded, so `ExecutionEnvironmentGPUMemoryUsed` stays in the same range as before the republish.

## Clean up
<a name="lambda-managed-instances-gpu-inference-cleanup"></a>

Delete the function, then delete the capacity provider if you no longer need it.

Using AWS CLI:

```bash
aws lambda delete-function --function-name my-gpu-function
aws lambda delete-capacity-provider --capacity-provider-name my-gpu-capacity-provider
```