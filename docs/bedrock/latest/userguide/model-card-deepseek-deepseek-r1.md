# DeepSeek-R1

## DeepSeek — DeepSeek-R1

## Model Details

DeepSeek-R1 is DeepSeek's reasoning model that uses chain-of-thought to solve complex math, coding, and logic problems. For more information about model development and performance, see the [model/service card](https://api-docs.deepseek.com/news/news250120 "https://api-docs.deepseek.com/news/news250120").

- **Model launch date:** Jan 20, 2025
- **Model EOL date:** No sooner than 3/10/2026
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 128K tokens
- **Max output tokens:** 8K
- **Reasoning:** Supported
- **Knowledge cutoff:** Jan 2025

| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.md "apis.md")** | **[Endpoints supported](endpoints.md "endpoints.md")** |
| -------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------ |
| No Audio             | No Embedding          | No `Responses`                          | Yes `bedrock-runtime`                                  |
| No Image             | No Image              | No `Chat Completions`                   | No `bedrock-mantle`                                    |
| No Speech            | No Speech             | Yes `Invoke`                            |                                                        |
| Yes Text             | Yes Text              | Yes `Converse`                          |                                                        |
| No Video             | No Video              |                                         |                                                        |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                         | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Yes [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Yes [Guardrails](guardrails.md "guardrails.md")<br>• Yes [Prompt management](prompt-management.md "prompt-management.md")<br>• Yes [Flows](flows.md "flows.md")<br>• Yes [Agents](agents.md "agents.md") | • No [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• No [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• No [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• No [Count tokens](count-tokens.md "count-tokens.md")<br>• No [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• No [Model evaluation](evaluation.md "evaluation.md") |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**       | **In-Region endpoint URL**                       | **Geo inference ID**  | **Global inference ID** |
| ----------------- | ------------------ | ------------------------------------------------ | --------------------- | ----------------------- |
| `bedrock-runtime` | `deepseek.r1-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.deepseek.r1-v1:0` | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

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
| `us-east-1` (N. Virginia) | No            | Yes     | No         |
| `us-east-2` (Ohio)        | No            | Yes     | No         |
| `us-west-2` (Oregon)      | No            | Yes     | No         |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.deepseek.r1-v1:0`

| **Source Region**       | **Destination Regions**                                       |
| ----------------------- | ------------------------------------------------------------- |
| us-east-1 (N. Virginia) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |
| us-east-2 (Ohio)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |
| us-west-2 (Oregon)      | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, please refer to [Quotas](quotas.md "quotas.md") documentation.

| **Quota**                        | **Default value** |
| -------------------------------- | ----------------- |
| Cross-region requests per minute | 200               |
| Cross-region tokens per minute   | 200,000           |
| Max tokens per day               | 144,000,000       |

_These are default quotas shown for us-east-1. To see quotas and limits for your account, please log in to your [AWS Console](https://aws.amazon.com/console/ "https://aws.amazon.com/console/")._

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

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='deepseek.r1-v1:0',
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
    modelId='deepseek.r1-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
