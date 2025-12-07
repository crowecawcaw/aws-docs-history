# Complete request schema

The request schema is nearly identical between the Invoke API (streaming and
non-streaming) and the Converse API. There are subtle differences related to image and video
payload encoding. Because Amazon Nova Micro does not support images or videos as input, those
parts of the request schema do not apply to Amazon Nova Micro. Otherwise, the request schema is
the same for all Amazon Nova understanding models.

###### Important

The timeout period for inference calls to Amazon Nova is 60 minutes.
By default, AWS SDK clients timeout after 1 minute. We recommend that you increase the
read timeout period of your AWS SDK client to at least 60 minutes. For example, in the
AWS Python botocore SDK, change the value of the `read_timeout`field in
[botocore.config](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html# "https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#") to at least 3600.

```
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
    config=Config(
        connect_timeout=3600,  # 60 minutes
        read_timeout=3600,     # 60 minutes
        retries={'max_attempts': 1}
    )
)
```

```
`{
 "system": [
 {
 "text": `"string"`
 }
 ],
 "messages": [
 {
 "role": "user", //first turn should always be the user turn
 "content": [
 {
 "text": `"string"`
 },
 {
 "image": {
 "format": "jpeg" | "png" | "gif" | "webp",
 "source": {
 "bytes": `image` // Binary array (Converse API) or Base64-encoded string (Invoke API)
 }
 }
 },
 {
 "video": {
 "format": "mkv" | "mov" | "mp4" | "webm" | "three_gp" | "flv" | "mpeg" | "mpg" | "wmv",
 "source": {
 // Option 1: Sending a S3 location
 "s3Location": {
 "uri": `"string"`, // example: s3://my-bucket/object-key
 "bucketOwner": `"string"` // (Optional) example: "123456789012"
 },
 // Option 2: Sending file bytes
 "bytes": `video` // Binary array (Converse API) or Base64-encoded string (Invoke API)
 }
 }
 },
 {
 "audio": {
 "format": "mp3" | "opus" | "wav" | "aac" | "flac" | "mp4" | "ogg" | "mkv",
 "source": {
 // Option 1: Sending a S3 location
 "s3Location": {
 "uri": `"string"`, // example: s3://my-bucket/object-key
 "bucketOwner": `"string"` // (Optional) example: "123456789012"
 },
 // Option 2: Sending file bytes
 "bytes": `audio` // Binary array (Converse API) or Base64-encoded string (Invoke API)
 }
 }
 }
 ]
 },
 {
 "role": "assistant",
 "content": [
 {
 "text": `"string"` //prefilling assistant turn
 }
 ]
 }
 ],
 "inferenceConfig":{ // all Optional, Invoke parameter names used in this example
 "maxTokens": `int`, // greater than 0, equal or less than 5k (default: dynamic*)
 "temperature": `float`, // greater than 0 and less than 1.0 (default: 0.7)
 "topP": `float`, // greater than 0, equal or less than 1.0 (default: 0.9)
 "topK": `int`, // 0 or greater (default: 50)
 "stopSequences": `["string"]`,
 "reasoningConfig": {
 "type": `"string"`, //"enabled"/"disabled" (default: "disabled")
 "maxReasoningEffort": `"string"` // "low", "medium", "high"
 }
 },
 "toolConfig": { // all Optional
 "tools": [
 {
 "toolSpec": {
 "name": `"string"`, //meaningful tool name (Max char: 64)
 "description": `"string"`, //meaningful description of the tool
 "inputSchema": {
 "json": { // The JSON schema for the tool. For more information, see JSON Schema Reference
 "type": "`object`",
 "properties": {
 `"arg1"`: { //arguments
 "type": "`string`", //argument data type
 "description": "`string`" //meaningful description
 }
 },
 "required": [
 `"string"` //args
 ]
 }
 }
 }
 }
 ],
 },
 "toolChoice": { //can select one of three options
 "auto": {},
 "any": {},
 "tool": {
 "name": `"string"` //name of tool
 }
 }
}`
```

The following are required parameters:

- `system` – (Optional) The system prompt for the request.

A system prompt is a way of providing context and instructions to Amazon Nova, such as
specifying a particular goal or role.

- `messages` – (Required) The input messages.
  - `role` – The role of the conversation turn. Valid values are
    `user` and `assistant`.
  - `content` – (required) A list of [ContentBlock](../../../bedrock/latest/APIReference/API_runtime_ContentBlock.md "../../../bedrock/latest/APIReference/API_runtime_ContentBlock.md") objects that contain content for the conversation. Each object contains a key that specifies the type of content (`text`, `image`, `video`, or `audio`). The value of the object depends on the key type. The following types are supported for the key:
    - `text` – Maps to an object containing a single field, `text`, whose value is the textual prompt for the conversational turn. If the conversational turn also includes an `image` or `video` object, the `text` object is interpreted as a text prompt accompanying the image or video.
    - `image` – (Not supported for Amazon Nova Micro) Maps to an object representing image content and containing the following fields:
      - `format` – (required) The image format. You can specify the
        following image formats:
        - `jpeg`
        - `png`
        - `webp`
        - `gif`

      - `source` – (required) The image data. For the Invoke API,
        this must be a Base64 encoded image string. For the Converse
        API, this must be a byte array.
      - `bytes` – (required) The image data. For the Invoke API,
        this must be a Base64 encoded image string. For the Converse API, this
        must be a byte array.

    - `video` – (Not supported for Amazon Nova Micro) Maps to an object representing video content and containing the following fields:
      - `format` – (required) The video format. You can specify the
        following values:
        - `mkv`
        - `mov`
        - `mp4`
        - `webm`
        - `three_gp`
        - `flv`
        - `mpeg`
        - `mpg`
        - `wmv`

      - `source` – (required) The source of the video data. You can
        specify an Amazon S3 URI or the video file bytes in the request.
        - `uri` – (required) The Amazon S3 URI of the video file. For
          example, `“s3://my-bucket/object-key”`
        - `bucketOwner` – (optional) The Account ID that owns the
          bucket. Use this if you are invoking the model from a separate
          account.
        - `bytes` – (required) The video data. For the Invoke
          API, this must be a Base64 encoded video string. For the Converse API,
          this must be a byte array.

    - `audio` – ( only) Maps to an object representing audio content and containing the following fields:
      - `format` – (required) The audio format. You can specify the
        following values:
        - `aac`
        - `flac`
        - `mkv`
        - `mp3`
        - `mp4`
        - `ogg`
        - `opus`
        - `wav`

      - `source` – (required) The source of the audio data. You can
        specify an Amazon S3 URI or the audio file bytes in the request.
        - `uri` – (required) The Amazon S3 URI of the audio file. For
          example, `"s3://my-bucket/object-key"`
        - `bucketOwner` – (optional) The Account ID that owns the
          bucket. Use this if you are invoking the model from a separate
          account.
        - `bytes` – (required) The audio data. For the Invoke
          API, this must be a Base64 encoded audio string. For the Converse API,
          this must be a byte array.

- `inferenceConfig:` These are inference config values that can be passed in
  inference.
  - `maxTokens` – (Optional) The maximum number of tokens to generate before stopping.

  Note that Amazon Nova models might stop generating tokens before reaching the value
  of `maxTokens`. The maximum new tokens value allowed is 5K.
  - `temperature` – (Optional) The amount of randomness injected into the response. Valid values are between 0.00001 and 1, inclusive. The default value is 0.7.
  - `topP` – (Optional) Use nucleus sampling.

  Amazon Nova computes the cumulative distribution over all the options for each
  subsequent token in decreasing probability order and cuts it off once it reaches a
  particular probability specified by `topP`. You should alter either
  `temperature` or `topP`, but not both. Valid values are
  between 0 and 1, inclusive. The default value is 0.9.
  - `topK` – (Optional)
    Only sample from the top K options for each subsequent token.

  Use the `topK` parameter to remove long tail, low probability responses. Valid
  values are between 0 and 128. The default value is that this parameter is not
  used.

  ###### Note

  When using the Converse API with the `topK` parameter, an additional
  `inferenceConfig` parameter must be included in an
  `additionalModelRequestFields` field. See [Using the Converse API](using-converse-api.md "using-converse-api.md") for an example
  of how these parameters are passed.
  - `stopSequences` – (Optional) Array of strings containing stop
    sequences. If the model generates any of those strings, generation will stop and
    response is returned up until that point.
  - `reasoningConfig` – (Amazon Nova Pro and Amazon Nova Lite only) The reasoning configuration values that can be passed in inference.
    - `type` – (Optional) Whether to enable or disable the reasoning. Valid options are `enabled` or `disabled`. The default value is `disabled`.
    - `maxReasoningEffort` – The computational effort used in the reasoning process. Valid options are `low`, `medium`, or `high`. In streaming, when using `low` and `medium` settings, reasoning content will be streamed as each token is generated when using `ConverseStream`, however, the `high` works differently, applying different approaches to improve quality resulting in outputting all the reasoning content in a final chunk.

  ###### Note

  When using the Converse API with the `reasoningConfig` parameter, the parameter should be placed in the `additionalModelRequestFields` field. See [Using the Converse API](using-converse-api.md "using-converse-api.md") for an example
  of how these parameters are passed.

| Parameter     | Default value | Range     |
| ------------- | ------------- | --------- |
| `temperature` | 0.7           | 0.00001-1 |
| `topP`        | 0.9           | 0-1       |
| `topK`        | Not used      | 0-128     |

- `toolConfig` – (Optional) JSON object following [ToolConfig schema](../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md "../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md"), containing the tool specification and tool choice. This
  schema is the same followed [by the
  Converse API](../../../bedrock/latest/userguide/tool-use.md "../../../bedrock/latest/userguide/tool-use.md")
  - `toolChoice` – (Optional) Specifies which tools the model can use. You can select one of three options:
    - `auto` – The model automatically decides whether to use tools and which tools to use.
    - `any` – The model must use at least one of the provided tools.
    - `tool` – The model must use the specific tool identified by name.
