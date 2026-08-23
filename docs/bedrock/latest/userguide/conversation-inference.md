# Inference using Converse API

The Converse API is available on the `bedrock-runtime` endpoint only.

You can use the Amazon Bedrock Converse API to create conversational applications
that send and receive messages to and from an Amazon Bedrock model. For example, you can create a
chat bot that maintains a conversation over many turns and uses a persona or tone
customization that is unique to your needs, such as a helpful technical support
assistant.

To use the Converse API, you use the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") (for streaming
responses) operations to send messages to a model. It is possible to use the existing base
inference operations ([InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")) for conversation applications. However, the
Converse API provides a consistent API that works
with all Amazon Bedrock models that support messages. This means you can write code once and use
it with different models. Should a model have unique inference parameters, the
Converse API also allows you to pass those unique parameters in a model
specific structure.

You can use the Converse API to implement [tool
use](tool-use.md "tool-use.md") and [guardrails](guardrails-use-converse-api.md "guardrails-use-converse-api.md") in your
applications.

###### Note

- With Mistral AI and Meta models, the Converse API embeds your input in
  a model-specific prompt template that enables
  conversations.
- Restrictions apply to the following operations: `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, and `ConverseStream`. See [API restrictions](inference-api-restrictions.md "inference-api-restrictions.md") for details.
  For code examples, see the following:

- Python examples for this topic – [Converse API examples](conversation-inference-examples.md "conversation-inference-examples.md")
- Various languages and models – [Code examples for Amazon Bedrock Runtime using AWS SDKs](service_code_examples_bedrock-runtime.md "service_code_examples_bedrock-runtime.md")
- Java tutorial – [A Java developer's guide to Bedrock's new Converse
  API](https://community.aws/content/2hUiEkO83hpoGF5nm3FWrdfYvPt/amazon-bedrock-converse-api-java-developer-guide "https://community.aws/content/2hUiEkO83hpoGF5nm3FWrdfYvPt/amazon-bedrock-converse-api-java-developer-guide")
- JavaScript tutorial – [A developer's guide to Bedrock's new Converse API](https://community.aws/content/2dtauBCeDa703x7fDS9Q30MJoBA/amazon-bedrock-converse-api-developer-guide "https://community.aws/content/2dtauBCeDa703x7fDS9Q30MJoBA/amazon-bedrock-converse-api-developer-guide")

## Using the Converse API

To use the Converse API, you call the `Converse` or
`ConverseStream` operations to send messages to a model. To call
`Converse`, you require permission for the
`bedrock:InvokeModel` operation. To call `ConverseStream`, you
require permission for the `bedrock:InvokeModelWithResponseStream`
operation.

### Request

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

#### messages

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
see what models support what blocks, see [models at a glance](model-cards.md "model-cards.md")):

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
`cachePoint` fields to use prompt caching.
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

#### system

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

#### inferenceConfig

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

#### additionalModelRequestFields

If the model you are using has additional inference parameters, you can
set those parameters by specifying them as JSON in the
`additionalModelRequestFields` field. The following example
JSON shows how to set `top_k`, which is available in Anthropic
Claude models, but isn't a base inference parameter in the messages API.

```
{"top_k": 200}
```

#### promptVariables

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
      "genre": {
         "text": "pop"
      },
      "number": {
         "text": "3"
      }
   }
}
```

#### guardrailConfig

You can apply a guardrail that you created with [Amazon Bedrock Guardrails](guardrails.md "guardrails.md") by including this field. To apply the guardrail to a
specific message in the conversation, include the message in a [GuardrailConverseContentBlock](../APIReference/API_runtime_GuardrailConverseContentBlock.md "../APIReference/API_runtime_GuardrailConverseContentBlock.md").
If you don't include any `GuardrailConverseContentBlock`s in the
request body, the guardrail is applied to all the messages in the
`messages` field. For an example, see [Include a guardrail with the Converse API](guardrails-use-converse-api.md "guardrails-use-converse-api.md").

#### toolConfig

This field lets you define a tool for the model to use to help it generate
a response. For more information, see [Use a tool to complete an Amazon Bedrock model response](tool-use.md "tool-use.md").

#### additionalModelResponseFieldPaths

Each model that Amazon Bedrock supports has its own native response shape with
provider-specific fields (for example, Anthropic Claude returns a
`stop_sequence` field; Cohere returns `is_finished`;
and so on). To give you a uniform response across models, [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") and
[ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") drop most model-native fields by default and return a
normalized envelope with `output`, `stopReason`,
`usage`, and `metrics`.

If your application needs one or more of those model-native fields, list
their JSON Pointer paths in `additionalModelResponseFieldPaths`.
[Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") and [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") then include those fields in the
`additionalModelResponseFields` field of the response.

The following example asks [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") to also return Anthropic
Claude's `stop_sequence` field, which contains the value of
the stop sequence that ended generation:

```
[ "/stop_sequence" ]
```

Each path is a JSON Pointer ([RFC 6901](https://datatracker.ietf.org/doc/html/rfc6901 "https://datatracker.ietf.org/doc/html/rfc6901"))
into the model's native response. Empty pointers and malformed pointers
return a `400` error. If a pointer is valid but the requested
path doesn't exist in the model's response, it is silently ignored.

###### Note

This field controls which model-native _response
fields_ are surfaced through [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"). It does not control
text-output formatting. Some models — particularly reasoning
models such as DeepSeek-R1, Claude 3.7 Sonnet with extended thinking,
and Amazon Nova reasoning models — can include reasoning content or
model-specific tokens in their text output. For how to work with
reasoning content, see [Enhance model responses with model reasoning](inference-reasoning.md "inference-reasoning.md").

#### requestMetadata

The `requestMetadata` field maps to a JSON object of key-value
tags that are recorded with the request in your model invocation logs. You
can use request metadata to filter and aggregate logs by team, application,
environment, or any other dimension that varies per call.

The same capability is available on [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")
through the `X-Amzn-Bedrock-Request-Metadata` HTTP header. For
details on supported APIs, limits, and how request metadata appears in
invocation logs, see [Per-request metadata tagging](cost-mgmt-request-metadata.md "cost-mgmt-request-metadata.md").

#### serviceTier

This field maps to a JSON object. You can specify the service tier for a particular request.

The following example shows the `serviceTier` structure:

```
"serviceTier": {
  "type": "reserved" | "priority" | "default" | "flex"
}
```

For detailed information about service tiers, including pricing and performance characteristics, see [Service tiers for optimizing performance and cost](service-tiers-inference.md "service-tiers-inference.md").

You can also optionally add cache checkpoints to the `system` or
`tools` fields to use prompt caching, depending on which model you're
using. For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").

### Response

The response you get from the Converse API depends on which
operation you call, `Converse` or `ConverseStream`.

#### Converse response

In the response from `Converse`, the `output` field
([ConverseOutput](../APIReference/API_runtime_ConverseOutput.md "../APIReference/API_runtime_ConverseOutput.md")) contains the message ([Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md")) that the model
generates. The message content is in the `content` ([ContentBlock](../APIReference/API_runtime_ContentBlock.md "../APIReference/API_runtime_ContentBlock.md")) field and the role (`user` or
`assistant`) that the message corresponds to is in the
`role` field.

If you used [prompt caching](prompt-caching.md "prompt-caching.md"), then in the
usage field, `cacheReadInputTokens` and
`cacheWriteInputTokens` tell you how many total tokens were
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

#### ConverseStream response

If you call `ConverseStream` to stream the response from a model,
the stream is returned in the `stream` response field. The stream
emits the following events. The diagram below shows the order in which the
events are received; the content block events repeat once per content block,
grouped by `contentBlockIndex`.

```
messageStart                          (once per response)
    |
    v
+-- for each content block (indexed by contentBlockIndex) --+
|                                                           |
|   contentBlockStart    (tool use only)                    |
|   contentBlockDelta    (one or more; text / reasoning /   |
|                         tool use partial JSON)            |
|   contentBlockStop                                        |
|                                                           |
+-----------------------------------------------------------+
    |
    v
messageStop                           (once per response;
    |                                  carries stopReason)
    v
metadata                              (once per response;
                                       usage + metrics)
```

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

## Converse API examples

The following examples show you how to use the `Converse` and
`ConverseStream` operations.

Text
This example shows how to call the `Converse` operation with
the _Anthropic Claude 3 Sonnet_ model. The example
shows how to send the input text, inference parameters, and additional
parameters that are unique to the model. The code starts a conversation by
asking the model to create a list of songs. It then continues the
conversation by asking that the songs are by artists from the United
Kingdom.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to use the <noloc>Converse</noloc> API with Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3

from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_conversation(bedrock_client,
                          model_id,
                          system_prompts,
                          messages):
    """
    Sends messages to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        system_prompts (JSON) : The system prompts for the model to use.
        messages (JSON) : The messages to send to the model.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Inference parameters to use.
    temperature = 0.5
    top_k = 200

    # Base inference parameters to use.
    inference_config = {"temperature": temperature}
    # Additional inference parameters to use.
    additional_model_fields = {"top_k": top_k}

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    # Log token usage.
    token_usage = response['usage']
    logger.info("Input tokens: %s", token_usage['inputTokens'])
    logger.info("Output tokens: %s", token_usage['outputTokens'])
    logger.info("Total tokens: %s", token_usage['totalTokens'])
    logger.info("Stop reason: %s", response['stopReason'])

    return response

def main():
    """
    Entrypoint for Anthropic Claude 3 Sonnet example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Setup the system prompts and messages to send to the model.
    system_prompts = [{"text": "You are an app that creates playlists for a radio station that plays rock and pop music. Only return song names and the artist."}]
    message_1 = {
        "role": "user",
        "content": [{"text": "Create a list of 3 pop songs."}]
    }
    message_2 = {
        "role": "user",
        "content": [{"text": "Make sure the songs are by artists from the United Kingdom."}]
    }
    messages = []

    try:

        bedrock_client = boto3.client(service_name='bedrock-runtime')

        # Start the conversation with the 1st message.
        messages.append(message_1)
        response = generate_conversation(
            bedrock_client, model_id, system_prompts, messages)

        # Add the response message to the conversation.
        output_message = response['output']['message']
        messages.append(output_message)

        # Continue the conversation with the 2nd message.
        messages.append(message_2)
        response = generate_conversation(
            bedrock_client, model_id, system_prompts, messages)

        output_message = response['output']['message']
        messages.append(output_message)

        # Show the complete conversation.
        for message in messages:
            print(f"Role: {message['role']}")
            for content in message['content']:
                print(f"Text: {content['text']}")
            print()

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print(f"A client error occured: {message}")

    else:
        print(
            f"Finished generating text with model {model_id}.")


if __name__ == "__main__":
    main()

```

Image
This example shows how to send an image as part of a message and requests
that the model describe the image. The example uses `Converse`
operation and the _Anthropic Claude 3 Sonnet_ model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to send an image with the <noloc>Converse</noloc> API with an accompanying text prompt to Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_conversation(bedrock_client,
                          model_id,
                          input_text,
                          input_image):
    """
    Sends a message to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input text : The text prompt accompanying the image.
        input_image : The path to the input image.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Get image extension and read in image as bytes
    image_ext = input_image.split(".")[-1]
    with open(input_image, "rb") as f:
        image = f.read()

    message = {
        "role": "user",
        "content": [
            {
                "text": input_text
            },
            {
                "image": {
                    "format": image_ext,
                    "source": {
                        "bytes": image
                    }
                }
            }
        ]
    }

    messages = [message]

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages
    )

    return response


def main():
    """
    Entrypoint for Anthropic Claude 3 Sonnet example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    input_text = "What's in this image?"
    input_image = "path/to/image"

    try:

        bedrock_client = boto3.client(service_name="bedrock-runtime")

        response = generate_conversation(
            bedrock_client, model_id, input_text, input_image)

        output_message = response['output']['message']

        print(f"Role: {output_message['role']}")

        for content in output_message['content']:
            print(f"Text: {content['text']}")

        token_usage = response['usage']
        print(f"Input tokens:  {token_usage['inputTokens']}")
        print(f"Output tokens:  {token_usage['outputTokens']}")
        print(f"Total tokens:  {token_usage['totalTokens']}")
        print(f"Stop reason: {response['stopReason']}")

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print(f"A client error occured: {message}")

    else:
        print(
            f"Finished generating text with model {model_id}.")


if __name__ == "__main__":
    main()

```

Document
This example shows how to send a document as part of a message and
requests that the model describe the contents of the document. The example
uses `Converse` operation and the _Anthropic
Claude 3 Sonnet_ model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to send an document as part of a message to Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_message(bedrock_client,
                     model_id,
                     input_text,
                     input_document_path):
    """
    Sends a message to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input text : The input message.
        input_document_path : The path to the input document.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Get format from path and read the path
    input_document_format = input_document_path.split(".")[-1]
    with open(input_document_path, 'rb') as input_document_file:
        input_document = input_document_file.read()

    # Message to send.
    message = {
        "role": "user",
        "content": [
            {
                "text": input_text
            },
            {
                "document": {
                    "name": "MyDocument",
                    "format": input_document_format,
                    "source": {
                        "bytes": input_document
                    }
                }
            }
        ]
    }

    messages = [message]

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages
    )

    return response


def main():
    """
    Entrypoint for Anthropic Claude 3 Sonnet example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    input_text = "What's in this document?"
    input_document_path = "path/to/document"

    try:

        bedrock_client = boto3.client(service_name="bedrock-runtime")


        response = generate_message(
            bedrock_client, model_id, input_text, input_document_path)

        output_message = response['output']['message']

        print(f"Role: {output_message['role']}")

        for content in output_message['content']:
            print(f"Text: {content['text']}")

        token_usage = response['usage']
        print(f"Input tokens:  {token_usage['inputTokens']}")
        print(f"Output tokens:  {token_usage['outputTokens']}")
        print(f"Total tokens:  {token_usage['totalTokens']}")
        print(f"Stop reason: {response['stopReason']}")

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print(f"A client error occured: {message}")

    else:
        print(
            f"Finished generating text with model {model_id}.")


if __name__ == "__main__":
    main()
```

Streaming
This example shows how to call the `ConverseStream` operation
with the _Anthropic Claude 3 Sonnet_ model. The example
shows how to send the input text, inference parameters, and additional
parameters that are unique to the model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to use the <noloc>Converse</noloc> API to stream a response from Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def stream_conversation(bedrock_client,
                    model_id,
                    messages,
                    system_prompts,
                    inference_config,
                    additional_model_fields):
    """
    Sends messages to a model and streams the response.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        messages (JSON) : The messages to send.
        system_prompts (JSON) : The system prompts to send.
        inference_config (JSON) : The inference configuration to use.
        additional_model_fields (JSON) : Additional model fields to use.

    Returns:
        Nothing.

    """

    logger.info("Streaming messages with model %s", model_id)

    response = bedrock_client.converse_stream(
        modelId=model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    stream = response.get('stream')
    if stream:
        for event in stream:

            if 'messageStart' in event:
                print(f"\nRole: {event['messageStart']['role']}")

            if 'contentBlockDelta' in event:
                print(event['contentBlockDelta']['delta']['text'], end="")

            if 'messageStop' in event:
                print(f"\nStop reason: {event['messageStop']['stopReason']}")

            if 'metadata' in event:
                metadata = event['metadata']
                if 'usage' in metadata:
                    print("\nToken usage")
                    print(f"Input tokens: {metadata['usage']['inputTokens']}")
                    print(
                        f":Output tokens: {metadata['usage']['outputTokens']}")
                    print(f":Total tokens: {metadata['usage']['totalTokens']}")
                if 'metrics' in event['metadata']:
                    print(
                        f"Latency: {metadata['metrics']['latencyMs']} milliseconds")


def main():
    """
    Entrypoint for streaming message API response example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    system_prompt = """You are an app that creates playlists for a radio station
      that plays rock and pop music. Only return song names and the artist."""

    # Message to send to the model.
    input_text = "Create a list of 3 pop songs."

    message = {
        "role": "user",
        "content": [{"text": input_text}]
    }
    messages = [message]

    # System prompts.
    system_prompts = [{"text" : system_prompt}]

    # inference parameters to use.
    temperature = 0.5
    top_k = 200
    # Base inference parameters.
    inference_config = {
        "temperature": temperature
    }
    # Additional model inference parameters.
    additional_model_fields = {"top_k": top_k}

    try:
        bedrock_client = boto3.client(service_name='bedrock-runtime')

        stream_conversation(bedrock_client, model_id, messages,
                        system_prompts, inference_config, additional_model_fields)

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print("A client error occured: " +
              format(message))

    else:
        print(
            f"Finished streaming messages with model {model_id}.")


if __name__ == "__main__":
    main()

```

Video
This example shows how to send a video as part of a message and requests
that the model describes the video. The example uses `Converse`
operation and the Amazon Nova Pro model.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to send a video with the <noloc>Converse</noloc> API to Amazon Nova Pro (on demand).
"""

import logging
import boto3


from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_conversation(bedrock_client,
                          model_id,
                          input_text,
                          input_video):
    """
    Sends a message to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input text : The input message.
        input_video : The input video.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Message to send.

    with open(input_video, "rb") as f:
        video = f.read()

    message = {
        "role": "user",
        "content": [
            {
                "text": input_text
            },
            {
                    "video": {
                        "format": 'mp4',
                        "source": {
                            "bytes": video
                        }
                    }
            }
        ]
    }

    messages = [message]

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages
    )

    return response


def main():
    """
    Entrypoint for Amazon Nova Pro example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "amazon.nova-pro-v1:0"
    input_text = "What's in this video?"
    input_video = "path/to/video"

    try:

        bedrock_client = boto3.client(service_name="bedrock-runtime")

        response = generate_conversation(
            bedrock_client, model_id, input_text, input_video)

        output_message = response['output']['message']

        print(f"Role: {output_message['role']}")

        for content in output_message['content']:
            print(f"Text: {content['text']}")

        token_usage = response['usage']
        print(f"Input tokens:  {token_usage['inputTokens']}")
        print(f"Output tokens:  {token_usage['outputTokens']}")
        print(f"Total tokens:  {token_usage['totalTokens']}")
        print(f"Stop reason: {response['stopReason']}")

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print(f"A client error occured: {message}")

    else:
        print(
            f"Finished generating text with model {model_id}.")


if __name__ == "__main__":
    main()
```
