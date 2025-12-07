# Request and response schema

The request schema is nearly identical between the Invoke API and Converse API. The primary difference is how binary data (images, video, audio) is encoded: the Converse API uses binary arrays while the Invoke API uses Base64-encoded strings.

## Complete request structure

The following shows the complete request structure for Amazon Nova models. All fields are optional unless marked as required:

```
{
  "system": [
    {
      "text": "string"
    }
  ],
  "messages": [  // Required
    {
      "role": "user",  // Required - first turn must be user
      "content": [  // Required
        {
          "text": "string"
        },
        {
          "image": {
            "format": "jpeg" | "png" | "gif" | "webp",  // Required
            "source": {  // Required
              "bytes": image  // Binary array (Converse) or Base64 string (Invoke)
            }
          }
        },
        {
          "video": {
            "format": "mkv" | "mov" | "mp4" | "webm" | "three_gp" | "flv" | "mpeg" | "mpg" | "wmv",
            "source": {
              // Option 1: S3 location
              "s3Location": {
                "uri": "string",  // e.g., s3://my-bucket/object-key
                "bucketOwner": "string"  // Optional, e.g., "123456789012"
              },
              // Option 2: File bytes
              "bytes": video  // Binary array (Converse) or Base64 string (Invoke)
            }
          }
        },
        {
          "audio": {  // Nova 2 Omni and Sonic only
            "format": "mp3" | "opus" | "wav" | "aac" | "flac" | "mp4" | "ogg" | "mkv",
            "source": {
              // Option 1: S3 location
              "s3Location": {
                "uri": "string",
                "bucketOwner": "string"  // Optional
              },
              // Option 2: File bytes
              "bytes": audio  // Binary array (Converse) or Base64 string (Invoke)
            }
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "string"  // For prefilling assistant response
        }
      ]
    }
  ],
  "inferenceConfig": {  // All optional
    "maxTokens": int,  // 1-5000, default: dynamic
    "temperature": float,  // 0.00001-1, default: 0.7
    "topP": float,  // 0-1, default: 0.9
    "topK": int,  // 0-128, default: not used
    "stopSequences": ["string"],
    "reasoningConfig": {  // Nova 2 Lite and Sonic only
      "type": "enabled" | "disabled",  // default: "disabled"
      "maxReasoningEffort": "low" | "medium" | "high"
    }
  },
  "toolConfig": {  // Optional
    "tools": [
      {
        "toolSpec": {
          "name": "string",  // Max 64 characters
          "description": "string",
          "inputSchema": {
            "json": {
              "type": "object",
              "properties": {
                "arg1": {
                  "type": "string",
                  "description": "string"
                }
              },
              "required": ["string"]
            }
          }
        }
      }
    ],
    "toolChoice": {  // Choose one option
      "auto": {},
      "any": {},
      "tool": {
        "name": "string"
      }
    }
  }
}
```

Key request parameters:

- `system`: System prompt providing context and instructions
- `messages`: Array of conversation turns with role (user or assistant) and content
- `inferenceConfig`: Controls model output behavior (temperature, tokens, and so on.)
- `toolConfig`: Tool specifications for function calling

###### Note

When using the Converse API, the `topK` and `reasoningConfig` parameters must be placed in `additionalModelRequestFields` instead of `inferenceConfig`.

The following sections provide detailed explanations of each request parameter:

`system` – (Optional) The system prompt for the request. A system prompt provides context and instructions to Amazon Nova, such as specifying a particular goal or role.

`messages` – (Required) The input messages array containing conversation turns.

- `role` – (Required) The role of the conversation turn. Valid values are `user` and `assistant`. The first message must always use the `user` role.
- `content` – (Required) An array of content blocks. Each block specifies a content type (`text`, `image`, `video`, or `audio`):

      + `text` – Text content for the conversation turn. If combined with image or video, interpreted as accompanying text.
      + `image` – (Not supported for Nova 2 Lite) Image content with:




      	- `format` – (Required) Image format: `jpeg`, `png`, `webp`, or `gif`
      	- `source.bytes` – (Required) Image data as binary array (Converse API) or Base64 string (Invoke API)
      + `video` – (Not supported for Nova 2 Lite) Video content with:




      	- `format` – (Required) Video format: `mkv`, `mov`, `mp4`, `webm`, `three_gp`, `flv`, `mpeg`, `mpg`, or `wmv`
      	- `source` – (Required) Video source via S3 URI (`s3Location.uri` and optional `bucketOwner`) or file bytes (`bytes`)
      + `audio` – (Amazon Nova Sonic and only) Audio content with:




      	- `format` – (Required) Audio format: `mp3`, `opus`, `wav`, `aac`, `flac`, `mp4`, `ogg`, or `mkv`
      	- `source` – (Required) Audio source via S3 URI or file bytes

  `inferenceConfig` – (Optional) Configuration parameters controlling model output generation.

