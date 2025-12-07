# Tool configuration

Amazon Nova 2 Sonic supports tool use, allowing the model to request external
information or actions during conversations. Tools enable integration with APIs,
databases and other services to provide dynamic, context-aware responses.

The following diagram illustrates how tool use works:

![](images/How-tool-use-works_5.png)

## Defining tools

Tools are defined in the `PromptStartEvent` using the
`toolConfig` parameter. Each tool definition includes a name,
description and input schema that describes the parameters the tool
accepts.

The tool definition should clearly describe what the tool does and what
parameters it requires. This helps the model understand when and how to use the
tool effectively.

## Receiving and processing tool use

events

When Amazon Nova 2 Sonic determines it needs a tool, it sends a
`toolUse` event containing the tool name and input parameters.
Your application must:

1. Receive the `toolUse` event
2. Extract the tool name and parameters
3. Execute the requested tool with the provided parameters
4. Send the tool result back using `toolResultContent`
   events

Tool results follow the standard three-event pattern:
`contentStart` (with role: "TOOL"), the tool result content and
`contentEnd`.

## Best practices

- Provide clear, descriptive tool names and descriptions
- Define comprehensive input schemas with all required parameters
- Handle tool execution errors gracefully and return meaningful error
  messages
- Keep tool responses concise and relevant
- Implement timeout handling for long-running tool operations
