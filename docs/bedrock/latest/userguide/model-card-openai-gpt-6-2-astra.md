

# GPT-6.2 Astra

## ![OpenAI logo.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/models/openai.png) OpenAI — GPT-6.2 Astra
<a name="model-card-openai-gpt-6-2-astra-header"></a>

## Model Details
<a name="model-card-openai-gpt-6-2-astra-details"></a>

GPT-6.2 Astra is the next generation of GPT-6 Astra. It is OpenAI's frontier model for complex, multistep projects such as implementing and testing changes in existing codebases and producing professional deliverables (slides, spreadsheets, documents). It launches with an Ultrafast speed tier for latency-sensitive applications.
+ **Model launch date:** November 17, 2026
+ **EOL no sooner than:** November 17, 2027
+ **Legacy period:** at least 6 months
+ **Model lifecycle policy:** [Model lifecycle](model-lifecycle.md)
+ **Model EOL date:** N/A
+ **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/)
+ **Model lifecycle:** Active
+ **Context window:** 1,050,000 tokens
+ **Max output tokens:** 128,000
+ **Marketplace product ID:** `prod-e4mdsiazbjejo`


| **Input Modalities** | **Output Modalities** | 
| --- | --- | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Image | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | 

## Endpoints and APIs supported
<a name="model-card-openai-gpt-6-2-astra-apis-endpoints"></a>

The following tables show which endpoints and APIs GPT-6.2 Astra supports. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Inference endpoints supported by Amazon Bedrock](endpoints.md).

**Endpoint support**


| **Endpoint** | **Supported** | 
| --- | --- | 
| bedrock-runtime | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| bedrock-mantle | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

**APIs supported on `bedrock-runtime`**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

**APIs supported on `bedrock-mantle`**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**Note**  
On `bedrock-mantle`, both APIs use the `/openai/v1` base path, not `/v1`. Use either API with this model:  
For Responses, use `/openai/v1/responses`.
For Chat Completions, use `/openai/v1/chat/completions`.

## Capabilities and Features
<a name="model-card-openai-gpt-6-2-astra-capabilities"></a>

***Bedrock Features***

**Features supported using `bedrock-runtime`**


