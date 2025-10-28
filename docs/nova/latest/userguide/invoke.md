# Invoking Amazon Nova understanding models

Amazon Nova Multimodal understanding models are available for use for inferencing through
the Invoke API ([InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md"), [InvokeModelWithResponseStream](../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")) and the Converse API ([Converse](../../../bedrock/latest/APIReference/API_runtime_Converse.md "../../../bedrock/latest/APIReference/API_runtime_Converse.md") and [ConverseStream](../../../bedrock/latest/APIReference/API_runtime_ConverseStream.md "../../../bedrock/latest/APIReference/API_runtime_ConverseStream.md")). To create conversational applications see [Carry out a conversation with the converse API operations](../../../bedrock/latest/userguide/conversation-inference.md "../../../bedrock/latest/userguide/conversation-inference.md"). Both of the API
methods (Invoke and Converse) follow a very similar request pattern as detailed below

Key Differences between the Invoke API and Converse API are as follows:

- Inference parameters like topK are not supported in Converse and need to be passed
  in `additionalModelRequestFields`, while in the Invoke API it can be
  passed directly in the inference parameters.
- Document Support is limited to only Converse API and is not supported in Invoke
  API.
- Response parsing formats are different between the Invoke API and Convserse API
  constructs.
- Response streaming is different between `ConverseStream` and
  `InvokeModelWithStreaming`.
  In order to invoke the Amazon Nova models, you must [Request
  access to an Amazon Bedrock foundation model](../../../bedrock/latest/userguide/getting-started.md#getting-started-model-access "../../../bedrock/latest/userguide/getting-started.md#getting-started-model-access") in every region that you intend to use the
  models.

###### Topics

- [Messages API overview](#messages-api-overview "#messages-api-overview")
- [Utilizing the system prompt](#utilizing-system-prompt "#utilizing-system-prompt")
- [Using the Converse API](using-converse-api.md "using-converse-api.md")
- [Using the Invoke API](using-invoke-api.md "using-invoke-api.md")
- [Deploy a custom model for on-demand inference](deploy-custom-model.md "deploy-custom-model.md")
- [Complete request schema](complete-request-schema.md "complete-request-schema.md")

## Messages API overview

The Amazon Nova Understanding models utilize the Messages API, which enables the
submission of structured lists of input messages containing text, images, videos, and
documents. The model then generates the next message in the conversation. The Messages
API supports both single queries and stateless multi-turn conversations, allowing for
the creation of chatbots and virtual assistant applications. The API manages the
conversational exchanges between a user and an Amazon Nova model (assistant).

Amazon Nova models are trained to operate on alternating user and assistant
conversational turns. When creating a new message, you specify the prior conversational
turns with the messages parameter. The model then generates the next messages in the
conversation.

Each input message must be an object containing a role and content. Users may specify
a single message with the user role, or include multiple messages with both user and
assistant roles. However, the first message must always use the user role. If the
technique of prefilling the response from Amazon Nova is employed (by including a final
message with the assistant role), the model will continue its response from the provided
content. This approach will still result in a response with the assistant role.

The following represents a single user message:

```
`[{
 "role": "user",
 "content": [{"text":"Hello, Nova"}]
}]`
```

Here is an example with multiple conversational turns:

```
`[
 {"role": "user", "content": [{"text": "Hello there."}]},
 {"role": "assistant", "content": [{"text": "Hi, I'm Chatbot trained to answer your questions. How can I help you?"}]},
 {"role": "user", "content": [{"text": "Can you explain LLMs in plain English?"}]}
]`
```

Here is an example with a partially-filled response from Amazon Nova:

```
`[
 {"role": "user", "content": [{"text":"Please describe yourself using only JSON"}]},
 {"role": "assistant", "content": [{"text":"Here is my JSON description:\n{"}]}
]`
```

For information about creating prompts for Amazon Nova models, see [Text understanding prompting best
practices](prompting-text-understanding.md "prompting-text-understanding.md").

## Utilizing the system prompt

You can include a system prompt in the request. A system prompt lets you provide
context and instructions to Amazon Nova, such as specifying a particular goal or role.
Specify a system prompt in the `system` field, as shown in the following
example:

```
`[
 {"text": "You are an expert SaS analyst......"}
]`
```

See the following sections for examples of how to include a system prompt:

- [Using the Converse
  API](using-converse-api.md "using-converse-api.md")
- [Using the Invoke API](using-invoke-api.md "using-invoke-api.md")
- [Complete request
  schema](complete-request-schema.md "complete-request-schema.md")
