# Preparing data for distilling understanding models

As a first step, follow the [Text understanding prompting best
practices](prompting-text-understanding.md "prompting-text-understanding.md") and tune your input prompt with Amazon Nova Premier and Amazon Nova Pro to ensure the prompt is optimized to get the best out of the teacher model.

When preparing your input dataset for a distillation job using your own prompts, follow
the recommendations below:

- When only unlabeled prompt data is available, supplement it with a small amount
  (~10) of curated high quality labeled prompt-response pair data to help the model learn
  better. If you submit a small number of high-quality, representative examples, you can
  create a custom model that exceeds the performance of the teacher model.
- When labeled prompt-response pair data is available but has some room for
  improvement, include the responses in the submitted data.
- When labeled prompt-response pair data is available but the labels are of poor
  quality and the training would be better suited to align with the teacher model
  directly, remove all responses before submitting the data.

## Example dataset formats

The following prompts provide examples of how you can provide both labeled and unlabeled prompts for model distillation.

**Distillation using prompts with no labels**

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "A chat between a curious User and an artificial intelligence Bot. The Bot gives helpful, detailed, and polite answers to the User's questions."
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "Why is the sky blue?"
                }
            ]
        }
    ]
}
```

**Distillation using prompts with labels**

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "A chat between a curious User and an artificial intelligence Bot. The Bot gives helpful, detailed, and polite answers to the User's questions."
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "Why is the sky blue?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "The sky is blue because molecules in the air scatter blue light from the Sun more than other colors."
                }
            ]
        }
    ]
}
```

## Dataset constraints

When you perform model distillation, there are a minimum and maximum number of prompts or prompt-response pairs that you must provide.

| Item                  | Minimum | Maximum |
| --------------------- | ------- | ------- |
| Prompts               | 100     | 15K     |
| Prompt-response pairs | 100     | 15K     |
