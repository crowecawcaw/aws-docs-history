

# Build
<a name="build"></a>

This section covers how to interact with Amazon Bedrock programmatically. For new applications, we recommend the `bedrock-runtime` endpoint. Pick an API, and start making inference requests.

**Quick start**


| **Your situation** | **Recommended path** | 
| --- | --- | 
| Want a unified AWS-native interface across all models | Use the bedrock-runtime endpoint with the [Converse API](conversation-inference.md) | 
| Need direct model control or non-text modalities | Use the bedrock-runtime endpoint with the [Invoke API](inference-invoke.md) | 
| Migrating from OpenAI APIs | Use the bedrock-runtime endpoint with the [Responses API](bedrock-mantle.md#bedrock-mantle-responses) or [Chat Completions API](inference-chat-completions.md) — same OpenAI shape, plus Amazon Bedrock features such as [Guardrails](guardrails.md) and [cross-Region inference](cross-region-inference.md). | 
| Migrating from Anthropic APIs | Use the bedrock-runtime endpoint with the [Messages API](inference-messages-api.md) | 

**Topics**
+ [Endpoints supported by Amazon Bedrock](endpoints.md)
+ [APIs supported by Amazon Bedrock](apis.md)
+ [Making inference requests](inference.md)
+ [Use a tool to complete an Amazon Bedrock model response](tool-use.md)
+ [Web Search](web-search.md)
+ [Projects (OpenAI-compatible)](projects.md)
+ [Workspaces (Anthropic-compatible)](workspaces.md)
+ [API keys](api-keys.md)