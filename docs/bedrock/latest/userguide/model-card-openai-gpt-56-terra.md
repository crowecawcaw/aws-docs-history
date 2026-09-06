

# GPT-5.6 Terra
<a name="model-card-openai-gpt-56-terra"></a>

## ![Icon showing a circular pattern with interwoven curved segments forming a pinwheel design.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/models/openai.png) OpenAI — GPT-5.6 Terra
<a name="model-card-openai-gpt-56-terra-header"></a>

## Model Details
<a name="model-card-openai-gpt-56-terra-details"></a>

GPT-5.6 Terra is the balanced model for everyday production work. It delivers superior performance to GPT-5.5 at a lower cost, completing tasks with fewer output tokens for stronger performance per dollar. Use Terra for code generation, content workflows, structured data extraction, and general-purpose agentic tasks. For more information about model development and performance, see the [model/service card](https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf).
+ **Model launch date:** July 13, 2026
+ **Model EOL date:** N/A
+ **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/)
+ **Model lifecycle:** Active
+ **Context window:** 1M tokens


| **Input Modalities** | **Output Modalities** | 
| --- | --- | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | 
| ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video | 

## Endpoints and APIs supported
<a name="model-card-openai-gpt-56-terra-apis-endpoints"></a>

The following tables show which endpoints and APIs are supported for GPT-5.6 Terra. For more information, see [APIs supported by Amazon Bedrock](apis.md) and [Endpoints supported by Amazon Bedrock](endpoints.md).

**Endpoint support**


| **Endpoint** | **Supported** | 
| --- | --- | 
| bedrock-runtime | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| bedrock-mantle | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

**APIs supported on `bedrock-runtime` endpoint**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**APIs supported on `bedrock-mantle` endpoint**


| **Messages** | **Responses** | **Chat Completions** | **Converse** | **Invoke** | 
| --- | --- | --- | --- | --- | 
| ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

*On `bedrock-mantle`, this model is served at `/openai/v1/responses`, not the default `/v1/responses`.*

**Tip**  
Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md) for details.

## Capabilities and Features
<a name="model-card-openai-gpt-56-terra-capabilities"></a>

***Bedrock Features***

**Features supported using `bedrock-runtime` endpoint**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects (default project only)](projects.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Invocation logs](model-invocation-logging.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Response streaming](/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Abuse detection](abuse-detection.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Guardrails](guardrails.html) ([Converse API](conversation-inference.html) only)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Application inference profiles](cost-mgmt-application-inference-profiles.html) ([Converse API](conversation-inference.html) only; not supported with Responses or Chat Completions APIs)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Implicit Prompt Caching](prompt-caching.html#prompt-caching-implicit) (Responses API only)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Explicit Prompt Caching](prompt-caching.html#prompt-caching-explicit) (Responses API only)  |  + ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Server-side tool use](tool-use.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Intelligent prompt routing](prompt-routing.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Count tokens](count-tokens.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Structured outputs](structured-output.html)  | 

**Features supported using `bedrock-mantle` endpoint**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Server-side tool calling](tool-use.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Projects](projects.html)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Implicit Prompt Caching](prompt-caching.html#prompt-caching-implicit) (Responses API only)<br />+ ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Explicit Prompt Caching](prompt-caching.html#prompt-caching-explicit) (Responses API only)  |  + ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Application inference profiles](cost-mgmt-application-inference-profiles.html) (Responses and Chat Completions APIs only)  | 

## Pricing
<a name="model-card-openai-gpt-56-terra-pricing"></a>

**Short Context Window (272K)**


| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $2.20 | $2.75 | $0.22 | $13.20 | 
| Geo CRIS | $2.20 | $2.75 | $0.22 | $13.20 | 
| Global CRIS | $2.00 | $2.50 | $0.20 | $12.00 | 

**Long Context Window (1M)**


| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $4.40 | $5.50 | $0.44 | $19.80 | 
| Geo CRIS | $4.40 | $5.50 | $0.44 | $19.80 | 
| Global CRIS | $4.00 | $5.00 | $0.40 | $18.00 | 

**AWS GovCloud (US-East and US-West)**

**Short Context Window (272K)**


| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $2.64 | $3.30 | $0.264 | $15.84 | 

**Long Context Window (1M)**


| **Inference option** | **Input** | **Input — 30m cache write** | **Input — cache read** | **Output** | 
| --- | --- | --- | --- | --- | 
| In-Region | $5.28 | $6.60 | $0.528 | $23.76 | 

*All prices are per 1 million tokens. Pricing shown is for the Standard tier. Priority and Flex tiers are not supported for this model.*

## Programmatic Access
<a name="model-card-openai-gpt-56-terra-programmatic-access"></a>

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](apis.html) and [Endpoints supported](endpoints.html).


