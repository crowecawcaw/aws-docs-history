

# Returning tool results
<a name="tool-use-results"></a>

Once the tool has been invoked by the application, the final step is to provide the tool result to the model. This is done by returning a tool result with the ID of the tool call and the response content. This content follows the [ToolResultBlock](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ToolResultBlock.html) schema:

```
{
    "toolResult": {
        "toolUseId": tool['toolUseId'],
        "content": [{"json": {"song": song, "artist": artist}}],
        "status": "success"
    }
}
```

The contents of the `ToolResultBlock` should be either a single JSON or a mix of text and images.

The status field can be used to indicate to the model the status of the tool execution. If the tool execution failed you can indicate the failure, and Amazon Nova will attempt the modify its original tool call.

Refer to the [ToolResultContentBlock](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ToolResultContentBlock.html) documentation for more details on the schema.

Here is an example of how to use the Converse API to return the tool results:

```
messages.append({
    "role": "user",
    "content": [
        {
            "toolResult": {
                "toolUseId": tool['toolUseId'],
                "content": [{"json": {"song": song, "artist": artist}}],
                "status": "success"
            }
        }
    ]
})

inf_params = {"maxTokens": 1000, "temperature": 0}

# Send the tool result to the model.
response = client.converse(
    modelId="us.amazon.nova-lite-v1:0",
    messages=messages,
    toolConfig=tool_config,
    inferenceConfig=inf_params
)

print(response['output']['message'])
```

For more details on how to leverage tools refer to [Amazon Bedrock Tool Use](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) documentation or visit the [tool use samples](https://github.com/aws-samples/amazon-nova-samples/blob/main/multimodal-understanding/repeatable-patterns/10-tool-calling-with-converse/10_tool_calling_with_converse.ipynb) in the Amazon Nova samples repository.