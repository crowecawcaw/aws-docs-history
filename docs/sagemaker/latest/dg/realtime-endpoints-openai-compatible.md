

# Invoke endpoints with OpenAI-compatible APIs
<a name="realtime-endpoints-openai-compatible"></a>

Amazon SageMaker AI real-time inference endpoints support an OpenAI-compatible API path. Customers using the OpenAI SDK, LangChain, or Strands Agents can invoke models on SageMaker AI by changing only their endpoint URL, without requiring custom clients, SigV4 wrappers, or code rewrites.

With this capability, SageMaker AI endpoints expose an `/openai/v1/chat/completions` path that accepts Chat Completions requests and returns responses directly from the container, including streaming. OpenAI-compatible endpoints are available on all endpoints and inference components using standard SageMaker AI APIs and SDKs.

SageMaker AI routes requests based on the endpoint name in the URL. Any OpenAI-compatible client works without additional configuration. You can create short-lived bearer tokens for your endpoints and use them with your OpenAI clients.

## Prerequisites
<a name="realtime-endpoints-openai-compatible-prerequisites"></a>

Before you begin, make sure you have the following:
+ An AWS account with permissions to create SageMaker AI endpoints.
+ The SageMaker AI Python SDK installed (`pip install sagemaker`).
+ The OpenAI Python SDK installed (`pip install openai`).
+ A model stored in Amazon S3 (for example, Qwen3-4B downloaded from Hugging Face).
+ An IAM execution role with the `AmazonSageMakerFullAccess` policy to create the endpoints.
+ An IAM role or user with the `sagemaker:CallWithBearerToken` and `sagemaker:InvokeEndpoint` permissions to invoke the endpoint.

## Authentication with bearer tokens
<a name="realtime-endpoints-openai-compatible-auth"></a>

SageMaker AI OpenAI-compatible endpoints use bearer token authentication. The SageMaker AI Python SDK includes a token generator that creates short-lived tokens (valid up to 12 hours) from your existing AWS credentials. No additional secrets or API keys are required.

The token contains your role or user credentials and requires the `sagemaker:CallWithBearerToken` and `sagemaker:InvokeEndpoint` action permissions.

### Generate a token
<a name="realtime-endpoints-openai-compatible-auth-generate"></a>

Use the `generate_token` function from the SageMaker AI Python SDK to create a bearer token:

```
from sagemaker.core.token_generator import generate_token
from datetime import timedelta

token = generate_token(region="us-west-2", expiry=timedelta(minutes=5))
```

The `generate_token` function generates a short-lived bearer token for authenticating with SageMaker AI APIs. By default, tokens are valid for 12 hours. You can override this with the `expiry` parameter using a `timedelta` value anywhere between 1 second and 12 hours.

The function accepts a `region`, an optional `aws_credentials_provider`, and the `expiry` duration. If no region is provided, it falls back to the `AWS_REGION` environment variable. If no credentials provider is supplied, it resolves credentials using the default AWS credential chain, which searches multiple sources including environment variables, `~/.aws/credentials`, `~/.aws/config`, container credentials, and instance profiles. For the full resolution order, see the [boto3 credentials documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html).

### Auto-refresh tokens for long-running applications
<a name="realtime-endpoints-openai-compatible-auth-refresh"></a>

For applications that run continuously, you can implement an auto-refreshing pattern using `httpx` so that a fresh token is generated on each request:

```
import httpx
from sagemaker.core.token_generator import generate_token

class SageMakerAuth(httpx.Auth):
    def __init__(self, region: str):
        self.region = region

    def auth_flow(self, request):
        request.headers["Authorization"] = f"Bearer {generate_token(region=self.region)}"
        yield request

http_client = httpx.Client(auth=SageMakerAuth(region="us-west-2"))
```

### IAM permissions
<a name="realtime-endpoints-openai-compatible-auth-iam"></a>

