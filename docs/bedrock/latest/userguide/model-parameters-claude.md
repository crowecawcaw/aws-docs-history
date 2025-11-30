# Anthropic Claude models

This section describes the request parameters and response fields for Anthropic Claude models. Use this information
to make inference calls to Anthropic Claude models with the [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") (streaming) operations.
This section also includes Python code examples that shows how to call Anthropic Claude models. To use a model in an inference operation, you need the model ID for the model.
To get the model ID, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). Some
models also work with the [Converse API](conversation-inference.md "conversation-inference.md").
To check if the Converse API supports a specific Anthropic Claude model, see
[Supported models and
model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md"). For more code examples,
see [Code examples for Amazon Bedrock using AWS SDKs](service_code_examples.md "service_code_examples.md").

Foundation models in Amazon Bedrock support input and output modalities, which vary from model to
model. To check the modalities that Anthropic Claude models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which Amazon Bedrock
features the Anthropic Claude models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which AWS Regions that Anthropic Claude models
are available in, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

When you make inference calls with Anthropic Claude models, you include a prompt for the model. For general information
about creating prompts for the models that Amazon Bedrock supports, see [Prompt engineering concepts](prompt-engineering-guidelines.md "prompt-engineering-guidelines.md").
For Anthropic Claude specific prompt information, see the [Anthropic Claude prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview").

You can use Amazon Bedrock to send [Anthropic Claude Text Completions API](model-parameters-anthropic-claude-text-completion.md "model-parameters-anthropic-claude-text-completion.md") or [Anthropic Claude
Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md") inference requests.

You use the messages API to create conversational applications, such as a virtual
assistant or a coaching application. Use the text completion API for single-turn text
generation applications. For example, generating text for a blog post or summarizing
text that a user supplies.

Anthropic Claude models support the use of XML tags to structure and delineate your prompts. For example, you can surround examples in your prompt with an `<examples>` tag. Use descriptive tag names for optimal results. For more information, see [Use XML tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags") in the [Anthropic user guide](https://docs.anthropic.com/en/docs/welcome "https://docs.anthropic.com/en/docs/welcome").

Anthropic Claude models support the use of PDF document processing and citations. Citations provide
references to information in the document used by the model in a response.

###### Note

To use system prompts in inference calls, you must use Anthropic Claude versions that are 2.1 or greater.

For information about creating system prompts, see [Giving Claude a role with a system prompt](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts") in the
Anthropic Claude documentation.

To avoid timeouts with Anthropic Claude version 2.1, we recommend limiting the input token count in the
`prompt` field to 180K. We expect to address this timeout issue soon.

In the inference call, fill the
`body` field with a JSON object that conforms
the type call you want to make, [Anthropic Claude Text Completions API](model-parameters-anthropic-claude-text-completion.md "model-parameters-anthropic-claude-text-completion.md") or
[Anthropic Claude
Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md").

###### Topics

- [Anthropic Claude Text Completions API](model-parameters-anthropic-claude-text-completion.md "model-parameters-anthropic-claude-text-completion.md")
- [Anthropic Claude
  Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md")
