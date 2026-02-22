# Fine-tune Nova 2.0

## Prerequisites

Before you start a training job, note the following.

- Amazon S3 buckets to store your input data and output of training jobs. You can
  either use one bucket for both or separate buckets for each type of the
  data. Make sure your buckets are in the same AWS Region where you create
  all the other resources for training. For more information, see [Creating a
  general purpose bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").
- An IAM role with permissions to run a training job. Make sure you attach
  an IAM policy with `AmazonSageMakerFullAccess`. For more
  information, see [How to use SageMaker AI execution roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md").
- Base Amazon Nova recipes, see [Getting Amazon Nova recipes](nova-model-recipes.md#nova-model-get-recipes "nova-model-recipes.md#nova-model-get-recipes").

## What is SFT?

Supervised fine-tuning (SFT) trains a language model using labeled input-output pairs. The model learns from demonstration examples consisting of prompts and responses, refining its capabilities to align with specific tasks, instructions, or desired behaviors.

## Data preparation

### Overview

Nova 2.0 SFT data uses the same Converse API format as Nova 1.0, with the addition of optional reasoning content fields. For complete format specifications, see:

- Reasoning content: [ReasoningContentBlock](../../../bedrock/latest/APIReference/API_runtime_ReasoningContentBlock.md "../../../bedrock/latest/APIReference/API_runtime_ReasoningContentBlock.md")
- Converse API schema: [Converse API](../../../bedrock/latest/userguide/conversation-inference-call.md "../../../bedrock/latest/userguide/conversation-inference-call.md")
- Dataset constraints: [Dataset constraints](../userguide/fine-tune-prepare-data-understanding.md "../userguide/fine-tune-prepare-data-understanding.md")

### Supported features

- **Input types** – Text, image, or video in user content blocks
- **Assistant content** – Text-only responses and reasoning content
- **Dataset composition** – Must be homogeneous. Choose one of:
  - Text-only turns
  - Text + image turns
  - Text + video turns (supports document understanding)

###### Important

You cannot mix images and videos within the same dataset or across different turns.

### Current limitations

- **Multimodal reasoning content** – Although the Converse format supports image-based reasoning content, Nova 2.0 SFT supports only text-based reasoning content in the reasoningText field.
- **Validation sets** – You cannot provide a validation dataset for SFT with Nova 2.0. If you provide a validation dataset, it is ignored during training. This limitation applies to both UI-based and programmatic job submissions.

### Supported media formats

- **Images** – PNG, JPEG, GIF
- **Videos** – MOV, MKV, MP4

### Data format examples

Text-only (Nova 1.0 compatible)

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

Text with reasoning (Nova 2.0)

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

Image + text input

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

Video + text input

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

## Tool calling

Nova 2.0 SFT supports training models on tool calling patterns, enabling your model to learn when and how to invoke external tools or functions.

### Data format for tool calling

Tool calling training data includes a `toolConfig` section that defines available tools, along with conversation turns that demonstrate tool usage patterns.

**Sample input**

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

### Tool calling requirements

When creating tool calling training data, follow these requirements:

| Requirement          | Description                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| ToolUse placement    | ToolUse must appear in assistant turns only                                                                                                 |
| ToolResult placement | ToolResult must appear in user turns only                                                                                                   |
| ToolResult format    | ToolResult should be text or JSON only. Other modalities are not supported for Nova models                                                  |
| inputSchema format   | The inputSchema within the toolSpec must be a valid JSON Schema object                                                                      |
| toolUseId matching   | Each ToolResult must reference a valid toolUseId from a preceding assistant ToolUse, with each toolUseId used exactly once per conversation |

### Important notes

- Ensure your tool definitions are consistent across all training samples
- The model learns tool invocation patterns from the demonstrations you provide
- Include diverse examples of when to use each tool and when not to use tools

## Document understanding

Nova 2.0 SFT supports training on document-based tasks, enabling your model to learn how to analyze and respond to questions about PDF documents.

### Data format for document understanding

Document understanding training data includes document references in the user content blocks, with the model learning to extract and reason over document content.

**Sample input**

```
{
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
          "reasoningContent": {
            "reasoningText": {
              "text": "I need to find the relevant section in the document to answer the question."
            }
          }
        },
        {
          "text": "Customers can experience issues with 1. Data entry, 2. Payment methods, 3. Connectivity while placing the order. Which one would you like to dive into?"
        }
      ]
    }
  ]
}
}
```

### Document understanding limitations

| Limitation            | Details                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| Supported format      | PDF files only                                                                                               |
| Maximum document size | 10 MB                                                                                                        |
| Modality mixing       | A sample can have documents and text, but cannot have documents mixed with other modalities (images, videos) |

### Best practices for document understanding

- Ensure documents are clearly formatted and text is extractable
- Provide diverse examples covering different document types and question formats
- Include reasoning content to help the model learn document analysis patterns

## Video understanding

Nova 2.0 SFT supports training on video-based tasks, enabling your model to learn how to analyze and respond to questions about video content.

### Data format for video understanding

Video understanding training data includes video references in the user content blocks, with the model learning to extract information and reason over video content.

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
          "reasoningContent": {
            "reasoningText": {
              "text": "I need to find the relevant section in the video to answer the question."
            }
          }
        },
        {
          "text": "Customers can experience issues with 1. Data entry, 2. Payment methods, 3. Connectivity while placing the order. Which one would you like to dive into?"
        }
      ]
    }
  ]
}
```

### Video understanding limitations

| Limitation             | Details                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| Maximum video size     | 50 MB                                                                                                      |
| Maximum video duration | 15 minutes                                                                                                 |
| Videos per sample      | Only one video is allowed per sample. Multiple videos in the same sample are not supported                 |
| Modality mixing        | A sample can have video and text, but cannot have video combined with other modalities (images, documents) |

### Supported video formats

- MOV
- MKV
- MP4

### Best practices for video understanding

- Keep videos concise and focused on the content relevant to your task
- Ensure video quality is sufficient for the model to extract meaningful information
- Provide clear questions that reference specific aspects of the video content
- Include diverse examples covering different video types and question formats

## Reasoning vs non-reasoning modes

### Understanding reasoning content

Reasoning content (also called chain-of-thought) captures the model's intermediate thinking steps before generating a final answer. In the `assistant` turn, use the `reasoningContent` field to include these reasoning traces.

**How loss is calculated**

- **With reasoning content** – Training loss includes both reasoning tokens and final output tokens
- **Without reasoning content** – Training loss is calculated only on the final output tokens

You can include `reasoningContent` across multiple assistant turns in multi-turn conversations.

**Formatting guidelines**

- Use plain text for reasoning content
- Avoid markup tags like `<thinking>` and `</thinking>` unless specifically required by your task
- Ensure reasoning content is clear and relevant to the problem-solving process

### When to enable reasoning mode

Set `reasoning_enabled: true` in your training configuration when:

- Your training data has reasoning tokens
- You want the model to generate thinking tokens before producing final outputs
- You need improved performance on complex reasoning tasks

Training Nova on a non-reasoning dataset with `reasoning_enabled = true` is permitted. However, doing so may cause the model to lose its reasoning capabilities, as Nova primarily learns to generate the responses presented in the data without applying reasoning. If you want to train Nova on a non-reasoning dataset but still expect reasoning during inference, you can disable reasoning during training (`reasoning_enabled = false`) but enable it for inference. While this approach allows reasoning to be used at inference time, it does not guarantee improved performance compared to inference without reasoning. In general, enable reasoning for both training and inference when using reasoning datasets, and disable it for both when using non-reasoning datasets.

Set `reasoning_enabled: false` when:

- Your training data does not have reasoning tokens
- You're training on straightforward tasks that don't benefit from explicit reasoning steps
- You want to optimize for speed and reduce token usage

### Generating reasoning data

If your dataset lacks reasoning traces, you can create them using a reasoning-capable model like Nova Premier. Provide your input-output pairs to the model and capture its reasoning process to build a reasoning-augmented dataset.

### Using reasoning tokens for training

When training with reasoning mode enabled, the model learns to separate internal reasoning from the final answer. The training process:

- Organizes data as triples: input, reasoning, and answer
- Optimizes using standard next-token prediction loss from both reasoning and answer tokens
- Encourages the model to reason internally before generating responses

### Effective reasoning content

High-quality reasoning content should include:

- Intermediate thoughts and analysis
- Logical deductions and inference steps
- Step-by-step problem-solving approaches
- Explicit connections between steps and conclusions

This helps the model develop the ability to "think before answering."

## Dataset preparation guidelines

### Size and quality

- **Recommended size** – 2,000-10,000 samples
- **Minimum samples** – 200
- **Priority** – Quality over quantity. Ensure examples are accurate and well-annotated
- **Application alignment** – Dataset should closely reflect your production use cases

### Diversity

Include diverse examples that:

- Cover the full range of expected inputs
- Represent different difficulty levels
- Include edge cases and variations
- Prevent overfitting to narrow patterns

### Output formatting

Clearly specify the desired output format in assistant responses:

- JSON structures
- Tables
- CSV format
- Custom formats specific to your application

### Multi-turn conversations

For multi-turn datasets, remember:

- Loss is calculated only on assistant turns, not user turns
- Each assistant response should be properly formatted
- Maintain consistency across conversation turns

### Quality checklist

- Sufficient dataset size (2K-10K samples)
- Diverse examples covering all use cases
- Clear, consistent output formatting
- Accurate labels and annotations
- Representative of production scenarios
- Free from contradictions or ambiguities

### Uploading your data

Datasets should be uploaded to a bucket that can be accessed by SageMaker training jobs. For information about setting the right permissions, see [Prerequisites](../../../sagemaker/latest/dg/nova-model-general-prerequisites.md "../../../sagemaker/latest/dg/nova-model-general-prerequisites.md").

## Starting a training job

### Selecting hyperparameters and updating the recipe

The setup for Nova 2.0 is largely the same as for Nova 1.0. Once the input data has been uploaded to S3, use the recipe from [SageMaker HyperPod Recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova") under Fine tuning folder. For Nova 2.0, the following are some of the key hyperparameters that you can update based on the use case. The following is an example of the Nova 2.0 SFT PEFT recipe. For the container image URI, use `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-V2-latest` to run an SFT fine-tuning job.

Please use v2.254.1 of SageMaker AI PySDK for strict compatibility with Nova
training. Upgrading the SDK to v3.0 version will result in breaking changes. Support
for v3 of SageMaker AI PySDK is coming soon.

**Sample Input**

```
!pip install sagemaker==2.254.1
```

```
run:
  name: {peft_recipe_job_name}
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: {peft_model_name_or_path}
  data_s3_path: {train_dataset_s3_path} # SageMaker HyperPod (SMHP) only and not compatible with SageMaker Training jobs. Note replace my-bucket-name with your real bucket name for SMHP job
  replicas: 4                      # Number of compute instances for training, allowed values are 4, 8, 16, 32
  output_s3_path: ""               # Output artifact path (Hyperpod job-specific; not compatible with standard SageMaker Training jobs). Note replace my-bucket-name with your real bucket name for SMHP job