| **Supported** | **Not Supported** | 
| --- | --- | 
| + ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects (default project only)](projects.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Invocation logs](model-invocation-logging.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Response streaming](/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Abuse detection](abuse-detection.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Guardrails](guardrails.html) ([Converse API](conversation-inference.html) only)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Application inference profiles](cost-mgmt-application-inference-profiles.html) (InvokeModel and [Converse](conversation-inference.html) APIs only; not supported with Responses or Chat Completions)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Implicit Prompt Caching](prompt-caching.html#prompt-caching-implicit) (Responses, Chat Completions, InvokeModel, and Converse APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Explicit Prompt Caching](prompt-caching.html#prompt-caching-explicit) (Responses, Chat Completions, and InvokeModel APIs; not supported with Converse)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Structured outputs (JSON Schema; see API configuration)](#model-card-openai-gpt-6-2-astra-structured-output)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Reasoning Summaries](https://developers.openai.com/api/docs/guides/reasoning#reasoning-summaries) (Responses, [Converse](conversation-inference.html), and ConverseStream APIs; on Converse, set `additionalModelRequestFields.reasoning.summary`) | + ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Server-side tool use](tool-use.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Intelligent prompt routing](prompt-routing.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Count tokens](count-tokens.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Watermarking](watermarking.html) | 

**Features supported using `bedrock-mantle`**


| **Supported** | **Not Supported** | 
| --- | --- | 
| + ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Server-side tool calling](tool-use.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects](projects.html)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Implicit Prompt Caching](prompt-caching.html#prompt-caching-implicit) (Responses and Chat Completions APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Explicit Prompt Caching](prompt-caching.html#prompt-caching-explicit) (Responses and Chat Completions APIs)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Reasoning Summaries](https://developers.openai.com/api/docs/guides/reasoning#reasoning-summaries) (Responses API only)<br />+ ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Structured outputs](structured-output.html) (JSON Schema; Responses and Chat Completions APIs) | + ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Application inference profiles](cost-mgmt-application-inference-profiles.html)<br />+ ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Watermarking](watermarking.html) | 

### JSON Schema output on bedrock-runtime
<a name="model-card-openai-gpt-6-2-astra-structured-output"></a>

Use JSON Schema to set the format of the model response. These settings apply to non-streaming calls on the `bedrock-runtime` endpoint. Choose a profile ID from [Programmatic access](#model-card-openai-gpt-6-2-astra-programmatic-access).
+ For Chat Completions, set `response_format.type` to `json_schema`. Put `name`, `schema`, and `strict: true` in `response_format.json_schema`.
+ For Responses, set `text.format.type` to `json_schema`. Put `name`, `schema`, and `strict: true` in `text.format`.
+ For Converse, set `outputConfig.textFormat.type` to `json_schema`. In `outputConfig.textFormat.structure.jsonSchema`, set `name` and `schema`. Encode the schema as a JSON string. Then set `additionalModelRequestFields.text.format.strict` to `true`.

Use an object schema. Put all fields in `required`. Set `additionalProperties` to `false`. Validate your schema before you send it. Check for refusals or incomplete responses before you parse the output.

**Important**  
For JSON Schema output with the Converse API, you must set `additionalModelRequestFields.text.format.strict` to `true`, in addition to specifying the schema in `outputConfig`. Include the following field in your request.  

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
<a name="model-card-openai-gpt-6-2-astra-pricing"></a>

All prices are in USD per 1 million tokens.

The **Input — 30-minute cache write** column is the price per 1 million tokens written to the prompt cache. The 30-minute figure is how long a cached prompt prefix is retained, not a quantity of tokens. For more information, see [prompt caching](prompt-caching.md).

### Standard — Commercial Regions, short context (272K input tokens or fewer)
<a name="model-card-openai-gpt-6-2-astra-pricing-commercial-short"></a>


| **Inference option** | **Input** | **Input — 30-minute cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $8.80 | $11.00 | $0.44 | $44.00 | 
| Geo CRIS | $8.80 | $11.00 | $0.44 | $44.00 | 
| Global CRIS | $8.00 | $10.00 | $0.40 | $40.00 | 

### Standard — Commercial Regions, long context (more than 272K input tokens)
<a name="model-card-openai-gpt-6-2-astra-pricing-commercial-long"></a>


| **Inference option** | **Input** | **Input — 30-minute cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $17.60 | $22.00 | $0.88 | $66.00 | 
| Geo CRIS | $17.60 | $22.00 | $0.88 | $66.00 | 
| Global CRIS | $16.00 | $20.00 | $0.80 | $60.00 | 

Note: GPT-6.2 Astra in Ultrafast mode is available at promotional pricing of 3x the Standard rate through February 28, 2027. Starting March 1, 2027, Ultrafast pricing moves to 6x the Standard rate.

### Ultrafast — Commercial Regions, short context (272K input tokens or fewer)
<a name="model-card-openai-gpt-6-2-astra-pricing-ultrafast-short"></a>


| **Inference option** | **Input** | **Input — 30-minute cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $26.40 | $33.00 | $1.32 | $132.00 | 
| Geo CRIS | $26.40 | $33.00 | $1.32 | $132.00 | 
| Global CRIS | $24.00 | $30.00 | $1.20 | $120.00 | 

### Ultrafast — Commercial Regions, long context (more than 272K input tokens)
<a name="model-card-openai-gpt-6-2-astra-pricing-ultrafast-long"></a>


| **Inference option** | **Input** | **Input — 30-minute cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $52.80 | $66.00 | $2.64 | $198.00 | 
| Geo CRIS | $52.80 | $66.00 | $2.64 | $198.00 | 
| Global CRIS | $48.00 | $60.00 | $2.40 | $180.00 | 

## Programmatic Access
<a name="model-card-openai-gpt-6-2-astra-programmatic-access"></a>

To call this model from code, use the following model IDs and endpoint URLs. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Inference endpoints supported by Amazon Bedrock](endpoints.md).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-mantle | openai.gpt-6.2-astra | https://bedrock-mantle.{region}.api.aws/openai/v1 | Not supported | Not supported | 
| bedrock-runtime | openai.gpt-6.2-astra | Not supported | us.openai.gpt-6.2-astra | global.openai.gpt-6.2-astra | 

*The `bedrock-mantle` endpoint is available in `us-east-1` (N. Virginia). Ultrafast is available only in `us-east-1` on this endpoint. On `bedrock-runtime`, the base URL is `https://bedrock-runtime.{region}.amazonaws.com/openai/v1`. Name `us.openai.gpt-6.2-astra` for US geographic cross-Region inference or `global.openai.gpt-6.2-astra` for global cross-Region inference.*

## Service Tiers
<a name="model-card-openai-gpt-6-2-astra-tiers"></a>

Amazon Bedrock offers several service tiers for different workloads. **Standard** gives you pay-per-token access with no commitment. To use it, set `"service_tier": "default"` or omit the field. For more information, see [service tiers](service-tiers-inference.html).

**Ultrafast** is a speed tier for GPT-6.2 Astra. OpenAI reports API speeds up to six times faster than Standard. To request it with the Responses API, set `"service_tier": "ultrafast"`.


| **Standard** | **Ultrafast** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | --- | 
| ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

Use one of these routes for Ultrafast:
+ `bedrock-mantle` in `us-east-1`, with model ID `openai.gpt-6.2-astra`.
+ `bedrock-runtime`, with `us.openai.gpt-6.2-astra` for US geographic CRIS or `global.openai.gpt-6.2-astra` for Global CRIS.

## Regional Availability
<a name="model-card-openai-gpt-6-2-astra-regional-availability"></a>

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

Geo inference ID: `us.openai.gpt-6.2-astra`


| **Source Region** | **Destination Regions** | 
| --- | --- | 
| us-east-1 (N. Virginia) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| us-east-2 (Ohio) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| us-west-1 (N. California) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-1 (N. California), us-west-2 (Oregon) | 
| us-west-2 (Oregon) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| ca-central-1 (Canada) | ca-central-1 (Canada), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 
| ca-west-1 (Calgary) | ca-west-1 (Calgary), us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) | 

