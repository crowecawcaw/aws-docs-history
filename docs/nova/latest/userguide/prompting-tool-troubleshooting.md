# Troubleshooting tool calls

You might see different errors when working with tools and Amazon Nova models. Here are a few examples and tips to help you troubleshoot.

`An error occurred (ModelErrorException) when calling the Converse operation: The model produced an invalid sequence as part of ToolUse. Please refer to the model tool use troubleshooting guide.`

**Validate your inference parameters** - Amazon Nova models have more success calling tools when using greedy decoding. To enable greedy decoding, set the temperature parameters to 0.

```
`inferenceConfig={
 "temperature": 0
}

additionalModelRequestFields={"inferenceConfig": {"topK": 1}}`
```

**Increase the maximum token count** - It is common for tool outputs to require a large token output, ensure that the max tokens set is large enough to accommodate the expected return schema. If the model response is larger than your max token count, it will trigger an exception. You can set the maximum tokens in the `inferenceConfig` parameter:

```
`inferenceConfig={
 "maxTokens": 3000
}`
```

**Review the system prompt** - To improve the accuracy of tool calling, Amazon Nova uses chain-of-thought reasoning when calling a tool. You will see this output in the response in <thinking> tags. We do not recommended trying to remove this functionality. Instead, we recommend that you drop the output if you do not need it in your application.

`An error occurred (ValidationException) when calling the Converse operation`

The passed tool configuration does not comply to the required conventions. Refer to the [Converse API spec](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html") for specifications for all parameters.

If it looks like tools are being ignored by the model, make sure you are following the correct JSON schema for the tool config:

- Top level schema must of of type [Object](https://json-schema.org/understanding-json-schema/reference/object "https://json-schema.org/understanding-json-schema/reference/object")
- Only three fields are supported in top-level Object - `type` (must be set to "object"), `properties`, and `required`
- Common unsupported fields at the top level are: `$schema`, `description`, `title`, and `additionalProperties`
  If a tool is not being returned when expected, it is recommended to leverage the `tool_choice` API parameter.

- **Tool**: The specified tool will be called once.

```
{
   "toolChoice": {
        "tool": {
            "name": "name_of_tool"
        }
    }
}
```

- **Any**: One of the provided tools will be called at least once.

```
{
   "toolChoice": {
        "any": {}
    }
}
```
