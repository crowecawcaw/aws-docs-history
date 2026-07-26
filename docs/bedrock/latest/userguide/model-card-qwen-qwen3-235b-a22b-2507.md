# Qwen3 235B A22B 2507

## Icon showing purple arrows and sparkles indicating AI or translation functionality. Qwen — Qwen3 235B A22B 2507

## Model Details

Qwen3 235B A22B is Qwen's 235-billion parameter mixture-of-experts model with 22 billion active parameters, supporting text and code generation with a 256K context window. For more information about model development and performance, see the [model/service card](https://qwen.ai/blog?id=qwen3 "https://qwen.ai/blog?id=qwen3").

- **Model launch date:** Apr 28, 2025
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507/blob/main/LICENSE "https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507/blob/main/LICENSE")
- **Model lifecycle:** Active
- **Context window:** 256K tokens
- **Max output tokens:** 8K
- **Reasoning:** Supported

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                                             | **[Endpoints supported](endpoints.md "endpoints.md")**    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses` | Green circle with white checkmark icon. `bedrock-runtime` |
| Red circle with white X icon indicating error, cancel, or close action. Image  | Red circle with white X icon indicating error, cancel, or close action. Image     | Green circle with white checkmark icon. `Chat Completions`                          | Green circle with white checkmark icon. `bedrock-mantle`  |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                    |                                                           |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                  |                                                           |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                     |                                                           |

###### Note

Whenever possible, we recommend you use the `bedrock-mantle` endpoint.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                      | **Not Supported**                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Projects](projects.md "projects.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](tool-use.md "tool-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Server-side tool calling](tool-use.md "tool-use.md") |

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Guardrails](guardrails.md "guardrails.md")<br>• Green circle with white checkmark icon. [Model evaluation](evaluation.md "evaluation.md")<br>• Green circle with white checkmark icon. [Prompt management](prompt-management.md "prompt-management.md")<br>• Green circle with white checkmark icon. [Flows](flows.md "flows.md")<br>• Green circle with white checkmark icon. [Agents](agents.md "agents.md")<br>• Green circle with white checkmark icon. [Structured outputs](structured-outputs.md "structured-outputs.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](tool-use.md "tool-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](count-tokens.md "count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](knowledge-base.md "knowledge-base.md") |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                     | **In-Region endpoint URL**                       | **Geo inference ID** | **Global inference ID** |
| ----------------- | -------------------------------- | ------------------------------------------------ | -------------------- | ----------------------- |
| `bedrock-runtime` | `qwen.qwen3-235b-a22b-2507-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | Not supported        | Not supported           |
| `bedrock-mantle`  | `qwen.qwen3-235b-a22b-2507`      | `https://bedrock-mantle.{region}.api.aws/v1`     | Not supported        | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                            | **Flex**                                | **Reserved**                                                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Green circle with white checkmark icon. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                 | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| -------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-2` (Ohio)         | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-central-1` (Frankfurt) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-north-1` (Stockholm)   | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-south-1` (Milan)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-2` (London)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-northeast-1` (Tokyo)   | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-south-1` (Mumbai)      | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-2` (Sydney)  | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-3` (Jakarta) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-1` (Ireland)      | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `sa-east-1` (São Paulo)    | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-1` (N. Virginia)  | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

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
    model="qwen.qwen3-235b-a22b-2507",
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
    modelId='qwen.qwen3-235b-a22b-2507-v1:0',
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
    modelId='qwen.qwen3-235b-a22b-2507-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
