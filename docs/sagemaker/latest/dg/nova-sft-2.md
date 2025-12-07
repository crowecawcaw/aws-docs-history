# SFT on Nova 2.0

Amazon Nova Lite 2.0 brings enhanced capabilities for supervised fine-tuning, including
advanced reasoning mode, improved multimodal understanding, and extended context handling.
SFT on Nova 2.0 enables you to adapt these powerful capabilities to your specific use cases
while maintaining the model's superior performance on complex tasks.

Key features of SFT on Nova 2.0 include:

- **Reasoning mode support**: Train models to generate
  explicit reasoning traces before final answers for enhanced analytical
  capabilities.
- **Advanced multimodal training**: Fine-tune on document
  understanding (PDF), video understanding, and image-based tasks with improved
  accuracy.
- **Tool calling capabilities**: Train models to
  effectively use external tools and function calling for complex workflows.
- **Extended context support**: Leverage longer context
  windows with better stability and accuracy for document-intensive applications.

###### Topics

- [Reasoning Mode Selection (Nova 2.0
  Only)](#nova-sft-2-reasoning-mode "#nova-sft-2-reasoning-mode")
- [Tool calling data format](#nova-sft-2-tool-calling "#nova-sft-2-tool-calling")
- [Document understanding data
  format](#nova-sft-2-document-understanding "#nova-sft-2-document-understanding")
- [Video Understanding for SFT](#nova-sft-2-video-understanding "#nova-sft-2-video-understanding")
- [Data Upload Instructions](#nova-sft-2-data-upload "#nova-sft-2-data-upload")
- [Creating a Fine-Tuning Job](#nova-sft-2-creating-job "#nova-sft-2-creating-job")
- [Hyperparameter Guidance](#nova-sft-2-hyperparameters "#nova-sft-2-hyperparameters")

###### Topics

- [Reasoning Mode Selection (Nova 2.0
  Only)](#nova-sft-2-reasoning-mode "#nova-sft-2-reasoning-mode")
- [Tool calling data format](#nova-sft-2-tool-calling "#nova-sft-2-tool-calling")
- [Document understanding data
  format](#nova-sft-2-document-understanding "#nova-sft-2-document-understanding")
- [Video Understanding for SFT](#nova-sft-2-video-understanding "#nova-sft-2-video-understanding")
- [Data Upload Instructions](#nova-sft-2-data-upload "#nova-sft-2-data-upload")
- [Creating a Fine-Tuning Job](#nova-sft-2-creating-job "#nova-sft-2-creating-job")
- [Hyperparameter Guidance](#nova-sft-2-hyperparameters "#nova-sft-2-hyperparameters")

## Reasoning Mode Selection (Nova 2.0

Only)

Amazon Nova 2.0 supports reasoning mode for enhanced analytical capabilities:

- **Reasoning Mode (enabled)**:
  - Set `reasoning_enabled: true` in the training configuration
  - Model trains to generate reasoning traces before final answers
  - Improves performance on complex reasoning tasks

- **Non-Reasoning Mode (disabled)**:
  - Set `reasoning_enabled: false` or omit the parameter
    (default)
  - Standard SFT without explicit reasoning
  - Suitable for tasks that don't benefit from step-by-step reasoning

###### Note

- When reasoning is enabled, it operates at high reasoning effort. There is no low
  reasoning option for SFT.
- Multimodal reasoning content is not supported for SFT. Reasoning mode applies to
  text-only inputs.

Training Amazon Nova on a non-reasoning dataset with `reasoning_enabled:
 true` is permitted. However, doing so may cause the model to lose its
reasoning capabilities, as Amazon Nova primarily learns to generate the responses presented
in the data without applying reasoning.

If training Amazon Nova on a non-reasoning dataset but still want to use reasoning
during inference:

1. Disable reasoning during training (`reasoning_enabled:
false`)
2. Enable reasoning later during inference
   While this approach allows reasoning at inference time, it does not guarantee
   improved performance compared to inference without reasoning.

**Best practice:** Enable reasoning for both training
and inference when using reasoning datasets, and disable it for both when using
non-reasoning datasets.

## Tool calling data format

SFT supports training models to use tools (function calling). Below is a sample input
format for tool calling:

**Sample input:**

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are an expert in composing function calls."
    }
  ],
  "toolConfig": {
    "tools": [
      {
        "toolSpec": {
          "name": "getItemCost",
          "description": "Retrieve the cost of an item from the catalog",
          "inputSchema": {
            "json": {
              "type": "object",
              "properties": {
                "item_name": {
                  "type": "string",
                  "description": "The name of the item to retrieve cost for"
                },
                "item_id": {
                  "type": "string",
                  "description": "The ASIN of item to retrieve cost for"
                }
              },
              "required": [
                "item_id"
              ]
            }
          }
        }
      },
      {
        "toolSpec": {
          "name": "getItemAvailability",
          "description": "Retrieve whether an item is available in a given location",
          "inputSchema": {
            "json": {
              "type": "object",
              "properties": {
                "zipcode": {
                  "type": "string",
                  "description": "The zipcode of the location to check in"
                },
                "quantity": {
                  "type": "integer",
                  "description": "The number of items to check availability for"
                },
                "item_id": {
                  "type": "string",
                  "description": "The ASIN of item to check availability for"
                }
              },
              "required": [
                "item_id", "zipcode"
              ]
            }
          }
        }
      }
    ]
  },
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "I need to check whether there are twenty pieces of the following item available. Here is the item ASIN on Amazon: id-123. Please check for the zipcode 94086"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "reasoningContent": {
            "reasoningText": {
              "text": "The user wants to check how many pieces of the item with ASIN id-123 are available in the zipcode 94086"
            }
          }
        },
        {
          "toolUse": {
            "toolUseId": "getItemAvailability_0",
            "name": "getItemAvailability",
            "input": {
              "zipcode": "94086",
              "quantity": 20,
              "item_id": "id-123"
            }
          }
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "toolResult": {
            "toolUseId": "getItemAvailability_0",
            "content": [
              {
                "text": "[{\"name\": \"getItemAvailability\", \"results\": {\"availability\": true}}]"
              }
            ]
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Yes, there are twenty pieces of item id-123 available at 94086. Would you like to place an order or know the total cost?"
        }
      ]
    }
  ]
}
```

Important considerations for tool calling data:

- ToolUse must appear in assistant turns only
- ToolResult must appear in user turns only
- ToolResult should be text or JSON only; other modalities are not currently
  supported for Amazon Nova models
- The inputSchema within the toolSpec must be a valid JSON Schema object
- Each ToolResult must reference a valid toolUseId from a preceding assistant
  ToolUse, with each toolUseId used exactly once per conversation

## Document understanding data

format

SFT supports training models on document understanding tasks. Below is a sample input
format:

**Sample input**

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What are the ways in which a customer can experience issues during checkout on Amazon?"
        },
        {
          "document": {
            "format": "pdf",
            "source": {
              "s3Location": {
                "uri": "s3://my-bucket-name/path/to/documents/customer_service_debugging.pdf",
                "bucketOwner": "123456789012"
              }
            }
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Customers can experience issues with 1. Data entry, 2. Payment methods, 3. Connectivity while placing the order. Which one would you like to dive into?"
        }
      ],
      "reasoning_content": [
        {
          "text": "I need to find the relevant section in the document to answer the question.",
          "type": "text"
        }
      ]
    }
  ]
}
```

Important considerations for document understanding:

- Only PDF files are supported
- Maximum document size is 10 MB
- A sample can contain documents and text, but cannot mix documents with other
  modalities (such as images or video)

## Video Understanding for SFT

SFT supports fine-tuning models for video understanding tasks. Below is a sample input
format:

**Sample input**

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What are the ways in which a customer can experience issues during checkout on Amazon?"
        },
        {
          "video": {
            "format": "mp4",
            "source": {
              "s3Location": {
                "uri": "s3://my-bucket-name/path/to/videos/customer_service_debugging.mp4",
                "bucketOwner": "123456789012"
              }
            }
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Customers can experience issues with 1. Data entry, 2. Payment methods, 3. Connectivity while placing the order. Which one would you like to dive into?"
        }
      ],
      "reasoning_content": [
        {
          "text": "I need to find the relevant section in the video to answer the question.",
          "type": "text"
        }
      ]
    }
  ]
}
```

Important considerations for video understanding:

- Videos can be a maximum of 50 MB
- Videos can be up to 15 minutes long
- Only one video is allowed per sample; multiple videos in the same sample are not
  supported
- A sample can contain video and text, but cannot mix video with other modalities
  (such as images or documents)

## Data Upload Instructions

Upload training and validation datasets to an S3 bucket. Specify these locations in
the recipe's `run` block:

```
## Run config
run:
  ...
  data_s3_path: "s3://<bucket-name>/<training-directory>/<training-file>.jsonl"
  validation_data_s3_path: "s3://<bucket-name>/<validation-directory>/<validation-file>.jsonl"
```

**Note**: Replace `<bucket-name>`,
`<training-directory>`, `<validation-directory>`,
`<training-file>`, and `<validation-file>` with actual
S3 paths.

**Note**: Validation datasets are not currently supported
for SFT with Amazon Nova 2.0. If a validation dataset is provided, it will be ignored.

## Creating a Fine-Tuning Job

Define the base model using the `model_type` and
`model_name_or_path` fields in the `run` block:

```
## Run config
run:
  ...
  model_type: "amazon.nova-lite-v1:0:300k"
  model_name_or_path: "nova-lite-2/prod"
  ...
```

## Hyperparameter Guidance

Use the following recommended hyperparameters based on the training approach:

**Full Rank Training**

- **Epochs**: 1
- **Learning rate (lr)**: 1e-5
- **Minimum learning rate (min_lr)**: 1e-6

**LoRA (Low-Rank Adaptation)**

- **Epochs**: 2
- **Learning rate (lr)**: 5e-5
- **Minimum learning rate (min_lr)**: 1e-6

**Note**: Adjust these values based on dataset size and
validation performance. Monitor training metrics to prevent overfitting.
