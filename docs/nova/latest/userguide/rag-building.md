# Building a custom RAG system with Amazon Nova

###### Note

Amazon Nova Premier is not yet available via the [RetrieveAndGenerate](../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md "../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md") API. To use the [RetrieveAndGenerate](../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md "../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md") API with Amazon Nova Premier, you need to provide a custom prompt when calling the [RetrieveAndGenerate](../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md "../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md") API. This is done by supplying the `promptTemplate` in the `generationConfiguration` argument in the [RetrieveAndGenerate](../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md "../../../bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md") API call as shown below:

```
'generationConfiguration': {
                        'promptTemplate': {
                            'textPromptTemplate': promptTemplate
                        }
                    }
```

To build a custom prompt template, see [prompting guidance for RAG](prompting-tools-rag.md "prompting-tools-rag.md").

You can use Amazon Nova Models as the LLM within a custom text RAG system. To build your
own RAG system with Amazon Nova, you can either configure your RAG system to query a
knowledge base directly or you can associate a knowledge base with an Agent (for more
information see [Building AI agents with Amazon Nova](agents.md "agents.md"))

When Using Amazon Nova within any RAG system there are two general approaches

- **Using a retriever as a tool** (Recommended):
  You can define your retriever for use as a tool in the ToolParameter of the
  converse API or Invokemodel API. For example, you can define the Bedrock [Retrieve API](../../../bedrock/latest/APIReference/API_agent-runtime_Retrieve.md "../../../bedrock/latest/APIReference/API_agent-runtime_Retrieve.md") or any other retriever as a "tool".
- **Using Custom Instructions for RAG systems:**
  You can define your own custom instructions in order to build a custom RAG
  system.
  **Using a retriever as a tool**

Define a tool that allows the model to invoke a retriever. The definition of the tool
is a JSON schema that you pass in the `toolConfig` ([ToolConfiguration](../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md "../../../bedrock/latest/APIReference/API_runtime_ToolConfiguration.md")) request parameter to the `Converse`
operation.

```
`{
 "tools": [
 {
 "toolSpec": {
 "name": "Retrieve information tool",
 "description": "This tool retrieves information from a custom database",
 "inputSchema": {
 "json": {
 "type": "object",
 "properties": {
 "query": {
 "type": "string",
 "description": "This is the description of the query parameter"
 }
 },
 "required": [
 "query"
 ]
 }
 }
 }
 }
 ]
}`
```

After the tool is defined you can pass the tool configuration as a parameter in the
converse API.

**How to interpret the response elements**

You will receive a response from the model as a JSON under the assistant "role" with
the content type being "toolUse" or as a context type being "text" if the model chooses
not to use the retriever tool. If the model chooses to use the retriever tool, the
response will identify the tool (tool_name). Information about how the requested tool
should be used is in the message that the model returns in the `output`
([ConverseOutput](../../../bedrock/latest/APIReference/API_runtime_ConverseOutput.md "../../../bedrock/latest/APIReference/API_runtime_ConverseOutput.md")) field. Specifically, the `toolUse` ([ToolUseBlock](../../../bedrock/latest/APIReference/API_runtime_ToolUseBlock.md "../../../bedrock/latest/APIReference/API_runtime_ToolUseBlock.md")) field. You use the `toolUseId` field to identify
the tool request in later calls.

```
`{
 "output": {
 "message": {
 "role": "assistant",
 "content": [
 {
 "toolUse": {
 "toolUseId": "tooluse_1234567",
 "name": "Retrieve information tool",
 "input": {
 "query": "Reformatted user query" #various arguments needed by the chosen tool
 }
 }
 }
 ]
 }
 },
 "stopReason": "tool_use"
}`
```

From the `toolUse` field in the model response, you can use the
`name` field to identify the name of the tool. Then call the
implementation of the tool and pass the input parameters from the `input`
field.

**How to input the retrieved content back into the Converse
API**

To rerun the retrieved results back to Amazon Nova, you can now construct a Tool Block
message that includes a `toolResult` ([ToolResultBlock](../../../bedrock/latest/APIReference/API_runtime_ToolResultBlock.md "../../../bedrock/latest/APIReference/API_runtime_ToolResultBlock.md")) content block within the user role. In the content block,
include the response from the tool and the ID for the tool request that you got in the
previous step.

```
`{
 "role": "user",
 "content": [
 {
 "toolResult": {
 "toolUseId": "tooluse_1234567",
 "content": [
 {
 "json": {
 "Text chunk 1": "retrieved information chunk 1",
 "Text chunk 2": "retrieved information chunk 2"
 }
 }
 ],
 "status": "success | error"
 }
 }
 ]
}`
```

The [toolResult](../../../bedrock/latest/APIReference/API_runtime_ToolResultBlock.md "../../../bedrock/latest/APIReference/API_runtime_ToolResultBlock.md") can have "content" which can have "text", "JSON", and "image"
(dependent on the model used). If an error occurs in the tool, such as a request for a
nonexistent or wrong arguments, you can send error information to the model in the
`toolResult` field. To indicate an error, specify `error` in
the `status` field.
