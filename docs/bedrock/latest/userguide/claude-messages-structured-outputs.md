# Get validated JSON results from models

You can use structured outputs with Claude Sonnet 4.5, Claude Haiku 4.5,
Claude Opus 4.5, and Claude Opus 4.6 through the Converse API ([Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") or
[ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md")) or the InvokeModel API ([InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")) on the
`bedrock-runtime` endpoint. Structured outputs is _not_
supported on the Anthropic Messages API path on the `bedrock-mantle` endpoint
(`https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`); the
`output_config.format` parameter is rejected with a `400`
error.

To learn more, see [Get validated JSON results from models](structured-output.md "structured-output.md").
