# Claude 3 Haiku

## Orange rounded square icon with white radial loading spinner design. Anthropic — Claude 3 Haiku

## Model Details

Claude 3 Haiku is Anthropic's fastest and most compact Claude 3 model, optimized for speed and efficiency in near-instant responses. For more information about model development and performance, see the [model/service card](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf "https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf").

- **Model launch date:** Mar 13, 2024
- **Model EOL date:** September 10, 2026
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Legacy (certain regions)
- **Context window:** 200K tokens
- **Max output tokens:** 4K
- **Knowledge cutoff:** Aug 2023
- **Marketplace product ID:** `prod-ozonys2hmmpeu`

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")**  | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime`                                                |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Red circle with white X icon indicating error, cancel, or close action. `bedrock-mantle`                 |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                           |                                                                                                          |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                         |                                                                                                          |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                            |                                                                                                          |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**      | **Model ID**                             | **In-Region endpoint URL**                       | **Geo inference ID**                                                                   | **Global inference ID** |
| ----------------- | ---------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------- | ----------------------- |
| `bedrock-runtime` | `anthropic.claude-3-haiku-20240307-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.anthropic.claude-3-haiku-20240307-v1:0``eu.anthropic.claude-3-haiku-20240307-v1:0` | N/A                     |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                   | **In-Region**                                                           | **Geo**                                                                 | **Global**                                                              |
| ---------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia)    | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-2` (Ohio)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)         | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `us-gov-east-1` (GovCloud)   | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `us-gov-west-1` (GovCloud)   | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ca-central-1` (Canada)      | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-central-1` (Frankfurt)   | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-central-2` (Zurich)      | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-1` (Ireland)        | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-2` (London)         | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-3` (Paris)          | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-northeast-1` (Tokyo)     | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-northeast-2` (Seoul)     | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-south-1` (Mumbai)        | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-1` (Singapore) | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-2` (Sydney)    | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `sa-east-1` (São Paulo)      | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.anthropic.claude-3-haiku-20240307-v1:0`

| **Source Region**                      | **Destination Regions**                                                        |
| -------------------------------------- | ------------------------------------------------------------------------------ |
| us-east-1 (N. Virginia)                | us-east-1 (N. Virginia), us-west-2 (Oregon)                                    |
| us-east-2 (Ohio)                       | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                  |
| us-west-2 (Oregon)                     | us-east-1 (N. Virginia), us-west-2 (Oregon)                                    |
| us-gov-east-1 (AWS GovCloud (US-East)) | us-gov-east-1 (AWS GovCloud (US-East)), us-gov-west-1 (AWS GovCloud (US-West)) |

**Geo: EU**

Geo Inference ID: `eu.anthropic.claude-3-haiku-20240307-v1:0`

| **Source Region**        | **Destination Regions**                                          |
| ------------------------ | ---------------------------------------------------------------- |
| eu-central-1 (Frankfurt) | eu-central-1 (Frankfurt), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-west-1 (Ireland)      | eu-central-1 (Frankfurt), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-west-3 (Paris)        | eu-central-1 (Frankfurt), eu-west-1 (Ireland), eu-west-3 (Paris) |

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
    modelId='anthropic.claude-3-haiku-20240307-v1:0',
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
    modelId='anthropic.claude-3-haiku-20240307-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