The IAM role or user invoking the endpoint needs the following permissions:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sagemaker:InvokeEndpoint",
            "Resource": "arn:aws:sagemaker:{{REGION}}:{{ACCOUNT_ID}}:endpoint/{{ENDPOINT_NAME}}"
        },
        {
            "Effect": "Allow",
            "Action": "sagemaker:CallWithBearerToken",
            "Resource": "*"
        }
    ]
}
```

**Important**  
Always restrict the `Resource` for `sagemaker:InvokeEndpoint` to specific endpoint ARNs rather than using a wildcard. The bearer token generated from this role has the same level of access, so a narrowly scoped policy limits the blast radius if a token is inadvertently exposed.

**Note**  
`sagemaker:CallWithBearerToken` requires a wildcard (`"*"`) for the `Resource` field. It does not support resource-level restrictions.

### How the token works
<a name="realtime-endpoints-openai-compatible-auth-how-it-works"></a>

The bearer token is a base64-encoded SigV4 pre-signed URL. When you call `generate_token`, the SageMaker AI SDK constructs a request to the SageMaker AI service for the `CallWithBearerToken` action, signs it locally using your AWS credentials, and encodes the resulting signed URL as a portable token string. No network call is made during token generation — the signing happens entirely on the client side.

When you present this token to a SageMaker AI endpoint, the service decodes it, validates the SigV4 signature, verifies that the token has not expired, and confirms that the originating IAM identity has the required permissions. The token's effective lifetime is the lesser of the `expiry` value and the remaining validity of the AWS credentials used to sign it.

### Security best practices
<a name="realtime-endpoints-openai-compatible-auth-security"></a>

The bearer token carries the same authorization as the underlying AWS credentials used to generate it. Treat tokens with the same care as credentials. Follow these best practices:
+ Scope the IAM role used for token generation to the minimum permissions required — specifically `sagemaker:InvokeEndpoint` and `sagemaker:CallWithBearerToken` on only the endpoint ARNs that the caller needs to access.
+ Do not generate tokens from roles with expansive permissions, such as those granted by `AdministratorAccess` or `AmazonSageMakerFullAccess` managed policies.
+ Do not store tokens on disk, in environment variables, in configuration files, in databases, or in distributed caches. Do not log tokens, and only transmit them over encrypted communication protocols such as HTTPS.
+ Token generation is a local operation with no network overhead. Generate a fresh token at the point of use or use the auto-refreshing `httpx.Auth` pattern shown above.
+ Set the token expiry to the shortest duration your workload requires.

## Invoke a single-model endpoint
<a name="realtime-endpoints-openai-compatible-single-model"></a>

A single-model endpoint hosts one model and serves requests directly. The following example deploys Qwen3-4B using the SageMaker AI vLLM Deep Learning Container on an `ml.g6.2xlarge` instance.

**Note**  
SageMaker AI endpoints incur charges while in service, regardless of traffic. See the [SageMaker AI pricing page](https://aws.amazon.com/sagemaker/pricing/) for details.

### Deploy the endpoint
<a name="realtime-endpoints-openai-compatible-single-model-deploy"></a>

```
import boto3
import sagemaker
import time
from sagemaker.core.helper.session_helper import Session
from sagemaker.core.helper.session_helper import get_execution_role

# AWS configuration
REGION = "us-west-2"

# Automatically resolve account ID and default SageMaker execution role
session = Session(boto_session=boto3.Session(region_name=REGION))
ACCOUNT_ID = boto3.client("sts", region_name=REGION).get_caller_identity()["Account"]
EXECUTION_ROLE = get_execution_role(sagemaker_session=session)

# HF Model ID
MODEL_HF_ID = "Qwen/Qwen3-4B"

# SageMaker vLLM Deep Learning Container
VLLM_IMAGE = (
    f"763104351884.dkr.ecr.{REGION}.amazonaws.com/"
    f"vllm:0.20.2-gpu-py312-cu130-ubuntu22.04-sagemaker"
)

# Instance type (1x NVIDIA L4 GPU)
INSTANCE_TYPE = "ml.g6.2xlarge"

sagemaker_client = boto3.client("sagemaker", region_name=REGION)
```

Create the model, endpoint configuration, and endpoint:

```
TIMESTAMP = str(int(time.time()))

