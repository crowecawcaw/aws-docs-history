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

###### Note

For more information on which container images, or example recipes to use go to [Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md").

###### Topics

- [Reasoning Mode Selection (Nova 2.0
  Only)](#nova-sft-2-reasoning-mode "#nova-sft-2-reasoning-mode")
- [Tool calling data format](#nova-sft-2-tool-calling "#nova-sft-2-tool-calling")
- [Document understanding data
  format](#nova-sft-2-document-understanding "#nova-sft-2-document-understanding")
- [Video Understanding for SFT](#nova-sft-2-video-understanding "#nova-sft-2-video-understanding")
- [Data Upload Instructions](#nova-sft-2-data-upload "#nova-sft-2-data-upload")
- [Creating a Fine-Tuning Job](#nova-sft-2-creating-job "#nova-sft-2-creating-job")
- [SFT Tuning Parameters](#nova-sft-2-tuning-parameters "#nova-sft-2-tuning-parameters")
- [Hyperparameter Guidance](#nova-sft-2-hyperparameters "#nova-sft-2-hyperparameters")
  Below is a sample recipe for SFT. You can find this recipe and others in the [recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova") repository.

```
run:
  name: my-full-rank-sft-run
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://my-bucket-name/train.jsonl  #  only and not compatible with SageMaker Training Jobs
  replicas: 4                                     # Number of compute instances for training, allowed values are 4, 8, 16, 32
  output_s3_path: s3://my-bucket-name/outputs/    # Output artifact path (HyperPod job-specific; not compatible with standard SageMaker Training Jobs)
  mlflow_tracking_uri: ""                         # Required for MLFlow
  mlflow_experiment_name: "my-full-rank-sft-experiment"  # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-full-rank-sft-run"         # Optional for MLFlow. Note: leave this field non-empty

training_config:
  max_steps: 100                    # Maximum training steps. Minimal is 4.
  save_steps: ${oc.select:training_config.max_steps}  # How many training steps the checkpoint will be saved
  save_top_k: 5                     # Keep top K best checkpoints. Note supported only for  jobs. Minimal is 1.
  max_length: 32768                 # Sequence length (options: 8192, 16384, 32768 [default], 65536)
  global_batch_size: 32             # Global batch size (options: 32, 64, 128)
  reasoning_enabled: true           # If data has reasoningContent, set to true; otherwise False

  lr_scheduler:
    warmup_steps: 15                # Learning rate warmup steps. Recommend 15% of max_steps
    min_lr: 1e-6                    # Minimum learning rate, must be between 0.0 and 1.0

  optim_config:                     # Optimizer settings
    lr: 1e-5                        # Learning rate, must be between 0.0 and 1.0
    weight_decay: 0.0               # L2 regularization strength, must be between 0.0 and 1.0
    adam_beta1: 0.9                  # Exponential decay rate for first-moment estimates
    adam_beta2: 0.95                 # Exponential decay rate for second-moment estimates

  peft:                             # Parameter-efficient fine-tuning (LoRA)
    peft_scheme: "null"             # Disable LoRA for PEFT
```

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

###### Note

For more information on which container images, or example recipes to use go to [Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md").

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

###### Note

For more information on which container images, or example recipes to use go to [Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md").

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

###### Note

For more information on which container images, or example recipes to use go to [Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md").

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

###### Note

For more information on which container images, or example recipes to use go to [Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md").

## Data Upload Instructions

Upload training and validation datasets to an S3 bucket. Specify these locations in
the recipe's `run` block:

```
## Run config
run:
  ...
  data_s3_path: "s3://<bucket-name>/<training-directory>/<training-file>.jsonl"

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
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  ...
```

## SFT Tuning Parameters

The parameters that are available for tuning with SFT include:

###### Run Configuration

- **name**: A descriptive name for your training job. This helps identify your job in the AWS Management Console.
- **model_type**: The Amazon Nova model variant to use. The available options are `amazon.nova-2-lite-v1:0:256k`.
- **model_name_or_path**: The path to the base model to use for your training. The available options are `nova-lite-2/prod`, or the S3 path for the post-training checkpoint (`s3://customer-escrow-bucket-unique_id/training_run_name`).
- **replicas**: The number of compute instances to use for distributed training. Available values vary based on the model you choose. Amazon Nova Lite 2.0 supports 4, 8, 16, or 32 replicas.
- **data_s3_path**: The S3 location of the training dataset, which is a JSONL file. This file must reside in the same AWS account and Region as the cluster. All of the S3 locations provided must be in the same account and Region.
- **validation_data_s3_path**: (Optional) The S3 location of the validation dataset, which is a JSONL file. This file must reside in the same account and region as the cluster. All of the S3 locations provided must be in the same account and Region.
- **output_s3_path**: The S3 location where the manifest and TensorBoard logs are stored. All of the S3 locations provided must be in the same AWS account and AWS Region.
- **mlflow_tracking_uri**: The ARN of the MLFlow App to use for MLFlow logging.
- **mlflow_experiment_name**: MLFlow experiment name.
- **mlflow_run_name**: MLFlow run name.

###### Training Configuration

- **max_steps**: The number of training steps to run. Each step will train the model with `global_batch_size` number of elements.
- **save_steps**: The frequency (in steps) at which to save model checkpoints during training.
- **save_top_k**: The maximum number of best checkpoints to retain based on validation metrics.
- **max_length**: The maximum sequence length in tokens. This determines the context window size for training. The maximum supported value is 32768 tokens for SFT.

Longer sequences will improve training efficiencies at the cost of increased memory requirements. We recommend that you match the max_length parameter to your data distribution.

- **global_batch_size**: The total number of training samples processed together in one forward or backward pass across all devices and workers.

This value multiplies the per-device batch size and number of devices. It affects the stability of training and throughput. We recommend that you start with a batch size that fits comfortably within your memory and scale up from there. For domain-specific data, larger batches might over-smooth gradients.

- **reasoning_enabled**: Boolean flag to enable reasoning capabilities during training.

###### Learning Rate Scheduler

- **warmup_steps**: The number of steps to gradually increase learning rate. This improves training stability.
- **min_lr**: The minimum learning rate at the end of decay. Valid values are between 0-1, inclusive, but must be less than learning rate.

###### Optimizer Configuration

- **lr**: The learning rate, which controls the step size during optimization. We recommend values between 1e-6-1e-4 for good performance. Valid values are between 0-1, inclusive.
- **weight_decay**: The L2 regularization strength. Higher values (between 0.01-0.1) increase regularization.
- **adam_beta1**: The exponential decay rate for the first moment estimates in Adam optimizer. Default is 0.9.
- **adam_beta2**: The exponential decay rate for the second moment estimates in Adam optimizer. Default is 0.95.

###### PEFT Configuration

- **peft_scheme**: The parameter-efficient fine-tuning scheme to use. Options are `'null'` for full-rank fine-tuning or `lora` for LoRA-based fine-tuning.

###### LoRA Tuning (when peft_scheme is 'lora')

- **alpha**: The LoRA scaling parameter. Controls the magnitude of the low-rank adaptation. Typical values range from 8 to 128.
- **lora_plus_lr_ratio**: The learning rate ratio for LoRA+ optimization. This multiplier adjusts the learning rate specifically for LoRA parameters.

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
