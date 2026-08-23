# Nova 2 Lite

## Amazon logo with curved arrow from A to Z forming a smile. Amazon — Nova 2 Lite

## Model Details

Nova 2 Lite is Amazon's cost-efficient multimodal model for simple automation, document processing, and customer support across text, images, and video. For more information about model development and performance, see the [model/service card](../../../pdfs/ai/responsible-ai/nova-2-lite/nova-2-lite.pdf.md "../../../pdfs/ai/responsible-ai/nova-2-lite/nova-2-lite.pdf.md").

- **Model launch date:** Dec 02, 2025
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 1M tokens
- **Max output tokens:** 64K
- **Knowledge cutoff:** Oct 2025

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](apis.md "apis.md")**                                                    | **[Endpoints supported](endpoints.md "endpoints.md")**                                   |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime`                                |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Red circle with white X icon indicating error, cancel, or close action. `bedrock-mantle` |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                           |                                                                                          |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      | Green circle with white checkmark icon. `Converse`                                         |                                                                                          |
| Green circle with white checkmark icon. Video                                  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                            |                                                                                          |

###### Tip

Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") for details.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Green circle with white checkmark icon. [Guardrails](guardrails.md "guardrails.md")<br>• Green circle with white checkmark icon. [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](tool-use.md "tool-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](count-tokens.md "count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Structured outputs](structured-outputs.md "structured-outputs.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Model evaluation](evaluation.md "evaluation.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt management](prompt-management.md "prompt-management.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Flows](flows.md "flows.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Agents](agents.md "agents.md") |

**Prompt caching using `bedrock-runtime` endpoint**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoints** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ----------------------------------------------- |
| Yes                          | 1K\*                                | 4                                     | 5 minutes         | `system` and `messages`                         |

_\* Amazon Nova models support a maximum of 20K tokens for prompt caching. Prompt caching is primarily for text prompts._

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**              | **In-Region endpoint URL**                       | **Geo inference ID**                                                                 | **Global inference ID**          |
| ----------------- | ------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------- |
| `bedrock-runtime` | `amazon.nova-2-lite-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.amazon.nova-2-lite-v1:0``eu.amazon.nova-2-lite-v1:0``jp.amazon.nova-2-lite-v1:0` | `global.amazon.nova-2-lite-v1:0` |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                            | **Flex**                                | **Reserved**                                                            |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Green circle with white checkmark icon. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                     | **In-Region**                                                           | **Geo**                                                                 | **Global**                              |
| ------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------- |
| `us-east-1` (N. Virginia)      | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-east-2` (Ohio)             | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-1` (N. California)    | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `us-west-2` (Oregon)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ca-central-1` (Canada)        | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ca-west-1` (Calgary)          | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-central-1` (Frankfurt)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-north-1` (Stockholm)       | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-south-1` (Milan)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-south-2` (Spain)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-west-1` (Ireland)          | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `eu-west-2` (London)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `eu-west-3` (Paris)            | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ap-east-2` (Taipei)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-northeast-1` (Tokyo)       | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. |
| `ap-northeast-2` (Seoul)       | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-south-1` (Mumbai)          | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-1` (Singapore)   | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-2` (Sydney)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-3` (Jakarta)     | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-4` (Melbourne)   | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-5` (Malaysia)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-6` (New Zealand) | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `ap-southeast-7` (Thailand)    | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `il-central-1` (Tel Aviv)      | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |
| `me-central-1` (UAE)           | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.amazon.nova-2-lite-v1:0`

| **Source Region**         | **Destination Regions**                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| us-east-1 (N. Virginia)   | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-east-2 (Ohio)          | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| us-west-1 (N. California) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) |
| us-west-2 (Oregon)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)                            |
| ca-central-1 (Canada)     | ca-central-1 (Canada), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)     |
| ca-west-1 (Calgary)       | ca-west-1 (Calgary), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon)       |

**Geo: EU**

Geo Inference ID: `eu.amazon.nova-2-lite-v1:0`

| **Source Region**        | **Destination Regions**                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| eu-central-1 (Frankfurt) | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-north-1 (Stockholm)   | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-south-1 (Milan)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-south-2 (Spain)       | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-west-1 (Ireland)      | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |
| eu-west-3 (Paris)        | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |

**Geo: JP**

Geo Inference ID: `jp.amazon.nova-2-lite-v1:0`

| **Source Region**      | **Destination Regions**                        |
| ---------------------- | ---------------------------------------------- |
| ap-northeast-1 (Tokyo) | ap-northeast-1 (Tokyo), ap-northeast-3 (Osaka) |

**Global inference details**

| **Global Inference ID**        | **Americas**                                                                                                                                               | **EMEA**                                                                                                                                                                                                                            | **Asia Pacific**                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| global.amazon.nova-2-lite-v1:0 | • us-east-1 (N. Virginia)<br>• us-east-2 (Ohio)<br>• us-west-1 (N. California)<br>• us-west-2 (Oregon)<br>• ca-central-1 (Canada)<br>• ca-west-1 (Calgary) | • eu-central-1 (Frankfurt)<br>• eu-north-1 (Stockholm)<br>• eu-south-1 (Milan)<br>• eu-south-2 (Spain)<br>• eu-west-1 (Ireland)<br>• eu-west-2 (London)<br>• eu-west-3 (Paris)<br>• il-central-1 (Tel Aviv)<br>• me-central-1 (UAE) | • ap-east-2 (Taipei)<br>• ap-northeast-1 (Tokyo)<br>• ap-northeast-2 (Seoul)<br>• ap-south-1 (Mumbai)<br>• ap-southeast-1 (Singapore)<br>• ap-southeast-2 (Sydney)<br>• ap-southeast-3 (Jakarta)<br>• ap-southeast-4 (Melbourne)<br>• ap-southeast-5 (Malaysia)<br>• ap-southeast-6 (New Zealand)<br>• ap-southeast-7 (Thailand) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

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
    modelId='amazon.nova-2-lite-v1:0',
    body=json.dumps({
            'messages': [{
                'role': 'user',
                'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
            }],
            'inferenceConfig': {
                'maxTokens': 1024
            }
    })
)
print(json.loads(response['body'].read()))
```

Converse API

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='amazon.nova-2-lite-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
