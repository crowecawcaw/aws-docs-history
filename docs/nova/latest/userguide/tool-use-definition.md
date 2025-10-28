# Defining a tool

A critical step in the tool calling workflow is defining the tool. The tool definition must include all of the necessary context to guide the model on when it is appropriate to invoke the tool.

To define a tool, create a tool configuration and pass it with the user message to the API. The [tool configuration](../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md "../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md") schema expects an array of tools and optionally a tool choice parameter.

###### Note

Amazon Nova supports the `auto`, `any`, and `tool` options for `toolChoice`. For more information, see [ToolChoice](../../../bedrock/latest/APIReference/API_runtime_ToolChoice.md "../../../bedrock/latest/APIReference/API_runtime_ToolChoice.md") in the Amazon Bedrock API documentation and [Use a tool to complete an Amazon Bedrock model response](../../../bedrock/latest/userguide/tool-use.md "../../../bedrock/latest/userguide/tool-use.md").

Here is an example of how to define a tool:

```
`tool_config = {
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
 "description": "The call sign for the radio station for which you want the most popular song. Example calls signs are WZPZ, and WKRP."
 }
 },
 "required": [
 "sign"
 ]
 }
 }
 }
 }
 ],
}`
```

The name, description, and the input schema must be explicit with the exact functionality of the tool. Ensure any key differentiators for when to use the tool are reflected in the tool configuration.

###### Note

Amazon Nova understanding models currently support only a subset of JsonSchema functionality when used to define the [ToolInputSchema](../../../bedrock/latest/APIReference/API_runtime_ToolInputSchema.md "../../../bedrock/latest/APIReference/API_runtime_ToolInputSchema.md") in Converse API.

- The top level schema must be of type [Object](https://json-schema.org/understanding-json-schema/reference/object "https://json-schema.org/understanding-json-schema/reference/object").
- Only three fields are supported in the top-level Object - type (must be set to ‘object’), [`properties`](https://json-schema.org/understanding-json-schema/reference/object#properties "https://json-schema.org/understanding-json-schema/reference/object#properties"), and [`required`](https://json-schema.org/understanding-json-schema/reference/object#required "https://json-schema.org/understanding-json-schema/reference/object#required").
  For tool calling, we recommend setting the temperature to 0 to enable greedy decoding.

Here is an example of calling a tool with the Converse API:

```
`import json
import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

input_text = "What is the most popular song on WZPZ?"

messages = [{
 "role": "user",
 "content": [{"text": input_text}]
}]

inf_params = {"maxTokens": 1000, "temperature": 0}

response = client.converse(
 modelId="us.amazon.nova-lite-v1:0",
 messages=messages,
 toolConfig=tool_config,
 inferenceConfig=inf_params
)

messages.append(response["output"]["message"])

# Pretty print the response JSON.
print("[Full Response]")
print(json.dumps(response, indent=2))

# Print the tool content for easy readability.
tool = next(
 block["toolUse"]
 for block in response["output"]["message"]["content"]
 if "toolUse" in block
)
print("\n[Tool Response]")
print(tool)`
```
