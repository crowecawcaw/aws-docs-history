# Use a tool to complete an Amazon Bedrock model response

You can use the Amazon Bedrock API to give a model access to tools that can help it generate
responses for messages that you send to the model. For example, you might have a chat
application that lets users find out the most popular song played on a radio station. To
answer a request for the most popular song, a model needs a tool that can query and return
the song information.

###### Note

Tool use with models is also known as _Function calling_.

In Amazon Bedrock, the model doesn't directly call the tool. Rather, when you send a message to
a model, you also supply a definition for one or more tools that could potentially help the
model generate a response. In this example, you would supply a definition for a tool that
returns the most popular song for a specified radio station. If the model determines that it
needs the tool to generate a response for the message, the model responds with a request for
you to call the tool. It also includes the input parameters (the required radio station) to
pass to the tool.

In your code, you call the tool on the model's behalf. In this scenario, assume the tool
implementation is an API. The tool could just as easily be a database, Lambda function, or
some other software. You decide how you want to implement the tool. You then continue the
conversation with the model by supplying a message with the result from the tool. Finally
the model generates a response for the original message that includes the tool results that
you sent to the model.

To use tools with a model you can use the Converse API ([Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md")). The example
code in this topic uses the Converse API to show how to use a tool that gets the most
popular song for a radio station. For general information about calling the Converse API,
see [Carry out a conversation with the
Converse API operations](conversation-inference.md "conversation-inference.md").

It is possible to use tools with the base inference operations ([InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")). To find the inference parameters that you pass
in the request body, see the [inference parameters](model-parameters.md "model-parameters.md")
for the model that you want to use. We recommend using the Converse API as it provides
a consistent API, that works with all Amazon Bedrock models that support tool use.

For information about models that support tool calling, see
[Supported models and
model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md").

###### Topics

- [Call a tool with the Converse API](tool-use-inference-call.md "tool-use-inference-call.md")
- [Converse API tool use examples](tool-use-examples.md "tool-use-examples.md")
