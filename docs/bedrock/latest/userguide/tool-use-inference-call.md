# Call a tool with the Converse API

To let a model use a tool to complete a response for a message, you send the message
and the definitions for one or more tools to the model. If the model determines that one
of the tools can help generate a response, it returns a request for you to use the tool
and send the tool results back to the model. The model then uses the results to generate
a response to the original message.

The following steps show how to use a tool with the Converse API. For example code, see
[Converse API tool use examples](tool-use-examples.md "tool-use-examples.md").

###### Topics

- [Step 1: Send the message and tool definition](#tool-use-send-tool-info "#tool-use-send-tool-info")
- [Step 2: Get the tool request from the model](#tool-calllng-get-tool-request "#tool-calllng-get-tool-request")
- [Step 3: Make the tool request for
  the model](#tool-calllng-make-tool-request "#tool-calllng-make-tool-request")
- [Step 4: Get the model response](#tool-callling-get-model-response "#tool-callling-get-model-response")

## Step 1: Send the message and tool definition

To send the message and tool definition, you use the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") (for streaming responses) operations.

###### Note

Meta has specific recommendations for creating prompts that use tools with
Llama 3.1 (or later) models. For more information, see
[JSON based tool calling](https://llama.meta.com/docs/model-cards-and-prompt-formats/llama3_1/#json-based-tool-calling "https://llama.meta.com/docs/model-cards-and-prompt-formats/llama3_1/#json-based-tool-calling") in the Meta documentation.

The definition of the tool is a JSON schema that you pass in the `toolConfig`
([ToolConfiguration](../APIReference/API_runtime_ToolConfiguration.md "../APIReference/API_runtime_ToolConfiguration.md")) request parameter to the `Converse` operation. For
information about the schema, see [JSON schema](https://json-schema.org/ "https://json-schema.org/"). The following is an example
schema for a tool that gets the most popular song played on a radio station.

```
{
    "tools": [
        {
            "toolSpec": {
                "name": "top_song",
                "description": "Get the most popular song played on a radio station.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "sign": {
                                "type": "string",
                                "description": "The call sign for the radio station for which you want the most popular song. Example calls signs are WZPZ and WKRP."
                            }
                        },
                        "required": [
                            "sign"
                        ]
                    }
                }
            }
        }
    ]
}
```

In the same request, you also pass a user message in the `messages` ([Message](../APIReference/API_runtime_Message.md "../APIReference/API_runtime_Message.md")) request parameter.

```
[
    {
        "role": "user",
        "content": [
            {
                "text": "What is the most popular song on WZPZ?"
            }
        ]
    }
]
```

If you are using an Anthropic Claude 3 model, you can force the use of a tool
by specifying the `toolChoice` ([ToolChoice](../APIReference/API_runtime_ToolChoice.md "../APIReference/API_runtime_ToolChoice.md")) field in the `toolConfig` request parameter. Forcing
the use of a tool is useful for testing your tool during development. The following
example shows how to force the use of a tool called
_top_song_.

```
{"tool" : {"name" : "top_song"}}
```

For information about other parameters that
you can pass, see [Carry out a conversation with the
Converse API operations](conversation-inference.md "conversation-inference.md").

## Step 2: Get the tool request from the model

When you invoke the `Converse` operation with the message and tool definition, the model uses
the tool definition to determine if the tool is needed to answer the
message. For example, if your chat app user sends
the message _What's the most popular song on WZPZ?_, the model matches the message with
the schema in the top_song tool definition and determines that the
tool can help generate a response.

When the model decides that it needs a tool to generate a response, the model sets the `stopReason`
response field to `tool_use`. The response also identifies the tool (top_song) that the model
wants you to run and the radio station (WZPZ) that it wants you to query with the tool.
Information about the requested tool is in the message that the model returns in
the `output` ([ConverseOutput](../APIReference/API_runtime_ConverseOutput.md "../APIReference/API_runtime_ConverseOutput.md")) field. Specifically, the
`toolUse` ([ToolUseBlock](../APIReference/API_runtime_ToolUseBlock.md "../APIReference/API_runtime_ToolUseBlock.md")) field. You use the
`toolUseId` field to identify the tool request in later calls.

The following example shows the response from `Converse`
when you pass the message discussed in [Step 1: Send the message and tool definition](#tool-use-send-tool-info "#tool-use-send-tool-info").

```
{
    "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "toolUse": {
                        "toolUseId": "tooluse_kZJMlvQmRJ6eAyJE5GIl7Q",
                        "name": "top_song",
                        "input": {
                            "sign": "WZPZ"
                        }
                    }
                }
            ]
        }
    },
    "stopReason": "tool_use"
}

```

## Step 3: Make the tool request for

the model

From the `toolUse` field in the model response, use the
`name` field to identify the name of the tool. Then call your
implementation of the tool and pass the input parameters from the `input`
field.

Next, construct a user message that includes a `toolResult` ([ToolResultBlock](../APIReference/API_runtime_ToolResultBlock.md "../APIReference/API_runtime_ToolResultBlock.md")) content block. In the content block, include the
response from the tool and the ID for the tool request that you got in the previous
step.

```
{
    "role": "user",
    "content": [
        {
            "toolResult": {
                "toolUseId": "tooluse_kZJMlvQmRJ6eAyJE5GIl7Q",
                "content": [
                    {
                        "json": {
                            "song": "Elemental Hotel",
                            "artist": "8 Storey Hike"
                        }
                    }
                ]
            }
        }
    ]
}

```

Should an error occur in the tool, such as a request for a nonexistent radio
station, you can send error information to the model in the `toolResult`
field. To indicate an error, specify `error` in the `status`
field. The following example error is for when the tool can't find the radio
station.

```
{
    "role": "user",
    "content": [
        {
            "toolResult": {
                "toolUseId": "tooluse_kZJMlvQmRJ6eAyJE5GIl7Q",
                "content": [
                    {
                        "text": "Station WZPA not found."
                    }
                ],
                "status": "error"
            }
        }
    ]
}
```

## Step 4: Get the model response

Continue the conversation with the model by including the user message that you
created in the previous step in a call to `Converse`.
The model then generates a response that answers the original message (
_What's the most popular song on WZPZ?_) with the information that you
provided in the `toolResult` field of the message.

```
{
     "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "text": "The most popular song on WZPZ is Elemental Hotel by 8 Storey Hike."
                }
            ]
        }
    },
    "stopReason": "end_turn"

```
