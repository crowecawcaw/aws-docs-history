# Claude Fable 5.1

## Anthropic — Claude Fable 5.1

## Model Details

Claude Fable 5.1 is Anthropic's frontier model for ambitious coding, long-horizon agents, and enterprise knowledge work. It handles software projects that span an entire codebase, runs multi-hour jobs across many tools inside agent harnesses, and brings best-in-class vision to dense filings, charts, and diagrams.

- **Model launch date:** September 1, 2026
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Context window:** 1M tokens
- **Max output tokens:** 128K
- **Sampling parameters:** temperature must be 1.0 or unset; top\_p must be 0.99 or unset; temperature and top\_p cannot be specified together; top\_k is not supported
- **Reasoning:** Supported (adaptive thinking is always on and cannot be disabled; effort level configurable — low, medium, high, xhigh, max; default: high)
- **Knowledge cutoff:** June 2026
- **Marketplace product ID:** prod-lt3y75wunrtv4

| **Input Modalities**                                                           | **Output Modalities**                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding |
| Green circle with white checkmark icon. Image                                  | Red circle with white X icon indicating error, cancel, or close action. Image     |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |

## Endpoints and APIs supported

The following tables show which endpoints and APIs are supported for Claude Fable 5.1. For more information, see [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md").

**Endpoint support**

| **Endpoint**      | **Supported** |
| ----------------- | ------------- |
| `bedrock-runtime` | supported     |
| `bedrock-mantle`  | supported     |

**APIs supported on `bedrock-runtime` endpoint**

| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** |
| ------------ | ------------- | -------------------- | ------------ | ---------- |
| supported    | not-supported | not-supported        | supported    | supported  |

**APIs supported on `bedrock-mantle` endpoint**

| **Messages** | **Responses** | **Chat Completions** | **Converse**  | **Invoke**    |
| ------------ | ------------- | -------------------- | ------------- | ------------- |
| supported    | not-supported | not-supported        | not-supported | not-supported |

###### Tip

Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") for details.

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Not Supported**                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| • [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• [Prompt caching](prompt-caching.md "prompt-caching.md")<br>• [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• [Guardrails](guardrails.md "guardrails.md")<br>• [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• [Model evaluation](evaluation.md "evaluation.md")<br>• [Prompt management](prompt-management.md "prompt-management.md")<br>• [Flows](flows.md "flows.md")<br>• [Agents](agents.md "agents.md") | • [Intelligent prompt routing](prompt-routing.md "prompt-routing.md") |

**Bedrock Features**

**Features supported using `bedrock-mantle` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                                                           | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • [Response streaming](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• [Prompt caching](prompt-caching.md "prompt-caching.md")<br>• [Abuse detection](abuse-detection.md "abuse-detection.md")<br>• [Count tokens](count-tokens.md "count-tokens.md") | • [Guardrails](guardrails.md "guardrails.md")<br>• [Prompt optimization](prompt-management-optimize.md "prompt-management-optimize.md")<br>• [Knowledge base](knowledge-base.md "knowledge-base.md")<br>• [Model evaluation](evaluation.md "evaluation.md")<br>• [Prompt management](prompt-management.md "prompt-management.md")<br>• [Flows](flows.md "flows.md")<br>• [Agents](agents.md "agents.md")<br>• [Intelligent prompt routing](prompt-routing.md "prompt-routing.md") |

**Prompt caching using `bedrock-runtime` and `bedrock-mantle` endpoints**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoint** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ---------------------------------------------- |
| Yes                          | 512                                 | 4                                     | 5 minutes, 1 hour | `system`, `messages`, and `tools`              |

## Content Restrictions

Claude Fable 5.1 includes blocking classifiers for dual-use content in cybersecurity and life sciences. When a classifier blocks a request, the API returns a standard HTTP 200 response with `stop_reason: "refusal"` and a `stop_details` object containing the restriction category. Refusal rates on this model are materially higher than on previous Claude models.

Customers should handle `stop_reason: "refusal"` as a primary response path. Prompt-stage refusals (blocked before inference begins) are not billed. Mid-stream refusals (blocked after partial output) are billed for tokens generated before the block.

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                 | **In-Region endpoint URL**                                      | **Geo inference ID**            | **Global inference ID**             |
| ----------------- | ---------------------------- | --------------------------------------------------------------- | ------------------------------- | ----------------------------------- |
| `bedrock-runtime` | `anthropic.claude-fable-5-1` | N/A                                                             | `us.anthropic.claude-fable-5-1` | `global.anthropic.claude-fable-5-1` |
| `bedrock-mantle`  | `anthropic.claude-fable-5-1` | `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages` | N/A                             | N/A                                 |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-runtime` endpoint**

| **Region**                      | **In-Region** | **Geo**       | **Global**    |
| ------------------------------- | ------------- | ------------- | ------------- |
| `us-east-1` (N. Virginia)       | not-supported | supported     | supported     |
| `us-east-2` (Ohio)              | not-supported | supported     | supported     |
| `us-west-1` (N. California)     | not-supported | supported     | supported     |
| `us-west-2` (Oregon)            | not-supported | supported     | supported     |
| `ca-central-1` (Canada)         | not-supported | supported     | supported     |
| `ca-west-1` (Calgary)           | not-supported | supported     | supported     |
| `eu-central-1` (Frankfurt)      | not-supported | not-supported | supported     |
| `eu-central-2` (Zurich)         | not-supported | not-supported | supported     |
| `eu-north-1` (Stockholm)        | not-supported | not-supported | supported     |
| `eu-south-1` (Milan)            | not-supported | not-supported | supported     |
| `eu-south-2` (Spain)            | not-supported | not-supported | supported     |
| `eu-west-1` (Ireland)           | not-supported | not-supported | supported     |
| `eu-west-2` (London)            | not-supported | not-supported | supported     |
| `eu-west-3` (Paris)             | not-supported | not-supported | supported     |
| `ap-east-2` (Taipei)            | not-supported | not-supported | supported     |
| `ap-northeast-1` (Tokyo)        | not-supported | not-supported | supported     |
| `ap-northeast-2` (Seoul)        | not-supported | not-supported | supported     |
| `ap-northeast-3` (Osaka)        | not-supported | not-supported | supported     |
| `ap-south-1` (Mumbai)           | not-supported | not-supported | supported     |
| `ap-south-2` (Hyderabad)        | not-supported | not-supported | supported     |
| `ap-southeast-1` (Singapore)    | not-supported | not-supported | supported     |
| `ap-southeast-2` (Sydney)       | not-supported | not-supported | supported     |
| `ap-southeast-3` (Jakarta)      | not-supported | not-supported | supported     |
| `ap-southeast-4` (Melbourne)    | not-supported | not-supported | supported     |
| `ap-southeast-5` (Malaysia)     | not-supported | not-supported | supported     |
| `ap-southeast-6` (New Zealand)  | not-supported | not-supported | supported     |
| `ap-southeast-7` (Thailand)     | not-supported | not-supported | supported     |
| `il-central-1` (Tel Aviv)       | not-supported | not-supported | supported     |
| `me-central-1` (UAE)            | not-supported | not-supported | supported     |
| `me-south-1` (Bahrain)          | not-supported | not-supported | supported     |
| `af-south-1` (Cape Town)        | not-supported | not-supported | supported     |
| `sa-east-1` (São Paulo)         | not-supported | not-supported | supported     |
| `mx-central-1` (Mexico)         | not-supported | not-supported | supported     |
| `us-gov-east-1` (GovCloud East) | not-supported | supported     | not-supported |
| `us-gov-west-1` (GovCloud West) | not-supported | supported     | not-supported |

**Availability using the `bedrock-mantle` endpoint**

| **Region**                      | **In-Region** | **Geo**       | **Global**    |
| ------------------------------- | ------------- | ------------- | ------------- |
| `us-gov-west-1` (GovCloud West) | supported     | not-supported | not-supported |

## Data Retention

To use this model, you must opt in to AWS review by setting your data retention mode to `aws_review` via the Data Retention API. For more information, see [Amazon Bedrock abuse detection](abuse-detection.md "abuse-detection.md").

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.md "quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Messages API

```
pip install -U anthropic aws-bedrock-token-generator
```

Invoke/Converse API

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

Messages API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

Invoke/Converse API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Messages API

```
from anthropic import Anthropic
from aws_bedrock_token_generator import provide_token

token = provide_token(region="us-east-1")

client = Anthropic(
    base_url="https://bedrock-runtime.us-east-1.amazonaws.com/anthropic",
    api_key=token,
)

response = client.messages.create(
    model="global.anthropic.claude-fable-5-1",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}],
)

print(response)
```

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='global.anthropic.claude-fable-5-1',
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
    modelId='global.anthropic.claude-fable-5-1',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
