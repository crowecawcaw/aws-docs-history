# DeepSeek V3.2

## DeepSeek — DeepSeek V3.2

## Model Details

DeepSeek V3.2 is DeepSeek's mixture-of-experts model with improved reasoning, coding, and instruction following capabilities. For more information about model development and performance, see the [model/service card](https://api-docs.deepseek.com/news/news251201 "https://api-docs.deepseek.com/news/news251201").

- **Model launch date:** Dec 01, 2025
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 164K tokens
- **Max output tokens:** 8K
- **Knowledge cutoff:** Mar 2025

| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.md "apis.md")** | **[Endpoints supported](endpoints.md "endpoints.md")** |
| -------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------ |
| No Audio             | No Embedding          | No `Responses`                          | Yes `bedrock-runtime`                                  |
| No Image             | No Image              | Yes `Chat Completions`                  | Yes `bedrock-mantle`                                   |
| No Speech            | No Speech             | Yes `Invoke`                            |                                                        |
| Yes Text             | Yes Text              | Yes `Converse`                          |                                                        |
| No Video             | No Video              |                                         |                                                        |

###### Note

Whenever possible, we recommend you use the `bedrock-mantle` endpoint.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                              | **Not Supported**                                          |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| • Yes [Projects](projects.md "projects.md")<br>• Yes [Client-side tool calling](tool-use.md "tool-use.md") | • No [Server-side tool calling](tool-use.md "tool-use.md") |

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Not Supported**                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| • Yes [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Yes [Guardrails](guardrails.md "guardrails.md")<br>• Yes [Model evaluation](evaluation.md "evaluation.md")<br>• Yes [Prompt management](prompt-management.md "prompt-management.md")<br>• Yes [Flows](flows.md "flows.md")<br>• Yes [Agents](agents.md "agents.md")<br>• Yes [Structured outputs](structured-outputs.md "structured-outputs.md") | • No [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• No [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• No [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• No [Count tokens](count-tokens.md "count-tokens.md")<br>• No [Knowledge base](knowledge-base.md "knowledge-base.md") |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**    | **In-Region endpoint URL**                       | **Geo inference ID** | **Global inference ID** |
| ----------------- | --------------- | ------------------------------------------------ | -------------------- | ----------------------- |
| `bedrock-runtime` | `deepseek.v3.2` | `https://bedrock-runtime.{region}.amazonaws.com` | Not supported        | Not supported           |
| `bedrock-mantle`  | `deepseek.v3.2` | `https://bedrock-mantle.{region}.api.aws/v1`     | Not supported        | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard** | **Priority** | **Flex** | **Reserved** |
| ------------ | ------------ | -------- | ------------ |
| Yes          | Yes          | Yes      | No           |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                   | **In-Region** | **Geo** | **Global** |
| ---------------------------- | ------------- | ------- | ---------- |
| `us-east-1` (N. Virginia)    | Yes           | No      | No         |
| `us-east-2` (Ohio)           | Yes           | No      | No         |
| `us-west-2` (Oregon)         | Yes           | No      | No         |
| `eu-north-1` (Stockholm)     | Yes           | No      | No         |
| `eu-west-2` (London)         | Yes           | No      | No         |
| `ap-northeast-1` (Tokyo)     | Yes           | No      | No         |
| `ap-south-1` (Mumbai)        | Yes           | No      | No         |
| `ap-southeast-2` (Sydney)    | Yes           | No      | No         |
| `ap-southeast-3` (Jakarta)   | Yes           | No      | No         |
| `sa-east-1` (São Paulo)      | Yes           | No      | No         |
| `ap-southeast-4` (Melbourne) | Yes           | No      | No         |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, please refer to [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

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
OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/v1"
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
    model="deepseek.v3.2",
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
    modelId='deepseek.v3.2',
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
    modelId='deepseek.v3.2',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
