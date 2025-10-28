# Cohere models

This section describes the request parameters and response fields for Cohere models. Use this information
to make inference calls to Cohere models with the [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") (streaming) operations.
This section also includes Python code examples that shows how to call Cohere models. To use a model in an inference operation, you need the model ID for the model.
To get the model ID, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). Some
models also work with the [Converse API](conversation-inference.md "conversation-inference.md").
To check if the Converse API supports a specific Cohere model, see
[Supported models and
model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md"). For more code examples,
see [Code examples for Amazon Bedrock using AWS SDKs](service_code_examples.md "service_code_examples.md").

Foundation models in Amazon Bedrock support input and output modalities, which vary from model to
model. To check the modalities that Cohere models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which Amazon Bedrock
features the Cohere models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which AWS Regions that Cohere models
are available in, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

When you make inference calls with Cohere models, you include a prompt for the model. For general information
about creating prompts for the models that Amazon Bedrock supports, see [Prompt engineering concepts](prompt-engineering-guidelines.md "prompt-engineering-guidelines.md").
For Cohere specific prompt information, see the [Cohere prompt engineering guide](https://txt.cohere.com/how-to-train-your-pet-llm-prompt-engineering "https://txt.cohere.com/how-to-train-your-pet-llm-prompt-engineering").

###### Models

- [Cohere Command models](model-parameters-cohere-command.md "model-parameters-cohere-command.md")
- [Cohere Embed and Cohere Embed v4 models](model-parameters-embed.md "model-parameters-embed.md")
- [Cohere Command R and Command R+ models](model-parameters-cohere-command-r-plus.md "model-parameters-cohere-command-r-plus.md")
