# GPT-5.6 Luna

## Icon showing a circular pattern with interwoven curved segments forming a pinwheel design. OpenAI — GPT-5.6 Luna

## Model Details

GPT-5.6 Luna is the fast and affordable model from OpenAI. Use Luna for high-volume inference tasks like classification, summarization, routing, and real-time applications where latency and cost per token matter most. For more information about model development and performance, see the [model/service card](https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf "https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf").

- **Model launch date:** July 13, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 272K tokens

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                                                    | **[Endpoints supported](endpoints.md "endpoints.md")**                                    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Green circle with white checkmark icon. `Responses`                                        | Red circle with white X icon indicating error, cancel, or close action. `bedrock-runtime` |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Green circle with white checkmark icon. `bedrock-mantle`                                  |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Red circle with white X icon indicating error, cancel, or close action. `Invoke`           |                                                                                           |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Red circle with white X icon indicating error, cancel, or close action. `Converse`         |                                                                                           |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                            |                                                                                           |

###### Note

This model is available on the `openai/v1/responses` path on the `bedrock-mantle` endpoint. This is different from the `v1/responses` path used by other models on the responses endpoint.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                           | **Not Supported** |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| • Green circle with white checkmark icon. [Server-side tool calling](tool-use.md "tool-use.md")<br>• Green circle with white checkmark icon. [Projects](projects.md "projects.md")<br>• Green circle with white checkmark icon. [Prompt caching](prompt-caching.md "prompt-caching.md") | —                 |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**     | **Model ID**          | **In-Region endpoint URL**                          | **Geo inference ID** | **Global inference ID** |
| ---------------- | --------------------- | --------------------------------------------------- | -------------------- | ----------------------- |
| `bedrock-mantle` | `openai.gpt-5.6-luna` | `https://bedrock-mantle.{region}.api.aws/openai/v1` | Not supported        | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws/openai/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| ------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-2` (Ohio)        | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)      | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, please refer to [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Responses API

```
pip install openai
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

Responses API

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/openai/v1"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Responses API

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-5.6-luna",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```
