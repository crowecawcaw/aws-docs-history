# Claude Opus 4.8

## Orange rounded square icon with white radial loading or progress indicator symbol. Anthropic — Claude Opus 4.8

## Model Details

Claude Opus 4.8 is an Anthropic Opus model optimized for coding, agents, and deeper reasoning in enterprise workflows.

- **Model launch date:** May 28, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 1M tokens
- **Max output tokens:** 128K
- **Reasoning:** Supported
- **Knowledge cutoff:** January 2026
- **Marketplace product ID:** `prod-bk5rjg4eo2pke`

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                                                    | **[Endpoints supported](endpoints.md "endpoints.md")**    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime` |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Green circle with white checkmark icon. `bedrock-mantle`  |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                           |                                                           |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                         |                                                           |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     | Green circle with white checkmark icon. `Messages`                                         |                                                           |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Green circle with white checkmark icon. [Count tokens](count-tokens.md "count-tokens.md")<br>• Green circle with white checkmark icon. [Computer use](computer-use.md "computer-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Guardrails](guardrails.md "guardrails.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Model evaluation](evaluation.md "evaluation.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt management](prompt-management.md "prompt-management.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Flows](flows.md "flows.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Agents](agents.md "agents.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Structured outputs](structured-outputs.md "structured-outputs.md") |

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Green circle with white checkmark icon. [Guardrails](guardrails.md "guardrails.md")<br>• Green circle with white checkmark icon. [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Green circle with white checkmark icon. [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• Green circle with white checkmark icon. [Model evaluation](evaluation.md "evaluation.md")<br>• Green circle with white checkmark icon. [Prompt management](prompt-management.md "prompt-management.md")<br>• Green circle with white checkmark icon. [Flows](flows.md "flows.md")<br>• Green circle with white checkmark icon. [Agents](agents.md "agents.md")<br>• Green circle with white checkmark icon. [Computer use](computer-use.md "computer-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](count-tokens.md "count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Structured outputs](structured-outputs.md "structured-outputs.md") |

**Prompt caching**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoints** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ----------------------------------------------- |
| Yes                          | 4,096                               | 4                                     | 5 minutes, 1 hour | `system`, `messages`, and `tools`               |

**Computer use using `bedrock-runtime` and `bedrock-mantle` endpoints**

For more information, see [Computer use](computer-use.md "computer-use.md").

| **Tool type**       | **Beta header**           |
| ------------------- | ------------------------- |
| `computer_20251124` | `computer-use-2025-11-24` |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                | **In-Region endpoint URL**                                      | **Geo inference ID**                                                                                                     | **Global inference ID**            |
| ----------------- | --------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| `bedrock-runtime` | `anthropic.claude-opus-4-8` | N/A                                                             | `us.anthropic.claude-opus-4-8``eu.anthropic.claude-opus-4-8``jp.anthropic.claude-opus-4-8``au.anthropic.claude-opus-4-8` | `global.anthropic.claude-opus-4-8` |
| `bedrock-mantle`  | `anthropic.claude-opus-4-8` | `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages` | N/A                                                                                                                      | N/A                                |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/anthropic/v1/messages"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options:

- **In-Region** keeps requests within a single Region for strict compliance.
- **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency.
- **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints.

For more details, see the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page.

| **Region**                      | **In-Region**                                                           | **Geo**                                                                 | **Global**                                                              |
| ------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia)       | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-east-2` (Ohio)              | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-west-1` (N. California)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-west-2` (Oregon)            | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `ca-central-1` (Canada)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `ca-west-1` (Calgary)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-gov-west-1` (GovCloud West) | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `us-gov-east-1` (GovCloud East) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-central-1` (Frankfurt)      | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `eu-central-2` (Zurich)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `eu-north-1` (Stockholm)        | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `eu-south-1` (Milan)            | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `eu-south-2` (Spain)            | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `eu-west-1` (Ireland)           | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `eu-west-2` (London)            | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `eu-west-3` (Paris)             | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `ap-east-2` (Taipei)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-northeast-1` (Tokyo)        | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `ap-northeast-2` (Seoul)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-northeast-3` (Osaka)        | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `ap-south-1` (Mumbai)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-south-2` (Hyderabad)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-1` (Singapore)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-2` (Sydney)       | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `ap-southeast-3` (Jakarta)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-4` (Melbourne)    | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `ap-southeast-5` (Malaysia)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-6` (New Zealand)  | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-7` (Thailand)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `il-central-1` (Tel Aviv)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `me-central-1` (UAE)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `me-south-1` (Bahrain)          | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `af-south-1` (Cape Town)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `sa-east-1` (São Paulo)         | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `mx-central-1` (Mexico)         | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.anthropic.claude-opus-4-8`

| **Source Region**         | **Destination Regions**                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| us-east-1 (N. Virginia)   | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-east-2 (Ohio)          | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-west-1 (N. California) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) |
| us-west-2 (Oregon)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| ca-central-1 (Canada)     | ca-central-1 (Canada), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)     |
| ca-west-1 (Calgary)       | ca-west-1 (Calgary), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)       |

**Geo: EU**

Geo Inference ID: `eu.anthropic.claude-opus-4-8`

| **Source Region**        | **Destination Regions**                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eu-central-1 (Frankfurt) | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-central-2 (Zurich)    | eu-central-1 (Frankfurt), eu-central-2 (Zurich), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-north-1 (Stockholm)   | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-south-1 (Milan)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-south-2 (Spain)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-west-1 (Ireland)      | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-west-2 (London)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-2 (London), eu-west-3 (Paris)    |
| eu-west-3 (Paris)        | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |

**Geo: JP**

Geo Inference ID: `jp.anthropic.claude-opus-4-8`

| **Source Region**      | **Destination Regions**                        |
| ---------------------- | ---------------------------------------------- |
| ap-northeast-1 (Tokyo) | ap-northeast-1 (Tokyo), ap-northeast-3 (Osaka) |
| ap-northeast-3 (Osaka) | ap-northeast-1 (Tokyo), ap-northeast-3 (Osaka) |

**Geo: AU**

Geo Inference ID: `au.anthropic.claude-opus-4-8`

| **Source Region**          | **Destination Regions**                             |
| -------------------------- | --------------------------------------------------- |
| ap-southeast-2 (Sydney)    | ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |
| ap-southeast-4 (Melbourne) | ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |

**Global inference details**

| **Global Inference ID**          | **Americas**                                                                                                                                                                                                     | **EMEA**                                                                                                                                                                                                                                                                                                             | **Asia Pacific**                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| global.anthropic.claude-opus-4-8 | • us-east-1 (N. Virginia)<br>• us-east-2 (Ohio)<br>• us-west-1 (N. California)<br>• us-west-2 (Oregon)<br>• ca-central-1 (Canada)<br>• ca-west-1 (Calgary)<br>• sa-east-1 (São Paulo)<br>• mx-central-1 (Mexico) | • eu-central-1 (Frankfurt)<br>• eu-central-2 (Zurich)<br>• eu-north-1 (Stockholm)<br>• eu-south-1 (Milan)<br>• eu-south-2 (Spain)<br>• eu-west-1 (Ireland)<br>• eu-west-2 (London)<br>• eu-west-3 (Paris)<br>• il-central-1 (Tel Aviv)<br>• me-central-1 (UAE)<br>• me-south-1 (Bahrain)<br>• af-south-1 (Cape Town) | • ap-east-2 (Taipei)<br>• ap-northeast-1 (Tokyo)<br>• ap-northeast-2 (Seoul)<br>• ap-northeast-3 (Osaka)<br>• ap-south-1 (Mumbai)<br>• ap-south-2 (Hyderabad)<br>• ap-southeast-1 (Singapore)<br>• ap-southeast-2 (Sydney)<br>• ap-southeast-3 (Jakarta)<br>• ap-southeast-4 (Melbourne)<br>• ap-southeast-5 (Malaysia)<br>• ap-southeast-6 (New Zealand)<br>• ap-southeast-7 (Thailand) |

## Quotas and Limits

Your AWS account has default quotas for Amazon Bedrock. These quotas might change depending on regional factors, payment history, or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") and the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

Default quotas for Claude Opus 4.8 are 20M input TPM and 4M output TPM on `bedrock-mantle` and 30M TPM on `bedrock-runtime` for each supported region. Claude Opus 4.8 does not have a requests-per-minute (RPM) quota; throttling is governed solely by the token-per-minute (TPM) quotas above.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Messages API

```
pip install -U "anthropic[bedrock]"
```

Invoke/Converse API

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

Messages API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

Invoke/Converse API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Messages API

```
from anthropic import AnthropicBedrockMantle

client = AnthropicBedrockMantle(aws_region="us-east-1")

message = client.messages.create(
    model="anthropic.claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}],
)

print(message.content[0].text)
```

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='anthropic.claude-opus-4-8',
    body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
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
    modelId='anthropic.claude-opus-4-8',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