## Quotas and Limits
<a name="model-card-openai-gpt-6-2-astra-quotas"></a>

Your AWS account has default quotas. These quotas help keep Amazon Bedrock running well. A few things can change your quotas. These include Region, payment history, fraudulent use, or an approved quota [increase request](quotas-increase.html). For more information, see the [Quotas for Amazon Bedrock](quotas.md) documentation and the [limits](/general/latest/gr/bedrock.html#limits_bedrock) for the model.

On the `bedrock-runtime` endpoint, limits are managed as tokens per minute (TPM) with a 10x burndown rate, where 1 output token consumes 10 tokens.

## Sample Code
<a name="model-card-openai-gpt-6-2-astra-sample-code"></a>

**Step 1 - AWS Account:** If you already have an AWS account, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup).

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create) and generate a long-term API key.

**Step 3 - Get the SDK:** You must have Python installed to use this guide. Then install the OpenAI SDK.

```bash
pip install openai
```

### Step 4 - Set environment variables
<a name="model-card-openai-gpt-6-2-astra-sample-code-environment"></a>

Set up your environment to use the API key for authentication.

------
#### [ bedrock-mantle ]

```bash
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/openai/v1"
```

------
#### [ bedrock-runtime ]

```bash
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1"
```

------

**Note**  
On `bedrock-runtime`, name a cross-Region inference profile as the model: `us.openai.gpt-6.2-astra` or `global.openai.gpt-6.2-astra`. This model is not available for in-Region inference on that endpoint.

### Step 5 - Run your first inference request
<a name="model-card-openai-gpt-6-2-astra-sample-code-request"></a>

Save the file as `bedrock-first-request.py`.

#### bedrock-mantle
<a name="model-card-openai-gpt-6-2-astra-sample-code-mantle"></a>

Use the settings from [Step 4 - Set environment variables](#model-card-openai-gpt-6-2-astra-sample-code-environment). Choose the `bedrock-mantle` tab. The Chat tab uses the Chat Completions API.

------
#### [ Responses API ]

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-6.2-astra",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

------
#### [ Chat ]

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="openai.gpt-6.2-astra",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
)
print(response)
```

------

#### bedrock-runtime: OpenAI SDK
<a name="model-card-openai-gpt-6-2-astra-sample-code-runtime-openai"></a>

Use the settings from [Step 4 - Set environment variables](#model-card-openai-gpt-6-2-astra-sample-code-environment). Choose the `bedrock-runtime` tab. Send your request with the Responses API.

------
#### [ Responses API ]

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="us.openai.gpt-6.2-astra",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

------

## Ultrafast example
<a name="model-card-openai-gpt-6-2-astra-ultrafast-example"></a>

Set `OPENAI_API_KEY` to your Amazon Bedrock API key. This example uses the `bedrock-mantle` endpoint in `us-east-1`.

```bash
export OPENAI_API_KEY="<your Amazon Bedrock API key>"
```

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://bedrock-mantle.us-east-1.api.aws/openai/v1",
)
response = client.responses.create(
    model="openai.gpt-6.2-astra",
    service_tier="ultrafast",
    input="Explain how Amazon Bedrock cross-Region inference works.",
)
print(response.output_text)
```

For `bedrock-runtime`, use the OpenAI-compatible base URL from [Programmatic Access](#model-card-openai-gpt-6-2-astra-programmatic-access). Set the model to `us.openai.gpt-6.2-astra` for US geographic CRIS or `global.openai.gpt-6.2-astra` for Global CRIS, and keep `service_tier="ultrafast"`.