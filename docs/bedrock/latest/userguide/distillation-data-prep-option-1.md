# Option 1: Provide your own prompts for data preparation

Collect your prompts and store them in `.jsonl` file format. Each record in the
JSONL must use the following structure.

- Include the `schemaVersion` field that must have the
  value `bedrock-conversion-2024`.
- [Optional] Include a system prompt that indicates the role
  assigned to the model.
- In `messages` field, include the user role containing
  the input prompt provided to the model.
- [Optional] In the `messages` field, include assistant
  role containing the desired response.
  Anthropic and Meta Llama models support only single-turn
  conversation prompts, meaning you can only have one user prompt. The Amazon Nova models
  support multi-turn conversations, allowing you to provide multiple user and assistant exchanges within
  one record.

**Example format**

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [{
        "text": "A chat between a curious User and an artificial intelligence Bot. The Bot gives helpful, detailed, and polite answers to the User's questions."
    }],
    "messages": [{
            "role": "user",
            "content": [{
                "text": "why is the sky blue"
            }]
        },
        {
            "role": "assistant",
            "content": [{
                "text": "The sky is blue because molecules in the air scatter blue light from the Sun more than other colors."
            }]
        }
    ]
}}
```

## Validate your dataset

Before you run your distillation job, you can validate your input dataset using a [Python script](https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/model_distillation/dataset-validation/README.md "https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/model_distillation/dataset-validation/README.md").
