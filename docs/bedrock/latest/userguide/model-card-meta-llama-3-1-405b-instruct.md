# Llama 3.1 405B Instruct

## Blue infinity symbol or figure-eight icon on white background. Meta — Llama 3.1 405B Instruct

## Model Details

Llama 3.1 405B Instruct is Meta's largest open model with 405 billion parameters and a 128K context window, supporting tool use and multilingual tasks. For more information about model development and performance, see the [model/service card](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/ "https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/").

- **Model launch date:** Jul 23, 2024
- **Model EOL date:** Legacy: July 7, 2026
- **End User License Agreements and Terms of Use:** [View](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE "https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE")
- **Model lifecycle:** Legacy
- **Context window:** 128K tokens
- **Max output tokens:** 4K
- **Knowledge cutoff:** Dec 2023

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")**  | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime`                                                |
| Red circle with white X icon indicating error, cancel, or close action. Image  | Red circle with white X icon indicating error, cancel, or close action. Image     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Red circle with white X icon indicating error, cancel, or close action. `bedrock-mantle`                 |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Red circle with white X icon indicating error, cancel, or close action. `Invoke`           |                                                                                                          |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                         |                                                                                                          |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                            |                                                                                                          |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Guardrails](bedrock/latest/userguide/guardrails.md "bedrock/latest/userguide/guardrails.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](bedrock/latest/userguide/tool-use.md "bedrock/latest/userguide/tool-use.md")<br>• Green circle with white checkmark icon. [Prompt management](bedrock/latest/userguide/prompt-management.md "bedrock/latest/userguide/prompt-management.md")<br>• Green circle with white checkmark icon. [Flows](bedrock/latest/userguide/flows.md "bedrock/latest/userguide/flows.md")<br>• Green circle with white checkmark icon. [Agents](bedrock/latest/userguide/agents.md "bedrock/latest/userguide/agents.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](bedrock/latest/userguide/prompt-routing.md "bedrock/latest/userguide/prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Abuse detection](bedrock/latest/userguide/abuse-detection.md "bedrock/latest/userguide/abuse-detection.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](bedrock/latest/userguide/prompt-management-optimize.md "bedrock/latest/userguide/prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](bedrock/latest/userguide/count-tokens.md "bedrock/latest/userguide/count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](bedrock/latest/userguide/knowledge-base.md "bedrock/latest/userguide/knowledge-base.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Model evaluation](bedrock/latest/userguide/evaluation.md "bedrock/latest/userguide/evaluation.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Structured outputs](bedrock/latest/userguide/structured-outputs.md "bedrock/latest/userguide/structured-outputs.md") |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**      | **Model ID**                       | **In-Region endpoint URL**                       | **Geo inference ID**                  | **Global inference ID** |
| ----------------- | ---------------------------------- | ------------------------------------------------ | ------------------------------------- | ----------------------- |
| `bedrock-runtime` | `meta.llama3-1-405b-instruct-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.meta.llama3-1-405b-instruct-v1:0` | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**           | **In-Region**                                                           | **Geo**                                                                 | **Global**                                                              |
| -------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-2` (Ohio)   | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon) | Green circle with white checkmark icon.                                 | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.meta.llama3-1-405b-instruct-v1:0`

| **Source Region** | **Destination Regions**                                       |
| ----------------- | ------------------------------------------------------------- |
| us-east-2 (Ohio)  | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |

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

Converse API

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='meta.llama3-1-405b-instruct-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
