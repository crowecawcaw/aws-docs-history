

# Jamba 1.5 Large
<a name="model-card-ai21-labs-jamba-1-5-large"></a>

## ![AI21 Labs logo with pink and black text.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/models/ai21.png) AI21 Labs — Jamba 1.5 Large
<a name="model-card-ai21-labs-jamba-1-5-large-header"></a>

## Model Details
<a name="model-card-ai21-labs-jamba-1-5-large-details"></a>

Jamba 1.5 Large is AI21 Labs' hybrid SSM-Transformer model with 398B total parameters and a 256K context window, optimized for complex reasoning tasks across long documents. For more information about model development and performance, see the [model/service card](https://www.ai21.com/blog/announcing-jamba-model-family).
+ **Model launch date:** Aug 22, 2024
+ **Model EOL date:** November 26, 2026
+ **End User License Agreements and Terms of Use:** [View](https://www.ai21.com/jamba-open-model-license/)
+ **Model lifecycle:** Legacy
+ **Context window:** 256K tokens
+ **Max output tokens:** 4K
+ **Knowledge cutoff:** Mar 2024
+ **Marketplace product ID:** `prod-evcp4w4lurj26`


| **Input Modalities** | **Output Modalities** | 
| --- | --- | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | 

## Endpoints and APIs supported
<a name="model-card-ai21-labs-jamba-1-5-large-apis-endpoints"></a>

The following tables show which endpoints and APIs are supported for Jamba 1.5 Large. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Endpoints supported by Amazon Bedrock](endpoints.md).

**Endpoint support**


| **Endpoint** | **Supported** | 
| --- | --- | 
| bedrock-runtime | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| bedrock-mantle | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**APIs supported on `bedrock-runtime` endpoint**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

**APIs supported on `bedrock-mantle` endpoint**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**Tip**  
Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md) for details.

## Capabilities and Features
<a name="model-card-ai21-labs-jamba-1-5-large-capabilities"></a>

***Bedrock Features***

**Features supported using `bedrock-runtime` endpoint**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Response streaming](/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Guardrails](guardrails.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Client-side tool calling](tool-use.html)  |  + ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Structured outputs](structured-outputs.html)  | 

## Pricing
<a name="model-card-ai21-labs-jamba-1-5-large-pricing"></a>

This model is a third-party model offered and billed through AWS Marketplace. Charges appear on your AWS bill and in AWS Cost Explorer under the model provider (not under Amazon Bedrock). For pricing, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/) page.

## Programmatic Access
<a name="model-card-ai21-labs-jamba-1-5-large-programmatic-access"></a>

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.html) and [Endpoints supported](endpoints.html).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-runtime | ai21.jamba-1-5-large-v1:0 | https://bedrock-runtime.{region}.amazonaws.com | Not supported | Not supported | 

*For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1".*

## Service Tiers
<a name="model-card-ai21-labs-jamba-1-5-large-tiers"></a>

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-ai21-labs-jamba-1-5-large-regional-availability"></a>

***Regional availability at a glance***

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md) page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-runtime` endpoint**


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Quotas and Limits
<a name="model-card-ai21-labs-jamba-1-5-large-quotas"></a>

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.html). For more information, see [Quotas for Amazon Bedrock](quotas.md) documentation and see the [limits](/general/latest/gr/bedrock.html#limits_bedrock) for the model.

## Sample Code
<a name="model-card-ai21-labs-jamba-1-5-large-sample-code"></a>

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup).

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create) and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

------
#### [ Invoke API ]

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='ai21.jamba-1-5-large-v1:0',
    body=json.dumps({
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
)
print(json.loads(response['body'].read()))
```

------
#### [ Converse API ]

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='ai21.jamba-1-5-large-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```

------