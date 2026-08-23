# Claude Sonnet 4

## Orange rounded square icon with white radial loading spinner design. Anthropic — Claude Sonnet 4

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

| **Input Modalities**                                                           | **Output Modalities**                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |

## Endpoints and APIs supported

The following tables show which endpoints and APIs are supported for Claude Sonnet 4. For more information, see [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md").

**Endpoint support**

| **Endpoint**      | **Supported** |
| ----------------- | ------------- |
| `bedrock-runtime` | supported     |
| `bedrock-mantle`  | not-supported |

**APIs supported on `bedrock-runtime` endpoint**

| **Messages**  | **Responses** | **Chat Completions** | **Converse** | **Invoke** |
| ------------- | ------------- | -------------------- | ------------ | ---------- |
| not-supported | not-supported | not-supported        | supported    | supported  |

**APIs supported on `bedrock-mantle` endpoint**

| **Messages**  | **Responses** | **Chat Completions** | **Converse**  | **Invoke**    |
| ------------- | ------------- | -------------------- | ------------- | ------------- |
| not-supported | not-supported | not-supported        | not-supported | not-supported |

###### Tip

Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") for details.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Not Supported**                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Green circle with white checkmark icon. [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• Green circle with white checkmark icon. [Guardrails](guardrails.md "guardrails.md")<br>• Green circle with white checkmark icon. [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• Green circle with white checkmark icon. [Count tokens](count-tokens.md "count-tokens.md")<br>• Green circle with white checkmark icon. [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• Green circle with white checkmark icon. [Model evaluation](evaluation.md "evaluation.md")<br>• Green circle with white checkmark icon. [Prompt management](prompt-management.md "prompt-management.md")<br>• Green circle with white checkmark icon. [Client-side tool calling](tool-use.md "tool-use.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](prompt-routing.md "prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Flows](flows.md "flows.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Agents](agents.md "agents.md") |

**Prompt caching using `bedrock-runtime` endpoint**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoints** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ----------------------------------------------- |
| Yes                          | 1,024                               | 4                                     | 5 minutes         | `system`, `messages`, and `tools`               |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                              | **In-Region endpoint URL** | **Geo inference ID**                                                                                                                   | **Global inference ID**                          |
| ----------------- | ----------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `bedrock-runtime` | `anthropic.claude-sonnet-4-20250514-v1:0` | N/A                        | `us.anthropic.claude-sonnet-4-20250514-v1:0``eu.anthropic.claude-sonnet-4-20250514-v1:0``apac.anthropic.claude-sonnet-4-20250514-v1:0` | `global.anthropic.claude-sonnet-4-20250514-v1:0` |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                   | **In-Region**                                                           | **Geo**                                 | **Global**                                                              |
| ---------------------------- | ----------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia)    | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Green circle with white checkmark icon.                                 |
| `us-east-2` (Ohio)           | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Green circle with white checkmark icon.                                 |
| `us-west-1` (N. California)  | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Green circle with white checkmark icon.                                 |
| `eu-central-1` (Frankfurt)   | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-north-1` (Stockholm)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-south-1` (Milan)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-south-2` (Spain)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-1` (Ireland)        | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Green circle with white checkmark icon.                                 |
| `eu-west-3` (Paris)          | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `il-central-1` (Tel Aviv)    | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-east-2` (Taipei)         | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-northeast-1` (Tokyo)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Green circle with white checkmark icon.                                 |
| `ap-northeast-2` (Seoul)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-northeast-3` (Osaka)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-south-1` (Mumbai)        | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-south-2` (Hyderabad)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-1` (Singapore) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-2` (Sydney)    | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-3` (Jakarta)   | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-4` (Melbourne) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-5` (Malaysia)  | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `ap-southeast-7` (Thailand)  | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

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

**Geo: APAC**

Geo Inference ID: `apac.anthropic.claude-sonnet-4-20250514-v1:0`

| **Source Region**          | **Destination Regions**                                                                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ap-northeast-1 (Tokyo)     | ap-northeast-1 (Tokyo), ap-northeast-2 (Seoul), ap-northeast-3 (Osaka), ap-south-1 (Mumbai), ap-south-2 (Hyderabad), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |
| ap-northeast-2 (Seoul)     | ap-northeast-1 (Tokyo), ap-northeast-2 (Seoul), ap-northeast-3 (Osaka), ap-south-1 (Mumbai), ap-south-2 (Hyderabad), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |
| ap-northeast-3 (Osaka)     | ap-northeast-1 (Tokyo), ap-northeast-2 (Seoul), ap-northeast-3 (Osaka), ap-south-1 (Mumbai), ap-south-2 (Hyderabad), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |
| ap-south-1 (Mumbai)        | ap-northeast-1 (Tokyo), ap-northeast-2 (Seoul), ap-northeast-3 (Osaka), ap-south-1 (Mumbai), ap-south-2 (Hyderabad), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |
| ap-south-2 (Hyderabad)     | ap-northeast-1 (Tokyo), ap-northeast-2 (Seoul), ap-northeast-3 (Osaka), ap-south-1 (Mumbai), ap-south-2 (Hyderabad), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |
| ap-southeast-1 (Singapore) | ap-northeast-1 (Tokyo), ap-northeast-2 (Seoul), ap-northeast-3 (Osaka), ap-south-1 (Mumbai), ap-south-2 (Hyderabad), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |
| ap-southeast-2 (Sydney)    | ap-northeast-1 (Tokyo), ap-northeast-2 (Seoul), ap-northeast-3 (Osaka), ap-south-1 (Mumbai), ap-south-2 (Hyderabad), ap-southeast-1 (Singapore), ap-southeast-2 (Sydney), ap-southeast-4 (Melbourne) |

**Global inference details**

| **Global Inference ID**                        | **Americas**                                                            | **EMEA**              | **Asia Pacific**         |
| ---------------------------------------------- | ----------------------------------------------------------------------- | --------------------- | ------------------------ |
| global.anthropic.claude-sonnet-4-20250514-v1:0 | • us-east-1 (N. Virginia)<br>• us-east-2 (Ohio)<br>• us-west-2 (Oregon) | • eu-west-1 (Ireland) | • ap-northeast-1 (Tokyo) |

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
