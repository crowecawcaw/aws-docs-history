# Mistral AI models

This section describes the request parameters and response fields for Mistral AI models. Use this information
to make inference calls to Mistral AI models with the [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") (streaming) operations.
This section also includes Python code examples that shows how to call Mistral AI models. To use a model in an inference operation, you need the model ID for the model.
To get the model ID, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). Some
models also work with the [Converse API](conversation-inference.md "conversation-inference.md").
To check if the Converse API supports a specific Mistral AI model, see
[Supported models and
model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md"). For more code examples,
see [Code examples for Amazon Bedrock using AWS SDKs](service_code_examples.md "service_code_examples.md").

Foundation models in Amazon Bedrock support input and output modalities, which vary from model to
model. To check the modalities that Mistral AI models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which Amazon Bedrock
features the Mistral AI models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which AWS Regions that Mistral AI models
are available in, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

When you make inference calls with Mistral AI models, you include a prompt for the model. For general information
about creating prompts for the models that Amazon Bedrock supports, see [Prompt engineering concepts](prompt-engineering-guidelines.md "prompt-engineering-guidelines.md").
For Mistral AI specific prompt information, see the [Mistral AI prompt engineering guide](https://docs.mistral.ai/guides/prompting_capabilities/ "https://docs.mistral.ai/guides/prompting_capabilities/").

###### Topics

- [Mistral AI text completion](model-parameters-mistral-text-completion.md "model-parameters-mistral-text-completion.md")
- [Mistral AI chat completion](model-parameters-mistral-chat-completion.md "model-parameters-mistral-chat-completion.md")
- [Mistral AI Large (24.07) parameters and inference](model-parameters-mistral-large-2407.md "model-parameters-mistral-large-2407.md")
- [Pixtral Large (25.02)
  parameters and inference](model-parameters-mistral-pixtral-large.md "model-parameters-mistral-pixtral-large.md")
