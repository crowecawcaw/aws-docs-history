

# Pegasus v1.5
<a name="model-card-twelvelabs-pegasus-v1-5"></a>

## ![Icon showing branching arrows representing a merge or split workflow pattern.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/models/twelvelabs.png) TwelveLabs — Pegasus v1.5
<a name="model-card-twelvelabs-pegasus-v1-5-header"></a>

## Model Details
<a name="model-card-twelvelabs-pegasus-v1-5-details"></a>

Pegasus v1.5 is TwelveLabs' video-to-text generation model that produces summaries, detailed descriptions, and structured responses about video content. Building on Pegasus v1.2, it adds video segmentation to transform raw video into structured, timestamped metadata across an entire video. For more information about model development and performance, see the [model/service card](https://docs.twelvelabs.io/docs/concepts/models/pegasus).
+ **Model launch date:** October 5, 2026
+ **EOL no sooner than:** Not Applicable. At least a 45-day EOL notice will be provided.
+ **Legacy period:** at least 45 days
+ **Model lifecycle policy:** [Model lifecycle](model-lifecycle.md)
+ **Model EOL date:** N/A
+ **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/)
+ **Model lifecycle:** Active
+ **Marketplace product ID:** `prod-emhhqbi7fzsyo`


| **Input Modalities** | **Output Modalities** | **[APIs supported](apis.html)** | **[Endpoints supported](endpoints.html)** | 
| --- | --- | --- | --- | 
| ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Audio | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Embedding | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Responses | ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) bedrock-runtime | 
| ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Image | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Chat Completions | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) bedrock-mantle | 
| ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Speech | ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Invoke |  | 
| ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Text | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Converse |  | 
| ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) Video | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) Video |  |  | 

**Tip**  
Whenever possible, we recommend using the `bedrock-runtime` endpoint for new applications. See [Endpoints supported by Amazon Bedrock](endpoints.md) for details.

**Note**  
Pegasus v1.5 is available through cross-Region inference only. Requests must use the US geographic inference profile (`us.twelvelabs.pegasus-1-5-v1:0`) or the global inference profile (`global.twelvelabs.pegasus-1-5-v1:0`). In-Region on-demand inference is not supported.

## Capabilities and Features
<a name="model-card-twelvelabs-pegasus-v1-5-capabilities"></a>

***Bedrock Features***

**Features supported using `bedrock-runtime` endpoint**


| **Supported** | **Not Supported** | 
| --- | --- | 
|  + ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) [Response streaming](/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)  |  + ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Guardrails](guardrails.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Intelligent prompt routing](prompt-routing.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Abuse detection](abuse-detection.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Prompt optimization](prompt-management-optimize.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Count tokens](count-tokens.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Knowledge base](knowledge-base.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Model evaluation](evaluation.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Prompt management](prompt-management.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Flows](flows.html)<br />+ ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) [Agents](agents.html)  | 

## Advanced
<a name="model-card-twelvelabs-pegasus-v1-5-advanced"></a>

Use the following request parameters and response fields to make inference calls to Pegasus v1.5 with the InvokeModel and InvokeModelWithResponseStream (streaming) operations.

### Request parameters
<a name="model-card-twelvelabs-pegasus-v1-5-advanced-request"></a>


| **Field** | **Type** | **Required** | **Description** | 
| --- | --- | --- | --- | 
| analysis\_mode | string | No | The analysis to perform. Valid values: general (default) returns free-form text analysis driven by inputPrompt; time\_based\_metadata returns structured, timestamped segments defined by segment\_definitions. | 
| inputPrompt | string | Conditional | Prompt to analyze the video. Required when analysis\_mode is general. | 
| mediaSource | object | Yes | Describes the media source. Either base64String or s3Location must be provided. | 
| mediaSource.base64String | string | No | Base64 encoded byte string for the video. Max: 25MB. For larger videos, use s3Location. | 
| mediaSource.s3Location.uri | string | No | S3 URI where the video can be downloaded from. Max: up to 2 hours long (less than 2 GB file size). | 
| mediaSource.s3Location.bucketOwner | string | Conditional | AWS account ID of the bucket owner. Required when s3Location is used. | 
| temperature | double | No | Controls randomness in the output. Default: 0.2, Min: 0, Max: 1. | 
| maxOutputTokens | integer | No | The maximum number of tokens to generate. Min: 512, Max: 98304. | 
| responseFormat | object | No | Specifies a structured-output JSON Schema. Set the schema object directly under responseFormat.jsonSchema. Applies to general analysis mode. | 
| segment\_definitions | array | Conditional | Required when analysis\_mode is time\_based\_metadata. Each entry defines a segment type to extract, with an id, a description, and a list of fields (each with name, type, and description) to populate per segment. | 

