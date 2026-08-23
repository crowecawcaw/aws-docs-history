# Daybreak Blue: GPT-5.6 Sol

## Icon showing a circular pattern with interwoven curved segments forming a pinwheel design. OpenAI — Daybreak Blue: GPT-5.6 Sol

## Model Details

Daybreak Blue: GPT-5.6 Sol is a specialized OpenAI model for verified defenders conducting advanced, authorized cybersecurity work.

###### Note

Access to this model is limited to eligible customers. To learn more, see [Accelerate cyber defense with OpenAI and AWS](https://aws.amazon.com/blogs/machine-learning/accelerate-cyber-defense-with-openai-and-aws-daybreak-red-daybreak-blue-now-available-to-eligible-customers-on-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/accelerate-cyber-defense-with-openai-and-aws-daybreak-red-daybreak-blue-now-available-to-eligible-customers-on-amazon-bedrock/").

- **Model launch date:** August 12, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 1M tokens
- **Languages:** English, Spanish, French, German, Portuguese, Italian, Dutch, Russian, Chinese (Simplified and Traditional), Japanese, Korean, Arabic, Hindi, Turkish, Polish, Ukrainian, and other languages.
- **Fine-tuning supported:** No
- **Supported use cases:** Vulnerability discovery, detection engineering, and incident response.

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                                                    | **[Endpoints supported](endpoints.md "endpoints.md")**                                    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Green circle with white checkmark icon. `Responses`                                        | Red circle with white X icon indicating error, cancel, or close action. `bedrock-runtime` |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Green circle with white checkmark icon. `bedrock-mantle`                                  |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Red circle with white X icon indicating error, cancel, or close action. `Invoke`           |                                                                                           |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Red circle with white X icon indicating error, cancel, or close action. `Converse`         |                                                                                           |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                            |                                                                                           |

_On `bedrock-mantle`, this model is served at `/openai/v1/responses`, not the default `/v1/responses`._

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                           | **Not Supported** |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| • Green circle with white checkmark icon. [Server-side tool calling](tool-use.md "tool-use.md")<br>• Green circle with white checkmark icon. [Projects](projects.md "projects.md")<br>• Green circle with white checkmark icon. [Prompt caching](prompt-caching.md "prompt-caching.md") | —                 |

## Pricing

**Short Context Window (272K)**

| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** |
| -------------------- | --------- | --------------------------- | ---------------------- | ---------- |
| In-Region            | $5.50     | $6.875                      | $0.55                  | $33.00     |

**Long Context Window (1M)**

| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** |
| -------------------- | --------- | --------------------------- | ---------------------- | ---------- |
| In-Region            | $11.00    | $13.75                      | $1.10                  | $49.50     |

_All prices are per 1 million tokens. Pricing shown is for the Standard tier. Priority and Flex tiers are not supported for this model._

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**     | **Model ID**                       | **In-Region endpoint URL**                          | **Geo inference ID** | **Global inference ID** |
| ---------------- | ---------------------------------- | --------------------------------------------------- | -------------------- | ----------------------- |
| `bedrock-mantle` | `openai.gpt-daybreak-blue-5.6-sol` | `https://bedrock-mantle.{region}.api.aws/openai/v1` | Not supported        | Not supported           |

_For example, if region is us-east-2 (Ohio), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-2.api.aws/openai/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**         | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| ------------------ | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-2` (Ohio) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Quotas and Limits

Model access is only available to eligible customers. Access to this model requires enrollment in Trusted Access for Cyber from OpenAI. To enroll, contact OpenAI or reach out to your AWS account team for guidance on eligibility. Once approved, work with your account team to request access on AWS.

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

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
OPENAI_BASE_URL="https://bedrock-mantle.us-east-2.api.aws/openai/v1"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Responses API

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-daybreak-blue-5.6-sol",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```
