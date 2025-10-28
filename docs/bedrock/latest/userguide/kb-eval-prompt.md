# Evaluator prompts used in a RAG evaluation job

The same prompts are used for _retrieve-only_ and _retrieve-and-generate_ evaluation jobs. All prompts contain an optional `chat_history` component.
If `conversationTurns` is specified, then `chat_history` is included in the prompt.

Double curly braces `{{}}` are used to indicate where data from your prompt dataset is inserted.

- `{{chat_history}}` – This represents the history of the conversation denoted in `conversationTurns`. For each turn, the next prompt is amended to the `chat_history`.
- `{{prompt}}` – The prompt from your prompt dataset
- `{{ground_truth}}` – The ground truth from your prompt dataset
- `{{prediction}}` – The final output from the LLM in your RAG system

###### Topics

- [Amazon Nova Pro](model-evaluation-type-kb-prompt-kb-nova.md "model-evaluation-type-kb-prompt-kb-nova.md")
- [Anthropic Claude 3.5 Sonnet](model-evaluation-type-kb-prompt-kb-sonnet-35.md "model-evaluation-type-kb-prompt-kb-sonnet-35.md")
- [Anthropic Claude 3.5 Sonnet v2](model-evaluation-type-kb-prompt-kb-sonnet-35v2.md "model-evaluation-type-kb-prompt-kb-sonnet-35v2.md")
- [Anthropic Claude 3.7 Sonnet](model-evaluation-type-kb-prompt-kb-sonnet-37.md "model-evaluation-type-kb-prompt-kb-sonnet-37.md")
- [Anthropic Claude 3 Haiku](model-evaluation-type-kb-haiku.md "model-evaluation-type-kb-haiku.md")
- [Anthropic Claude 3.5 Haiku](model-evaluation-type-kb-haiku35.md "model-evaluation-type-kb-haiku35.md")
- [MetaLlama 3.1 70B Instruct](model-evaluation-type-kb-llama.md "model-evaluation-type-kb-llama.md")
- [Mistral Large 1 (24.02)](model-evaluation-type-kb-prompt-kb-mistral.md "model-evaluation-type-kb-prompt-kb-mistral.md")