training_config:
  max_steps: 10                   # Maximum training steps. Minimal is 4.
  save_steps: 10                      # How many training steps the checkpoint will be saved. Should be less than or equal to max_steps
  save_top_k: 1                    # Keep top K best checkpoints. Note supported only for SageMaker HyperPod jobs. Minimal is 1.
  max_length: 32768                # Sequence length (options: 8192, 16384, 32768 [default], 65536)
  global_batch_size: 32            # Global batch size (options: 32, 64, 128)
  reasoning_enabled: true          # If data has reasoningContent, set to true; otherwise False

  lr_scheduler:
    warmup_steps: 15               # Learning rate warmup steps. Recommend 15% of max_steps
    min_lr: 1e-6                   # Minimum learning rate, must be between 0.0 and 1.0

  optim_config:                    # Optimizer settings
    lr: 1e-5                       # Learning rate, must be between 0.0 and 1.0
    weight_decay: 0.0              # L2 regularization strength, must be between 0.0 and 1.0
    adam_beta1: 0.9                # Exponential decay rate for first-moment estimates, must be between 0.0 and 1.0
    adam_beta2: 0.95               # Exponential decay rate for second-moment estimates, must be between 0.0 and 1.0

  peft:                            # Parameter-efficient fine-tuning (LoRA)
    peft_scheme: "lora"            # Enable LoRA for PEFT
    lora_tuning:
      alpha: 64                    # Scaling factor for LoRA weights ( options: 32, 64, 96, 128, 160, 192),
      lora_plus_lr_ratio: 64.0
