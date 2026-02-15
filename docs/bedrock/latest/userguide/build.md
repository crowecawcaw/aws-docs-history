# Build

To start building models using Amazon Bedrock, first, start from your use-case. Then choose an API, an endpoint, and then start using the models programmatically.

**Choose API based on your use-case**

Amazon Bedrock provide four main API patterns to perform inference in Amazon Bedrock. [Responses](bedrock-mantle.md "bedrock-mantle.md"), [Chat Completions](bedrock-mantle.md "bedrock-mantle.md"), [Invoke](inference-invoke.md "inference-invoke.md"), and [Converse](conversation-inference.md "conversation-inference.md"). Read more about the APIs supported.

| **Scenario**                                                | **Recommended API**                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Migrating from OpenAI API-compatible endpoint               | Use OpenAI-compatible APIs: [Responses API](https://platform.openai.com/docs/api-reference/responses "https://platform.openai.com/docs/api-reference/responses") or [Chat Completions API](https://platform.openai.com/docs/api-reference/chat "https://platform.openai.com/docs/api-reference/chat") |
| Using models not compatible with OpenAI-compatible endpoint | Use native Amazon Bedrock APIs: [Converse](conversation-inference.md "conversation-inference.md") and [Invoke](inference-invoke.md "inference-invoke.md"). Read more on choosing the right APIs for your use-case.                                                                                    |

**Choosing end-point for Amazon Bedrock**

Once you have identified which API to use, you can then identify the endpoint to use to interact programmatically with Amazon Bedrock. Read more about the APIs supported.

| **Endpoint**        | **Supported APIs**                                                                                                                                                                                                    |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bedrock-mantle.*`  | [Responses API](bedrock-mantle.md "bedrock-mantle.md"), [Chat Completions API](bedrock-mantle.md "bedrock-mantle.md")                                                                                                 |
| `bedrock-runtime.*` | [Invoke API](inference-invoke.md "inference-invoke.md"), [Converse API](conversation-inference.md "conversation-inference.md"), [Chat Completions API](inference-chat-completions.md "inference-chat-completions.md") |

**Choosing a model**

You can see the list of models that Amazon Bedrock supports based on the endpoint you are using.

| **Endpoint**        | **API**                | **Description**                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bedrock-runtime.*` | `ListFoundationModels` | Returns a list of all available foundation models in Bedrock. Provides summary information about multiple models, including their model IDs, provider names, supported modalities (text, image, embedding), input/output formats, and whether they support streaming or customization. Use `GetFoundationModel` API to retrieve detailed information about a specific foundation model using its model ID. |
| `bedrock-mantle.*`  | `client.models.list`   | OpenAI-compatible API to discover available models. Retrieves a list of models you can use with the Responses API and Chat Completions API.                                                                                                                                                                                                                                                                |
