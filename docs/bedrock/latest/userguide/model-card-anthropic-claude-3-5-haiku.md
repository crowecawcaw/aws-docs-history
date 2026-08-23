# Claude 3.5 Haiku

## Orange rounded square icon with white radial loading or progress indicator symbol. Anthropic — Claude 3.5 Haiku

## Model Details

Claude 3.5 Haiku is Anthropic's next-generation fast model with improved coding and reasoning performance over Claude 3 Haiku at the same speed tier. For more information about model development and performance, see the [model/service card](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf").

- **Model launch date:** Nov 4, 2024
- **Model EOL date:** June 19, 2026
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Legacy
- **Context window:** 200K tokens
- **Max output tokens:** 8K
- **Knowledge cutoff:** Jul 2024
- **Marketplace product ID:** `prod-5oba7y7jpji56`

| **Input Modalities**                                                           | **Output Modalities**                                                             |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding |
| Red circle with white X icon indicating error, cancel, or close action. Image  | Red circle with white X icon indicating error, cancel, or close action. Image     |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    |
| Green circle with white checkmark icon. Text                                   | Green circle with white checkmark icon. Text                                      |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |

**Prompt caching using `bedrock-runtime` endpoint**

For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

| **Prompt caching supported** | **Min tokens per cache checkpoint** | **Max cache checkpoints per request** | **Supported TTL** | **Fields that accept prompt cache checkpoints** |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ----------------- | ----------------------------------------------- |
| Yes                          | 2,048                               | 4                                     | 5 minutes         | `system`, `messages`, and `tools`               |

## Endpoints and APIs supported

The following tables show which endpoints and APIs are supported for Claude 3.5 Haiku. For more information, see [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md").

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

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                               | **In-Region endpoint URL**                       | **Geo inference ID**                          | **Global inference ID** |
| ----------------- | ------------------------------------------ | ------------------------------------------------ | --------------------------------------------- | ----------------------- |
| `bedrock-runtime` | `anthropic.claude-3-5-haiku-20241022-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.anthropic.claude-3-5-haiku-20241022-v1:0` | N/A                     |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                | **In-Region**                                                           | **Geo**                                 | **Global**                                                              |
| ------------------------- | ----------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-2` (Ohio)        | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)      | Green circle with white checkmark icon.                                 | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.anthropic.claude-3-5-haiku-20241022-v1:0`

| **Source Region**       | **Destination Regions**                                       |
| ----------------------- | ------------------------------------------------------------- |
| us-east-1 (N. Virginia) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |
| us-east-2 (Ohio)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |
| us-west-2 (Oregon)      | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |

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
    modelId='anthropic.claude-3-5-haiku-20241022-v1:0',
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
    modelId='anthropic.claude-3-5-haiku-20241022-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
