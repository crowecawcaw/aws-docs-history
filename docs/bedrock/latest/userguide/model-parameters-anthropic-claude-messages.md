# Anthropic Claude

Messages API

This section provides inference parameters and code examples for using the Anthropic
Claude Messages API.

###### Topics

- [Anthropic Claude Messages API overview](#model-parameters-anthropic-claude-messages-overview "#model-parameters-anthropic-claude-messages-overview")
- [Tool
  use](model-parameters-anthropic-claude-messages-tool-use.md "model-parameters-anthropic-claude-messages-tool-use.md")
- [Extended thinking](claude-messages-extended-thinking.md "claude-messages-extended-thinking.md")
- [Thinking encryption](claude-messages-thinking-encryption.md "claude-messages-thinking-encryption.md")
- [Differences in thinking
  across model versions](claude-messages-thinking-differences.md "claude-messages-thinking-differences.md")
- [Request and
  Response](model-parameters-anthropic-claude-messages-request-response.md "model-parameters-anthropic-claude-messages-request-response.md")
- [Code
  examples](api-inference-examples-claude-messages-code-examples.md "api-inference-examples-claude-messages-code-examples.md")
- [Supported models](claude-messages-supported-models.md "claude-messages-supported-models.md")

## Anthropic Claude Messages API overview

You can use the Messages API to create chat bots or virtual assistant applications.
The API manages the conversational exchanges between a user and an Anthropic Claude
model (assistant).

###### Tip

This topic shows how to use the Anthropic Claude messages API with the base
inference operations ([InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md")). However, we recommend that you use the
Converse API to implement messages in your application. The
Converse API provides a unified set of parameters that work
across all models that support messages. For more information, see [Carry out a conversation with the
Converse API operations](conversation-inference.md "conversation-inference.md").

Anthropic trains Claude models to operate on alternating user and assistant
conversational turns. When creating a new message, you specify the prior conversational
turns with the messages parameter. The model then generates the next Message in the
conversation.

Each input message must be an object with a role and content. You can specify a single
user-role message, or you can include multiple user and assistant messages.

If you are using the technique of prefilling the response from Claude (filling in
the beginning of Claude's response by using a final assistant role Message), Claude
will respond by picking up from where you left off. With this technique, Claude will
still return a response with the assistant role.

If the final message uses the assistant role, the response content will continue
immediately from the content in that message. You can use this to constrain part of the
model's response.

Example with a single user message:

```
[{"role": "user", "content": "Hello, Claude"}]
```

Example with multiple conversational turns:

```
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```

Example with a partially-filled response from Claude:

```
[
  {"role": "user", "content": "Please describe yourself using only JSON"},
  {"role": "assistant", "content": "Here is my JSON description:\n{"},
]
```

Each input message content may be either a single string or an array of content
blocks, where each block has a specific type. Using a string is shorthand for an array
of one content block of type "text". The following input messages are equivalent:

```
{"role": "user", "content": "Hello, Claude"}
```

```
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```

For information about creating prompts for Anthropic Claude models, see [Intro to
prompting](https://docs.anthropic.com/claude/docs/intro-to-prompting "https://docs.anthropic.com/claude/docs/intro-to-prompting") in the Anthropic Claude documentation. If you have existing
[Text
Completion](model-parameters-anthropic-claude-text-completion.md "model-parameters-anthropic-claude-text-completion.md") prompts that you want to migrate to the messages API, see [Migrating from Text Completions](https://docs.anthropic.com/claude/reference/migrating-from-text-completions-to-messages "https://docs.anthropic.com/claude/reference/migrating-from-text-completions-to-messages").

###### Important

The timeout period for inference calls to Anthropic Claude 3.7 Sonnet and
Claude 4 models is 60 minutes. By default, AWS SDK
clients timeout after 1 minute. We recommend that you increase the read timeout
period of your AWS SDK client to at least 60 minutes. For example, in the AWS
Python botocore SDK, change the value of the `read_timeout` field in
[botocore.config](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html# "https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#") to at least 3600.

### System

prompts

You can also include a system prompt in the request. A system prompt lets you
provide context and instructions to Anthropic Claude, such as specifying a
particular goal or role. Specify a system prompt in the `system` field,
as shown in the following example.

```
"system": "You are Claude, an AI assistant created by Anthropic to be helpful,
                harmless, and honest. Your goal is to provide informative and substantive responses
                to queries while avoiding potential harms."
```

For more information, see [System prompts](https://docs.anthropic.com/en/docs/system-prompts "https://docs.anthropic.com/en/docs/system-prompts")
in the Anthropic documentation.

### Multimodal prompts

A multimodal prompt combines multiple modalities (images and text) in a single
prompt. You specify the modalities in the `content` input field. The
following example shows how you could ask Anthropic Claude to describe the
content of a supplied image. For example code, see [Multimodal
code examples](api-inference-examples-claude-messages-code-examples.md#api-inference-examples-claude-multimodal-code-example "api-inference-examples-claude-messages-code-examples.md#api-inference-examples-claude-multimodal-code-example").

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": "iVBORw..."
                    }
                },
                {
                    "type": "text",
                    "text": "What's in these images?"
                }
            ]
        }
    ]
}
```

###### Note

The following restrictions pertain to the `content` field:

- You can include up to 20 images. Each image's size, height, and width must be no more than 3.75 MB, 8,000 px, and 8,000 px, respectively.
- You can include up to five documents. Each document's size must be no more than 4.5 MB.
- You can only include images and documents if the `role` is `user`.

Each image you include in a request counts towards your token usage. For more
information, see [Image
costs](https://docs.anthropic.com/claude/docs/vision#image-costs "https://docs.anthropic.com/claude/docs/vision#image-costs") in the Anthropic documentation.
