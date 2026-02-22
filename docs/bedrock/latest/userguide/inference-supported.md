# Supported Regions and models for running model inference

Model inference using foundation models is supported in all Regions and with all models supported by Amazon Bedrock. To see the Regions and models supported by Amazon Bedrock, refer to [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

You can also run model inference with Amazon Bedrock resources other than foundation models. Refer to the following pages to see Region and model availability for different resources:

- [Supported Regions and models for inference profiles](inference-profiles-support.md "inference-profiles-support.md")
- [Supported Regions and models for Prompt management](prompt-management-supported.md "prompt-management-supported.md")

###### Note

[InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") only work on prompts from Prompt management whose configuration specifies an Anthropic Claude or Meta Llama model.

- [Supported models and Regions for fine-tuning](custom-model-fine-tuning.md#custom-model-supported "custom-model-fine-tuning.md#custom-model-supported")
- [Use Custom model import to import a customized open-source model into Amazon Bedrock](model-customization-import-model.md "model-customization-import-model.md")
- [Supported Regions and models for Amazon Bedrock Guardrails](guardrails-supported.md "guardrails-supported.md")
