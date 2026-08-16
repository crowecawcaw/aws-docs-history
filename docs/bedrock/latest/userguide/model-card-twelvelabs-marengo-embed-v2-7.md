# Marengo Embed v2.7

## Icon showing branching arrows representing a merge or split workflow pattern. TwelveLabs — Marengo Embed v2.7

## Model Details

Marengo Embed v2.7 is TwelveLabs' video embedding model for multimodal video understanding, search, and classification. For more information about model development and performance, see the [model/service card](https://docs.twelvelabs.io/docs/concepts/models/marengo "https://docs.twelvelabs.io/docs/concepts/models/marengo").

- **Model launch date:** Dec 4, 2024
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active
- **Marketplace product ID:** `prod-o6xchhpirymvs`

| **Input Modalities**                                                          | **Output Modalities**                                                          | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")**  | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio | Green circle with white checkmark icon. Embedding                              | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime`                                                |
| Green circle with white checkmark icon. Image                                 | Red circle with white X icon indicating error, cancel, or close action. Image  | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Red circle with white X icon indicating error, cancel, or close action. `bedrock-mantle`                 |
| Green circle with white checkmark icon. Speech                                | Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. `Invoke`           |                                                                                                          |
| Green circle with white checkmark icon. Text                                  | Red circle with white X icon indicating error, cancel, or close action. Text   | Red circle with white X icon indicating error, cancel, or close action. `Converse`         |                                                                                                          |
| Green circle with white checkmark icon. Video                                 | Red circle with white X icon indicating error, cancel, or close action. Video  | Green circle with white checkmark icon. `StartAsyncInvoke`                                 |                                                                                                          |

###### Tip

Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") for details.

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**      | **Model ID**                        | **In-Region endpoint URL**                       | **Geo inference ID**                                                         | **Global inference ID** |
| ----------------- | ----------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------- | ----------------------- |
| `bedrock-runtime` | `twelvelabs.marengo-embed-2-7-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.twelvelabs.marengo-embed-2-7-v1:0``eu.twelvelabs.marengo-embed-2-7-v1:0` | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                | **In-Region**                                                           | **Geo**                                 | **Global**                                                              |
| ------------------------- | ----------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `eu-west-1` (Ireland)     | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.twelvelabs.marengo-embed-2-7-v1:0`

| **Source Region**       | **Destination Regions**                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| us-east-1 (N. Virginia) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) |

**Geo: EU**

Geo Inference ID: `eu.twelvelabs.marengo-embed-2-7-v1:0`

| **Source Region**   | **Destination Regions**                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| eu-west-1 (Ireland) | eu-central-1 (Frankfurt), eu-north-1 (Stockholm), eu-south-1 (Milan), eu-south-2 (Spain), eu-west-1 (Ireland), eu-west-3 (Paris) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](bedrock/latest/userguide/quotas-increase.md "bedrock/latest/userguide/quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](general/latest/gr/bedrock.md#limits_bedrock "general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:**

```
pip install boto3
```

**Step 4 - Set environment variables:**

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** This model uses `StartAsyncInvoke`. Save the file as `bedrock-first-request.py`

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.start_async_invoke(
    modelId='twelvelabs.marengo-embed-2-7-v1:0',
    modelInput={},
    outputDataConfig={'s3OutputDataConfig': {'s3Uri': 's3://your-bucket/output/'}}
)
print(response)
```
