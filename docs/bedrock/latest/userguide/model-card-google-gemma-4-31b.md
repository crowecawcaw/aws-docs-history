

# Gemma 4 31B
<a name="model-card-google-gemma-4-31b"></a>

## ![Google logo with multicolored G letter icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/models/google.png) Google — Gemma 4 31B
<a name="model-card-google-gemma-4-31b-header"></a>

## Model Details
<a name="model-card-google-gemma-4-31b-details"></a>

Gemma 4 31B is Google's 30.7-billion parameter dense model with built-in reasoning, native function calling, and multimodal input across text and image, supporting a 256K token context window. For more information about model development and performance, see the [model/service card](https://huggingface.co/google/gemma-4-31B-it).
+ **Model launch date:** Mar 31, 2026
+ **Model EOL date:** N/A
+ **End User License Agreements and Terms of Use:** [View](https://ai.google.dev/gemma/apache_2)
+ **Model lifecycle:** Active
+ **Context window:** 256K tokens


| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.html)** | **[Endpoints supported](endpoints.html)** | 
| --- | --- | --- | --- | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Responses | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) bedrock-runtime | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Chat Completions | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) bedrock-mantle | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Invoke |  | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Converse |  | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Video | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Messages |  | 

**Note**  
Gemma 4 models are available only on the `bedrock-mantle` endpoint.

*On `bedrock-mantle`, this model is served at `/openai/v1/responses`, not the default `/v1/responses`.*

## Capabilities and Features
<a name="model-card-google-gemma-4-31b-capabilities"></a>

***Bedrock Features***

**Features supported using `bedrock-mantle` endpoint**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Client-side tool calling](tool-use.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Reasoning](reasoning.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects](projects.html)  | — | 

## Pricing
<a name="model-card-google-gemma-4-31b-pricing"></a>

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/) page.

## Programmatic Access
<a name="model-card-google-gemma-4-31b-programmatic-access"></a>

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.html) and [Endpoints supported](endpoints.html).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-mantle | google.gemma-4-31b | https://bedrock-mantle.{region}.api.aws/openai/v1 | Not supported | Not supported | 

*For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws/openai/v1".*

## Service Tiers
<a name="model-card-google-gemma-4-31b-tiers"></a>

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-google-gemma-4-31b-regional-availability"></a>

***Regional availability at a glance***

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md) page for more details.


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-east-2 (Ohio) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-west-2 (Oregon) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| eu-central-1 (Frankfurt) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Quotas and Limits
<a name="model-card-google-gemma-4-31b-quotas"></a>

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.html). For more information, see [Quotas for Amazon Bedrock](quotas.md) documentation and see the [limits](/general/latest/gr/bedrock.html#limits_bedrock) for the model.

When consuming on-demand throughput on the `bedrock-mantle` endpoint, [available throughput scales over time](scaling-throughput-best-practices.html#scaling-ramp-up). Not all requests within your quota are guaranteed to succeed during periods of high demand, so ramping gradually is important. For this model, default limits aren't surfaced directly through Service Quotas, so we recommend following the ramp as your guide.

## Sample Code
<a name="model-card-google-gemma-4-31b-sample-code"></a>

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup).

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create) and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

```
pip install openai
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/openai/v1"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

------
#### [ Chat Completions API ]

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="google.gemma-4-31b",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
    )
print(response)
```

------
#### [ Responses API ]

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="google.gemma-4-31b",
    input="Explain the benefits of mixture-of-experts architectures for production inference.",
    max_output_tokens=512,
)
print(response.output_text)
```

------

## Usage Considerations and Limitations
<a name="model-card-google-gemma-4-31b-considerations"></a>
+ **Reasoning mode** — Reasoning effort is honored on both the Chat Completions and Responses APIs, and the model performs the extended reasoning in both cases. However, the reasoning content is returned only by the Responses API. The Chat Completions API does not return the reasoning tokens, because the OpenAI Chat Completions specification does not support returning them.
+ **Parallel tool calls** — Requesting more than one tool call in a single turn is not currently supported. Request tool calls one at a time.
+ **Request payload size** — The total request body payload for Gemma 4 31B, including images and video, supports a maximum size of 3.5 MB.