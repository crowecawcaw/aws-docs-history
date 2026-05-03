# Claude Sonnet 4

## Anthropic — Claude Sonnet 4

## Model Details

Claude Sonnet 4 is Anthropic's balanced model with strong coding and reasoning capabilities, improved instruction following, and extended thinking with tool use. For more information about model development and performance, see the [model/service card](https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf "https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf").

- **Model launch date:** May 23, 2025
- **Model EOL date:** October 14, 2026
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Legacy (certain regions)
- **Context window:** 200K tokens
- **Max output tokens:** 64K
- **Reasoning:** Supported
- **Knowledge cutoff:** Mar 2025
- **Marketplace product ID:** `prod-4pmewlybdftbs`

| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.md "apis.md")** | **[Endpoints supported](endpoints.md "endpoints.md")** |
| -------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------ |
| No Audio             | No Embedding          | No `Responses`                          | Yes `bedrock-runtime`                                  |
| Yes Image            | No Image              | No `Chat Completions`                   | No `bedrock-mantle`                                    |
| No Speech            | No Speech             | Yes `Invoke`                            |                                                        |
| Yes Text             | Yes Text              | Yes `Converse`                          |                                                        |
| No Video             | No Video              |                                         |                                                        |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Not Supported**                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Yes [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Yes [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Yes [Guardrails](guardrails.md "guardrails.md")<br>• Yes [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Yes [Count tokens](count-tokens.md "count-tokens.md")<br>• Yes [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• Yes [Model evaluation](evaluation.md "evaluation.md")<br>• Yes [Prompt management](prompt-management.md "prompt-management.md")<br>• Yes [Client-side tool calling](tool-use.md "tool-use.md") | • No [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• No [Flows](flows.md "flows.md")<br>• No [Agents](agents.md "agents.md") |

**Prompt caching using `bedrock-runtime` endpoint**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoints** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ----------------------------------------------- |
| Yes                          | 1,024                               | 4                                     | 5 minutes         | `system`, `messages`, and `tools`               |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                              | **In-Region endpoint URL**                       | **Geo inference ID**                                                                     | **Global inference ID**                          |
| ----------------- | ----------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `bedrock-runtime` | `anthropic.claude-sonnet-4-20250514-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.anthropic.claude-sonnet-4-20250514-v1:0``eu.anthropic.claude-sonnet-4-20250514-v1:0` | `global.anthropic.claude-sonnet-4-20250514-v1:0` |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard** | **Priority** | **Flex** | **Reserved** |
| ------------ | ------------ | -------- | ------------ |
| Yes          | No           | No       | No           |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                   | **In-Region** | **Geo** | **Global** |
| ---------------------------- | ------------- | ------- | ---------- |
| `us-east-1` (N. Virginia)    | No            | Yes     | Yes        |
| `us-east-2` (Ohio)           | No            | Yes     | Yes        |
| `us-west-1` (N. California)  | No            | Yes     | No         |
| `us-west-2` (Oregon)         | No            | Yes     | Yes        |
| `eu-central-1` (Frankfurt)   | No            | Yes     | No         |
| `eu-north-1` (Stockholm)     | No            | Yes     | No         |
| `eu-south-1` (Milan)         | No            | Yes     | No         |
| `eu-south-2` (Spain)         | No            | Yes     | No         |
| `eu-west-1` (Ireland)        | No            | Yes     | Yes        |
| `eu-west-3` (Paris)          | No            | Yes     | No         |
| `ap-northeast-1` (Tokyo)     | No            | No      | Yes        |
| `il-central-1` (Tel Aviv)    | No            | Yes     | No         |
| `ap-east-2` (Osaka)          | Yes           | No      | No         |
| `ap-northeast-2` (Seoul)     | Yes           | No      | No         |
| `ap-northeast-3` (Osaka)     | Yes           | No      | No         |
| `ap-south-1` (Mumbai)        | Yes           | No      | No         |
| `ap-south-2` (Hyderabad)     | Yes           | No      | No         |
| `ap-southeast-1` (Singapore) | Yes           | No      | No         |
| `ap-southeast-2` (Sydney)    | Yes           | No      | No         |
| `ap-southeast-3` (Jakarta)   | Yes           | No      | No         |
| `ap-southeast-4` (Melbourne) | Yes           | No      | No         |
| `ap-southeast-5` (Malaysia)  | Yes           | No      | No         |
| `ap-southeast-7` (Thailand)  | Yes           | No      | No         |
| `me-central-1` (UAE)         | Yes           | No      | No         |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.anthropic.claude-sonnet-4-20250514-v1:0`

| **Source Region**         | **Destination Regions**                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| us-east-1 (N. Virginia)   | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-east-2 (Ohio)          | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-west-1 (N. California) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) |
| us-west-2 (Oregon)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |

**Geo: EU**

Geo Inference ID: `eu.anthropic.claude-sonnet-4-20250514-v1:0`

| **Source Region**        | **Destination Regions**                                                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eu-central-1 (Frankfurt) | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                          |
| eu-north-1 (Stockholm)   | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                          |
| eu-south-1 (Milan)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                          |
| eu-south-2 (Spain)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                          |
| eu-west-1 (Ireland)      | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                          |
| eu-west-3 (Paris)        | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                          |
| il-central-1 (Tel Aviv)  | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris), il-central-1 (Tel Aviv) |

**Global inference details**

| **Global Inference ID**                        | **Americas**                                                            | **EMEA**              | **Asia Pacific**         |
| ---------------------------------------------- | ----------------------------------------------------------------------- | --------------------- | ------------------------ |
| global.anthropic.claude-sonnet-4-20250514-v1:0 | • us-east-1 (N. Virginia)<br>• us-east-2 (Ohio)<br>• us-west-2 (Oregon) | • eu-west-1 (Ireland) | • ap-northeast-1 (Tokyo) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, please refer to [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

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
    modelId='anthropic.claude-sonnet-4-20250514-v1:0',
    body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
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
    modelId='anthropic.claude-sonnet-4-20250514-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
