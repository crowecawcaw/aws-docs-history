# Tool use (function calling) with Amazon Nova

Tools are a way to provide external functionality to Amazon Nova such as an API call or a code function. This section will cover how you can define and integrate with tools when working with Amazon Nova models.

Tool use involves three high level steps:

- **User query** - You define the tools that Amazon Nova can use by providing a JSON schema that describes each tool's functionality and input requirements.
- **Tool Selection** - When a user sends a message, Amazon Nova will analyze it to determine if a tool is necessary to generate a response. This is referred to as `Auto` tool choice. See [Choosing a tool](tool-choice.md "tool-choice.md") for more information. If Amazon Nova identifies a suitable tool, it will "call the tool" and return the name of the tool and the parameters to use.

You, as the developer, are responsible for executing the tool based on the model's request. This means you need to write the code that invokes the tool's functionality and processes the input parameters provided by the model.

###### Note

Like all LLM responses, it is possible for Amazon Nova to hallucinate a tool call. It is the responsibility of you, the developer, to validate that the tool exists, inputs are formatted correctly, and the appropriate permissions are already in place.

- **Return Results** - After executing the tool, you must send the results back to Amazon Nova in a structured format. Valid formats include JSON or a combination of text and images. This allows Amazon Nova to incorporate the tool's output into the final response to the user.

If there are any errors during the tool's execution, you can denote this in the tool response to Amazon Nova, allowing Amazon Nova to adjust its response accordingly.
Consider a simple example of a calculator tool:

User query
The first step in the tool calling workflow is the user query to Amazon Nova for the result of a math equation - 10 times 5. This query is sent as the prompt to Amazon Nova along with a tool specification that represents the calculator.

```
`user_query = "10*5"

messages = [{
 "role": "user",
 "content": [{"text": user_query}]
}]

tool_config = {
 "tools": [
 {
 "toolSpec": {
 "name": "calculator", # Name of the tool
 "description": "A calculator tool that can execute a math equation", # Concise description of the tool
 "inputSchema": {
 "json": {
 "type": "object",
 "properties": {
 "equation": { # The name of the parameter
 "type": "string", # parameter type: string/int/etc
 "description": "The full equation to evaluate" # Helpful description of the parameter
 }
 },
 "required": [ # List of all required parameters
 "equation"
 ]
 }
 }
 }
 }
 ]
}`
```

Tool selection
Amazon Nova uses the context of the tool along with the user prompt to determine the necessary tool to use and the required configuration. This is returned as a part of the API response.

```
`{
 "toolUse": {
 "toolUseId": "tooluse_u7XTryCSReawd9lXwljzHQ",
 "name": "calculator",
 "input": {
 "equation": "10*5"
 }
 }
}`
```

The application is responsible for executing the tool and storing the result.

```
`def calculator(equation: str):
 return eval(equation)

tool_result = calculator("10*5")`
```

Return results
To return the result of the tool to Amazon Nova, the tool result is included in a new API request. Note that the tool use ID is consistent with the one returned from Amazon Nova in the previous response.

```
`{
 "toolResult": {
 "toolUseId": "tooluse_u7XTryCSReawd9lXwljzHQ",
 "content": [
 {
 "json": {
 "result": "50"
 }
 }
 ],
 "status": "success"
 }
}`
```

- Amazon Nova will use the full context of the messages, including the initial user query, the tool use, and tool result to determine the final response to the user. In this case, Amazon Nova will respond to the user that "10 times 5 is 50".

Amazon Nova allows tool use in both the Invoke and Converse API however, for full feature breadth we recommend using the [Converse API](../../../bedrock/latest/userguide/tool-use-inference-call.md "../../../bedrock/latest/userguide/tool-use-inference-call.md") and will be using examples with this API moving forward.

###### Topics

- [Defining a tool](tool-use-definition.md "tool-use-definition.md")
- [Invoking a tool](tool-use-invocation.md "tool-use-invocation.md")
- [Choosing a tool](tool-choice.md "tool-choice.md")
- [Returning tool results](tool-use-results.md "tool-use-results.md")
- [Reporting an error](tool-use-error.md "tool-use-error.md")
- [Additional references](#tool-use-resources "#tool-use-resources")

## Additional references

1. [Use
   a tool to complete a model response](../../../bedrock/latest/userguide/tool-use.md "../../../bedrock/latest/userguide/tool-use.md")
2. [Building AI agents with Amazon Nova](agents.md "agents.md")
3. [Text understanding prompting best
   practices](prompting-text-understanding.md "prompting-text-understanding.md")
4. [Troubleshooting tool calls](prompting-tool-troubleshooting.md "prompting-tool-troubleshooting.md")
