# AI21 Labs models

This section describes the request parameters and response fields for AI21 Labs models. Use this information
to make inference calls to AI21 Labs models with the [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") (streaming) operations.
This section also includes Python code examples that shows how to call AI21 Labs models. To use a model in an inference operation, you need the model ID for the model.
To get the model ID, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). Some
models also work with the [Converse API](conversation-inference.md "conversation-inference.md").
To check if the Converse API supports a specific AI21 Labs model, see
[Supported models and
model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md"). For more code examples,
see [Code examples for Amazon Bedrock using AWS SDKs](service_code_examples.md "service_code_examples.md").

Foundation models in Amazon Bedrock support input and output modalities, which vary from model to
model. To check the modalities that AI21 Labs models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which Amazon Bedrock
features the AI21 Labs models support, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). To check which AWS Regions that AI21 Labs models
are available in, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

When you make inference calls with AI21 Labs models, you include a prompt for the model. For general information
about creating prompts for the models that Amazon Bedrock supports, see [Prompt engineering concepts](prompt-engineering-guidelines.md "prompt-engineering-guidelines.md").
For AI21 Labs specific prompt information, see the [AI21 Labs prompt engineering guide](https://docs.ai21.com/docs/prompt-engineering "https://docs.ai21.com/docs/prompt-engineering").

###### Topics

- [AI21 Labs Jurassic-2 models](model-parameters-jurassic2.md "model-parameters-jurassic2.md")
- [AI21 Labs Jamba models](model-parameters-jamba.md "model-parameters-jamba.md")
