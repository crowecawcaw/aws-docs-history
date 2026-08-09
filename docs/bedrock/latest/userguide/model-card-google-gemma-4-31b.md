# Gemma 4 31B

## Google logo with multicolored G letter icon. Google — Gemma 4 31B

## Model Details

Gemma 4 31B is Google's 30.7-billion parameter dense model with built-in reasoning, native function calling, and multimodal input across text and image, supporting a 256K token context window. For more information about model development and performance, see the [model/service card](https://huggingface.co/google/gemma-4-31B-it "https://huggingface.co/google/gemma-4-31B-it").

- **Model launch date:** Jun 10, 2025
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://ai.google.dev/gemma/apache_2 "https://ai.google.dev/gemma/apache_2")
- **Model lifecycle:** Active
- **Context window:** 256K tokens

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")** | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Green circle with white checkmark icon. `Responses`                                       | Red circle with white X icon indicating error, cancel, or close action. `bedrock-runtime`                |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Green circle with white checkmark icon. `Chat Completions`                                | Green circle with white checkmark icon. `bedrock-mantle`                                                 |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Red circle with white X icon indicating error, cancel, or close action. `Invoke`          |                                                                                                          |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Red circle with white X icon indicating error, cancel, or close action. `Converse`        |                                                                                                          |
| Green circle with white checkmark icon. Video                                  | Red circle with white X icon indicating error, cancel, or close action. Video     | Red circle with white X icon indicating error, cancel, or close action. `Messages`        |                                                                                                          |

###### Note

Gemma 4 models are available only on the `bedrock-mantle` endpoint.

This model is available on the `openai/v1/responses` path on the `bedrock-mantle` endpoint. This is different from the `v1/responses` path used by other models on the responses endpoint.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                  | **Not Supported** |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| • Green circle with white checkmark icon. [Client-side tool calling](bedrock/latest/userguide/tool-use.md "bedrock/latest/userguide/tool-use.md")<br>• Green circle with white checkmark icon. [Reasoning](bedrock/latest/userguide/reasoning.md "bedrock/latest/userguide/reasoning.md")<br>• Green circle with white checkmark icon. [Projects](bedrock/latest/userguide/projects.md "bedrock/latest/userguide/projects.md") | —                 |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**     | **Model ID**         | **In-Region endpoint URL**                          | **Geo inference ID** | **Global inference ID** |
| ---------------- | -------------------- | --------------------------------------------------- | -------------------- | ----------------------- |
| `bedrock-mantle` | `google.gemma-4-31b` | `https://bedrock-mantle.{region}.api.aws/openai/v1` | Not supported        | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws/openai/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                            | **Flex**                                | **Reserved**                                                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Green circle with white checkmark icon. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                 | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| -------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia)  | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-2` (Ohio)         | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-central-1` (Frankfurt) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](bedrock/latest/userguide/quotas-increase.md "bedrock/latest/userguide/quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](general/latest/gr/bedrock.md#limits_bedrock "general/latest/gr/bedrock.md#limits_bedrock") for the model.

When consuming on-demand throughput on the `bedrock-mantle` endpoint, [available throughput scales over time](bedrock/latest/userguide/scaling-throughput-best-practices.md#scaling-ramp-up "bedrock/latest/userguide/scaling-throughput-best-practices.md#scaling-ramp-up"). Not all requests within your quota are guaranteed to succeed during periods of high demand, so ramping gradually is important. For this model, default limits aren't surfaced directly through Service Quotas, so we recommend following the ramp as your guide.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

```
pip install openai
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/openai/v1"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Chat Completions API

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="google.gemma-4-31b",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
    )
print(response)
```

Responses API

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="google.gemma-4-31b",
    input="Explain the benefits of mixture-of-experts architectures for production inference.",
    max_output_tokens=512,
)
print(response.output_text)
```

## Usage Considerations and Limitations

- **Reasoning mode** — Reasoning effort is honored on both the Chat Completions and Responses APIs, and the model performs the extended reasoning in both cases. However, the reasoning content is returned only by the Responses API. The Chat Completions API does not return the reasoning tokens, because the OpenAI Chat Completions specification does not support returning them.
- **Parallel tool calls** — Requesting more than one tool call in a single turn is not currently supported. Request tool calls one at a time.
- **Request payload size** — The total request body payload for Gemma 4 31B, including images and video, supports a maximum size of 3.5 MB.
