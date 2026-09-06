# Claude Mythos 5

## Anthropic — Claude Mythos 5

## Model Details

Claude Mythos 5 is Anthropic's most capable model for cybersecurity and life sciences, including vulnerability discovery, drug design, and biodefense screening. Access is currently limited due to the dual-use nature of these domains.

This model is a Preview and is made available to you as a "Beta Service" as defined in the AWS Service Terms. It is subject to your Agreement with AWS, the AWS Service Terms, and the applicable model EULA.

- **Model launch date:** June 9, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 1M tokens
- **Max output tokens:** 128K
- **Sampling parameters:** temperature must be 1.0 or unset; top\_p must be ≥ 0.99 and < 1.0, or unset; top\_k is not supported
- **Reasoning:** Supported (adaptive thinking is always on and cannot be disabled; effort level is configurable)
- **Knowledge cutoff:** January 2026
- **Marketplace product ID:** prod-kyryzgfmbtwtc

| **Input Modalities**                                                           | **Output Modalities**                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |

## Endpoints and APIs supported

The following tables show which endpoints and APIs are supported for Claude Mythos 5. For more information, see [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md").

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

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• [Implicit Prompt Caching](prompt-caching.md#prompt-caching-implicit "prompt-caching.md#prompt-caching-implicit")<br>• [Explicit Prompt Caching](prompt-caching.md#prompt-caching-explicit "prompt-caching.md#prompt-caching-explicit")<br>• [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• [Count tokens](count-tokens.md "count-tokens.md") | • [Guardrails](guardrails.md "guardrails.md")<br>• [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• [Model evaluation](evaluation.md "evaluation.md")<br>• [Prompt management](prompt-management.md "prompt-management.md")<br>• [Flows](flows.md "flows.md")<br>• [Agents](agents.md "agents.md")<br>• [Intelligent prompt routing](prompt-routing.md "prompt-routing.md") |

**Implicit and Explicit Prompt Caching using `bedrock-mantle` endpoint**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Explicit Prompt Caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoint** |
| ------------------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ---------------------------------------------- |
| Yes                                   | 512                                 | 4                                     | 5 minutes, 1 hour | `system`, `messages`, and `tools`              |

## Pricing

This model is a third-party model offered and billed through AWS Marketplace. Charges appear on your AWS bill and in AWS Cost Explorer under the model provider (not under Amazon Bedrock). For pricing, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**     | **Model ID**                | **In-Region endpoint URL**                                      | **Geo inference ID** | **Global inference ID** |
| ---------------- | --------------------------- | --------------------------------------------------------------- | -------------------- | ----------------------- |
| `bedrock-mantle` | `anthropic.claude-mythos-5` | `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages` | N/A                  | N/A                     |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws/anthropic/v1/messages"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-mantle` endpoint**

| **Region**                | **In-Region** | **Geo**       | **Global**    |
| ------------------------- | ------------- | ------------- | ------------- |
| `us-east-1` (N. Virginia) | supported     | not-supported | not-supported |

## Data retention

To use this model, you must opt in to provider data sharing by setting your data retention mode to `provider_data_share` via the Data Retention API. For more information, see [Amazon Bedrock abuse detection](abuse-detection.md "abuse-detection.md").

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

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
    model="anthropic.claude-mythos-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(message.content[0].text)
```
