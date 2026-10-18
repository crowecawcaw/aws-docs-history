

# TwelveLabs Pegasus 1.5
<a name="model-parameters-pegasus-1-5"></a>

The TwelveLabs Pegasus 1.5 model provides comprehensive video understanding and analysis capabilities. Building on TwelveLabs Pegasus 1.2, it adds video segmentation that transforms raw video into structured, timestamped metadata across an entire video. It can analyze video content and generate textual descriptions, insights, and answers to questions about the video.

Use this information to make inference calls to TwelveLabs models with the [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) (streaming) operations.
+ Provider — TwelveLabs
+ Categories — Video understanding, content analysis, video segmentation
+ Model ID — `twelvelabs.pegasus-1-5-v1:0`
+ Input modality — Video
+ Output modality — Text
+ Max video size — up to 2 hours long (less than 2 GB file size)

**Note**  
TwelveLabs Pegasus 1.5 is available through cross-Region inference only. Use the geo inference ID (`us.twelvelabs.pegasus-1-5-v1:0`) or the global inference ID (`global.twelvelabs.pegasus-1-5-v1:0`) rather than the base model ID.

## TwelveLabs Pegasus 1.5 request parameters
<a name="model-parameters-pegasus-1-5-request"></a>

The following table describes the input parameters for the TwelveLabs Pegasus 1.5 model:


**TwelveLabs Pegasus 1.5 request parameters**  

| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| analysis\_mode | string | No | The analysis to perform. Valid values: general (default) returns free-form text analysis driven by inputPrompt or prompt\_v2; time\_based\_metadata returns structured, timestamped segments defined by segment\_definitions. | 
| inputPrompt | string | Conditional | Prompt to analyze the video. Required when analysis\_mode is general, unless you supply prompt\_v2 instead. Must be omitted when analysis\_mode is time\_based\_metadata; including it returns a ValidationException. In that mode the segment\_definitions entries describe what to extract instead. | 
| prompt\_v2 | object | Conditional | An alternative to inputPrompt that can reference images from the prompt text. Use either inputPrompt or prompt\_v2, not both; supplying both returns a ValidationException. Like inputPrompt, it must be omitted when analysis\_mode is time\_based\_metadata. A video in mediaSource is still required: a request that supplies prompt\_v2 and no video fails. | 
| prompt\_v2.input\_text | string | Conditional | The prompt text. Required when you use prompt\_v2. To refer to an image, include a placeholder of the form <@{{name}}>, where {{name}} matches the name of an entry in media\_sources. A placeholder with no matching entry returns a ValidationException. | 
| prompt\_v2.media\_sources | array | No | Images that input\_text can refer to by placeholder. Each entry takes a name, a media\_type, and a base64String. These images supplement the video; they don't replace it. | 
| prompt\_v2.media\_sources[].name | string | Conditional | The name used to refer to this image from input\_text, as <@{{name}}>. Required for each entry. | 
| prompt\_v2.media\_sources[].media\_type | string | Conditional | The kind of media in this entry. The only valid value is image. Required for each entry. | 
| prompt\_v2.media\_sources[].base64String | string | Conditional | Base64 encoded byte string for the image. Required for each entry. | 
| mediaSource | object | Yes | Describes the media source. Either base64String or s3Location must be provided. | 
| mediaSource.base64String | string | No | Base64 encoded byte string for the video. Max: 25 MB. For larger videos, use s3Location. | 
| mediaSource.s3Location.uri | string | No | S3 URI where the video can be downloaded from. Max: up to 2 hours long (less than 2 GB file size). The bucket must be in the same AWS Region that you send the request to. This applies to the geo and global inference profiles as well: the profile determines where the request can be served, but it does not widen where the bucket can live. A bucket in any other Region fails with a ValidationException. | 
| mediaSource.s3Location.bucketOwner | string | Conditional | AWS account ID of the bucket owner. Required when s3Location is used. | 
| temperature | double | No | Controls randomness in the output. Default: 0.2, Min: 0, Max: 1. | 
| maxOutputTokens | integer | No | The maximum number of tokens to generate. Min: 512, Max: 98304. | 
| responseFormat | object | No | Specifies a structured output format. When you include responseFormat, you must also set responseFormat.type; omitting it returns a ValidationException. Note that this type is a sibling of jsonSchema and is not the same as the type inside the schema, which describes the schema's own root type. Valid values, each tied to an analysis mode:+ `json_schema` — required when `analysis_mode` is `general`. Supply the schema under `responseFormat.jsonSchema`. In addition to the standard JSON Schema types, a property can use `"type": "timestamp"` with a `format` of `seconds` or `hh:mm:ss.fff` to have the model return a video timestamp.<br />+ `segment_definitions` — required when `analysis_mode` is `time_based_metadata`. Supply the definitions under `responseFormat.segment_definitions`, as an alternative to the top-level `segment_definitions` field.Using a value that doesn't match the analysis mode returns a ValidationException. You can omit responseFormat entirely, in which case general mode returns free-form text and time\_based\_metadata mode uses the top-level segment\_definitions. | 
| start\_time | double | No | Analyze only the portion of the video starting at this offset, in seconds. Use with end\_time to analyze a clip rather than the whole video. Applies to both analysis modes; in time\_based\_metadata mode only segments inside the clip are returned. | 
| end\_time | double | No | Analyze only the portion of the video ending at this offset, in seconds. Must be greater than start\_time; otherwise the request returns a ValidationException. | 
| segment\_time\_format | string | No | Controls how segment boundaries are formatted in the response when analysis\_mode is time\_based\_metadata. Use seconds to return start\_sec and end\_sec as numbers, or hh:mm:ss.fff to return them as timestamp strings. | 
| segment\_definitions | array | Conditional | Required when analysis\_mode is time\_based\_metadata. Each entry defines a segment type to extract, with an id, a description, and a list of fields (each with name, type, and description) to populate per segment. A field can also carry an enum array, which restricts the model's output for that field to the listed values. | 

