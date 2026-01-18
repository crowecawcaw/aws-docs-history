# Supervised fine-tuning on Amazon Nova 2.0

## Overview

Amazon Nova 2.0 SFT data uses the same Converse API format as Amazon Nova 1.0, with the addition of optional reasoning content fields. For complete format specifications, see [ReasoningContentBlock](../APIReference/API_runtime_ReasoningContentBlock.md "../APIReference/API_runtime_ReasoningContentBlock.md") and [Converse API schema](conversation-inference-call.md "conversation-inference-call.md").

## Supported features

- **Input types** – Text, image, or video in user content blocks
- **Assistant content** – Text-only responses and reasoning content
- **Dataset composition** – Must be homogeneous. Choose one of the following: text-only turns, text + image turns, or text + video turns

###### Important

You cannot mix images and videos within the same dataset or across different turns.

## Current limitations

- **Tool usage** – Although tool usage is supported in the input format, it is not currently supported by Amazon Nova 2.0 SFT. Adding tool sections might cause your job to fail.
- **Multimodal reasoning content** – Although the Converse format supports image-based reasoning content, this is not supported by Amazon Nova 2.0 SFT.
- **Validation sets** – Providing a validation set might be supported through the UI but will not be supported during SFT training.

## Supported media formats

- **Images** – PNG, JPEG, GIF
- **Videos** – MOV, MKV, MP4

## Data format examples

Text-only
This example shows a basic text-only format compatible with Amazon Nova 1.0.

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
          "text": "What country is right next to Australia?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "The closest country is New Zealand"
        }
      ]
    }
  ]
}
```

Text with reasoning
This example shows text with optional reasoning content for Amazon Nova 2.0.

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
          "text": "What country is right next to Australia?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "reasoningContent": {
            "reasoningText": {
              "text": "I need to use my world knowledge of geography to answer this question"
            }
          }
        },
        {
          "text": "The closest country to Australia is New Zealand, located to the southeast across the Tasman Sea."
        }
      ]
    }
  ]
}
```

###### Note

Currently, only `reasoningText` is supported within `reasoningContent`. Multimodal reasoning content is not yet available.

Image + text
This example shows how to include image input with text.

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are a helpful assistant."
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "image": {
            "format": "jpeg",
            "source": {
              "s3Location": {
                "uri": "s3://your-bucket/your-path/your-image.jpg",
                "bucketOwner": "your-aws-account-id"
              }
            }
          }
        },
        {
          "text": "Which country is highlighted in the image?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "reasoningContent": {
            "reasoningText": {
              "text": "I will determine the highlighted country by examining its location on the map and using my geographical knowledge"
            }
          }
        },
        {
          "text": "The highlighted country is New Zealand"
        }
      ]
    }
  ]
}
```

Video + text
This example shows how to include video input with text.

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are a helpful assistant."
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "video": {
            "format": "mp4",
            "source": {
              "s3Location": {
                "uri": "s3://your-bucket/your-path/your-video.mp4",
                "bucketOwner": "your-aws-account-id"
              }
            }
          }
        },
        {
          "text": "What is shown in this video?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "reasoningContent": {
            "reasoningText": {
              "text": "I will analyze the video content to identify key elements"
            }
          }
        },
        {
          "text": "The video shows a map with New Zealand highlighted"
        }
      ]
    }
  ]
}
```

## Reasoning and non-reasoning modes

**Understanding reasoning content:** Reasoning content (also called chain-of-thought) captures the model's intermediate thinking steps before generating a final answer. In the `assistant` turn, use the `reasoningContent` field to include these reasoning traces.

**How loss is calculated:**

- **With reasoning content** – Training loss includes both reasoning tokens and final output tokens
- **Without reasoning content** – Training loss is calculated only on the final output tokens

You can include `reasoningContent` across multiple assistant turns in multi-turn conversations.

### When to enable reasoning mode

Set `reasoning_enabled: true` in your training configuration when you want the model to generate thinking tokens before producing final outputs or need improved performance on complex reasoning tasks.

###### Note

You can enable reasoning mode regardless of whether your training data contains reasoning content. However, including reasoning traces in your training data is recommended so the model can learn from these examples and improve reasoning quality.

Set `reasoning_enabled: false` when you're training on straightforward tasks that don't benefit from explicit reasoning steps or want to optimize for speed and reduce token usage.

### Formatting guidelines

- Use plain text for reasoning content.
- Avoid markup tags like `<thinking>` and `</thinking>` unless specifically required by your task.
- Ensure reasoning content is clear and relevant to the problem-solving process.

### Generating reasoning data

If your dataset lacks reasoning traces, you can create them using a reasoning-capable model like Nova Premier. Provide your input-output pairs to the model and capture its reasoning process to build a reasoning-augmented dataset.

### Using reasoning tokens for training

When training with reasoning mode enabled, the model learns to separate internal reasoning from the final answer. The training process does the following:

- Organizes data as triples: input, reasoning, and answer
- Optimizes using standard next-token prediction loss from both reasoning and answer tokens
- Encourages the model to reason internally before generating responses

### Effective reasoning content

High-quality reasoning content should include the following:

- Intermediate thoughts and analysis
- Logical deductions and inference steps
- Step-by-step problem-solving approaches
- Explicit connections between steps and conclusions

This helps the model develop the ability to think before answering.

## Dataset preparation guidelines

The following table provides guidelines for preparing your training dataset.

| Dataset preparation guidelines | Guideline                                                                                                                                                                                                                                                            | Description |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **Size and quality**           | • Recommended size: 2,000-10,000 samples<br>• Minimum samples: 200<br>• Prioritize quality over quantity. Ensure examples are accurate and well-annotated.<br>• Dataset should closely reflect your production use cases.                                            |
| **Diversity**                  | Include diverse examples that do the following:<br>• Cover the full range of expected inputs<br>• Represent different difficulty levels<br>• Include edge cases and variations<br>• Prevent overfitting to narrow patterns                                           |
| **Output formatting**          | Clearly specify the desired output format in assistant responses. Examples include JSON structures, tables, CSV format, or custom formats specific to your application.                                                                                              |
| **Multi-turn conversations**   | • Loss is calculated only on assistant turns, not user turns.<br>• Each assistant response should be properly formatted.<br>• Maintain consistency across conversation turns.                                                                                        |
| **Quality checklist**          | • Sufficient dataset size (2,000-10,000 samples)<br>• Diverse examples covering all use cases<br>• Clear, consistent output formatting<br>• Accurate labels and annotations<br>• Representative of production scenarios<br>• Free from contradictions or ambiguities |
