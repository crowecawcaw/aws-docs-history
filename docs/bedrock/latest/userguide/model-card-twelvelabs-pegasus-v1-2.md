# Pegasus v1.2

## TwelveLabs — Pegasus v1.2

## Model Details

Pegasus v1.2 is TwelveLabs' video-to-text generation model that produces detailed descriptions, summaries, and answers about video content. For more information about model development and performance, see the [model/service card](https://docs.twelvelabs.io/docs/concepts/models/pegasus "https://docs.twelvelabs.io/docs/concepts/models/pegasus").

- **Model launch date:** Feb 11, 2025
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active

| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.md "apis.md")** | **[Endpoints supported](endpoints.md "endpoints.md")** |
| -------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------ |
| No Audio             | No Embedding          | No `Responses`                          | Yes `bedrock-runtime`                                  |
| No Image             | No Image              | No `Chat Completions`                   | No `bedrock-mantle`                                    |
| No Speech            | No Speech             | Yes `Invoke`                            |                                                        |
| Yes Text             | Yes Text              | No `Converse`                           |                                                        |
| Yes Video            | No Video              |                                         |                                                        |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Yes [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Yes [Guardrails](guardrails.md "guardrails.md") | • No [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• No [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• No [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• No [Count tokens](count-tokens.md "count-tokens.md")<br>• No [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• No [Model evaluation](evaluation.md "evaluation.md")<br>• No [Prompt management](prompt-management.md "prompt-management.md")<br>• No [Flows](flows.md "flows.md")<br>• No [Agents](agents.md "agents.md") |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                  | **In-Region endpoint URL**                       | **Geo inference ID**                                             | **Global inference ID**              |
| ----------------- | ----------------------------- | ------------------------------------------------ | ---------------------------------------------------------------- | ------------------------------------ |
| `bedrock-runtime` | `twelvelabs.pegasus-1-2-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.twelvelabs.pegasus-1-2-v1:0``eu.twelvelabs.pegasus-1-2-v1:0` | `global.twelvelabs.pegasus-1-2-v1:0` |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard** | **Priority** | **Flex** | **Reserved** |
| ------------ | ------------ | -------- | ------------ |
| Yes          | No           | No       | No           |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                      | **In-Region** | **Geo** | **Global** |
| ------------------------------- | ------------- | ------- | ---------- |
| `us-east-1` (N. Virginia)       | Yes           | Yes     | Yes        |
| `us-east-2` (Ohio)              | No            | Yes     | Yes        |
| `us-west-1` (N. California)     | No            | Yes     | Yes        |
| `us-west-2` (Oregon)            | No            | Yes     | Yes        |
| `ca-central-1` (Canada)         | No            | No      | Yes        |
| `ca-west-1` (Calgary)           | No            | No      | Yes        |
| `eu-central-1` (Frankfurt)      | No            | Yes     | Yes        |
| `eu-central-2` (Zurich)         | No            | Yes     | Yes        |
| `eu-north-1` (Stockholm)        | No            | Yes     | Yes        |
| `eu-south-1` (Milan)            | No            | Yes     | Yes        |
| `eu-south-2` (Spain)            | No            | Yes     | Yes        |
| `eu-west-1` (Ireland)           | No            | Yes     | Yes        |
| `eu-west-2` (London)            | No            | Yes     | Yes        |
| `eu-west-3` (Paris)             | No            | Yes     | Yes        |
| `ap-east-2` (Malaysia)          | No            | No      | Yes        |
| `ap-northeast-1` (Tokyo)        | No            | No      | Yes        |
| `ap-northeast-2` (Seoul)        | Yes           | No      | Yes        |
| `ap-northeast-3` (Osaka)        | No            | No      | Yes        |
| `ap-south-1` (Mumbai)           | No            | No      | Yes        |
| `ap-south-2` (Hyderabad)        | No            | No      | Yes        |
| `ap-southeast-1` (Singapore)    | No            | No      | Yes        |
| `ap-southeast-2` (Sydney)       | No            | No      | Yes        |
| `ap-southeast-3` (Jakarta)      | No            | No      | Yes        |
| `ap-southeast-4` (Melbourne)    | No            | No      | Yes        |
| `ap-southeast-5` (Auckland)     | No            | No      | Yes        |
| `ap-southeast-7` (Kuala Lumpur) | No            | No      | Yes        |
| `il-central-1` (Tel Aviv)       | No            | No      | Yes        |
| `me-central-1` (UAE)            | No            | No      | Yes        |
| `me-south-1` (Bahrain)          | No            | No      | Yes        |
| `af-south-1` (Cape Town)        | No            | No      | Yes        |
| `sa-east-1` (São Paulo)         | No            | No      | Yes        |
| `mx-central-1` (Mexico)         | No            | No      | Yes        |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.twelvelabs.pegasus-1-2-v1:0`

| **Source Region**         | **Destination Regions**                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| us-east-1 (N. Virginia)   | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) |
| us-east-2 (Ohio)          | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-west-1 (N. California) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) |
| us-west-2 (Oregon)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |

**Geo: EU**

Geo Inference ID: `eu.twelvelabs.pegasus-1-2-v1:0`

| **Source Region**        | **Destination Regions**                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eu-central-1 (Frankfurt) | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-central-2 (Zurich)    | eu-central-1 (Frankfurt), eu-central-2 (Zurich), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-north-1 (Stockholm)   | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-south-1 (Milan)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-south-2 (Spain)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-west-1 (Ireland)      | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |
| eu-west-2 (London)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-2 (London), eu-west-3 (Paris)    |
| eu-west-3 (Paris)        | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris)                        |

**Global inference details**

| **Global Inference ID**            | **Americas**                                                                                                                                                                                                     | **EMEA**                                                                                                                                                                                                                                                                                                             | **Asia Pacific**                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| global.twelvelabs.pegasus-1-2-v1:0 | • us-east-1 (N. Virginia)<br>• us-east-2 (Ohio)<br>• us-west-1 (N. California)<br>• us-west-2 (Oregon)<br>• ca-central-1 (Canada)<br>• ca-west-1 (Calgary)<br>• sa-east-1 (São Paulo)<br>• mx-central-1 (Mexico) | • eu-central-1 (Frankfurt)<br>• eu-central-2 (Zurich)<br>• eu-north-1 (Stockholm)<br>• eu-south-1 (Milan)<br>• eu-south-2 (Spain)<br>• eu-west-1 (Ireland)<br>• eu-west-2 (London)<br>• eu-west-3 (Paris)<br>• il-central-1 (Tel Aviv)<br>• me-central-1 (UAE)<br>• me-south-1 (Bahrain)<br>• af-south-1 (Cape Town) | • ap-east-2 (Malaysia)<br>• ap-northeast-1 (Tokyo)<br>• ap-northeast-2 (Seoul)<br>• ap-northeast-3 (Osaka)<br>• ap-south-1 (Mumbai)<br>• ap-south-2 (Hyderabad)<br>• ap-southeast-1 (Singapore)<br>• ap-southeast-2 (Sydney)<br>• ap-southeast-3 (Jakarta)<br>• ap-southeast-4 (Melbourne)<br>• ap-southeast-5 (Auckland)<br>• ap-southeast-7 (Kuala Lumpur) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more details, please refer to [Quotas](quotas.md "quotas.md") documentation.

| **Quota**                        | **Default value** |
| -------------------------------- | ----------------- |
| On-demand requests per minute    | 60                |
| Cross-region requests per minute | 120               |
| Concurrent requests              | 30                |

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
    modelId='twelvelabs.pegasus-1-2-v1:0',
    body=json.dumps({
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
 )
 print(json.loads(response['body'].read()))
```
