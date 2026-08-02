# Claude Fable 5

## Anthropic — Claude Fable 5

## Model Details

Claude Fable 5 is Anthropic's next-generation model for complex knowledge work and coding, capable of sustained autonomous operation across multi-day tasks. It plans across stages, delegates to sub-agents, and self-verifies its work.

- **Model launch date:** June 9, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 1M tokens
- **Max output tokens:** 128K
- **Sampling parameters:** temperature must be 1.0 or unset; top\_p must be ≥ 0.99 and < 1.0, or unset; top\_k is not supported
- **Reasoning:** Supported (adaptive thinking is always on and cannot be disabled; effort level is configurable)
- **Knowledge cutoff:** January 2026
- **Marketplace product ID:** prod-h6swdfybvty7y

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                                                    | **[Endpoints supported](endpoints.md "endpoints.md")**    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime` |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Green circle with white checkmark icon. `bedrock-mantle`  |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                           |                                                           |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                         |                                                           |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     | Green circle with white checkmark icon. `Messages`                                         |                                                           |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Not Supported**                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| • [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• [Guardrails](guardrails.md "guardrails.md")<br>• [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• [Model evaluation](evaluation.md "evaluation.md")<br>• [Prompt management](prompt-management.md "prompt-management.md")<br>• [Flows](flows.md "flows.md")<br>• [Agents](agents.md "agents.md")<br>• [Count tokens](count-tokens.md "count-tokens.md") | • [Intelligent prompt routing](prompt-routing.md "prompt-routing.md") |

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                              | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• [Count tokens](count-tokens.md "count-tokens.md") | • [Guardrails](guardrails.md "guardrails.md")<br>• [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• [Model evaluation](evaluation.md "evaluation.md")<br>• [Prompt management](prompt-management.md "prompt-management.md")<br>• [Flows](flows.md "flows.md")<br>• [Agents](agents.md "agents.md")<br>• [Intelligent prompt routing](prompt-routing.md "prompt-routing.md") |

**Prompt caching**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoint** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ---------------------------------------------- |
| Yes                          | 1,024                               | 4                                     | 5 minutes, 1 hour | `system`, `messages`, and `tools`              |

## Content Restrictions

Claude Fable 5 includes blocking classifiers for dual-use content in cybersecurity and biology. When a classifier blocks a request, the API returns a standard HTTP 200 response with `stop_reason: "refusal"` and a `stop_details` object containing the restriction category. Refusal rates on this model are materially higher than on previous Claude models.

Customers should handle `stop_reason: "refusal"` as a primary response path. Prompt-stage refusals (blocked before inference begins) are not billed. Mid-stream refusals (blocked after partial output) are billed for tokens generated before the block.

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**               | **In-Region endpoint URL**                                      | **Geo inference ID**          | **Global inference ID**           |
| ----------------- | -------------------------- | --------------------------------------------------------------- | ----------------------------- | --------------------------------- |
| `bedrock-runtime` | `anthropic.claude-fable-5` | N/A                                                             | `us.anthropic.claude-fable-5` | `global.anthropic.claude-fable-5` |
| `bedrock-mantle`  | `anthropic.claude-fable-5` | `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages` | N/A                           | N/A                               |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                     | **In-Region**                                                           | **Geo**                                                                 | **Global**                              |
| ------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------- |
| `us-east-1` (N. Virginia)      | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-east-2` (Ohio)             | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-1` (N. California)    | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-2` (Oregon)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ca-central-1` (Canada)        | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ca-west-1` (Calgary)          | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-central-1` (Frankfurt)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-central-2` (Zurich)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-north-1` (Stockholm)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-south-1` (Milan)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-south-2` (Spain)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-west-1` (Ireland)          | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-west-2` (London)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-west-3` (Paris)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-east-2` (Taipei)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-northeast-1` (Tokyo)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-northeast-2` (Seoul)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-northeast-3` (Osaka)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-south-1` (Mumbai)          | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-south-2` (Hyderabad)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-1` (Singapore)   | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-2` (Sydney)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-3` (Jakarta)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-4` (Melbourne)   | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-5` (Malaysia)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-6` (New Zealand) | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-7` (Thailand)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `il-central-1` (Tel Aviv)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `me-central-1` (UAE)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `me-south-1` (Bahrain)         | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `af-south-1` (Cape Town)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `sa-east-1` (São Paulo)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `mx-central-1` (Mexico)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |

## Data Retention

To use this model, you must opt in to provider data sharing by setting your data retention mode to `provider_data_share` via the Data Retention API. There is no console UI for this setting at launch. For more information, see [Amazon Bedrock abuse detection](abuse-detection.md "abuse-detection.md").

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, please refer to [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

###### Invoke & Converse

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='anthropic.claude-fable-5',
    body=json.dumps({
        'messages': [{'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
        'max_tokens': 1024
    })
)
print(json.loads(response['body'].read()))
```

###### Messages

```
pip install -U "anthropic[bedrock]"
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

```
from anthropic import AnthropicBedrockMantle

client = AnthropicBedrockMantle(aws_region="us-east-1")

message = client.messages.create(
    model="anthropic.claude-fable-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(message.content[0].text)
```
