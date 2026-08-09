# Embed v4

## Three overlapping circles in dark green, coral, and purple colors forming a logo or icon. Cohere — Embed v4

## Model Details

Embed v4 is Cohere's unified multimodal embedding model that processes text, images, and mixed content in a single model for search and RAG. For more information about model development and performance, see the [model/service card](https://docs.cohere.com/docs/cohere-embed "https://docs.cohere.com/docs/cohere-embed").

- **Model launch date:** Apr 15, 2025
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 128K tokens
- **Marketplace product ID:** `prod-ft3cj5gst3spo`

| **Input Modalities**                                                           | **Output Modalities**                                                          | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")**  | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Green circle with white checkmark icon. Embedding                              | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime`                                                |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image  | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Red circle with white X icon indicating error, cancel, or close action. `bedrock-mantle`                 |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech | Green circle with white checkmark icon. `Invoke`                                           |                                                                                                          |
| Green circle with white checkmark icon. Text                                   | Red circle with white X icon indicating error, cancel, or close action. Text   | Red circle with white X icon indicating error, cancel, or close action. `Converse`         |                                                                                                          |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video  |                                                                                            |                                                                                                          |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                 | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Abuse detection](bedrock/latest/userguide/abuse-detection.md "bedrock/latest/userguide/abuse-detection.md")<br>• Green circle with white checkmark icon. [Knowledge base](bedrock/latest/userguide/knowledge-base.md "bedrock/latest/userguide/knowledge-base.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](bedrock/latest/userguide/prompt-routing.md "bedrock/latest/userguide/prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Response streaming](bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Guardrails](bedrock/latest/userguide/guardrails.md "bedrock/latest/userguide/guardrails.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](bedrock/latest/userguide/prompt-management-optimize.md "bedrock/latest/userguide/prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](bedrock/latest/userguide/count-tokens.md "bedrock/latest/userguide/count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Model evaluation](bedrock/latest/userguide/evaluation.md "bedrock/latest/userguide/evaluation.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt management](bedrock/latest/userguide/prompt-management.md "bedrock/latest/userguide/prompt-management.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Flows](bedrock/latest/userguide/flows.md "bedrock/latest/userguide/flows.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Agents](bedrock/latest/userguide/agents.md "bedrock/latest/userguide/agents.md") |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**      | **Model ID**        | **In-Region endpoint URL**                       | **Geo inference ID**                         | **Global inference ID**    |
| ----------------- | ------------------- | ------------------------------------------------ | -------------------------------------------- | -------------------------- |
| `bedrock-runtime` | `cohere.embed-v4:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.cohere.embed-v4:0``eu.cohere.embed-v4:0` | `global.cohere.embed-v4:0` |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                   | **In-Region**                                                           | **Geo**                                                                 | **Global**                              |
| ---------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------- |
| `us-east-1` (N. Virginia)    | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-east-2` (Ohio)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-1` (N. California)  | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-2` (Oregon)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ca-central-1` (Canada)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-central-1` (Frankfurt)   | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-central-2` (Zurich)      | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-north-1` (Stockholm)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-south-1` (Milan)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-south-2` (Spain)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-west-1` (Ireland)        | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-west-2` (London)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-west-3` (Paris)          | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ap-northeast-1` (Tokyo)     | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-northeast-2` (Seoul)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-northeast-3` (Osaka)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-south-1` (Mumbai)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-south-2` (Hyderabad)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-1` (Singapore) | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-2` (Sydney)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-3` (Jakarta)   | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-4` (Melbourne) | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `sa-east-1` (São Paulo)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.cohere.embed-v4:0`

| **Source Region**         | **Destination Regions**                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| us-east-1 (N. Virginia)   | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-east-2 (Ohio)          | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-west-1 (N. California) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) |
| us-west-2 (Oregon)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |

**Geo: EU**

Geo Inference ID: `eu.cohere.embed-v4:0`

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

**Global inference details**

| **Global Inference ID**  | **Americas**                                                                                                                                                 | **EMEA**                                                                                                                                                                                                  | **Asia Pacific**                                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| global.cohere.embed-v4:0 | • us-east-1 (N. Virginia)<br>• us-east-2 (Ohio)<br>• us-west-1 (N. California)<br>• us-west-2 (Oregon)<br>• ca-central-1 (Canada)<br>• sa-east-1 (São Paulo) | • eu-central-1 (Frankfurt)<br>• eu-central-2 (Zurich)<br>• eu-north-1 (Stockholm)<br>• eu-south-1 (Milan)<br>• eu-south-2 (Spain)<br>• eu-west-1 (Ireland)<br>• eu-west-2 (London)<br>• eu-west-3 (Paris) | • ap-northeast-1 (Tokyo)<br>• ap-northeast-2 (Seoul)<br>• ap-northeast-3 (Osaka)<br>• ap-south-1 (Mumbai)<br>• ap-south-2 (Hyderabad)<br>• ap-southeast-1 (Singapore)<br>• ap-southeast-2 (Sydney)<br>• ap-southeast-3 (Jakarta)<br>• ap-southeast-4 (Melbourne) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](bedrock/latest/userguide/quotas-increase.md "bedrock/latest/userguide/quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](general/latest/gr/bedrock.md#limits_bedrock "general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='cohere.embed-v4:0',
    body=json.dumps({
            'texts': ['What are the different services that you offer?'],
            'input_type': 'search_document',
            'embedding_types': ['float']
    })
)
print(json.loads(response['body'].read()))
```