### Response fields
<a name="model-card-twelvelabs-pegasus-v1-5-advanced-response"></a>


| **Field** | **Type** | **Description** | 
| --- | --- | --- | 
| message | string | Output message containing the model's analysis of the video. When responseFormat.jsonSchema is set, this field returns a JSON string that conforms to the supplied schema. Parse the string to access individual fields. | 
| stopReason | string | Reason the output ended. Valid values: stop (the model returned the full response without reaching any limits), length (the generation reached the maxOutputTokens limit). | 
| segments | array | Present when analysis\_mode is time\_based\_metadata. The list of extracted segments, each carrying the fields declared in the matching segment\_definitions entry along with its time range. | 
| definition\_errors | array | Present when analysis\_mode is time\_based\_metadata. Lists any segment\_definitions entries that could not be processed; empty ([]) when all definitions were applied successfully. | 
| finish\_reason | string | Present when analysis\_mode is time\_based\_metadata. Returned alongside stopReason in the segmentation response and carries the same value. | 

**Note**  
Pegasus v1.5 returns the stop reason in the `stopReason` field. This differs from Pegasus v1.2, which returns `finishReason`. In `time_based_metadata` mode, the response additionally includes a `finish_reason` field carrying the same value alongside `stopReason`.

### Examples
<a name="model-card-twelvelabs-pegasus-v1-5-advanced-examples"></a>

------
#### [ Request ]

The following examples show request formats for Pegasus v1.5.

**Using base64 encoded video:**

```
{
  "analysis_mode": "general",
  "inputPrompt": "Tell me about this video",
  "mediaSource": {
      "base64String": "<BASE64 STRING OF VIDEO FILE>"
  },
  "temperature": 0.2
}
```

**Using S3 stored video:**

```
{
    "analysis_mode": "general",
    "inputPrompt": "Summarize this video and list key scenes with timestamps",
    "mediaSource": {
        "s3Location": {
            "uri": "s3://path-to-video-object-in-s3",
            "bucketOwner": "bucket-owner-account-id"
        }
    },
    "temperature": 0.2,
    "maxOutputTokens": 2048
}
```

**Using structured output format:**

```
{
    "analysis_mode": "general",
    "inputPrompt": "Analyze this video and provide a structured summary",
    "mediaSource": {
        "s3Location": {
            "uri": "s3://path-to-video-object-in-s3",
            "bucketOwner": "bucket-owner-account-id"
        }
    },
    "temperature": 0.2,
    "maxOutputTokens": 2048,
    "responseFormat": {
        "jsonSchema": {
            "type": "object",
            "properties": {
                "summary":    { "type": "string" },
                "key_scenes": { "type": "array", "items": { "type": "string" } },
                "duration":   { "type": "string" }
            },
            "required": ["summary", "key_scenes"]
        }
    }
}
```

**Using time-based metadata (video segmentation):**

```
{
    "analysis_mode": "time_based_metadata",
    "mediaSource": {
        "s3Location": {
            "uri": "s3://path-to-video-object-in-s3",
            "bucketOwner": "bucket-owner-account-id"
        }
    },
    "maxOutputTokens": 4096,
    "temperature": 0,
    "segment_definitions": [
        {
            "id": "scenes",
            "description": "What happens in this segment",
            "fields": [
                { "name": "summary", "type": "string", "description": "What happens in the segment" }
            ]
        }
    ]
}
```

------
#### [ Response ]

The following examples show response formats from Pegasus v1.5.

**Standard response:**

```
{
  "message": "This video shows a person walking through a park during sunset. The scene includes trees, a walking path, and golden lighting from the setting sun.",
  "stopReason": "stop"
}
```

**Response with structured output:**

```
{
  "message": "{\"summary\": \"A peaceful evening walk through a park at sunset\", \"key_scenes\": [\"Person entering the park\", \"Walking along tree-lined path\", \"Sunset lighting through trees\"], \"duration\": \"Approximately 2 minutes\"}",
  "stopReason": "stop"
}
```

