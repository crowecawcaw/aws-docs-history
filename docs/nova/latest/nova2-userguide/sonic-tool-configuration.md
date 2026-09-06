

# Tool configuration
<a name="sonic-tool-configuration"></a>

Amazon Nova 2 Sonic supports tool use (also known as function calling), allowing the model to request external information or actions during conversations, such as API calls, database queries, or custom code functions. This allows your voice assistant to take actions, retrieve information, and integrate with external services based on user requests.

 Nova 2 Sonic features asynchronous tool calling, enabling the AI to continue conversing naturally while tools run in ther background - creating a more fluid and responsive user experience.

The following are simplified steps on how to use tools:

1. Define tools: specify available tools with their parameters in the promptStart event

1. User speaks: user makes a request that requires a tool (such as, "What's the weather in Seattle?")

1. Tool invocation: Nova 2 Sonic recognizes the need and sends a toolUse event

1. Execute rool: Your application executes the tool and returns results

1. Response Generation: Nova 2 Sonic incorporates the results into its spoken response

The following diagram illustrates how tool use works:

![Conversation flow showing client setup, tool use event handling with Amazon Bedrock Agents and Nova S2S, and transcript generation stages.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/How-tool-use-works_5.png)


## Defining tools
<a name="sonic-tool-defining"></a>

Tools are defined using a JSON schema that describes their purpose, parameters, and expected inputs.

The following are tool definition components and explanations:
+ Name: Unique identifier for the tool (use snake\_case)
+ Description: Clear explanation of what the tool does; helps the AI decide when to use it
+ InputSchema: JSON schema defining the parameters the tool accepts
+ Properties: Individual parameters with types and descriptions
+ Required: Array of parameter names that must be provided

### Example of tool definition
<a name="w2aac25c13c23c15b9b1"></a>

Here's a simple weather tool definition

```
{
  "toolSpec": {
    "name": "get_weather",
    "description": "Get current weather information for a specific location",
    "inputSchema": {
      "json": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "City name or zip code"
          },
          "units": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"],
            "description": "Temperature units"
          }
        },
        "required": ["location"]
      }
    }
  }
}
```

### Configuring Tools in PromptStart
<a name="w2aac25c13c23c15b9b3"></a>

Tool configuration is passed to Nova 2 Sonic in the `promptStart` event along with audio and text output settings:

```
{
    "event": {
        "promptStart": {
            "promptName": "<prompt-id>",
            "textOutputConfiguration": {
                "mediaType": "text/plain"
            },
            "audioOutputConfiguration": {
                "mediaType": "audio/lpcm",
                "sampleRateHertz": 16000,
                "sampleSizeBits": 16,
                "channelCount": 1,
                "voiceId": "matthew",
                "encoding": "base64",
                "audioType": "SPEECH"
            },
            "toolUseOutputConfiguration": {
                "mediaType": "application/json"
            },
            "toolConfiguration": {
                "tools": [
                    {
                        "toolSpec": {
                            "name": "get_weather",
                            "description": "Get current weather information for a specific location",
                            "inputSchema": {
                                "json": {
                                    "type": "object",
                                    "properties": {
                                        "location": {
                                            "type": "string",
                                            "description": "City name or zip code"
                                        },
                                        "units": {
                                            "type": "string",
                                            "enum": ["celsius", "fahrenheit"],
                                            "description": "Temperature units"
                                        }
                                    },
                                    "required": ["location"]
                                }
                            }
                        }
                    }
                ],
                "toolChoice": {
                    "auto": {}
                }
            }
        }
    }
}
```

## Tool Choice Parameters
<a name="sonic-tool-choice-parameters"></a>

Nova 2 Sonic supports three tool choice parameters to control when and which tools are used. Specify the toolChoice parameter in your tool configuration:
+ Auto (default): The model decides whether any tools are needed and can call multiple tools if required. Provides maximum flexibility.
+ Any: Ensures at least one of the available tools is called at the beginning of the response, with the model selecting the most appropriate one. Useful when you have multiple knowledge bases or tools and want to guarantee one is used.
+ Tool: Forces a specific named tool to be called exactly once at the beginning of the response. For example, if you specify a knowledge base tool, the model will query it before responding, regardless of whether it thinks the tool is needed.

**Tool Choice Examples**

Auto (default)

```
"toolChoice": { 
    "auto": {} 
}
```

Any:

```
"toolChoice": {
    "any": {}
}
```

Specific Tool:

```
"toolChoice": {
    "tool": {
        "name": "get_weather"
    }
}
```

## Receiving and processing tool use events
<a name="sonic-tool-receiving"></a>

When Amazon Nova 2 Sonic determines that a tool is needed, it sends a `toolUse` event containing:

1. `toolUseID`: unique identifier for this tool invocation

1. ToolName: the tool name to execute

1. Content: JSON string containing parameters extracted from the user's request

1. SessionID: current session identifier

1. Role: set to "TOOL" for tool use events

Example tool use event

```
{
    "event": {
        "toolUse": {
            "completionId": "<completion-id>",
            "content": "{\"location\": \"Seattle\", \"units\": \"fahrenheit\"}",
            "contentId": "<content-id>",
            "promptName": "<prompt-id>",
            "role": "TOOL",
            "sessionId": "<session-id>",
            "toolName": "get_weather",
            "toolUseId": "<tool-use-id>"
        }
    }
}
```

Processing steps

1. Receive the toolUse event from Nova 2 Sonic

1. Extract the tool name and parameters from the event

1. Execute your tool logic (API call, database query, and so on)

1. Return the result using a toolResult event

Example ToolResult Event

```
{
    "event": {
        "toolResult": {
            "promptName": "<prompt-id>",
            "contentName": "<content-id>",
            "content": "{\"temperature\": 72, \"condition\": \"sunny\", \"humidity\": 45}"
        }
    }
}
```

## Best practices
<a name="sonic-tool-best-practices"></a>
+ Clear descriptions: Write detailed tool descriptions to help Nova 2 Sonic understand when to use each tool.
+ Validate parameters: Always validate tool parameters before execution to prevent errors. Define tool parameters using proper JSON schema with structured data types (such as enums, numbers, or booleans) rather than open-ended strings whenever possible.
+ Error handling: Return meaningful error messages in toolResult events when tools fail.
+ Always respond to tool calls: Nova 2 Sonic expects a toolResult event after every toolUse event it sends. If your application fails to respond, even when an error occurs, the model enters a waiting state, causing unresponsive behavior or unexpected output. Always send a toolResult event in response, even if it contains an error message or signals that the session is ending.
+ Async execution: Take advantage of asynchronous tool calling to maintain conversation flow.
+ Tool naming: Use descriptive, action-oriented names (such as get\_weather, search\_database, send\_email).