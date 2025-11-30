# Request and

Response

The request body is passed in the `body` field of a request to [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or
[InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md"). The maximum size of the payload you can send
in a request is 20MB.

For more information, see [https://docs.anthropic.com/claude/reference/messages_post](https://docs.anthropic.com/claude/reference/messages_post "https://docs.anthropic.com/claude/reference/messages_post").

###### Warning

Claude Sonnet 4.5 and Claude Haiku 4.5 only support specification of one of `temperature` or `top_p` parameters, but cannot handle both. This does not apply to any older models.

Request
Anthropic Claude has the following inference parameters for a messages
inference call.

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "anthropic_beta": ["computer-use-2024-10-22"]
    "max_tokens": int,
    "system": string,
    "messages": [
        {
            "role": string,
            "content": [
                { "type": "image", "source": { "type": "base64", "media_type": "image/jpeg", "data": "`content image bytes`" } },
                { "type": "text", "text": "`content text`" }
      ]
        }
    ],
    "temperature": float,
    "top_p": float,
    "top_k": int,
    "tools": [
        {
                "type": "custom",
                "name": string,
                "description": string,
                "input_schema": json

        },
        {
            "type": "computer_20241022",
            "name": "computer",
            "display_height_px": int,
            "display_width_px": int,
            "display_number": 0 int
        },
        {
            "type": "bash_20241022",
            "name": "bash"
        },
        {
            "type": "text_editor_20241022",
            "name": "str_replace_editor"
        }

    ],
    "tool_choice": {
        "type" :  string,
        "name" : string,
    },



    "stop_sequences": [string]
}

```

The following are required parameters.

- **anthropic_version** –
  (Required) The anthropic version. The value must be
  `bedrock-2023-05-31`.
- **max_tokens** – (Required) The
  maximum number of tokens to generate before stopping.

Note that Anthropic Claude models might stop generating tokens
before reaching the value of `max_tokens`. Different
Anthropic Claude models have different maximum values for this
parameter. For more information, see [Model comparison](https://docs.anthropic.com/claude/docs/models-overview#model-comparison "https://docs.anthropic.com/claude/docs/models-overview#model-comparison").

- **messages** – (Required) The
  input messages.
  - **role** – The role of
    the conversation turn. Valid values are `user`
    and `assistant`.

  | Minimum | Maximum |
  | ------- | ------- |
  | 0       | 2000    |
  - **content** –
    (required) The content of the conversation turn, as an array
    of objects. Each object contains a **type** field, in which you can specify one of
    the following values:
    - `text` – If you specify this
      type, you must include a **text** field and specify the text prompt
      as its value. If another object in the array is an
      image, this text prompt applies to the
      images.
    - `image` – If you specify this
      type, you must include a **source** field that maps to an object
      with the following fields:
      - **type**
        – (required) The encoding type for the
        image. You can specify `base64`.
      - **media_type**
        – (required) The type of the image. You can
        specify the following image formats.
        - `image/jpeg`
        - `image/png`
        - `image/webp`
        - `image/gif`

      - **data**
        – (required) The base64 encoded image bytes
        for the image. The maximum image size is 3.75MB.
        The maximum height and width of an image is 8000
        pixels.

The following are optional parameters.

- **system** – (Optional) The
  system prompt for the request.

A system prompt is a way of providing context and instructions to
Anthropic Claude, such as specifying a particular goal or role.
For more information, see [System
prompts](https://docs.anthropic.com/en/docs/system-prompts "https://docs.anthropic.com/en/docs/system-prompts") in the Anthropic documentation.

###### Note

You can use system prompts with Anthropic Claude version
2.1 or higher.

- **anthropic_beta** – (Optional) The anthropic beta parameter is a list of strings of beta headers used to indicate opt-in to a particular set of beta features.

###### Note

The 1 million token context length variant of Claude Sonnet 4 is available to you in select AWS Regions as a "Beta Service" as defined in the AWS Service Terms. It is subject to your Agreement with AWS and the AWS Service Terms, and the applicable model EULA. Please see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page for more information about the pricing for longer context requests. Separate service quotas apply (for more information, see **Service Quotas** in the AWS Management Console).

Available beta headers include the following:

| Beta feature                                        | Beta header                        | Notes                                                                                 |
| --------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------- |
| Computer use                                        | `computer-use-2025-01-24`          | Compatible with Claude 3.7 Sonnet.                                                    |
| Tool use                                            | `token-efficient-tools-2025-02-19` | Compatible with Claude 3.7 Sonnet and Claude 4+.                                      |
| Interleaved thinking                                | `Interleaved-thinking-2025-05-14`  | Compatible with Claude 4+ models.                                                     |
| Enables output tokens up to 128K                    | `output-128k-2025-02-19`           | Compatible with Claude 3.7 Sonnet.                                                    |
| Developer mode for raw thinking on Claude 4+ models | `dev-full-thinking-2025-05-14`     | Compatible with Claude 4+ models only. Contact your account team to access this beta. |
| 1 million tokens                                    | `context-1m-2025-08-07`            | Compatible with Claude Sonnet 4                                                       |
| Context management                                  | `context-management-2025-06-27`    | Compatible with Claude Sonnet 4.5 and Claude Haiku 4.5                                |
| Effort                                              | `effort-2025-11-24`                | Compatible with Claude Opus 4.5                                                       |
| Tool search tool                                    | `tool-search-tool-2025-10-19`      | Compatible with Claude Opus 4.5                                                       |
| Tool use examples                                   | `tool-examples-2025-10-29`         | Compatible with Claude Opus 4.5                                                       |

- **stop_sequences** – (Optional)
  Custom text sequences that cause the model to stop generating.
  Anthropic Claude models normally stop when they have naturally
  completed their turn, in this case the value of the
  `stop_reason` response field is
  `end_turn`. If you want the model to stop generating when
  it encounters custom strings of text, you can use the
  `stop_sequences` parameter. If the model encounters
  one of the custom text strings, the value of the
  `stop_reason` response field is
  `stop_sequence` and the value of
  `stop_sequence` contains the matched stop
  sequence.

The maximum number of entries is 8191.

- **temperature** – (Optional) The
  amount of randomness injected into the response.

| Default | Minimum | Maximum |
| ------- | ------- | ------- |
| 1       | 0       | 1       |

- **top_p** – (Optional) Use
  nucleus sampling.

In nucleus sampling, Anthropic Claude computes the cumulative
distribution over all the options for each subsequent token in
decreasing probability order and cuts it off once it reaches a
particular probability specified by `top_p`. When
adjusting sampling parameters, modify either
`temperature` or `top_p`. Do not modify
both at the same time.

| Default | Minimum | Maximum |
| ------- | ------- | ------- |
| 0.999   | 0       | 1       |

- **top_k** – (Optional) Only
  sample from the top K options for each subsequent token.

Use `top_k` to remove long tail low probability
responses.

| Default             | Minimum | Maximum |
| ------------------- | ------- | ------- |
| Disabled by default | 0       | 500     |

- **tools** – (Optional)
  Definitions of tools that the model may use.

###### Note

Requires an Anthropic Claude 3 model.

If you include `tools` in your request, the model may
return `tool_use` content blocks that represent the
model's use of those tools. You can then run those tools using the
tool input generated by the model and then optionally return results
back to the model using `tool_result` content
blocks.

You can pass the following tool types:

###### Custom

Definition for a custom tool.

    + (optional) **type** –
     The type of the tool. If defined, use the value
     `custom`.
    + **name** – The name of
     the tool.
    + **description** –
     (optional, but strongly recommended) The description of the
     tool.
    + **input\_schema** – The
     JSON schema for the tool.

###### Computer

Definition for the computer tool that you use with the
computer use API.

    + **type** – The value must
     be `computer_20241022`.
    + **name** – The value
     must be `computer`.
    + (Required) **display\_height\_px** – The height of the
     display being controlled by the model, in pixels..




    | Default | Minimum | Maximum |
    | --- | --- | --- |
    | None | 1 | No maximum |
    + (Required) **display\_width\_px** – The width of the
     display being controlled by the model, in pixels.




    | Default | Minimum | Maximum |
    | --- | --- | --- |
    | None | 1 | No maximum |
    + (Optional) **display\_number**
     – The display number to control (only relevant for X11
     environments). If specified, the tool will be provided a
     display number in the tool definition.




    | Default | Minimum | Maximum |
    | --- | --- | --- |
    | None | 0 | N |

###### bash

Definition for the bash tool that you use with the computer
use API.

    + (optional) **type** –
     The value must be `bash_20241022`.
    + **name** – The value
     must be `bash`. the tool.

###### text editor

Definition for the text editor tool that you use with the
computer use API.

    + (optional) **type** –
     The value must be `text_editor_20241022`.
    + **name** – The value
     must be `str_replace_editor`. the tool.

- **tool_choice** – (Optional)
  Specifices how the model should use the provided tools. The model
  can use a specific tool, any available tool, or decide by
  itself.

###### Note

Requires an Anthropic Claude 3 model.

    + **type** – The type of
     tool choice. Possible values are `any` (use any
     available tool), `auto` (the model decides), and
     `tool` (use the specified tool).


    + **name** – (Optional)
     The name of the tool to use. Required if you specify
     `tool` in the `type` field.

Response
The Anthropic Claude model returns the following fields for a messages
inference call.

```
{
    "id": string,
    "model": string,
    "type" : "message",
    "role" : "assistant",
    "content": [
        {
            "type": string,
            "text": string,
            "image" :json,
            "id": string,
            "name":string,
            "input": json
        }
    ],
    "stop_reason": string,
    "stop_sequence": string,
    "usage": {
        "input_tokens": integer,
        "output_tokens": integer
    }

}
```

Example responses with new stop_reason values:

```
// Example with refusal
{
    "stop_reason": "refusal",
    "content": [
        {
            "type": "text",
            "text": "I can't help with that request."
        }
    ]
}

// Example with tool_use
{
    "stop_reason": "tool_use",
    "content": [
        {
            "type": "tool_use",
            "id": "toolu_123",
            "name": "calculator",
            "input": {"expression": "2+2"}
        }
    ]
}

// Example with model_context_window_exceeded (Claude Sonnet 4.5)
{
    "stop_reason": "model_context_window_exceeded",
    "content": [
        {
            "type": "text",
            "text": "The response was truncated due to context window limits..."
        }
    ]
}
```

- **id** – The unique identifier
  for the response. The format and length of the ID might change over
  time.
- **model** – The ID for the
  Anthropic Claude model that made the request.
- **stop_reason** – The reason
  why Anthropic Claude stopped generating the response.
  - **end_turn** – The
    model reached a natural stopping point
  - **max_tokens** – The
    generated text exceeded the value of the
    `max_tokens` input field or exceeded the
    maximum number of tokens that the model supports.' .
  - **stop_sequence** – The
    model generated one of the stop sequences that you specified
    in the `stop_sequences` input field.
  - **refusal** – Claude refuses to generate a response due to safety concerns
  - **tool_use** – Claude is calling a tool and expects you to execute it
  - **model_context_window_exceeded** – the model stopped generation due to hitting the context window limit.
    - New with Claude Sonnet 4.5

- **stop_sequence** – The stop
  sequence that ended the generation.
- **type** – The type of
  response. The value is always `message`.
- **role** – The conversational
  role of the generated message. The value is always
  `assistant`.
- **content** – The content
  generated by the model. Returned as an array. There are three types
  of content, _text_, _tool_use_
  and _image_.
  - _text_ – A text
    response.
    - **type** – The
      type of the content. This value is
      `text`.
    - **text** – If
      the value of `type` is text, contains the
      text of the content.

  - _tool use_ – A
    request from the model to use a tool.
    - **type** – The
      type of the content. This value is
      `tool_use`.
    - **id** – The ID
      for the tool that the model is requesting use
      of.
    - **name** –
      Contains the name of the requested tool.
    - **input** – The
      input parameters to pass to the tool.

  - _Image_ – A
    request from the model to use a tool.
    - **type** – The
      type of the content. This value is
      `image`.
    - **source** –
      Contains the image. For more information, see [Multimodal prompts](model-parameters-anthropic-claude-messages.md#model-parameters-anthropic-claude-messages-multimodal-prompts "model-parameters-anthropic-claude-messages.md#model-parameters-anthropic-claude-messages-multimodal-prompts").

- **usage** – Container for the
  number of tokens that you supplied in the request and the number
  tokens of that the model generated in the response.
  - **input_tokens** – The
    number of input tokens in the request.
  - **output_tokens** – The
    number tokens of that the model generated in the
    response.
  - **stop_sequence** – The
    model generated one of the stop sequences that you specified
    in the `stop_sequences` input field.

## Effort parameter

(beta)

The `effort` parameter is an alternative to thinking token budgets for Claude Opus 4.5. This parameter tells Claude how liberally it should spend tokens to produce the best result, adjusting token usage across thinking, tool calls, and user communication. It can be used with or without extended thinking mode.

The effort parameter can be set to:

- `high` (default) – Claude spends as many tokens as needed for the best result
- `medium` – Balanced token usage
- `low` – Conservative token usage

To use this feature you must pass the beta header `effort-2025-11-24`.

Request example:

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "anthropic_beta": [
        "effort-2025-11-24"
    ],
    "max_tokens": 4096,
    "output_config": {
        "effort": "medium"
    },
    "messages": [{
        "role": "user",
        "content": "Analyze this complex dataset and provide insights"
    }]
}
```
