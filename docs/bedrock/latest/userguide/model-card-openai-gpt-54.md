

# GPT-5.4
<a name="model-card-openai-gpt-54"></a>

## ![Icon showing a circular pattern with interwoven curved segments forming a pinwheel design.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/models/openai.png) OpenAI — GPT-5.4
<a name="model-card-openai-gpt-54-header"></a>

## Model Details
<a name="model-card-openai-gpt-54-details"></a>

GPT-5.4 brings frontier reasoning, coding, computer use, long-context workflows, and tool use to Amazon Bedrock. It helps developers build AI applications and production workflows that can interpret context, interact with tools, operate software environments, and verify outputs across multiple steps. GPT-5.4 is well suited for professional workflows that require reliable reasoning and action across complex business systems. For more information about model development and performance, see the [model/service card](https://deploymentsafety.openai.com/gpt-5-4-thinking/gpt-5-4-thinking.pdf).
+ **Model launch date:** June 1, 2026
+ **Model EOL date:** N/A
+ **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/)
+ **Model lifecycle:** Active
+ **Context window:** 272K tokens
+ **Max output tokens:** N/A


| **Input Modalities** | **Output Modalities** | 
| --- | --- | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | 

## Endpoints and APIs supported
<a name="model-card-openai-gpt-54-apis-endpoints"></a>

The following tables show which endpoints and APIs are supported for GPT-5.4. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Endpoints supported by Amazon Bedrock](endpoints.md).

**Endpoint support**


| **Endpoint** | **Supported** | 
| --- | --- | 
| bedrock-runtime | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| bedrock-mantle | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

**APIs supported on `bedrock-runtime` endpoint**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**APIs supported on `bedrock-mantle` endpoint**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**Note**  
This model is available on the `openai/v1/responses` path on the `bedrock-mantle` endpoint. This is different from the `v1/responses` path used by other models on the responses endpoint.

## Capabilities and Features
<a name="model-card-openai-gpt-54-capabilities"></a>

***Bedrock Features***

**Features supported using `bedrock-mantle` endpoint**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Server-side tool calling](tool-use.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects](projects.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Client-side tool calling](tool-use.html)  | — | 

## Pricing
<a name="model-card-openai-gpt-54-pricing"></a>


| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $2.75 | — | $0.275 | $16.50 | 

**AWS GovCloud (US-West)**


| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $3.30 | — | $0.33 | $19.80 | 

*All prices are per 1 million tokens. Pricing shown is for the Standard tier. Priority and Flex tiers are not supported for this model.*

## Programmatic Access
<a name="model-card-openai-gpt-54-programmatic-access"></a>

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.html) and [Endpoints supported](endpoints.html).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-mantle | openai.gpt-5.4 | https://bedrock-mantle.{region}.api.aws/openai/v1 | Not supported | Not supported | 

*For example, if region is us-east-2 (Ohio), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-2.api.aws/openai/v1". *

## Service Tiers
<a name="model-card-openai-gpt-54-tiers"></a>

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-openai-gpt-54-regional-availability"></a>

***Regional availability at a glance***

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md) page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-mantle` endpoint**


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-east-2 (Ohio) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-west-2 (Oregon) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-gov-west-1 (GovCloud) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Quotas and Limits
<a name="model-card-openai-gpt-54-quotas"></a>

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.html). For more information, see [Quotas for Amazon Bedrock](quotas.md) documentation and see the [limits](/general/latest/gr/bedrock.html#limits_bedrock) for the model.

## Sample Code
<a name="model-card-openai-gpt-54-sample-code"></a>

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup).

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create) and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

------
#### [ Responses API ]

```
pip install openai
```

------

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

------
#### [ bedrock-mantle ]

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.us-west-2.api.aws/openai/v1"
```

------

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

------
#### [ bedrock-mantle ]

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-5.4",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

------