# Grok 4.6

## Icon showing the xAI logo. xAI — Grok 4.6

## Model Details

Grok 4.6 is xAI's frontier model built for coding, agentic tasks, and knowledge work. It builds on previous generations of Grok with a particular focus on long-running agents and more ambitious interactive work. It offers 500K context window and configurable reasoning efforts (low, medium, high, xhigh).

- **Model launch date:** August 18, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 500K tokens
- **Reasoning:** Supported (configurable: low, medium, high, xhigh)

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                    | **[Endpoints supported](endpoints.md "endpoints.md")**    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Green circle with white checkmark icon. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime` |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Green circle with white checkmark icon. `Chat Completions` | Green circle with white checkmark icon. `bedrock-mantle`  |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Converse`         |                                                           |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Invoke`           |                                                           |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                            |                                                           |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Projects (default project only)](projects.md "projects.md")<br>• Green circle with white checkmark icon. [Invocation logs](model-invocation-logging.md "model-invocation-logging.md")<br>• Green circle with white checkmark icon. [Response streaming](bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Application inference profiles](cost-mgmt-application-inference-profiles.md "cost-mgmt-application-inference-profiles.md") (`Invoke` and [Converse](conversation-inference.md "conversation-inference.md") APIs only; not supported with Responses or Chat Completions APIs)<br>• Green circle with white checkmark icon. [Implicit Prompt Caching](prompt-caching.md#prompt-caching-implicit "prompt-caching.md#prompt-caching-implicit")<br>• Green circle with white checkmark icon. [Reasoning](reasoning.md "reasoning.md") | • Red circle with white X icon indicating error, cancel, or close action. [Server-side tool use](tool-use.md "tool-use.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](count-tokens.md "count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Structured outputs](structured-output.md "structured-output.md") |

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Not Supported**                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| • Green circle with white checkmark icon. [Client-side tool calling](tool-use.md "tool-use.md")<br>• Green circle with white checkmark icon. [Reasoning](reasoning.md "reasoning.md")<br>• Green circle with white checkmark icon. [Projects](projects.md "projects.md")<br>• Green circle with white checkmark icon. Abuse detection<br>• Green circle with white checkmark icon. Response streaming<br>• Green circle with white checkmark icon. Structured outputs<br>• Green circle with white checkmark icon. [Implicit Prompt Caching](prompt-caching.md#prompt-caching-implicit "prompt-caching.md#prompt-caching-implicit") | • Red circle with white X icon indicating error, cancel, or close action. [Application inference profiles](cost-mgmt-application-inference-profiles.md "cost-mgmt-application-inference-profiles.md") (Responses and Chat Completions APIs only) |

## Pricing

| **Inference option** | **Input** | **Output** | **Cache read** |
| -------------------- | --------- | ---------- | -------------- |
| In-Region            | $2.20     | $6.60      | $0.55          |
| Geo CRIS             | $2.20     | $6.60      | $0.55          |
| Global CRIS          | $2.00     | $6.00      | $0.50          |

_All prices are per 1 million tokens. Pricing shown is for the Standard tier._

**Priority and Flex tier support:** In addition to Standard, Grok 4.6 supports the Priority and Flex service tiers. Priority is billed at **1.75x** the Standard per-token rate (a 75% premium) and Flex at **0.5x** the Standard rate (a 50% discount); apply these multipliers to the Standard rates shown above. For details on each service tier, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**   | **In-Region endpoint URL**                          | **Geo inference ID** | **Global inference ID** |
| ----------------- | -------------- | --------------------------------------------------- | -------------------- | ----------------------- |
| `bedrock-mantle`  | `xai.grok-4.6` | `https://bedrock-mantle.{region}.api.aws/openai/v1` | Not supported        | Not supported           |
| `bedrock-runtime` | `xai.grok-4.6` | Not supported                                       | `us.xai.grok-4.6`    | `global.xai.grok-4.6`   |