SME_MODEL_NAME = f"openai-compat-sme-model-{TIMESTAMP}"
SME_ENDPOINT_CONFIG_NAME = f"openai-compat-sme-epc-{TIMESTAMP}"
SME_ENDPOINT_NAME = f"openai-compat-sme-ep-{TIMESTAMP}"

sagemaker_client.create_model(
    ModelName=SME_MODEL_NAME,
    ExecutionRoleArn=EXECUTION_ROLE,
    PrimaryContainer={
        "Image": VLLM_IMAGE,
        "Environment": {
            "HF_MODEL_ID": MODEL_HF_ID,
            "SM_VLLM_TENSOR_PARALLEL_SIZE": "1",
            "SM_VLLM_MAX_NUM_SEQS": "4",
            "SM_VLLM_ENABLE_AUTO_TOOL_CHOICE": "true",
            "SM_VLLM_TOOL_CALL_PARSER": "hermes",
            "SAGEMAKER_ENABLE_LOAD_AWARE": "1",
        },
    },
)

sagemaker_client.create_endpoint_config(
    EndpointConfigName=SME_ENDPOINT_CONFIG_NAME,
    ProductionVariants=[
        {
            "VariantName": "variant1",
            "ModelName": SME_MODEL_NAME,
            "InstanceType": INSTANCE_TYPE,
            "InitialInstanceCount": 1,
        }
    ],
)

sagemaker_client.create_endpoint(
    EndpointName=SME_ENDPOINT_NAME,
    EndpointConfigName=SME_ENDPOINT_CONFIG_NAME,
)

# Wait for endpoint to reach InService status (5-10 minutes)
waiter = sagemaker_client.get_waiter("endpoint_in_service")
waiter.wait(
    EndpointName=SME_ENDPOINT_NAME,
    WaiterConfig={"Delay": 30, "MaxAttempts": 40},
)
```

The endpoint transitions to `InService` status within a few minutes. Once ready, it serves both the standard SageMaker AI `/invocations` path and the OpenAI-compatible path at `/openai/v1/chat/completions`.

### Invoke the endpoint
<a name="realtime-endpoints-openai-compatible-single-model-invoke"></a>

With the endpoint in service, invoke it using the OpenAI Python SDK. The base URL follows this format:

```
https://runtime.sagemaker.{{REGION}}.amazonaws.com/endpoints/{{ENDPOINT_NAME}}/openai/v1
```

```
from openai import OpenAI
from sagemaker.core.token_generator import generate_token

REGION = "us-west-2"
sme_base_url = (
    f"https://runtime.sagemaker.{REGION}.amazonaws.com"
    f"/endpoints/{SME_ENDPOINT_NAME}/openai/v1"
)

client = OpenAI(
    base_url=sme_base_url,
    api_key=generate_token(region=REGION),
)

