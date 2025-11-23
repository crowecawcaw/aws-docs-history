# Supported Regions and models for Prompt management

Prompt management is supported in the following AWS Regions:

- ap-northeast-1
- ap-northeast-2
- ap-northeast-3
- ap-south-1
- ap-south-2
- ap-southeast-1
- ap-southeast-2
- ca-central-1
- eu-central-1
- eu-central-2
- eu-north-1
- eu-south-1
- eu-south-2
- eu-west-1
- eu-west-2
- eu-west-3
- sa-east-1
- us-east-1
- us-east-2
- us-gov-east-1
- us-gov-west-1
- us-west-2
  You can use Prompt management with any text model supported for the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") API. For a list of supported models, see [Supported models and
  model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md").

###### Note

[InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") only work on prompts from Prompt management whose configuration specifies an Anthropic Claude or Meta Llama model.
