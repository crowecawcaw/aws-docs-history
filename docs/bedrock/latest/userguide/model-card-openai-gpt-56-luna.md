# GPT-5.6 Luna

## Icon showing a circular pattern with interwoven curved segments forming a pinwheel design. OpenAI — GPT-5.6 Luna

## Model Details

GPT-5.6 Luna is the fast and affordable model from OpenAI. Use Luna for high-volume inference tasks like classification, summarization, routing, and real-time applications where latency and cost per token matter most. For more information about model development and performance, see the [model/service card](https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf "https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf").

- **Model launch date:** July 13, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 1M tokens

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")** | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Green circle with white checkmark icon. `Responses`                                       | Green circle with white checkmark icon. `bedrock-runtime`                                                |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Green circle with white checkmark icon. `Chat Completions`                                | Green circle with white checkmark icon. `bedrock-mantle`                                                 |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Red circle with white X icon indicating error, cancel, or close action. `Invoke`          |                                                                                                          |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                        |                                                                                                          |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                           |                                                                                                          |

_On `bedrock-mantle`, this model is served at `/openai/v1/responses`, not the default `/v1/responses`._

###### Tip

Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") for details.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Projects (default project only)](bedrock/latest/userguide/projects.md "bedrock/latest/userguide/projects.md")<br>• Green circle with white checkmark icon. [Invocation logs](bedrock/latest/userguide/model-invocation-logging.md "bedrock/latest/userguide/model-invocation-logging.md")<br>• Green circle with white checkmark icon. [Response streaming](bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Abuse detection](bedrock/latest/userguide/abuse-detection.md "bedrock/latest/userguide/abuse-detection.md")<br>• Green circle with white checkmark icon. [Guardrails](bedrock/latest/userguide/guardrails.md "bedrock/latest/userguide/guardrails.md") ([Converse API](bedrock/latest/userguide/conversation-inference.md "bedrock/latest/userguide/conversation-inference.md") only) | • Red circle with white X icon indicating error, cancel, or close action. [Server-side tool use](bedrock/latest/userguide/tool-use.md "bedrock/latest/userguide/tool-use.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](bedrock/latest/userguide/prompt-routing.md "bedrock/latest/userguide/prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](bedrock/latest/userguide/count-tokens.md "bedrock/latest/userguide/count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Structured outputs](bedrock/latest/userguide/structured-output.md "bedrock/latest/userguide/structured-output.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Application inference profiles](bedrock/latest/userguide/cost-mgmt-application-inference-profiles.md "bedrock/latest/userguide/cost-mgmt-application-inference-profiles.md") |

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Not Supported** |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| • Green circle with white checkmark icon. [Server-side tool calling](bedrock/latest/userguide/tool-use.md "bedrock/latest/userguide/tool-use.md")<br>• Green circle with white checkmark icon. [Projects](bedrock/latest/userguide/projects.md "bedrock/latest/userguide/projects.md")<br>• Green circle with white checkmark icon. [Prompt caching](bedrock/latest/userguide/prompt-caching.md "bedrock/latest/userguide/prompt-caching.md") | —                 |

## Pricing

**Short Context Window (272K)**

| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** |
| -------------------- | --------- | --------------------------- | ---------------------- | ---------- |
| In-Region            | $0.22     | $0.275                      | $0.022                 | $1.32      |
| Geo CRIS             | $0.22     | $0.275                      | $0.022                 | $1.32      |
| Global CRIS          | $0.20     | $0.25                       | $0.02                  | $1.20      |

**Long Context Window (1M)**

| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** |
| -------------------- | --------- | --------------------------- | ---------------------- | ---------- |
| In-Region            | $0.44     | $0.55                       | $0.044                 | $1.98      |
| Geo CRIS             | $0.44     | $0.55                       | $0.044                 | $1.98      |
| Global CRIS          | $0.40     | $0.50                       | $0.04                  | $1.80      |

_All prices are per 1 million tokens. Pricing shown is for the Standard tier. Priority and Flex tiers are not supported for this model._

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**      | **Model ID**          | **In-Region endpoint URL**                          | **Geo inference ID**     | **Global inference ID**      |
| ----------------- | --------------------- | --------------------------------------------------- | ------------------------ | ---------------------------- |
| `bedrock-mantle`  | `openai.gpt-5.6-luna` | `https://bedrock-mantle.{region}.api.aws/openai/v1` | Not supported            | Not supported                |
| `bedrock-runtime` | `openai.gpt-5.6-luna` | Not supported                                       | `us.openai.gpt-5.6-luna` | `global.openai.gpt-5.6-luna` |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws/openai/v1". On `bedrock-runtime`, the base URL is "https://bedrock-runtime.{region}.amazonaws.com/openai/v1" and requests must name the geographic cross-Region inference ID `us.openai.gpt-5.6-luna` as the model._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-mantle` endpoint**

| **Region**                | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| ------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-2` (Ohio)        | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)      | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

**Availability using the `bedrock-runtime` endpoint**

| **Region**                     | **In-Region**                                                           | **Geo**                                                                 | **Global**                              |
| ------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------- |
| `us-east-1` (N. Virginia)      | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-east-2` (Ohio)             | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-1` (N. California)    | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-2` (Oregon)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ca-central-1` (Canada)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ca-west-1` (Calgary)          | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
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

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](bedrock/latest/userguide/quotas-increase.md "bedrock/latest/userguide/quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](general/latest/gr/bedrock.md#limits_bedrock "general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Responses API

```
pip install openai
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

bedrock-mantle

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/openai/v1"
```

bedrock-runtime

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1"
```

###### Note

On `bedrock-runtime`, name a cross-Region inference profile as the model — `us.openai.gpt-5.6-luna` or `global.openai.gpt-5.6-luna`. This model is not available for in-Region inference on that endpoint. Your IAM identity also needs `bedrock:InvokeModel` on your account's default project (`arn:aws:bedrock:{region}:{account-id}:project/default`) in addition to the inference profile.

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

bedrock-mantle

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-5.6-luna",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

bedrock-runtime

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="us.openai.gpt-5.6-luna",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```
