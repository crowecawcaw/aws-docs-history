# Using the Converse

API

To use the Converse API, you call the `Converse` or
`ConverseStream` operations to send messages to a model. To call
`Converse`, you require permission for the
`bedrock:InvokeModel` operation. To call `ConverseStream`, you
require permission for the `bedrock:InvokeModelWithResponseStream`
operation.

###### Topics

- [Request](#conversation-inference-call-request "#conversation-inference-call-request")
- [Response](#conversation-inference-call-response "#conversation-inference-call-response")

## Request

When you make a [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") request with an [Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#br-rt "../../../general/latest/gr/bedrock.md#br-rt"), you can include the following
fields:

- **modelId** – A required parameter in
  the header that lets you specify the resource to use for inference.
- The following fields let you customize the prompt:
  - **messages** – Use to specify
    the content and role of the prompts.
  - **system** – Use to specify
    system prompts, which define instructions or context for the
    model.
  - **inferenceConfig** – Use to
    specify inference parameters that are common to all models.
    Inference parameters influence the generation of the
    response.
  - **additionalModelRequestFields**
    – Use to specify inference parameters that are specific to the
    model that you run inference with.
  - **promptVariables** – (If you
    use a prompt from Prompt management) Use this field to define the variables in
    the prompt to fill in and the values with which to fill them.

- The following fields let you customize how the response is
  returned:
  - **guardrailConfig** – Use this
    field to include a guardrail to apply to the entire prompt.
  - **toolConfig** – Use this field
    to include a tool to help a model generate responses.
  - **additionalModelResponseFieldPaths**
    – Use this field to specify fields to return as a JSON pointer
    object.
  - **serviceTier**
    – Use this field to specify the service tier for a particular
    request

- **requestMetadata** – Use this field to
  include metadata that can be filtered on when using invocation logs.

###### Note

The following restrictions apply when you use a Prompt management prompt with `Converse` or `ConverseStream`:

- You can't include the `additionalModelRequestFields`, `inferenceConfig`, `system`, or `toolConfig` fields.
- If you include the `messages` field, the messages are appended after the messages defined in the prompt.
- If you include the `guardrailConfig` field, the guardrail is applied to the entire prompt. If you include `guardContent` blocks in the [ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md") field, the guardrail will only be applied to those blocks.

Expand a section to learn more about a field in the `Converse` request
body:

The `messages` field is an array of [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") objects, each of
which defines a message between the user and the model. A
`Message` object contains the following fields:

- **role** – Defines whether the
  message is from the `user` (the prompt sent to the model)
  or `assistant` (the model response).
- **content** – Defines the
  content in the prompt.

###### Note

Amazon Bedrock doesn't store any text, images, or documents that you
provide as content. The data is only used to generate the
response.
You can maintain conversation context by including all the messages in the
conversation in subsequent `Converse` requests and using the
`role` field to specify whether the message is from the user
or the model.

The `content` field maps to an array of [ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md") objects.
Within each [ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md"), you can specify one of the following fields (to
see what models support what blocks, see [Supported models and
model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md")):

text
The `text` field maps to a string specifying the
prompt. The `text` field is interpreted alongside
other fields that are specified in the same
[ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md").

The following shows a [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") object with a
`content` array containing only a text
[ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md"):

```
{
    "role": "user",
    "content": [
        {
            "text": "`string`"
        }
    ]
}
```

image
The `image` field maps to an [ImageBlock](../APIReference/API_runtime_ImageBlock.md "../APIReference/API_runtime_ImageBlock.md"). Pass the
raw bytes, encoded in base64, for an image in the
`bytes` field. If you use an AWS SDK, you don't
need to encode the bytes in base64.

If you exclude the `text` field, the model
describes the image.

The following shows an example [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") object with a
`content` array containing only an image
[ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md"):

```
{
    "role": "user",
    "content": [
        {
            "image": {
                "format": "png",
                "source": {
                    "bytes": "`image in bytes`"
                }
            }
        }
    ]
}
```

You can also specify an Amazon S3 URI instead of passing the bytes directly in the request body. The following shows a sample `Message` object with a content array containing the source passed through an Amazon S3 URI.

```
{
    "role": "user",
    "content": [
        {
            "image": {
                "format": "png",
                "source": {
                    "s3Location": {
                        "uri": "s3://amzn-s3-demo-bucket/myImage",
                        "bucketOwner": "111122223333"
                    }
                }
            }
        }
    ]
}
```

document
The `document` field maps to an [DocumentBlock](../APIReference/API_runtime_DocumentBlock.md "../APIReference/API_runtime_DocumentBlock.md"). If
you include a `DocumentBlock`, check that your
request conforms to the following restrictions:

- In the `content` field of the [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md")
  object, you must also include a `text` field
  with a prompt related to the document.
- Pass the raw bytes, encoded in base64, for the
  document in the `bytes` field. If you use an
  AWS SDK, you don't need to encode the document bytes
  in base64.
- The `name` field can only contain the
  following characters:
  - Alphanumeric characters
  - Whitespace characters (no more than one in a
    row)
  - Hyphens
  - Parentheses
  - Square brackets

###### Note

The `name` field is vulnerable to
prompt injections, because the model might
inadvertently interpret it as instructions.
Therefore, we recommend that you specify a neutral
name.

When using a document you can enable the `citations` tag, which
will provide document specific citations in the response of the API call. See
the [DocumentBlock](../APIReference/API_runtime_DocumentBlock.md "../APIReference/API_runtime_DocumentBlock.md") API for more details.

The following shows a sample [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") object with a
`content` array containing only a document
[ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md") and a required accompanying text
[ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md").

```
{
    "role": "user",
    "content": [
        {
            "text": "`string`"
        },
        {
            "document": {
                "format": "pdf",
                "name": "MyDocument",
                "source": {
                    "bytes": "`document in bytes`"
                }
            }
        }
    ]
}
```

You can also specify an Amazon S3 URI instead of passing the bytes directly in the request body. The following shows a sample `Message` object with a content array containing the source passed through an Amazon S3 URI.

```
{
    "role": "user",
    "content": [
        {
            "text": "`string`"
        },
        {
            "document": {
                "format": "pdf",
                "name": "MyDocument",
                "source": {
                    "s3Location": {
                      "uri": "s3://amzn-s3-demo-bucket/myDocument",
                      "bucketOwner": "111122223333"
                    }
                }
            }
        }
    ]
}
```

video
The `video` field maps to a [VideoBlock](../APIReference/API_runtime_VideoBlock.md "../APIReference/API_runtime_VideoBlock.md") object.
Pass the raw bytes in the `bytes` field, encoded in
base64. If you use the AWS SDK, you don't need to encode the
bytes in base64.

If you don't include the `text` field, the model
will describe the video.

The following shows a sample [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") object with a
`content` array containing only a video
[ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md").

```
{
    "role": "user",
    "content": [
        {
            "video": {
                "format": "mp4",
                "source": {
                    "bytes": "`video in bytes`"
                }
            }
        }
    ]
}
```

You can also specify an Amazon S3 URI instead of passing the bytes directly in the request body. The following shows a sample `Message` object with a content array containing the source passed through an Amazon S3 URI.

```
{
    "role": "user",
    "content": [
        {
            "video": {
                "format": "mp4",
                "source": {
                    "s3Location": {
                        "uri": "s3://amzn-s3-demo-bucket/myVideo",
                        "bucketOwner": "111122223333"
                    }
                }
            }
        }
    ]
}
```

###### Note

The assumed role must have the `s3:GetObject`
permission to the Amazon S3 URI. The `bucketOwner`
field is optional but must be specified if the account
making the request does not own the bucket the Amazon S3 URI is
found in. For more information, see [Configure access to Amazon S3 buckets](s3-bucket-access.md "s3-bucket-access.md").

cachePoint
You can add cache checkpoints as a block in a message
alongside an accompanying prompt by using
`cachePoint` fields to utilize prompt caching.
Prompt caching is a feature that lets you begin caching the
context of conversations to achieve cost and latency savings.
For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

The following shows a sample [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") object with a
`content` array containing a document
[ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md") and a required accompanying text [ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md"),
as well as a **cachePoint** that adds both the
document and text contents to the cache.

```
{
    "role": "user",
    "content": [
        {
            "text": "`string`"
        },
        {
            "document": {
                "format": "pdf",
                "name": "string",
                "source": {
                    "bytes": "`document in bytes`"
                }
            }
        },
        {
            "cachePoint": {
                "type": "default"
            }
        }
    ]
}
```

guardContent
The `guardContent` field maps to a [GuardrailConverseContentBlock](../APIReference/API_runtime_GuardrailConverseContentBlock.md "../APIReference/API_runtime_GuardrailConverseContentBlock.md")
object. You can use this field to target an input to be
evaluated by the guardrail defined in the
`guardrailConfig` field. If you don't specify
this field, the guardrail evaluates all messages in the request
body. You can pass the following types of content in a
`GuardBlock`:

- **text** – The
  following shows an example [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") object with a
  `content` array containing only a text
  [GuardrailConverseContentBlock](../APIReference/API_runtime_GuardrailConverseContentBlock.md "../APIReference/API_runtime_GuardrailConverseContentBlock.md"):

```
{
    "role": "user",
    "content": [
        {
            "text": "Tell me what stocks to buy.",
            "qualifiers": [
                "guard_content"
            ]
        }
    ]
}
```

You define the text to be evaluated and include any
qualifiers to use for [contextual grounding](guardrails-contextual-grounding-check.md "guardrails-contextual-grounding-check.md").

- **image** – The
  following shows a [Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md") object with a
  `content` array containing only an image
  [GuardrailConverseContentBlock](../APIReference/API_runtime_GuardrailConverseContentBlock.md "../APIReference/API_runtime_GuardrailConverseContentBlock.md"):

```
{
    "role": "user",
    "content": [
        {
            "format": "png",
            "source": {
                "bytes": "`image in bytes`"
            }
        }
    ]
}
```

You specify the format of the image and define the
image in bytes.

For more information about using guardrails, see [Detect and filter harmful content by using Amazon Bedrock Guardrails](guardrails.md "guardrails.md").

reasoningContent
The `reasoningContent` field maps to a
[ReasoningContentBlock](../APIReference/API_runtime_ReasoningContentBlock.md "../APIReference/API_runtime_ReasoningContentBlock.md"). This block contains content regarding
the reasoning that was carried out by the model to generate the
response in the accompanying `ContentBlock`.

The following shows a `Message` object with a
`content` array containing only a
`ReasoningContentBlock` and an accompanying text
`ContentBlock`.

```
{
    "role": "user",
    "content": [
        {
            "text": "`string`"
        },
        {
            "reasoningContent": {
                "reasoningText": {
                    "text": "`string`",
                    "signature": "`string`"
                }
                "redactedContent": "`base64-encoded binary data object`"
            }
        }
    ]
}
```

The `ReasoningContentBlock` contains the reasoning
used to generate the accompanying content in the
`reasoningText` field, in addition to any content
in the reasoning that was encrypted by the model provider for
trust and safety reasons in the `redactedContent`
field.

Within the `reasoningText` field, the
`text` fields describes the reasoning. The
`signature` field is a hash of all the messages
in the conversation and is a safeguard against tampering of the
reasoning used by the model. You must include the signature and
all previous messages in subsequent `Converse`
requests. If any of the messages are changed, the response
throws an error.

toolUse
Contains information about a tool for the model to use.
For more information, see [Use a tool to complete an Amazon Bedrock model response](tool-use.md "tool-use.md").

toolResult
Contains information about the result from the model using a
tool. For more information, see [Use a tool to complete an Amazon Bedrock model response](tool-use.md "tool-use.md").

###### Note

The following restrictions pertain to the `content` field:

- You can include up to 20 images. Each image's size, height, and width must be no more than 3.75 MB, 8,000 px, and 8,000 px, respectively.
- You can include up to five documents. Each document's size must be no more than 4.5 MB.
- You can only include images and documents if the `role` is `user`.
  In the following `messages` example, the user asks for a list
  of three pop songs, and the model generates a list of songs.

```
[
    {
        "role": "user",
        "content": [
            {
                "text": "Create a list of 3 pop songs."
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "text": "Here is a list of 3 pop songs by artists from the United Kingdom:\n\n1. \"As It Was\" by Harry Styles\n2. \"Easy On Me\" by Adele\n3. \"Unholy\" by Sam Smith and Kim Petras"
            }
        ]
    }
]
```

A system prompt is a type of prompt that provides instructions or context
to the model about the task it should perform, or the persona it should
adopt during the conversation. You can specify a list of system prompts for
the request in the `system` ([SystemContentBlock](../APIReference/API_runtime_SystemContentBlock.md "../APIReference/API_runtime_SystemContentBlock.md")) field, as shown in the following
example.

```
[
    {
        "text": "You are an app that creates play lists for a radio station that plays rock and pop music. Only return song names and the artist. "
    }
]
```

The Converse API supports a base set of inference
parameters that you set in the `inferenceConfig` field ([InferenceConfiguration](../APIReference/API_runtime_InferenceConfiguration.md "../APIReference/API_runtime_InferenceConfiguration.md")). The base set of inference parameters
are:

- **maxTokens** – The maximum
  number of tokens to allow in the generated response.
- **stopSequences** – A list of
  stop sequences. A stop sequence is a sequence of characters that
  causes the model to stop generating the response.
- **temperature** – The
  likelihood of the model selecting higher-probability options while
  generating a response.
- **topP** – The percentage of
  most-likely candidates that the model considers for the next
  token.
  For more information, see [Influence response generation with inference parameters](inference-parameters.md "inference-parameters.md").

The following example JSON sets the `temperature` inference
parameter.

```
{"temperature": 0.5}
```

If the model you are using has additional inference parameters, you can
set those parameters by specifying them as JSON in the
`additionalModelRequestFields` field. The following example
JSON shows how to set `top_k`, which is available in Anthropic
Claude models, but isn't a base inference parameter in the messages API.

```
{"top_k": 200}
```

If you specify a prompt from [Prompt management](prompt-management.md "prompt-management.md")
in the `modelId` as the resource to run inference on, use this
field to fill in the prompt variables with actual values. The
`promptVariables` field maps to a JSON object with keys that
correspond to variables defined in the prompts and values to replace the
variables with.

For example, let's say that you have a prompt that says
`Make me a `{{genre}}`playlist consisting of the following number of songs:`{{number}}`.`. The prompt's ID is
`PROMPT12345` and its version is `1`. You could
send the following `Converse` request to replace the
variables:

```
POST /model/arn:aws:bedrock:us-east-1:111122223333:prompt/PROMPT12345:1/converse HTTP/1.1
Content-type: application/json

{
   "promptVariables": {
      "genre" : "pop",
      "number": 3
   }
}
```

You can apply a guardrail that you created with [Amazon Bedrock Guardrails](guardrails.md "guardrails.md") by including this field. To apply the guardrail to a
specific message in the conversation, include the message in a [GuardrailConverseContentBlock](../APIReference/API_runtime_GuardrailConverseContentBlock.md "../APIReference/API_runtime_GuardrailConverseContentBlock.md").
If you don't include any `GuardrailConverseContentBlock`s in the
request body, the guardrail is applied to all the messages in the
`messages` field. For an example, see [Include a guardrail with the
Converse API](guardrails-use-converse-api.md "guardrails-use-converse-api.md") .

This field lets you define a tool for the model to use to help it generate
a response. For more information, see [Use a tool to complete an Amazon Bedrock model response](tool-use.md "tool-use.md").

You can specify the paths for additional model parameters in the
`additionalModelResponseFieldPaths` field, as shown in the
following example.

```
[ "/stop_sequence" ]
```

The API returns the additional fields that you request in the
`additionalModelResponseFields` field.

This field maps to a JSON object. You can specify metadata keys and values
that they map to within this object. You can use request metadata to help
you filter model invocation logs.

This field maps to a JSON object. You can specify the service tier for a particular request.

The following example shows the `serviceTier` structure:

```
"serviceTier": {
  "type": "priority" | "default" | "flex"
}
```

For detailed information about service tiers, including pricing and performance characteristics, see [Service tiers for optimizing performance and cost](service-tiers-inference.md "service-tiers-inference.md").

You can also optionally add cache checkpoints to the `system` or
`tools` fields to use prompt caching, depending on which model you're
using. For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

## Response

The response you get from the Converse API depends on which
operation you call, `Converse` or `ConverseStream`.

###### Topics

- [Converse
  response](#conversation-inference-call-response-converse "#conversation-inference-call-response-converse")
- [ConverseStream response](#conversation-inference-call-response-converse-stream "#conversation-inference-call-response-converse-stream")

### Converse

response

In the response from `Converse`, the `output` field
([ConverseOutput](../APIReference/API_runtime_ConverseOutput.md "../APIReference/API_runtime_ConverseOutput.md")) contains the message ([Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md")) that the model
generates. The message content is in the `content` ([ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md")) field and the role (`user` or
`assistant`) that the message corresponds to is in the
`role` field.

If you used [prompt caching](prompt-caching.md "prompt-caching.md"), then in the
usage field, `cacheReadInputTokensCount` and
`cacheWriteInputTokensCount` tell you how many total tokens were
read from the cache and written to the cache, respectively.

If you used [service tiers](#inference-service-tiers "#inference-service-tiers"), then in the
response field, `service tier` would tell you which service tier was used for the request.

The `metrics` field ([ConverseMetrics](../APIReference/API_runtime_ConverseMetrics.md "../APIReference/API_runtime_ConverseMetrics.md"))
includes metrics for the call. To determine why the model stopped generating
content, check the `stopReason` field. You can get information about
the tokens passed to the model in the request, and the tokens generated in the
response, by checking the `usage` field ([TokenUsage](../APIReference/API_runtime_TokenUsage.md "../APIReference/API_runtime_TokenUsage.md")). If you
specified additional response fields in the request, the API returns them as
JSON in the `additionalModelResponseFields` field.

The following example shows the response from `Converse` when you
pass the prompt discussed in [Request](#conversation-inference-call-request "#conversation-inference-call-request").

```
{
    "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "text": "Here is a list of 3 pop songs by artists from the United Kingdom:\n\n1. \"Wannabe\" by Spice Girls\n2. \"Bitter Sweet Symphony\" by The Verve \n3. \"Don't Look Back in Anger\" by Oasis"
                }
            ]
        }
    },
    "stopReason": "end_turn",
    "usage": {
        "inputTokens": 125,
        "outputTokens": 60,
        "totalTokens": 185
    },
    "metrics": {
        "latencyMs": 1175
    }
}
```

### ConverseStream response

If you call `ConverseStream` to stream the response from a model,
the stream is returned in the `stream` response field. The stream
emits the following events in the following order.

1. `messageStart` ([MessageStartEvent](../APIReference/API_runtime_MessageStartEvent.md "../APIReference/API_runtime_MessageStartEvent.md")). The start event for a message. Includes
   the role for the message.
2. `contentBlockStart` ([ContentBlockStartEvent](../APIReference/API_runtime_ContentBlockStartEvent.md "../APIReference/API_runtime_ContentBlockStartEvent.md")). A Content block start event. Tool
   use only.
3. `contentBlockDelta` ([ContentBlockDeltaEvent](../APIReference/API_runtime_ContentBlockDeltaEvent.md "../APIReference/API_runtime_ContentBlockDeltaEvent.md")). A Content block delta event.
   Includes one of the following:
   - `text` – The partial text that the model
     generates.
   - `reasoningContent` – The partial reasoning
     carried out by the model to generate the response. You must
     submit the returned `signature`, in addition to all
     previous messages in subsequent `Converse` requests.
     If any of the messages are changed, the response throws an
     error.
   - `toolUse` – The partial input JSON object for
     tool use.

4. `contentBlockStop` ([ContentBlockStopEvent](../APIReference/API_runtime_ContentBlockStopEvent.md "../APIReference/API_runtime_ContentBlockStopEvent.md")). A Content block stop event.
5. `messageStop` ([MessageStopEvent](../APIReference/API_runtime_MessageStopEvent.md "../APIReference/API_runtime_MessageStopEvent.md")). The stop event for the message. Includes
   the reason why the model stopped generating output.
6. `metadata` ([ConverseStreamMetadataEvent](../APIReference/API_runtime_ConverseStreamMetadataEvent.md "../APIReference/API_runtime_ConverseStreamMetadataEvent.md")). Metadata for the request. The
   metadata includes the token usage in `usage` ([TokenUsage](../APIReference/API_runtime_TokenUsage.md "../APIReference/API_runtime_TokenUsage.md")) and metrics for the call in
   `metrics` ([ConverseStreamMetadataEvent](../APIReference/API_runtime_ConverseStreamMetadataEvent.md "../APIReference/API_runtime_ConverseStreamMetadataEvent.md")).

ConverseStream streams a complete content block as a
`ContentBlockStartEvent` event, one or more
`ContentBlockDeltaEvent` events, and a
`ContentBlockStopEvent` event. Use the
`contentBlockIndex` field as an index to correlate the events
that make up a content block.

The following example is a partial response from `ConverseStream`.

```
{'messageStart': {'role': 'assistant'}}
{'contentBlockDelta': {'delta': {'text': ''}, 'contentBlockIndex': 0}}
{'contentBlockDelta': {'delta': {'text': ' Title'}, 'contentBlockIndex': 0}}
{'contentBlockDelta': {'delta': {'text': ':'}, 'contentBlockIndex': 0}}
.
.
.
{'contentBlockDelta': {'delta': {'text': ' The'}, 'contentBlockIndex': 0}}
{'messageStop': {'stopReason': 'max_tokens'}}
{'metadata': {'usage': {'inputTokens': 47, 'outputTokens': 20, 'totalTokens': 67}, 'metrics': {'latencyMs': 100.0}}}

```
