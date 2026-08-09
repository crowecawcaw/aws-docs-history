# Qwen3 Coder Next

## Icon showing purple arrows and sparkles indicating AI or translation functionality. Qwen — Qwen3 Coder Next

## Model Details

Qwen3 Coder Next is Qwen's coding model with improved code generation, debugging, and software engineering capabilities. For more information about model development and performance, see the [model/service card](https://qwen.ai/blog?id=qwen3-coder "https://qwen.ai/blog?id=qwen3-coder").

- **Model launch date:** Feb 04, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/main/LICENSE "https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/main/LICENSE")
- **Model lifecycle:** Active
- **Context window:** 256K tokens
- **Max output tokens:** 16K

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")** | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses`       | Green circle with white checkmark icon. `bedrock-runtime`                                                |
| Red circle with white X icon indicating error, cancel, or close action. Image  | Red circle with white X icon indicating error, cancel, or close action. Image     | Green circle with white checkmark icon. `Chat Completions`                                | Green circle with white checkmark icon. `bedrock-mantle`                                                 |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                          |                                                                                                          |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                        |                                                                                                          |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                           |                                                                                                          |

###### Note

Whenever possible, we recommend you use the `bedrock-mantle` endpoint.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                          | **Not Supported**                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Projects](bedrock/latest/userguide/projects.md "bedrock/latest/userguide/projects.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](bedrock/latest/userguide/tool-use.md "bedrock/latest/userguide/tool-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Server-side tool calling](bedrock/latest/userguide/tool-use.md "bedrock/latest/userguide/tool-use.md") |

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Guardrails](bedrock/latest/userguide/guardrails.md "bedrock/latest/userguide/guardrails.md")<br>• Green circle with white checkmark icon. [Model evaluation](bedrock/latest/userguide/evaluation.md "bedrock/latest/userguide/evaluation.md")<br>• Green circle with white checkmark icon. [Prompt management](bedrock/latest/userguide/prompt-management.md "bedrock/latest/userguide/prompt-management.md")<br>• Green circle with white checkmark icon. [Flows](bedrock/latest/userguide/flows.md "bedrock/latest/userguide/flows.md")<br>• Green circle with white checkmark icon. [Agents](bedrock/latest/userguide/agents.md "bedrock/latest/userguide/agents.md")<br>• Green circle with white checkmark icon. [Structured outputs](bedrock/latest/userguide/structured-outputs.md "bedrock/latest/userguide/structured-outputs.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](bedrock/latest/userguide/prompt-routing.md "bedrock/latest/userguide/prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Abuse detection](bedrock/latest/userguide/abuse-detection.md "bedrock/latest/userguide/abuse-detection.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](bedrock/latest/userguide/prompt-management-optimize.md "bedrock/latest/userguide/prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](bedrock/latest/userguide/count-tokens.md "bedrock/latest/userguide/count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](bedrock/latest/userguide/knowledge-base.md "bedrock/latest/userguide/knowledge-base.md") |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**      | **Model ID**            | **In-Region endpoint URL**                       | **Geo inference ID** | **Global inference ID** |
| ----------------- | ----------------------- | ------------------------------------------------ | -------------------- | ----------------------- |
| `bedrock-runtime` | `qwen.qwen3-coder-next` | `https://bedrock-runtime.{region}.amazonaws.com` | Not supported        | Not supported           |
| `bedrock-mantle`  | `qwen.qwen3-coder-next` | `https://bedrock-mantle.{region}.api.aws/v1`     | Not supported        | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                 | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| -------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia)  | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-2` (London)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-2` (Sydney)  | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-northeast-1` (Tokyo)   | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-south-1` (Mumbai)      | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-3` (Jakarta) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-central-1` (Frankfurt) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-north-1` (Stockholm)   | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-south-1` (Milan)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-1` (Ireland)      | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `sa-east-1` (São Paulo)    | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-2` (Ohio)         | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](bedrock/latest/userguide/quotas-increase.md "bedrock/latest/userguide/quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](general/latest/gr/bedrock.md#limits_bedrock "general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Responses/Chat Completions API

```
pip install boto3 openai
```

Invoke/Converse API

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

Responses/Chat Completions API

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
    model="qwen.qwen3-coder-next",
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
    modelId='qwen.qwen3-coder-next',
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
    modelId='qwen.qwen3-coder-next',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
