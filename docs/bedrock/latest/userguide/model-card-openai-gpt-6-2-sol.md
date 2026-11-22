

# GPT-6.2 Sol

## ![OpenAI logo.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/models/openai.png) OpenAI — GPT-6.2 Sol
<a name="model-card-openai-gpt-6-2-sol-header"></a>

## Model Details
<a name="model-card-openai-gpt-6-2-sol-details"></a>

GPT-6.2 Sol is the next generation of GPT-6.1 Sol, a fast, versatile model for everyday work such as implementing features, writing technical content, and automating recurring workflows across business applications.
+  **Model launch date:** November 17, 2026
+  **Model lifecycle policy:** [OpenAI model deprecation notice periods](https://developers.openai.com/api/docs/deprecations#model-deprecation-notice-periods). This model follows OpenAI first-party lifecycle terms, with at least 6 months of deprecation notice for generally available models, unless safety or compliance concerns require a faster timeline.
+  **Model EOL date:** Not announced.
+  **End User License Agreements and Terms of Use:** [OpenAI models on Amazon Bedrock terms](https://aws.amazon.com/legal/bedrock/third-party-models/#amsc13--xttmgl) 
+  **Model lifecycle:** Active
+  **Context window:** 1,050,000 tokens
+  **Max output tokens:** 128,000 tokens
+  **Marketplace product ID:** `prod-vznp63pbdpexe`


| **Input Modalities** | **Output Modalities** | 
| --- | --- | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Image | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | 

## Endpoints and APIs supported
<a name="model-card-openai-gpt-6-2-sol-apis-endpoints"></a>

The following tables show which endpoints and APIs GPT-6.2 Sol supports. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Inference endpoints supported by Amazon Bedrock](endpoints.md).

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
<a name="model-card-openai-gpt-6-2-sol-capabilities"></a>

***Bedrock Features***

**Features supported using `bedrock-runtime`**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects (default project only)](projects.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Invocation logs](model-invocation-logging.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Response streaming](/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Abuse detection](abuse-detection.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Guardrails](guardrails.html) (Chat Completions, InvokeModel, and Converse APIs; not supported with Responses)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Application inference profiles](cost-mgmt-application-inference-profiles.html) (InvokeModel and Converse APIs only; not supported with Responses or Chat Completions)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Implicit Prompt Caching](#model-card-openai-gpt-6-2-sol-prompt-caching) (Responses, Chat Completions, InvokeModel, and Converse APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Explicit Prompt Caching](#model-card-openai-gpt-6-2-sol-prompt-caching) (Responses, Chat Completions, and InvokeModel APIs; not supported with Converse)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Structured outputs](#model-card-openai-gpt-6-2-sol-structured-output) (Responses, Chat Completions, InvokeModel, and Converse APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Reasoning Summaries](https://developers.openai.com/api/docs/guides/reasoning#reasoning-summaries) (Responses, [Converse](conversation-inference.html), and ConverseStream APIs; on Converse, set `additionalModelRequestFields.reasoning.summary`)  |  + ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Server-side system tools](tool-use.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Intelligent prompt routing](prompt-routing.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Count tokens](count-tokens.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Knowledge Bases](knowledge-base.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Prompt optimization](prompt-management-optimize.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Watermarking](watermarking.html)  | 

**Features supported using `bedrock-mantle`**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects](projects.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Response streaming](inference-responses-api.md#bedrock-mantle-responses-streaming)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Implicit Prompt Caching](#model-card-openai-gpt-6-2-sol-prompt-caching) (Responses and Chat Completions APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Explicit Prompt Caching](#model-card-openai-gpt-6-2-sol-prompt-caching) (Responses and Chat Completions APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Structured outputs](#model-card-openai-gpt-6-2-sol-structured-output) (Responses and Chat Completions APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Reasoning Summaries](https://developers.openai.com/api/docs/guides/reasoning#reasoning-summaries) (Responses API only)  |  + ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Guardrails](guardrails.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Invocation logs](model-invocation-logging.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Application inference profiles](cost-mgmt-application-inference-profiles.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Server-side system tools](tool-use.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Intelligent prompt routing](prompt-routing.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Count tokens](count-tokens.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Knowledge Bases](knowledge-base.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Prompt optimization](prompt-management-optimize.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Watermarking](watermarking.html)  | 

### Prompt caching
<a name="model-card-openai-gpt-6-2-sol-prompt-caching"></a>

GPT-6.2 Sol supports both [Implicit Prompt Caching](prompt-caching.html#prompt-caching-implicit) and [Explicit Prompt Caching](prompt-caching.html#prompt-caching-explicit). API support differs by endpoint:
+ Responses and Chat Completions support both caching types on the `bedrock-runtime` and `bedrock-mantle` endpoints.
+ InvokeModel supports both caching types on the `bedrock-runtime` endpoint.
+ Converse supports implicit caching on the `bedrock-runtime` endpoint. The native `cachePoint` field isn't supported for explicit caching with this model.

For explicit caching, set `prompt_cache_options.mode` to `explicit`. Set `prompt_cache_options.ttl` to `30m`, the only supported TTL and the default. In Responses requests, add `"prompt_cache_breakpoint": {"mode": "explicit"}` to an `input_text` content block. In Chat Completions and InvokeModel requests, add it to a `text` content part.

A cacheable prompt prefix must contain at least 1,024 tokens. You can include multiple explicit breakpoints, and each request can create up to four cache writes. Check the cache usage fields in the response to determine whether tokens were written to or read from the cache.

### JSON Schema output
<a name="model-card-openai-gpt-6-2-sol-structured-output"></a>

Use JSON Schema to set the format of the model response for streaming and non-streaming requests. Chat Completions and Responses support JSON Schema output on both the `bedrock-runtime` and `bedrock-mantle` endpoints. InvokeModel, InvokeModelWithResponseStream, Converse, and ConverseStream support JSON Schema output on the `bedrock-runtime` endpoint. Choose a model ID or inference profile ID from [Programmatic access](#model-card-openai-gpt-6-2-sol-programmatic-access).
+ For Chat Completions, set `response_format.type` to `json_schema`. Put `name`, `schema`, and `strict: true` in `response_format.json_schema`.
+ For Responses, set `text.format.type` to `json_schema`. Put `name`, `schema`, and `strict: true` in `text.format`.
+ For InvokeModel and InvokeModelWithResponseStream, use the same `response_format` fields as Chat Completions.
+ For Converse and ConverseStream, set `outputConfig.textFormat.type` to `json_schema`. In `outputConfig.textFormat.structure.jsonSchema`, set `name` and `schema`. Encode the schema as a JSON string. Then set `additionalModelRequestFields.text.format.strict` to `true`.

Use an object schema. Put all fields in `required`. Set `additionalProperties` to `false`. Validate your schema before you send it. Check for refusals or incomplete responses before you parse the output.

**Important**  
For JSON Schema output with Converse and ConverseStream, you must set `additionalModelRequestFields.text.format.strict` to `true`, in addition to specifying the schema in `outputConfig`. Include the following field in your request.  

```json
{
  "additionalModelRequestFields": {
    "text": {
      "format": { "strict": true }
    }
  }
}
```

**Converse content blocks**

On the `bedrock-runtime` endpoint, Converse accepts `text` and `image` content blocks in user messages. This model doesn't accept `document` content blocks, and it doesn't accept an `image` content block inside a `toolResult`. A request that includes either is rejected with a `ValidationException`. To send a document to this model, use the Responses API with an `input_file` content part instead.

## Pricing
<a name="model-card-openai-gpt-6-2-sol-pricing"></a>

All prices are in USD per 1 million tokens for the Standard tier.

The **Input — 30-minute cache write** column is the price per 1 million tokens written to the prompt cache. The 30-minute figure is how long a cached prompt prefix is retained, not a quantity of tokens. For more information, see [prompt caching](prompt-caching.md).

Long-context rates apply to the full request when input exceeds 272,000 tokens.

### Standard — Commercial Regions, short context (272K input tokens or fewer)
<a name="model-card-openai-gpt-6-2-sol-pricing-short"></a>


| **Inference option** | **Input** | **Input — 30-minute cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $2.20 | $2.75 | $0.11 | $11.00 | 
| Geo CRIS | $2.20 | $2.75 | $0.11 | $11.00 | 
| Global CRIS | $2.00 | $2.50 | $0.10 | $10.00 | 

### Standard — Commercial Regions, long context (more than 272K input tokens)
<a name="model-card-openai-gpt-6-2-sol-pricing-long"></a>


| **Inference option** | **Input** | **Input — 30-minute cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $4.40 | $5.50 | $0.22 | $16.50 | 
| Geo CRIS | $4.40 | $5.50 | $0.22 | $16.50 | 
| Global CRIS | $4.00 | $5.00 | $0.20 | $15.00 | 

## Programmatic Access
<a name="model-card-openai-gpt-6-2-sol-programmatic-access"></a>

To call this model from code, use the following model IDs and endpoint URLs. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Inference endpoints supported by Amazon Bedrock](endpoints.md).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-mantle | openai.gpt-6.2-sol | https://bedrock-mantle.{region}.api.aws/openai/v1 | Not supported | Not supported | 
| bedrock-runtime | openai.gpt-6.2-sol | Not supported | us.openai.gpt-6.2-sol | global.openai.gpt-6.2-sol | 

*For in-Region access, use `bedrock-mantle` in `us-east-1` (N. Virginia). On `bedrock-runtime`, the OpenAI-compatible base URL is `https://bedrock-runtime.{region}.amazonaws.com/openai/v1`. Use `us.openai.gpt-6.2-sol` for US geographic cross-Region inference or `global.openai.gpt-6.2-sol` for global cross-Region inference. Direct in-Region invocation is not supported on `bedrock-runtime`. Use a source Region enabled for the profile you choose; see [Route model inference requests across AWS Regions with cross-Region inference](cross-region-inference.md).*

## Service Tiers
<a name="model-card-openai-gpt-6-2-sol-tiers"></a>

Amazon Bedrock offers several service tiers for different workloads. **Standard** gives you pay-per-token access with no commitment. To use it, set `"service_tier": "default"` or omit the field. For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-openai-gpt-6-2-sol-regional-availability"></a>

***Regional availability at a glance***

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md) page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-mantle` endpoint**


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-east-2 (Ohio) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-west-2 (Oregon) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-gov-west-1 (GovCloud West) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-gov-east-1 (GovCloud East) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**Availability using the `bedrock-runtime` endpoint**


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-east-2 (Ohio) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-west-1 (N. California) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-west-2 (Oregon) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ca-central-1 (Canada) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ca-west-1 (Calgary) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-central-1 (Frankfurt) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-central-2 (Zurich) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-north-1 (Stockholm) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-south-1 (Milan) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-south-2 (Spain) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-west-1 (Ireland) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-west-2 (London) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-west-3 (Paris) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-east-2 (Taipei) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-northeast-1 (Tokyo) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-northeast-2 (Seoul) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-northeast-3 (Osaka) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-south-1 (Mumbai) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-south-2 (Hyderabad) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-1 (Singapore) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-2 (Sydney) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-3 (Jakarta) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-4 (Melbourne) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-5 (Malaysia) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-6 (New Zealand) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-7 (Thailand) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| il-central-1 (Tel Aviv) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| mx-central-1 | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| me-south-1 (Bahrain) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| af-south-1 (Cape Town) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| sa-east-1 (São Paulo) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

***Geo inference details***

The destination Regions available to a geographic inference profile depend on the source Region. To retrieve the current routing configuration, call [GetInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetInferenceProfile.html) from the source Region.

**Geo: US**

Geo inference ID: `us.openai.gpt-6.2-sol`


| **Source Region** | **Destination Regions** | 
| --- | --- | 
| us-east-1 (N. Virginia) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| us-east-2 (Ohio) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| us-west-1 (N. California) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) | 
| us-west-2 (Oregon) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| ca-central-1 (Canada) | ca-central-1 (Canada), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| ca-west-1 (Calgary) | ca-west-1 (Calgary), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 

## Quotas and Limits
<a name="model-card-openai-gpt-6-2-sol-quotas"></a>

Quotas vary by account and Region. See [Quotas for Amazon Bedrock](quotas.md) and the model's service quota settings.

The output-token burndown rate is 10: each output token consumes 10 tokens of quota.

## Sample Code
<a name="model-card-openai-gpt-6-2-sol-sample-code"></a>

**Step 1 - AWS Account:** If you already have an AWS account, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup).

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create) and generate a long-term API key.

**Step 3 - Get the SDK:** You must have Python installed to use this guide. Then install the OpenAI SDK.

```bash
python3 -m pip install openai
```

### Step 4 - Set environment variables
<a name="model-card-openai-gpt-6-2-sol-sample-code-environment"></a>

Set up your environment to use the API key for authentication.

------
#### [ bedrock-mantle ]

```bash
export OPENAI_API_KEY="<provide your Bedrock API key>"
export OPENAI_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/openai/v1"
```

------
#### [ bedrock-runtime ]

```bash
export OPENAI_API_KEY="<provide your Bedrock API key>"
export OPENAI_BASE_URL="https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1"
```

------

**Note**  
On `bedrock-runtime`, set the model to `us.openai.gpt-6.2-sol` for US CRIS or `global.openai.gpt-6.2-sol` for Global CRIS. Direct in-Region invocation is not supported on this endpoint.

### Step 5 - Run your first inference request
<a name="model-card-openai-gpt-6-2-sol-sample-code-request"></a>

Save the file as `bedrock-first-request.py`.

#### bedrock-mantle
<a name="model-card-openai-gpt-6-2-sol-sample-mantle"></a>

Use the settings from [Step 4 - Set environment variables](#model-card-openai-gpt-6-2-sol-sample-code-environment). Choose the `bedrock-mantle` tab. The Chat tab uses the Chat Completions API.

------
#### [ Responses API ]

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-6.2-sol",
    input="Can you explain the features of Amazon Bedrock?",
    max_output_tokens=512,
)
print(response.output_text)
```

------
#### [ Chat ]

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="openai.gpt-6.2-sol",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
)
print(response.choices[0].message.content)
```

------

#### bedrock-runtime: OpenAI SDK
<a name="model-card-openai-gpt-6-2-sol-sample-runtime"></a>

Use the settings from [Step 4 - Set environment variables](#model-card-openai-gpt-6-2-sol-sample-code-environment). Choose the `bedrock-runtime` tab. Send your request with the Responses API. The example uses the US CRIS profile. For Global CRIS, replace `us.openai.gpt-6.2-sol` with `global.openai.gpt-6.2-sol`.

------
#### [ Responses API ]

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="us.openai.gpt-6.2-sol",
    input="Can you explain the features of Amazon Bedrock?",
    max_output_tokens=512,
)
print(response.output_text)
```

------