**Response with time-based metadata:**

```
{
  "segments": [
    {
      "id": "scenes",
      "start_sec": 0,
      "end_sec": 12,
      "summary": "Opening shot establishing the location"
    },
    {
      "id": "scenes",
      "start_sec": 12,
      "end_sec": 30,
      "summary": "Main subject enters and the action begins"
    }
  ],
  "definition_errors": [],
  "stopReason": "stop",
  "finish_reason": "stop"
}
```

**Response when max tokens reached:**

```
{
  "message": "This video contains multiple scenes showing various activities. The first scene shows...",
  "stopReason": "length"
}
```

------

## Pricing
<a name="model-card-twelvelabs-pegasus-v1-5-pricing"></a>

This model is a third-party model offered and billed through AWS Marketplace. Charges appear on your AWS bill and in AWS Cost Explorer under the model provider (not under Amazon Bedrock). For pricing, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/) page.

## Programmatic Access
<a name="model-card-twelvelabs-pegasus-v1-5-programmatic-access"></a>

Use the following model IDs and endpoint URLs to access this model programmatically. Pegasus v1.5 is available through cross-Region inference only, so you must use the geo or global inference ID rather than the base model ID. For more information about the available APIs and endpoints, see [APIs supported](apis.html) and [Endpoints supported](endpoints.html).


| **Endpoint** | **Model ID** | **Geo inference ID** | **Global inference ID** | 
| --- | --- | --- | --- | 
| bedrock-runtime | twelvelabs.pegasus-1-5-v1:0 | us.twelvelabs.pegasus-1-5-v1:0 | global.twelvelabs.pegasus-1-5-v1:0 | 

## Service Tiers
<a name="model-card-twelvelabs-pegasus-v1-5-tiers"></a>

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment (set `"service_tier": "default"` or omit the field). **Priority** delivers the fastest response times for a price premium (set `"service_tier": "priority"`). **Flex** provides lower-cost access for flexible, non-time-sensitive workloads (set `"service_tier": "flex"`). **Reserved** provides dedicated throughput with a term commitment for predictable workloads; it is set at the account level rather than per request (contact your AWS account team to enable). For more information, see [service tiers](service-tiers-inference.html).


| **Standard** | **Priority** | **Flex** | **Reserved** | 
| --- | --- | --- | --- | 
| ![Green circle with white checkmark icon.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![Red circle with white X icon indicating error, cancel, or close action.](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | 

## Regional Availability
<a name="model-card-twelvelabs-pegasus-v1-5-regional-availability"></a>

***Regional availability at a glance***

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md) page for more details.

Pegasus v1.5 supports Geo Cross-Region inference from the US Regions and Global Cross-Region inference from the Regions listed in the following table. In-Region inference is not supported.


| **Region** | **In-Region** | **Geo** | **Global** | 
| --- | --- | --- | --- | 
| us-east-1 (N. Virginia) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-east-2 (Ohio) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-west-1 (N. California) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| us-west-2 (Oregon) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ca-central-1 (Canada) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| ca-west-1 (Calgary) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
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
| af-south-1 (Cape Town) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| mx-central-1 (Mexico) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 
| sa-east-1 (São Paulo) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![not-supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-no.png) | ![supported](https://docs.aws.amazon.com/bedrock/latest/userguide/images/icons/icon-yes.png) | 

## Quotas and Limits
<a name="model-card-twelvelabs-pegasus-v1-5-quotas"></a>

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](quotas-increase.html). For more information, see [Quotas for Amazon Bedrock](quotas.md) documentation and see the [limits](/general/latest/gr/bedrock.html#limits_bedrock) for the model.

## Sample Code
<a name="model-card-twelvelabs-pegasus-v1-5-sample-code"></a>

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
    modelId='us.twelvelabs.pegasus-1-5-v1:0',
    body=json.dumps({
            'inputPrompt': 'Tell me about this video',
            'mediaSource': {
                's3Location': {
                    'uri': 's3://your-bucket/your-video.mp4',
                    'bucketOwner': '123456789012'
                }
            },
            'maxOutputTokens': 4096
    })
)
print(json.loads(response['body'].read()))
```

------