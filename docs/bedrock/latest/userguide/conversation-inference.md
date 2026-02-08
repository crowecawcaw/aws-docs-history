# Carry out a conversation with the

Converse API operations

You can use the Amazon Bedrock Converse API to create conversational applications
that send and receive messages to and from an Amazon Bedrock model. For example, you can create a
chat bot that maintains a conversation over many turns and uses a persona or tone
customization that is unique to your needs, such as a helpful technical support
assistant.

To use the Converse API, you use the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") (for streaming
responses) operations to send messages to a model. It is possible to use the existing base
inference operations ([InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")) for conversation applications. However, we
recommend using the Converse API as it provides consistent API, that works
with all Amazon Bedrock models that support messages. This means you can write code once and use
it with different models. Should a model have unique inference parameters, the
Converse API also allows you to pass those unique parameters in a model
specific structure.

You can use the Converse API to implement [tool
use](tool-use.md "tool-use.md") and [guardrails](guardrails-use-converse-api.md "guardrails-use-converse-api.md") in your
applications.

###### Note

- With Mistral AI and Meta models, the Converse API embeds your input in
  a model-specific prompt template that enables
  conversations.
- Restrictions apply to the following operations: `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, and `ConverseStream`. See [API restrictions](inference-api-restrictions.md "inference-api-restrictions.md") for details.
  For code examples, see the following:

- Python examples for this topic – [Converse API
  examples](conversation-inference-examples.md "conversation-inference-examples.md")
- Various languages and models – [Code examples for Amazon Bedrock Runtime using AWS SDKs](service_code_examples_bedrock-runtime.md "service_code_examples_bedrock-runtime.md")
- Java tutorial – [A Java developer's guide to Bedrock's new Converse
  API](https://community.aws/content/2hUiEkO83hpoGF5nm3FWrdfYvPt/amazon-bedrock-converse-api-java-developer-guide "https://community.aws/content/2hUiEkO83hpoGF5nm3FWrdfYvPt/amazon-bedrock-converse-api-java-developer-guide")
- JavaScript tutorial – [A developer's guide to Bedrock's new Converse API](https://community.aws/content/2dtauBCeDa703x7fDS9Q30MJoBA/amazon-bedrock-converse-api-developer-guide "https://community.aws/content/2dtauBCeDa703x7fDS9Q30MJoBA/amazon-bedrock-converse-api-developer-guide")

###### Topics

- [Supported models and
  model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md")
- [Using the Converse
  API](conversation-inference-call.md "conversation-inference-call.md")
- [Converse API
  examples](conversation-inference-examples.md "conversation-inference-examples.md")