_For example, if region is us-west-2 (Oregon), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-west-2.api.aws/openai/v1". On `bedrock-runtime`, the base URL is "https://bedrock-runtime.{region}.amazonaws.com/openai/v1" and requests must name the geographic cross-Region inference ID `us.xai.grok-4.6` or `global.xai.grok-4.6` as the model._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers faster, prioritized processing for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                            | **Flex**                                | **Reserved**                                                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Green circle with white checkmark icon. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-mantle` endpoint**

| **Region**                      | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| ------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-west-2` (Oregon)            | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-gov-east-1` (GovCloud East) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

**Availability using the `bedrock-runtime` endpoint**

| **Region**                      | **In-Region**                                                           | **Geo**                                                                 | **Global**                                                              |
| ------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia)       | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-east-2` (Ohio)              | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-west-1` (N. California)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-west-2` (Oregon)            | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon.                                 |
| `us-gov-west-1` (GovCloud West) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `us-gov-east-1` (GovCloud East) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `ca-central-1` (Canada)         | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ca-west-1` (Calgary)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-central-1` (Frankfurt)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-central-2` (Zurich)         | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-north-1` (Stockholm)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-south-1` (Milan)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-south-2` (Spain)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-west-1` (Ireland)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-west-2` (London)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `eu-west-3` (Paris)             | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-east-2` (Taipei)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-northeast-1` (Tokyo)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-northeast-2` (Seoul)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-northeast-3` (Osaka)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-south-1` (Mumbai)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-south-2` (Hyderabad)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-1` (Singapore)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-2` (Sydney)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-3` (Jakarta)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-4` (Melbourne)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-5` (Malaysia)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-6` (New Zealand)  | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `ap-southeast-7` (Thailand)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `il-central-1` (Tel Aviv)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `me-central-1` (UAE)            | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `me-south-1` (Bahrain)          | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `af-south-1` (Cape Town)        | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |
| `sa-east-1` (São Paulo)         | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

###### Note

Grok 4.6 is an xAI model. Amazon Bedrock serves its Responses and Chat Completions APIs through OpenAI-compatible endpoints, so those examples use the OpenAI Python SDK as the client. Configure the SDK with your Amazon Bedrock API key and an Amazon Bedrock base URL as shown below; the requests invoke the xAI model on Amazon Bedrock and are not sent to OpenAI.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Responses API / Chat Completions API

```
pip install openai
```

Converse API

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

bedrock-mantle

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.us-west-2.api.aws/openai/v1"
```

bedrock-runtime

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1"
```

###### Note

On `bedrock-runtime`, name a cross-Region inference profile as the model — `us.xai.grok-4.6` or `global.xai.grok-4.6`. This model is not available for in-Region inference on that endpoint. Your IAM identity also needs `bedrock:InvokeModel` on your account's default project (`arn:aws:bedrock:{region}:{account-id}:project/default`) in addition to the inference profile.

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Responses API (bedrock-mantle)

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="xai.grok-4.6",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

Responses API (bedrock-runtime)

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="us.xai.grok-4.6",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

Chat Completions API (bedrock-mantle)

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="xai.grok-4.6",
    messages=[
        {"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}
    ]
)
print(response)
```

Chat Completions API (bedrock-runtime)

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="us.xai.grok-4.6",
    messages=[
        {"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}
    ]
)
print(response)
```

Converse API (bedrock-runtime)

```
import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId="us.xai.grok-4.6",
    messages=[
        {"role": "user", "content": [{"text": "Can you explain the features of Amazon Bedrock?"}]}
    ]
)
print(response["output"]["message"]["content"][0]["text"])
```

## Usage Considerations and Limitations

- **Reasoning effort** — Reasoning is always active by default. You can configure effort through the `reasoning` parameter: `"low"` (default), `"medium"`, `"high"`, or `"xhigh"`. Reasoning content is encrypted and can be returned by passing `include: ["reasoning.encrypted_content"]` in the Responses API request. You can send the encrypted content back in subsequent turns to provide reasoning context for multi-turn conversations. The Chat Completions API does not return reasoning tokens.

```
response = client.responses.create(
    model="us.xai.grok-4.6",
    reasoning={"effort": "high"},
    include=["reasoning.encrypted_content"],
    input="Explain quantum entanglement simply."
)
print(response.output_text)
```