```

The recipe also contains largely the same hyperparameters as Nova 1.0. The notable hyperparameters are:

- `max_steps` – The number of steps you want to run the job for. Generally, for one epoch (one run through your entire dataset), the number of steps = number of data samples / global batch size. The larger the number of steps and the smaller your global batch size, the longer the job will take to run.
- `reasoning_enabled` – Controls reasoning mode for your dataset. Options:

      + `true`: Enables reasoning mode (equivalent to high reasoning)
      + `false`: Disables reasoning mode

  Note: For SFT, there is no granular control over reasoning effort levels. Setting `reasoning_enabled: true` enables full reasoning capability.

- `peft.peft_scheme` – Setting this to "lora" enables PEFT-based fine tuning. Setting it to null (no quotes) enables Full-Rank fine tuning.

### Start the training job

```
from sagemaker.pytorch import PyTorch

# define OutputDataConfig path
if default_prefix:
    output_path = f"s3://{bucket_name}/{default_prefix}/{sm_training_job_name}"
else:
    output_path = f"s3://{bucket_name}/{sm_training_job_name}"

output_kms_key = "<KMS key arn to encrypt trained model in Amazon-owned S3 bucket>" # optional, leave blank for Amazon managed encryption

recipe_overrides = {
    "run": {
        "replicas": instance_count,  # Required
        "output_s3_path": output_path
    },
}

estimator = PyTorch(
    output_path=output_path,
    base_job_name=sm_training_job_name,
    role=role,
    disable_profiler=True,
    debugger_hook_config=False,
    instance_count=instance_count,
    instance_type=instance_type,
    training_recipe=training_recipe,
    recipe_overrides=recipe_overrides,
    max_run=432000,
    sagemaker_session=sagemaker_session,
    image_uri=image_uri,
    output_kms_key=output_kms_key,
    tags=[
        {'Key': 'model_name_or_path', 'Value': model_name_or_path},
    ]
)

print(f"\nsm_training_job_name:\n{sm_training_job_name}\n")
print(f"output_path:\n{output_path}")
```

```
from sagemaker.inputs import TrainingInput

train_input = TrainingInput(
    s3_data=train_dataset_s3_path,
    distribution="FullyReplicated",
    s3_data_type="Converse",
)

estimator.fit(inputs={"validation": val_input}, wait=False)
```

###### Note

Passing a validation dataset is not supported for supervised fine tuning of Nova 2.0.

To kick off the job:

- Update the recipe with your dataset paths and hyperparameters
- Execute the specified cells in the notebook to submit the training job

The notebook handles job submission and provides status tracking.
