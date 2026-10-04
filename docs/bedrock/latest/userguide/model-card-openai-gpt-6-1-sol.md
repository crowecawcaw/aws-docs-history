

# GPT-6.1 Sol
<a name="model-card-openai-gpt-6-1-sol"></a>

## ![OpenAI logo](https://docs.aws.amazon.com/bedrock/latest/userguide/images/models/openai.png) OpenAI — GPT-6.1 Sol
<a name="model-card-openai-gpt-6-1-sol-header"></a>

## Model Details
<a name="model-card-openai-gpt-6-1-sol-details"></a>

OpenAI GPT-6.1 Sol brings advanced capabilities to workloads where both performance and cost matter. GPT-6.1 Sol helps agents investigate codebases and iterate on solutions. Agents can also use it to understand complex documents and complete business and computer use workflows across multiple steps.
+  **Model launch date:** September 29, 2026
+  **Model lifecycle policy:** [OpenAI model deprecation notice periods](https://developers.openai.com/api/docs/deprecations#model-deprecation-notice-periods). This model follows OpenAI first-party lifecycle terms, with at least 6 months of deprecation notice for generally available models, unless safety or compliance concerns require a faster timeline.
+  **Model EOL date:** Not announced.
+  **End User License Agreements and Terms of Use:** [OpenAI models on Amazon Bedrock terms](https://aws.amazon.com/legal/bedrock/third-party-models/#amsc13--xttmgl) 
+  **Model lifecycle:** Active
+  **Context window:** 1M tokens
+  **Max output tokens:** 131,072 tokens
+  **Marketplace product ID:** `prod-qco655ut2vn54` 


| **Input Modalities** | **Output Modalities** | 
| --- | --- | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Image | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | 

## Endpoints and APIs supported
<a name="model-card-openai-gpt-6-1-sol-apis-endpoints"></a>

The following tables show which endpoints and APIs GPT-6.1 Sol supports. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Endpoints supported by Amazon Bedrock](endpoints.md).

**Endpoint support**


| **Endpoint** | **Supported** | 
| --- | --- | 
| bedrock-runtime | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| bedrock-mantle | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

**APIs supported on `bedrock-runtime`**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
|  ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png)  |  ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png)  |  ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png)  |  ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png)  |  ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png)  | 

**APIs supported on `bedrock-mantle`**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
|  ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png)  |  ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png)  |  ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png)  |  ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png)  |  ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png)  | 

**Note**  
On `bedrock-mantle`, both APIs use the `/openai/v1` base path, not `/v1`. Use either API with this model:  
For Responses, use `/openai/v1/responses`.
For Chat Completions, use `/openai/v1/chat/completions`.

## Capabilities and Features
<a name="model-card-openai-gpt-6-1-sol-capabilities"></a>

***Bedrock Features***


