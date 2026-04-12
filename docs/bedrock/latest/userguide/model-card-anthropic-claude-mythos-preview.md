# Claude Mythos Preview

## Anthropic — Claude Mythos Preview

## Model Details

According to Anthropic, Claude Mythos Preview (gated research preview) is a new class of intelligence built for ambitious projects focusing on cybersecurity, autonomous coding, and long-running agents.

Available only as a gated research preview with access prioritized for defensive cybersecurity use cases.

- **Model launch date:** Apr 07, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Preview
- **Context window:** 1M tokens
- **Max output tokens:** 128K
- **Reasoning:** Supported
- **Knowledge cutoff:** Dec 2025

| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.md "apis.md")** | **[Endpoints supported](endpoints.md "endpoints.md")** |
| -------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------ |
| No Audio             | No Embedding          | No `Responses`                          | No `bedrock-runtime`                                   |
| Yes Image            | No Image              | No `Chat Completions`                   | Yes `bedrock-mantle`                                   |
| No Speech            | No Speech             | No `Invoke`                             |                                                        |
| Yes Text             | Yes Text              | No `Converse`                           |                                                        |
| No Video             | No Video              | Yes `Messages`                          |                                                        |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                           | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Yes [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") | • No [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• No [Guardrails](guardrails.md "guardrails.md")<br>• No [Count tokens](count-tokens.md "count-tokens.md")<br>• No [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• No [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• No [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• No [Model evaluation](evaluation.md "evaluation.md")<br>• No [Prompt management](prompt-management.md "prompt-management.md")<br>• No [Flows](flows.md "flows.md")<br>• No [Agents](agents.md "agents.md") |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**     | **Model ID**                      | **In-Region endpoint URL**                   | **Geo inference ID** | **Global inference ID** |
| ---------------- | --------------------------------- | -------------------------------------------- | -------------------- | ----------------------- |
| `bedrock-mantle` | `anthropic.claude-mythos-preview` | `https://bedrock-mantle.{region}.api.aws/v1` | N/A                  | N/A                     |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard** | **Priority** | **Flex** | **Reserved** |
| ------------ | ------------ | -------- | ------------ |
| Yes          | No           | No       | No           |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                | **In-Region** | **Geo** | **Global** |
| ------------------------- | ------------- | ------- | ---------- |
| `us-east-1` (N. Virginia) | Yes           | No      | No         |