stream = client.chat.completions.create(
    model="",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain how transformers work in machine learning, in three sentences."},
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
print()
```

The `model` field is passed through to the container. Because SageMaker AI routes requests based on the endpoint name in the URL, you can leave this field empty or set it to match the model name your container expects.

## Invoke inference components
<a name="realtime-endpoints-openai-compatible-inference-components"></a>

Inference components allow you to host multiple models on a single endpoint, each with dedicated compute resource allocations. With inference components, the model is associated with the component rather than the endpoint configuration.

### Deploy an inference component endpoint
<a name="realtime-endpoints-openai-compatible-ic-deploy"></a>

```
IC_MODEL_NAME = f"openai-compat-ic-model-{TIMESTAMP}"
IC_ENDPOINT_CONFIG_NAME = f"openai-compat-ic-epc-{TIMESTAMP}"
IC_ENDPOINT_NAME = f"openai-compat-ic-ep-{TIMESTAMP}"
IC_NAME = f"openai-compat-ic-qwen3-4b-{TIMESTAMP}"

sagemaker_client.create_model(
    ModelName=IC_MODEL_NAME,
    ExecutionRoleArn=EXECUTION_ROLE,
    PrimaryContainer={
        "Image": VLLM_IMAGE,
        "Environment": {
            "HF_MODEL_ID": MODEL_HF_ID,
            "SM_VLLM_TENSOR_PARALLEL_SIZE": "1",
            "SM_VLLM_MAX_NUM_SEQS": "4",
            "SM_VLLM_ENABLE_AUTO_TOOL_CHOICE": "true",
            "SM_VLLM_TOOL_CALL_PARSER": "hermes",
            "SAGEMAKER_ENABLE_LOAD_AWARE": "1",
        },
    },
)

sagemaker_client.create_endpoint_config(
    EndpointConfigName=IC_ENDPOINT_CONFIG_NAME,
    ExecutionRoleArn=EXECUTION_ROLE,
    ProductionVariants=[
        {
            "VariantName": "variant1",
            "InstanceType": INSTANCE_TYPE,
            "InitialInstanceCount": 1,
        }
    ],
)

sagemaker_client.create_endpoint(
    EndpointName=IC_ENDPOINT_NAME,
    EndpointConfigName=IC_ENDPOINT_CONFIG_NAME,
)

# Wait for endpoint
waiter = sagemaker_client.get_waiter("endpoint_in_service")
waiter.wait(
    EndpointName=IC_ENDPOINT_NAME,
    WaiterConfig={"Delay": 30, "MaxAttempts": 40},
)

# Create the inference component
sagemaker_client.create_inference_component(
    InferenceComponentName=IC_NAME,
    EndpointName=IC_ENDPOINT_NAME,
    VariantName="variant1",
    Specification={
        "ModelName": IC_MODEL_NAME,
        "ComputeResourceRequirements": {
            "MinMemoryRequiredInMb": 1024,
            "NumberOfCpuCoresRequired": 2,
            "NumberOfAcceleratorDevicesRequired": 1,
        },
    },
    RuntimeConfig={"CopyCount": 1},
)

# Wait for inference component
while True:
    desc = sagemaker_client.describe_inference_component(InferenceComponentName=IC_NAME)
    status = desc["InferenceComponentStatus"]
    if status == "InService":
        break
    elif status == "Failed":
        raise RuntimeError(f"Inference component failed: {desc.get('FailureReason', 'unknown')}")
    time.sleep(30)
```

You can create additional inference components on the same endpoint to host multiple models with independent scaling and resource allocation.

### Invoke an inference component
<a name="realtime-endpoints-openai-compatible-ic-invoke"></a>

To invoke a specific inference component, include its name in the URL path:

```
https://runtime.sagemaker.{{REGION}}.amazonaws.com/endpoints/{{ENDPOINT_NAME}}/inference-components/{{IC_NAME}}/openai/v1
```

The following example shows how to invoke an inference component using the OpenAI SDK with a shared connection pool:

```
import httpx
from openai import OpenAI
from sagemaker.core.token_generator import generate_token

shared_http = httpx.Client()

client_a = OpenAI(
    base_url=(
        f"https://runtime.sagemaker.{REGION}.amazonaws.com"
        f"/endpoints/{IC_ENDPOINT_NAME}/inference-components/{IC_NAME}/openai/v1"
    ),
    api_key=generate_token(region=REGION),
    http_client=shared_http,
)

response = client_a.chat.completions.create(
    model="",
    messages=[{"role": "user", "content": "What is 42 * 3? Reply with the number."}],
)
print(response.choices[0].message.content)
```

The shared `httpx.Client` allows multiple OpenAI client instances to reuse the same TLS sessions and connection pool when targeting different inference components on the same endpoint.

## Supported containers
<a name="realtime-endpoints-openai-compatible-containers"></a>

The following containers support OpenAI-compatible APIs on SageMaker AI. The container must implement the `/v1/chat/completions` path and return streaming responses in SSE format.


|  Container  |  Support status  | 
| --- | --- | 
| SageMaker AI vLLM Deep Learning Container | Supported | 
| SageMaker AI SGLang Deep Learning Container | Supported | 
| Custom containers implementing OpenAI API paths and `/ping` | Supported | 