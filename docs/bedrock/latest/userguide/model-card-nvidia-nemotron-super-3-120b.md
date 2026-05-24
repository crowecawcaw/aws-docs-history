# NVIDIA Nemotron 3 Super 120B

## NVIDIA — NVIDIA Nemotron 3 Super 120B

## Model Details

NVIDIA Nemotron 3 Super is a 120B-parameter open hybrid MoE model, activating just 12B parameters for maximum compute efficiency and accuracy in complex multi-agent applications. It delivers up to 7x higher throughput, providing fast, cost-efficient inference for agentic tasks. A long context window gives the model long-term memory, preventing AI agents from losing focus on long, multi-step tasks and ensuring high-accuracy results. Fully open with weights, datasets, and recipes, it allows easy customization and secure deployment. For more information about model development and performance, see the [model/service card](https://build.nvidia.com/nvidia/nemotron-3-super-120b-a12b/modelcard "https://build.nvidia.com/nvidia/nemotron-3-super-120b-a12b/modelcard").

- **Model launch date:** Mar 11, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/ "https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/")
- **Model lifecycle:** Active
- **Context window:** 256K tokens
- **Max output tokens:** 32K

| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.md "apis.md")** | **[Endpoints supported](endpoints.md "endpoints.md")** |
| -------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------ |
| Audio                | Embedding             | `Responses`                             | `bedrock-runtime`                                      |
| Image                | Image                 | `Chat Completions`                      | `bedrock-mantle`                                       |
| Speech               | Speech                | `Invoke`                                |                                                        |
| Text                 | Text                  | `Converse`                              |                                                        |
| Video                | Video                 |                                         |                                                        |

###### Note

Whenever possible, we recommend you use the `bedrock-mantle` endpoint.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                      | **Not Supported**                                       |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| • [Projects](projects.md "projects.md")<br>• [Client-side tool calling](tool-use.md "tool-use.md") | • [Server-side tool calling](tool-use.md "tool-use.md") |

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Not Supported**                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• [Guardrails](guardrails.md "guardrails.md")<br>• [Model evaluation](evaluation.md "evaluation.md")<br>• [Prompt management](prompt-management.md "prompt-management.md")<br>• [Flows](flows.md "flows.md")<br>• [Agents](agents.md "agents.md")<br>• [Structured outputs](structured-outputs.md "structured-outputs.md") | • [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• [Count tokens](count-tokens.md "count-tokens.md")<br>• [Knowledge base](knowledge-base.md "knowledge-base.md") |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                   | **In-Region endpoint URL**                       | **Geo inference ID**                  | **Global inference ID** |
| ----------------- | ------------------------------ | ------------------------------------------------ | ------------------------------------- | ----------------------- |
| `bedrock-runtime` | `nvidia.nemotron-super-3-120b` | `https://bedrock-runtime.{region}.amazonaws.com` | `us-gov.nvidia.nemotron-super-3-120b` | Not supported           |
| `bedrock-mantle`  | `nvidia.nemotron-super-3-120b` | `https://bedrock-mantle.{region}.api.aws/v1`     | Not supported                         | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard** | **Priority** | **Flex** | **Reserved** |
| ------------ | ------------ | -------- | ------------ |
|              |              |          |              |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                   | **In-Region** | **Geo** | **Global** |
| ---------------------------- | ------------- | ------- | ---------- |
| `us-east-1` (N. Virginia)    |               |         |            |
| `us-east-2` (Ohio)           |               |         |            |
| `us-west-2` (Oregon)         |               |         |            |
| `eu-south-1` (Milan)         |               |         |            |
| `eu-west-1` (Ireland)        |               |         |            |
| `eu-west-2` (London)         |               |         |            |
| `ap-northeast-1` (Tokyo)     |               |         |            |
| `ap-south-1` (Mumbai)        |               |         |            |
| `ap-southeast-2` (Sydney)    |               |         |            |
| `sa-east-1` (São Paulo)      |               |         |            |
| `ap-southeast-4` (Melbourne) |               |         |            |
| `us-gov-west-1` (GovCloud)   |               |         |            |

**Geo CRIS inference details**

**US GovCloud CRIS**

US GovCloud CRIS Inference ID: `us-gov.nvidia.nemotron-super-3-120b`

| **Source Region**             | **Destination Regions**                                      |
| ----------------------------- | ------------------------------------------------------------ |
| us-gov-west-1 (GovCloud West) | us-gov-west-1 (GovCloud West), us-gov-east-1 (GovCloud East) |
| us-gov-east-1 (GovCloud East) | us-gov-west-1 (GovCloud West), us-gov-east-1 (GovCloud East) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, please refer to [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Chat Completions API

```
pip install boto3 openai
```

Invoke/Converse API

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

Chat Completions API

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/v1"
```

Invoke/Converse API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Chat Completions API

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="nvidia.nemotron-super-3-120b",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
    )
print(response)
```

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='nvidia.nemotron-super-3-120b',
    body=json.dumps({
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
)
print(json.loads(response['body'].read()))
```

Converse API

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='nvidia.nemotron-super-3-120b',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
