# Supported Regions and models for Prompt management

Prompt management is supported in the following Regions (for more information about Regions supported in Amazon Bedrock see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md")):

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Osaka)
- Asia Pacific (Mumbai)
- Asia Pacific (Hyderabad)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Zurich)
- Europe (Stockholm)
- Europe (Milan)
- Europe (Spain)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- South America (São Paulo)
  You can use Prompt management with any text model supported for the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") API. For a list of supported models, see [Supported models and
  model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md").

###### Note

[InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") only work on prompts from Prompt management whose configuration specifies an Anthropic Claude or Meta Llama model.
