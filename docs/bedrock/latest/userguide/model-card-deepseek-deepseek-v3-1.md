# DeepSeek-V3.1

## Blue icon showing a stylized whale with containers, representing Docker or container services. DeepSeek — DeepSeek-V3.1

## Model Details

DeepSeek-V3.1 is DeepSeek's 685B parameter mixture-of-experts model with strong performance across coding, math, and general reasoning tasks. For more information about model development and performance, see the [model/service card](https://api-docs.deepseek.com/news/news250821 "https://api-docs.deepseek.com/news/news250821").

- **Model launch date:** Aug 21, 2025
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://huggingface.co/deepseek-ai/DeepSeek-V3.1/blob/main/LICENSE "https://huggingface.co/deepseek-ai/DeepSeek-V3.1/blob/main/LICENSE")
- **Model lifecycle:** Active
- **Context window:** 128K tokens
- **Max output tokens:** 8K
- **Knowledge cutoff:** Jan 2025

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                                             | **[Endpoints supported](endpoints.md "endpoints.md")**    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses` | Green circle with white checkmark icon. `bedrock-runtime` |
| Red circle with white X icon indicating error, cancel, or close action. Image  | Red circle with white X icon indicating error, cancel, or close action. Image     | Green circle with white checkmark icon. `Chat Completions`                          | Green circle with white checkmark icon. `bedrock-mantle`  |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                    |                                                           |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                  |                                                           |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                     |                                                           |

###### Tip

Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") for details.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                      | **Not Supported**                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Projects](projects.md "projects.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](tool-use.md "tool-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Server-side tool calling](tool-use.md "tool-use.md") |

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Guardrails](guardrails.md "guardrails.md")<br>• Green circle with white checkmark icon. [Model evaluation](evaluation.md "evaluation.md")<br>• Green circle with white checkmark icon. [Prompt management](prompt-management.md "prompt-management.md")<br>• Green circle with white checkmark icon. [Flows](flows.md "flows.md")<br>• Green circle with white checkmark icon. [Agents](agents.md "agents.md")<br>• Green circle with white checkmark icon. [Structured outputs](structured-outputs.md "structured-outputs.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](tool-use.md "tool-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](count-tokens.md "count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](knowledge-base.md "knowledge-base.md") |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**       | **In-Region endpoint URL**                       | **Geo inference ID** | **Global inference ID** |
| ----------------- | ------------------ | ------------------------------------------------ | -------------------- | ----------------------- |
| `bedrock-runtime` | `deepseek.v3-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | Not supported        | Not supported           |
| `bedrock-mantle`  | `deepseek.v3.1`    | `https://bedrock-mantle.{region}.api.aws/v1`     | Not supported        | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                 | **In-Region**                           | **Geo**                                                                 | **Global**                                                              |
| -------------------------- | --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-2` (Ohio)         | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-north-1` (Stockholm)   | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-2` (London)       | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-northeast-1` (Tokyo)   | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-south-1` (Mumbai)      | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-2` (Sydney)  | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-3` (Jakarta) | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-1` (N. Virginia)  | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Chat Completions API

```
pip install boto3 openai
```

Invoke/Converse API

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

Chat Completions API

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-runtime.<your-region>.amazonaws.com/openai/v1"
```

Invoke/Converse API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Chat Completions API

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="deepseek.v3.1",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
    )
print(response)
```

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='deepseek.v3-v1:0',
    body=json.dumps({
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
    modelId='deepseek.v3-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