## TwelveLabs Pegasus 1.5 response fields
<a name="model-parameters-pegasus-1-5-response"></a>

The following table describes the output fields for the TwelveLabs Pegasus 1.5 model:


**TwelveLabs Pegasus 1.5 response fields**  

| Field | Type | Description | 
| --- | --- | --- | 
| message | string | Output message containing the model's analysis of the video. When responseFormat.jsonSchema is set, this field returns a JSON string that conforms to the supplied schema. Parse the string to access individual fields. | 
| stopReason | string | Reason the output ended. Valid values: stop (the model returned the full response without reaching any limits), length (the generation reached the maxOutputTokens limit). | 
| segments | array | Present when analysis\_mode is time\_based\_metadata. The list of extracted segments, each carrying the fields declared in the matching segment\_definitions entry along with its start\_sec and end\_sec time range. When you supply two or more segment\_definitions entries, each segment also carries a \_definition\_id field holding the id of the definition that produced it. With a single definition, no identifier field is returned. | 
| definition\_errors | array | Present when analysis\_mode is time\_based\_metadata. Lists any segment\_definitions entries that could not be processed; empty ([]) when all definitions were applied successfully. | 
| finish\_reason | string | Present when analysis\_mode is time\_based\_metadata. Returned alongside stopReason in the segmentation response and carries the same value. | 

**Note**  
TwelveLabs Pegasus 1.5 returns the stop reason in the `stopReason` field. This differs from TwelveLabs Pegasus 1.2, which returns `finishReason`. In `time_based_metadata` mode, the response additionally includes a `finish_reason` field carrying the same value alongside `stopReason`.

## TwelveLabs Pegasus 1.5 request and response
<a name="model-parameters-pegasus-1-5-examples"></a>

The following examples show how to use the TwelveLabs Pegasus 1.5 model with different input sources and analysis modes.

------
#### [ Request ]

The following examples show request formats for the TwelveLabs Pegasus 1.5 model.

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
        "type": "json_schema",
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

**Referring to an image from the prompt:**

```
{
    "prompt_v2": {
        "input_text": "Does the logo in <@logo> appear anywhere in this video?",
        "media_sources": [
            {
                "name": "logo",
                "media_type": "image",
                "base64String": "{{base64-encoded image}}"
            }
        ]
    },
    "mediaSource": {
        "s3Location": {
            "uri": "s3://path-to-video-object-in-s3",
            "bucketOwner": "bucket-owner-account-id"
        }
    },
    "maxOutputTokens": 4096
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

The following examples show response formats from the TwelveLabs Pegasus 1.5 model.

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

The following response corresponds to the single `segment_definitions` entry in the preceding request. Each segment carries the fields declared in that definition along with its time range, and no identifier field is present.

```
{
  "segments": [
    {
      "start_sec": 0,
      "end_sec": 12,
      "summary": "Opening shot establishing the location"
    },
    {
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

**Response with time-based metadata and multiple definitions:**

When the request supplies two or more `segment_definitions` entries, each segment additionally carries a `_definition_id` field holding the `id` of the definition that produced it. Use that field to correlate a segment back to its definition. The following response is for a request with the definitions `scenes` and `colors`.

```
{
  "segments": [
    {
      "start_sec": 0,
      "end_sec": 12,
      "summary": "Opening shot establishing the location",
      "_definition_id": "scenes"
    },
    {
      "start_sec": 0,
      "end_sec": 12,
      "palette": "Muted blues and greys",
      "_definition_id": "colors"
    },
    {
      "start_sec": 12,
      "end_sec": 30,
      "summary": "Main subject enters and the action begins",
      "_definition_id": "scenes"
    },
    {
      "start_sec": 12,
      "end_sec": 30,
      "palette": "Warm reds and oranges",
      "_definition_id": "colors"
    }
  ],
  "definition_errors": [],
  "stopReason": "stop",
  "finish_reason": "stop"
}
```

**Note**  
The segment identifier is named `_definition_id`, not `id`. The `id` field appears only on the request side, in each `segment_definitions` entry. The response carries `_definition_id` only when the request supplies two or more definitions, so a parser should treat it as optional. This behavior is the same for `InvokeModel` and `InvokeModelWithResponseStream`; in the streaming case the `segments` array arrives in the final chunk.

**Response when max tokens reached:**

```
{
  "message": "This video contains multiple scenes showing various activities. The first scene shows...",
  "stopReason": "length"
}
```

------