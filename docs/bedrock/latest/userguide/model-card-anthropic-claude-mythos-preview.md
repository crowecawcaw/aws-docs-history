# Claude Mythos Preview

## Orange rounded square icon with white radial loading spinner design. Anthropic — Claude Mythos Preview

## Model Details

According to Anthropic, Claude Mythos Preview (gated research preview) is a new class of intelligence built for ambitious projects focusing on cybersecurity, autonomous coding, and long-running agents.

Available only as a gated research preview with access prioritized for defensive cybersecurity use cases.

- **Model launch date:** Apr 07, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Preview
- **Context window:** 1M tokens
- **Max output tokens:** 128K
- **Reasoning:** Supported (`thinking.type: "adaptive"` only). For more information, see [Adaptive thinking](claude-messages-adaptive-thinking.md "claude-messages-adaptive-thinking.md").
- **Knowledge cutoff:** Dec 2025

| **Input Modalities**                                                           | **Output Modalities**                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |

## Endpoints and APIs supported

The following tables show which endpoints and APIs are supported for Claude Mythos (Preview). For more information, see [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md").

**Endpoint support**

| **Endpoint**      | **Supported** |
| ----------------- | ------------- |
| `bedrock-runtime` | not-supported |
| `bedrock-mantle`  | supported     |

**APIs supported on `bedrock-runtime` endpoint**

| **Messages**  | **Responses** | **Chat Completions** | **Converse**  | **Invoke**    |
| ------------- | ------------- | -------------------- | ------------- | ------------- |
| not-supported | not-supported | not-supported        | not-supported | not-supported |

**APIs supported on `bedrock-mantle` endpoint**

| **Messages** | **Responses** | **Chat Completions** | **Converse**  | **Invoke**    |
| ------------ | ------------- | -------------------- | ------------- | ------------- |
| supported    | not-supported | not-supported        | not-supported | not-supported |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                      | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Green circle with white checkmark icon. [Count tokens](count-tokens.md "count-tokens.md") | • Red circle with white X icon indicating error, cancel, or close action. [Guardrails](guardrails.md "guardrails.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Model evaluation](evaluation.md "evaluation.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt management](prompt-management.md "prompt-management.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Flows](flows.md "flows.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Agents](agents.md "agents.md") |

**Prompt caching**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoints** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ----------------------------------------------- |
| Yes                          | 4,096                               | 4                                     | 5 minutes, 1 hour | `system`, `messages`, and `tools`               |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**     | **Model ID**                      | **In-Region endpoint URL**                | **Geo inference ID** | **Global inference ID** |
| ---------------- | --------------------------------- | ----------------------------------------- | -------------------- | ----------------------- |
| `bedrock-mantle` | `anthropic.claude-mythos-preview` | `https://bedrock-mantle.{region}.api.aws` | N/A                  | N/A                     |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                   | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| ---------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia)    | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-4` (Melbourne) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software.

```
pip install -U "anthropic[bedrock]"
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Messages API

```
from anthropic import AnthropicBedrockMantle

client = AnthropicBedrockMantle(aws_region="us-east-1")

message = client.messages.create(
    model="anthropic.claude-mythos-preview",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}],
)

print(message.content[0].text)
```