| **Supported** | **Not Supported** | 
| --- | --- | 
| + ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Response streaming](/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Guardrails](guardrails.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Structured outputs (bedrock-runtime JSON Schema; see API configuration)](#model-card-openai-gpt-6-1-sol-structured-output) | + ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Server-side system tools](tool-use.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Intelligent prompt routing](prompt-routing.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Count tokens](count-tokens.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Explicit prompt caching](prompt-caching.html#prompt-caching-explicit) | 

### JSON Schema output on bedrock-runtime
<a name="model-card-openai-gpt-6-1-sol-structured-output"></a>

Use JSON Schema to set the format of the model response. These settings apply to non-streaming calls on the `bedrock-runtime` endpoint. Choose a profile ID from [Programmatic access](#model-card-openai-gpt-6-1-sol-programmatic-access).
+ For Chat Completions, set `response_format.type` to `json_schema`. Put `name`, `schema`, and `strict: true` in `response_format.json_schema`.
+ For Responses, set `text.format.type` to `json_schema`. Put `name`, `schema`, and `strict: true` in `text.format`.
+ For Converse, set `outputConfig.textFormat.type` to `json_schema`. In `outputConfig.textFormat.structure.jsonSchema`, set `name` and `schema`. Encode the schema as a JSON string. Then set `additionalModelRequestFields.text.format.strict` to `true`.

Use an object schema. Put all fields in `required`. Set `additionalProperties` to `false`. Validate your schema before you send it. Check for refusals or incomplete responses before you parse the output.

**Important**  
For JSON Schema output with the Converse API, you must set `additionalModelRequestFields.text.format.strict` to `true`, in addition to specifying the schema in `outputConfig`. Include the following field in your request.  

```
{
  "additionalModelRequestFields": {
    "text": {
      "format": { "strict": true }
    }
  }
}
```

## Pricing
<a name="model-card-openai-gpt-6-1-sol-pricing"></a>

All prices are in USD per 1 million tokens for the Standard tier. Global CRIS rates match [OpenAI first-party Standard pricing](https://developers.openai.com/api/docs/pricing).

Commercial In-Region and US geographic cross-Region inference (US CRIS) prices include a 10% premium over the global base rates. You do not need to add this premium.

Explicit prompt caching is not supported for this Bedrock model; the cache pricing dimensions do not change that feature support.

Long-context rates apply to the full request when input exceeds 272,000 tokens.

*Priority and Flex tiers are not supported for this model.*

### Commercial Regions — short context (272K input tokens or fewer)
<a name="model-card-openai-gpt-6-1-sol-pricing-short"></a>


| **Inference option** | **Input** | **Input — cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| Regional (Mantle in IAD) | $2.20 | $2.75 | $0.11 | $11.00 | 
| US CRIS (bedrock-runtime) | $2.20 | $2.75 | $0.11 | $11.00 | 
| Global CRIS (bedrock-runtime) | $2.00 | $2.50 | $0.10 | $10.00 | 

### Commercial Regions — long context (more than 272K input tokens)
<a name="model-card-openai-gpt-6-1-sol-pricing-long"></a>


| **Inference option** | **Input** | **Input — cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| Regional (Mantle in IAD) | $4.40 | $5.50 | $0.22 | $16.50 | 
| US CRIS (bedrock-runtime) | $4.40 | $5.50 | $0.22 | $16.50 | 
| Global CRIS (bedrock-runtime) | $4.00 | $5.00 | $0.20 | $15.00 | 

## Programmatic Access
<a name="model-card-openai-gpt-6-1-sol-programmatic-access"></a>

To call this model from code, use the following model IDs and endpoint URLs. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Endpoints supported by Amazon Bedrock](endpoints.md).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-mantle | openai.gpt-6.1-sol | https://bedrock-mantle.us-east-1.api.aws/openai/v1 | Not supported | Not supported | 
| bedrock-runtime | openai.gpt-6.1-sol | Not supported | us.openai.gpt-6.1-sol | global.openai.gpt-6.1-sol | 

*For in-Region access, use `bedrock-mantle` in `us-east-1` (N. Virginia, IAD). On `bedrock-runtime`, use `us.openai.gpt-6.1-sol` for US geographic cross-Region inference or `global.openai.gpt-6.1-sol` for global cross-Region inference. Direct in-Region invocation is not supported on `bedrock-runtime`. Use a source Region enabled for the profile you choose; see [Route model inference requests across AWS Regions with cross-Region inference](cross-region-inference.md).*

## Service Tiers
<a name="model-card-openai-gpt-6-1-sol-tiers"></a>

Amazon Bedrock offers several service tiers for different workloads. **Standard** gives you pay-per-token access with no commitment. To use it, set `"service_tier": "default"` or omit the field. For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-openai-gpt-6-1-sol-regional-availability"></a>

***Regional availability at a glance***

Mantle access is available in US East (N. Virginia), `us-east-1` (IAD). Runtime access supports both US geographic and global inference profiles. For more information, see [Regional availability by models](models-region-compatibility.md).

**Availability using the `bedrock-mantle` endpoint**


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**Availability using the `bedrock-runtime` endpoint**


| **Scope** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| US geographic and global inference | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

## Quotas and Limits
<a name="model-card-openai-gpt-6-1-sol-quotas"></a>

Quotas vary by account and Region. See [Quotas for Amazon Bedrock](quotas.md) and the model's service quota settings.

The output-token burndown rate is 10: each output token consumes 10 tokens of quota.

## Sample Code
<a name="model-card-openai-gpt-6-1-sol-sample-code"></a>

**Step 1 - AWS Account:** If you already have an AWS account, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup).

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create) and generate a long-term API key.

**Step 3 - Get the SDK:** You must have Python installed to use this guide. Then install the OpenAI SDK.

```
python3 -m pip install openai
```

### Step 4 - Set environment variables
<a name="model-card-openai-gpt-6-1-sol-sample-code-environment"></a>

Set up your environment to use the API key for authentication.

------
#### [ bedrock-mantle ]

```
export OPENAI_API_KEY="<provide your Bedrock API key>"
export OPENAI_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/openai/v1"
```

------
#### [ bedrock-runtime ]

```
export OPENAI_API_KEY="<provide your Bedrock API key>"
export OPENAI_BASE_URL="https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1"
```

------

**Note**  
On `bedrock-runtime`, set the model to `us.openai.gpt-6.1-sol` for US CRIS or `global.openai.gpt-6.1-sol` for Global CRIS. Direct in-Region invocation is not supported on this endpoint.

### Step 5 - Run your first inference request
<a name="model-card-openai-gpt-6-1-sol-sample-code-request"></a>

Save the file as `bedrock-first-request.py`.

#### bedrock-mantle
<a name="model-card-openai-gpt-6-1-sol-sample-mantle"></a>

Use the settings from [Step 4 - Set environment variables](#model-card-openai-gpt-6-1-sol-sample-code-environment). Choose the `bedrock-mantle` tab. The Chat tab uses the Chat Completions API.

------
#### [ Responses API ]

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-6.1-sol",
    input="Can you explain the features of Amazon Bedrock?",
    max_output_tokens=512,
)
print(response.output_text)
```

------
#### [ Chat ]

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="openai.gpt-6.1-sol",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
)
print(response.choices[0].message.content)
```

------

#### bedrock-runtime: OpenAI SDK
<a name="model-card-openai-gpt-6-1-sol-sample-runtime"></a>

Use the settings from [Step 4 - Set environment variables](#model-card-openai-gpt-6-1-sol-sample-code-environment). Choose the `bedrock-runtime` tab. Send your request with the Responses API. The example uses the US CRIS profile. For Global CRIS, replace `us.openai.gpt-6.1-sol` with `global.openai.gpt-6.1-sol`.

------
#### [ Responses API ]

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="us.openai.gpt-6.1-sol",
    input="Can you explain the features of Amazon Bedrock?",
    max_output_tokens=512,
)
print(response.output_text)
```

------