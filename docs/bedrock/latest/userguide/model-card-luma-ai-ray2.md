

# Ray2
<a name="model-card-luma-ai-ray2"></a>

## ![Luma AI logo.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/models/luma.png) Luma AI — Ray2
<a name="model-card-luma-ai-ray2-header"></a>

## Model Details
<a name="model-card-luma-ai-ray2-details"></a>

Ray2 is Luma AI's large-scale video-generation model for creating realistic video clips with natural, coherent motion from text prompts and images. For more information about model development and performance, see the [model/service card](https://lumalabs.ai/ray).
+ **Model launch date:** Jan 23, 2025
+ **EOL no sooner than:** Jan 23, 2026
+ **Legacy period:** at least 6 months
+ **Model lifecycle policy:** [Model lifecycle (For Models Launched Prior to Sept 7 2026)](model-lifecycle-legacy.md)
+ **Model EOL date:** N/A
+ **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/)
+ **Model lifecycle:** Active
+ **Marketplace product ID:** `prod-bi33bxqeqavl6`


| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.html)** | **[Endpoints supported](endpoints.html)** | 
| --- | --- | --- | --- | 
| ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Responses | ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) bedrock-runtime | 
| ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Chat Completions | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) bedrock-mantle | 
| ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Invoke |  | 
| ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Text | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Converse |  | 
| ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Video | ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) StartAsyncInvoke |  | 

**Tip**  
Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md) for details.

## Pricing
<a name="model-card-luma-ai-ray2-pricing"></a>

This model is a third-party model offered and billed through AWS Marketplace. Charges appear on your AWS bill and in AWS Cost Explorer under the model provider (not under Amazon Bedrock). For pricing, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/) page.

## Programmatic Access
<a name="model-card-luma-ai-ray2-programmatic-access"></a>

Use the following model ID and endpoint URL to access this model programmatically. Ray2 uses the [StartAsyncInvoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_StartAsyncInvoke.html) operation. For more information about the available APIs and endpoints, see [APIs supported](apis.html) and [Endpoints supported](endpoints.html).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-runtime | luma.ray-v2:0 | https://bedrock-runtime.us-west-2.amazonaws.com | Not supported | Not supported | 

## Service Tiers
<a name="model-card-luma-ai-ray2-tiers"></a>

Amazon Bedrock offers multiple service tiers to match your workload requirements. For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-luma-ai-ray2-regional-availability"></a>

***Regional availability at a glance***

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography while respecting data residency, and **Global Cross-Region** routes worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md) page for more details.


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-west-2 (Oregon) | ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Quotas and Limits
<a name="model-card-luma-ai-ray2-quotas"></a>

The `prompt` request field accepts 1–5,000 characters. Ray2 also has a maximum model input of 300 tokens, so prompts must satisfy both limits.

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. For more information, see [Quotas for Amazon Bedrock](quotas.md) and the [Amazon Bedrock endpoints and quotas](/general/latest/gr/bedrock.html#limits_bedrock).

## Sample Code
<a name="model-card-luma-ai-ray2-sample-code"></a>

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup).

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create) and generate a long-term API key.

**Step 3 - Get the SDK:**

```
pip install boto3
```

**Step 4 - Set environment variables:**

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** This model uses `StartAsyncInvoke`. Replace the S3 URI with a bucket that you own, and save the file as `bedrock-first-request.py`.

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-west-2')
response = client.start_async_invoke(
    modelId='luma.ray-v2:0',
    modelInput={
        'prompt': 'a whale swimming through space particles',
        'duration': '5s',
        'resolution': '720p',
        'aspect_ratio': '16:9',
        'loop': False
    },
    outputDataConfig={
        's3OutputDataConfig': {
            's3Uri': 's3://your-bucket/output/'
        }
    }
)
print(response['invocationArn'])
```

For complete request parameters, image-to-video examples, and instructions for checking job status, see [Luma AI models](model-parameters-luma.md).