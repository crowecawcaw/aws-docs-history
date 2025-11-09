# Anthropic Claude Text Completions API

This section provides inference parameters and code examples for using Anthropic Claude models with the Text Completions API.

###### Topics

- [Anthropic Claude Text Completions API overview](#model-parameters-anthropic-claude-text-completion-overview "#model-parameters-anthropic-claude-text-completion-overview")
- [Supported models](#claude-messages-supported-models "#claude-messages-supported-models")
- [Request and Response](#model-parameters-anthropic-claude-text-completion-request-response "#model-parameters-anthropic-claude-text-completion-request-response")
- [Code example](#api-inference-examples-claude-text-completion "#api-inference-examples-claude-text-completion")

## Anthropic Claude Text Completions API overview

Use the Text Completion API for single-turn text generation from a user supplied prompt.
For example, you can use the Text Completion API to generate text for a blog post or to summarize text input from a user.

For information about creating prompts for Anthropic Claude models, see [Introduction to prompt design](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design "https://docs.anthropic.com/claude/docs/introduction-to-prompt-design"). If you want to use your existing Text
Completions prompts with the
[Anthropic Claude
Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md"), see [Migrating from Text Completions](https://docs.anthropic.com/claude/reference/migrating-from-text-completions-to-messages "https://docs.anthropic.com/claude/reference/migrating-from-text-completions-to-messages").

## Supported models

You can use the Text Completions API with the following Anthropic Claude models.

- Anthropic Claude Instant v1.2
- Anthropic Claude v2
- Anthropic Claude v2.1

## Request and Response

The request body is passed in the `body` field of a request to
[InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md").

For more information,
see [https://docs.anthropic.com/claude/reference/complete_post](https://docs.anthropic.com/claude/reference/complete_post "https://docs.anthropic.com/claude/reference/complete_post") in the
Anthropic Claude documentation.

Request
Anthropic Claude has the following
inference parameters for a Text Completion inference call.

```
{
    "prompt": "\n\nHuman:`<prompt>`\n\nAssistant:",
    "temperature": float,
    "top_p": float,
    "top_k": int,
    "max_tokens_to_sample": int,
    "stop_sequences": [string]
}
```

The following are required parameters.

- **prompt** – (Required) The
  prompt that you want Claude to complete. For proper response
  generation you need to format your prompt using alternating
  `\n\nHuman:` and `\n\nAssistant:`
  conversational turns. For example:

```
"\n\nHuman: {userQuestion}\n\nAssistant:"
```

For more information, see [Prompt validation](https://docs.anthropic.com/claude/reference/prompt-validation "https://docs.anthropic.com/claude/reference/prompt-validation") in the
Anthropic Claude documentation.

- **max_tokens_to_sample** –
  (Required) The maximum number of tokens to generate before stopping.
  We recommend a limit of 4,000 tokens for optimal performance.

Note that Anthropic Claude models might stop generating tokens
before reaching the value of `max_tokens_to_sample`.
Different Anthropic Claude models have different maximum values
for this parameter. For more information, see
[Model comparison](https://docs.anthropic.com/claude/docs/models-overview#model-comparison "https://docs.anthropic.com/claude/docs/models-overview#model-comparison") in
the Anthropic Claude documentation.

| Default | Minimum | Maximum |
| ------- | ------- | ------- |
| 200     | 0       | 4096    |

The following are optional parameters.

- **stop_sequences**
  – (Optional) Sequences that will cause the model to stop generating.

Anthropic Claude models stop on `"\n\nHuman:"`, and may
include additional built-in stop sequences in the future. Use the
`stop_sequences` inference parameter to include
additional strings that will signal the model to stop generating
text.

- **temperature**
  – (Optional) The amount of randomness injected into the response. Use a value closer to 0 for
  analytical / multiple choice, and a value closer to 1 for creative and
  generative tasks.

| Default | Minimum | Maximum |
| ------- | ------- | ------- |
| 1       | 0       | 1       |

- **top_p**
  – (Optional) Use nucleus sampling.

In nucleus sampling, Anthropic Claude computes the cumulative
distribution over all the options for each subsequent token in
decreasing probability order and cuts it off once it reaches a
particular probability specified by `top_p`. You should alter either
`temperature` or `top_p`, but not both.

| Default | Minimum | Maximum |
| ------- | ------- | ------- |
| 1       | 0       | 1       |

- **top_k**
  – (Optional) Only sample from the top K options for each subsequent token.

Use `top_k` to remove long tail low probability responses.

| Default | Minimum | Maximum |
| ------- | ------- | ------- |
| 250     | 0       | 500     |

Response
The Anthropic Claude model returns the following fields
for a Text Completion inference call.

```
{
    "completion": string,
    "stop_reason": string,
    "stop": string
}
```

- **completion** – The resulting
  completion up to and excluding the stop sequences.
- **stop_reason** – The reason why the model stopped generating
  the response.
  - **"stop_sequence"** –
    The model reached a stop sequence — either provided by you
    with the `stop_sequences` inference parameter, or a stop sequence built
    into the model.
  - **"max_tokens"** – The
    model exceeded `max_tokens_to_sample` or the
    model's maximum number of tokens.

- **stop** – If you specify the
  `stop_sequences` inference parameter, `stop`
  contains the stop sequence that signalled the model to stop generating
  text. For example, `holes` in the following response.

```
{
    "completion": " Here is a simple explanation of black ",
    "stop_reason": "stop_sequence",
    "stop": "holes"
}
```

If you don't specify `stop_sequences`, the value for `stop` is empty.

## Code example

These examples shows how to call the _Anthropic Claude V2_ model with on demand
throughput. To use Anthropic Claude version 2.1, change the value of `modelId` to `anthropic.claude-v2:1`.

```
import boto3
import json
brt = boto3.client(service_name='bedrock-runtime')

body = json.dumps({
    "prompt": "\n\nHuman: explain black holes to 8th graders\n\nAssistant:",
    "max_tokens_to_sample": 300,
    "temperature": 0.1,
    "top_p": 0.9,
})

modelId = 'anthropic.claude-v2'
accept = 'application/json'
contentType = 'application/json'

response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())

# text
print(response_body.get('completion'))
```

The following example shows how to generate streaming text with Python
using the prompt
`write an essay for living on mars in 1000
 words` and the
Anthropic Claude V2 model:

```
import boto3
import json

brt = boto3.client(service_name='bedrock-runtime')

body = json.dumps({
    'prompt': '\n\nHuman: write an essay for living on mars in 1000 words\n\nAssistant:',
    'max_tokens_to_sample': 4000
})

response = brt.invoke_model_with_response_stream(
    modelId='anthropic.claude-v2',
    body=body
)

stream = response.get('body')
if stream:
    for event in stream:
        chunk = event.get('chunk')
        if chunk:
            print(json.loads(chunk.get('bytes').decode()))
```