| **Endpoint** | **Model ID** | **In-Region endpoint URL** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | --- | 
| bedrock-mantle | openai.gpt-5.6-terra | https://bedrock-mantle.{region}.api.aws/openai/v1 | Not supported | Not supported | 
| bedrock-runtime | openai.gpt-5.6-terra | Not supported | us.openai.gpt-5.6-terra in the commercial AWS Regions, in.openai.gpt-5.6-terra in the India Regions | global.openai.gpt-5.6-terra | 

*For example, if region is us-east-1 (N. Virginia), then the bedrock-mantle endpoint URL will be "https://bedrock-mantle.us-east-1.api.aws/openai/v1". On `bedrock-runtime`, the base URL is "https://bedrock-runtime.{region}.amazonaws.com/openai/v1" and requests must name the geographic cross-Region inference ID `us.openai.gpt-5.6-terra` as the model.*

## Service Tiers
<a name="model-card-openai-gpt-56-terra-tiers"></a>

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-openai-gpt-56-terra-regional-availability"></a>

***Regional availability at a glance***

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md) page for more details.

Availability differs by endpoint.

**Availability using the `bedrock-mantle` endpoint**


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-east-2 (Ohio) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-west-2 (Oregon) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-gov-west-1 (GovCloud West) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 
| us-gov-east-1 (GovCloud East) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

**Availability using the `bedrock-runtime` endpoint**


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-east-2 (Ohio) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-west-1 (N. California) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-west-2 (Oregon) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ca-central-1 (Canada) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ca-west-1 (Calgary) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-central-1 (Frankfurt) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-central-2 (Zurich) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-north-1 (Stockholm) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-south-1 (Milan) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-south-2 (Spain) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-west-1 (Ireland) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-west-2 (London) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| eu-west-3 (Paris) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-east-2 (Taipei) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-northeast-1 (Tokyo) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-northeast-2 (Seoul) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-northeast-3 (Osaka) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-south-1 (Mumbai) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-south-2 (Hyderabad) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-1 (Singapore) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-2 (Sydney) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-3 (Jakarta) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-4 (Melbourne) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-5 (Malaysia) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-6 (New Zealand) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ap-southeast-7 (Thailand) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| il-central-1 (Tel Aviv) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| me-central-1 (UAE) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| me-south-1 (Bahrain) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| af-south-1 (Cape Town) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| sa-east-1 (São Paulo) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Green circle with white checkmark icon.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

## Quotas and Limits
<a name="model-card-openai-gpt-56-terra-quotas"></a>

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.html). For more information, see [Quotas for Amazon Bedrock](quotas.md) documentation and see the [limits](/general/latest/gr/bedrock.html#limits_bedrock) for the model.

On the `bedrock-runtime` endpoint, limits are managed as tokens per minute (TPM) with a 10x burndown rate, where 1 output token consumes 10 tokens.

## Sample Code
<a name="model-card-openai-gpt-56-terra-sample-code"></a>

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
OPENAI_BASE_URL="https://bedrock-mantle.us-east-1.api.aws/openai/v1"
```

------
#### [ bedrock-runtime ]

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-runtime.us-east-1.amazonaws.com/openai/v1"
```

------

**Note**  
On `bedrock-runtime`, name a cross-Region inference profile as the model — `us.openai.gpt-5.6-terra` or `global.openai.gpt-5.6-terra`. This model is not available for in-Region inference on that endpoint. Your IAM identity also needs `bedrock:InvokeModel` on your account's default project (`arn:aws:bedrock:{region}:{account-id}:project/default`) in addition to the inference profile.

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

------
#### [ bedrock-mantle ]

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-5.6-terra",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

------
#### [ bedrock-runtime ]

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="us.openai.gpt-5.6-terra",
    input="Can you explain the features of Amazon Bedrock?"
)
print(response)
```

------