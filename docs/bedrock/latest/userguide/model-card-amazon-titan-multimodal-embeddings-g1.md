# Titan Multimodal Embeddings G1

## Amazon — Titan Multimodal Embeddings G1

## Model Details

Titan Multimodal Embeddings G1 is Amazon's model that generates embeddings from text and images for multimodal search and recommendation use cases. For more information about model development and performance, see the [model/service card](../../../ai/responsible-ai/titan-text-embeddings/overview.md "../../../ai/responsible-ai/titan-text-embeddings/overview.md").

- **Model launch date:** Nov 29, 2023
- **Model EOL date:** No sooner than 11/29/2024
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active

| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.md "apis.md")** | **[Endpoints supported](endpoints.md "endpoints.md")** |
| -------------------- | --------------------- | --------------------------------------- | ------------------------------------------------------ |
| No Audio             | Yes Embedding         | No `Responses`                          | Yes `bedrock-runtime`                                  |
| Yes Image            | No Image              | No `Chat Completions`                   | No `bedrock-mantle`                                    |
| No Speech            | No Speech             | Yes `Invoke`                            |                                                        |
| Yes Text             | No Text               | No `Converse`                           |                                                        |
| No Video             | No Video              |                                         |                                                        |

## Pricing

For pricing, please refer to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.md "apis.md") and [Endpoints supported](endpoints.md "endpoints.md").

| **Endpoint**      | **Model ID**                  | **In-Region endpoint URL**                       | **Geo inference ID** | **Global inference ID** |
| ----------------- | ----------------------------- | ------------------------------------------------ | -------------------- | ----------------------- |
| `bedrock-runtime` | `amazon.titan-embed-image-v1` | `https://bedrock-runtime.{region}.amazonaws.com` | Not supported        | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](service-tiers-inference.md "service-tiers-inference.md").

| **Standard** | **Priority** | **Flex** | **Reserved** |
| ------------ | ------------ | -------- | ------------ |
| Yes          | No           | No       | No           |

## Regional Availability

**Regional availability at a glance**

Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (US, EU, etc.) for higher throughput while respecting data residency, and **Global Cross-Region** routes anywhere worldwide for maximum throughput when there are no residency constraints. Refer to the [Regional availability](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                 | **In-Region** | **Geo** | **Global** |
| -------------------------- | ------------- | ------- | ---------- |
| `us-east-1` (N. Virginia)  | Yes           | No      | No         |
| `us-west-2` (Oregon)       | Yes           | No      | No         |
| `ca-central-1` (Canada)    | Yes           | No      | No         |
| `eu-central-1` (Frankfurt) | Yes           | No      | No         |
| `eu-west-1` (Ireland)      | Yes           | No      | No         |
| `eu-west-2` (London)       | Yes           | No      | No         |
| `eu-west-3` (Paris)        | Yes           | No      | No         |
| `ap-south-1` (Mumbai)      | Yes           | No      | No         |
| `ap-southeast-2` (Sydney)  | Yes           | No      | No         |
| `sa-east-1` (São Paulo)    | Yes           | No      | No         |

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
    modelId='amazon.titan-embed-image-v1',
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
