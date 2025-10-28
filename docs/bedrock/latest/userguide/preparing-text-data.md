# Prepare data for fine-tuning text-to-text models

###### Note

For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

For fine-tuning text-to-text models, each JSON object is a sample containing structured fields
designed to guide the model toward generating the desired textual output based on a provided textual
prompt. The data format varies depending on the use case, broadly categorized into non-conversational
and conversational use cases. Non-conversational tasks involve standalone prompts and outputs, while
conversational tasks can be further divided into single-turn exchanges, where the model responds to a
single user input, and multi-turn dialogues, where the model maintains context across multiple
exchanges.

**Non-conversational tasks**

Non-conversational tasks involve generating a single output for a given input. Each dataset sample
includes a `prompt` field containing the input text and a `completion` field with
the expected output. This format supports a range of tasks such as question-answering, summarizing,
translation, text completion, and information extraction.

Example format

```
{"prompt": "What is the capital of France?", "completion": "The capital of France is Paris."}
{"prompt": "Summarize the article about climate change.", "completion": "Climate change refers to the long-term alteration of temperature and typical weather patterns in a place."}
```

Use approximately 6 characters per token to estimate the number of tokens for planning dataset
size.

**Converse API format (Single turn and Multi turn)**

To use the Converse API, you call the `Converse` or `ConverseStream` operations
to send messages to a model. To call `Converse`, you require permission for the
`bedrock:InvokeModel` operation. To call `ConverseStream`, you require
permission for the `bedrock:InvokeModelWithResponseStream` operation. For more information,
see [Using the Converse
API](conversation-inference-call.md "conversation-inference-call.md").
For more information about Converse API operations, see [Carry out a conversation with the
Converse API operations](conversation-inference.md "conversation-inference.md")

Example format

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "You are a digital assistant with a friendly personality"
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "What is the capital of Mars?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "Mars does not have a capital. Perhaps it will one day."
                }
            ]
        }
    ]
}
```

**For Anthropic Claude 3 Haiku only: Single-turn conversations**

Single-turn conversational tasks involve isolated exchanges, where the model generates a response
based solely on the current user input without considering prior context. Each dataset sample uses a
messages array, with alternating roles of `user` and `assistant`.

Format

```
{"system": "<system message>","messages":[{"role": "user", "content": "<user query>"},{"role": "assistant", "content": "<expected generated text>"}]}
```

Example

```
{"system": "You are an helpful assistant.","messages":[{"role": "user", "content": "what is AWS"},{"role": "assistant", "content": "it's Amazon Web Services."}]}
```

**For Anthropic Claude 3 Haiku only: Multi-turn conversations**

Multi-turn conversational tasks involve extended dialogues where the model must generate responses
while preserving the context of previous exchanges. This format captures the dynamic nature of
interactive tasks, such as customer support or complex discussions.

Format

```
{"system": "<system message>","messages":[{"role": "user", "content": "<user query 1>"},{"role": "assistant", "content": "<expected generated text 1>"}, {"role": "user", "content": "<user query 2>"},{"role": "assistant", "content": "<expected generated text 2>"}]}
```

Example

```
{"system": "system message","messages":[{"role": "user", "content": "Hello there."},{"role": "assistant", "content": "Hi, how can I help you?"},{"role": "user", "content": "what are LLMs?"},{"role": "assistant", "content": "LLM means large language model."},]}
```