- `maxTokens` – (Optional) Maximum tokens to generate before stopping. Amazon Nova models may stop before reaching this limit. Maximum value is 5,000. If not specified, uses a dynamic default based on request context.
- `temperature` – (Optional) Randomness in responses. Valid range: 0.00001-1 (default: 0.7). Lower values produce more deterministic output.
- `topP` – (Optional) Nucleus sampling threshold. Amazon Nova samples from tokens whose cumulative probability reaches `topP`. Valid range: 0-1 (default: 0.9). Adjust either `temperature` or `topP`, not both.
- `topK` – (Optional) Sample from top K tokens only. Removes low-probability responses. Valid range: 0-128 (default: not used).

###### Note

For Converse API, pass `topK` in `additionalModelRequestFields`.

- `stopSequences` – (Optional) Array of strings that stop generation when encountered.
- `reasoningConfig` – (Amazon Nova Sonic and only) Reasoning configuration:
  - `type` – (Optional) `enabled` or `disabled` (default: `disabled`)
  - `maxReasoningEffort` – Computational effort: `low`, `medium`, or `high`. With `low` and `medium`, reasoning streams incrementally; `high` outputs reasoning in a final chunk.

###### Note

For Converse API, pass `reasoningConfig` in `additionalModelRequestFields`.
`toolConfig` – (Optional) Tool configuration following [ToolConfiguration schema](../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md "../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md").

- `tools` – Array of tool specifications with `name`, `description` and `inputSchema`
- `toolChoice` – (Optional) Controls tool selection:
  - `auto` – Model decides whether and which tools to use
  - `any` – Model must use at least one tool
  - `tool` – Model must use the specified tool by name

## Complete response structure

The following shows the complete response structure for Amazon Nova models:

```
{
  "ResponseMetadata": {
    "RequestId": "string",
    "HTTPStatusCode": int,
    "HTTPHeaders": {
      "date": "string",
      "content-type": "application/json",
      "content-length": "string",
      "connection": "keep-alive",
      "x-amzn-requestid": "string"
    },
    "RetryAttempts": 0
  },
  "output": {
    "message": {
      "role": "assistant",
      "content": [
        {
          "reasoningContent": {  // Optional - if reasoning enabled
            "reasoningText": {
              "text": "[REDACTED]"
            }
          }
        },
        {
          "toolUse": {  // Optional - if tool called
            "toolUseId": "string",
            "name": "string",
            "input": {}  // Tool-specific arguments
          }
        },
        {
          "text": "string"  // Optional - text response
        },
        {
          "image": {  // Optional - Nova 2 Omni only
            "format": "png",
            "source": {
              "bytes": image  // Binary array (Converse) or Base64 string (Invoke)
            }
          }
        }
      ]
    }
  },
  "stopReason": "string",  // See stop reasons below
  "usage": {
    "inputTokens": int,
    "outputTokens": int,
    "totalTokens": int
  },
  "metrics": {
    "latencyMs": int
  }
}
```

Stop reasons:

- `end_turn`: Natural end of response
- `max_tokens`: Reached maxTokens limit
- `content_filtered`: Violated content policy
- `malformed_model_output`: Invalid model output
- `malformed_tool_use`: Invalid tool use output
- `service_unavailable`: Built-in tool service unreachable
- `invalid_query`: Invalid query to built-in tool
- `max_tool_invocations`: Tool retries exhausted

The following sections provide detailed explanations of each response field:

`output` – (Required) Contains the model's response message.

- `message` – (Required) The assistant's response message with role and content array.
- `content` – (Required) Array of content blocks that can include:

      + `reasoningContent` – (Optional) Returned if reasoning was enabled. Contains reasoning text, which will always be `[REDACTED]` in the response.
      + `toolUse` – (Optional) Returned if a tool was called. Contains tool use ID, name and input arguments.
      + `text` – (Optional) Returned if the model responded with text content.
      + `image` – (Optional, only) Returned if the model generated an image. Format will always be PNG.

  `stopReason` – (Required) Indicates why the model stopped generating output:

- `end_turn` – Natural end of response reached
- `max_tokens` – Reached maxTokens limit or model's maximum output limit
- `content_filtered` – Output violated AWS Responsible AI policy
- `malformed_model_output` – Model produced invalid output
- `malformed_tool_use` – Model produced invalid tool use output
- `service_unavailable` – Built-in tool service could not be reached
- `invalid_query` – Query to built-in tool was invalid
- `max_tool_invocations` – Built-in tool did not produce valid result after retries
  `usage` – (Required) Token usage information:

- `inputTokens` – Total tokens ingested by the model
- `outputTokens` – Number of tokens generated
- `totalTokens` – Sum of input and output tokens
  `metrics` – (Required) Performance metrics:

- `latencyMs` – Total inference completion time in milliseconds
