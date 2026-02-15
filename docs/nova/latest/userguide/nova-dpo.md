# Direct preference optimization (DPO)

Direct preference optimization (DPO) is an efficient fine-tuning method for foundation
models that uses paired comparison data to align model outputs with human preferences. This
approach enables direct optimization of model behavior based on human feedback about which
responses are more desirable.

Both full-rank DPO and low-rank adapter (LoRA) DPO are available.

###### Data format requirements

For both full-rank and LoRA DPO, the training data format requirements are similar to
SFT. However, for DPO, the final turn needs to have preference pairs. Here is an example of
the DPO data format:

```
// N-1 turns same as SFT format
{
    "role": "assistant",
    "candidates": [
        {
            "content": [
                {
                    "text": "..."
                } // content list can contain multiple 'text' objects
            ],
            "preferenceLabel": "preferred"
        },
        {
            "content": [
                {
                    "text": "..."
                } // content list can contain multiple 'text' objects
            ],
            "preferenceLabel": "non-preferred"
        }
    ]
}
```

Here is another complete DPO text sample:

```
{
    "system": [
        {
            "text": "..."
        }
    ],
    "messages":[
        {
            "role": "user",
            "content": [
                {
                    "text": "..."
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "..."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "text": "..."
                }
            ]
        },
        {
            "role": "assistant",
            "candidates": [
                {
                    "content": [
                        {
                            "text": "..."
                        }
                    ],
                    "preferenceLabel": "preferred"
                },
                {
                    "content": [
                        {
                            "text": "..."
                        }
                    ],
                    "preferenceLabel": "non-preferred"
                }
            ]
        }
    ],
}
```

Here is a complete DPO image sample:

```
{
    "system": [
        {
            "text": "..."
        }
    ],
    "messages":[
        {
            "role": "user",
            "content": [
                {
                    "text": "..."
                },
                {
                    "text": "..."
                },
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
                } // "content" can have multiple "text" and "image" objects.
                 // max image count is 10
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "..."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "text": "..."
                },
                {
                    "text": "..."
                },
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
                } // "content" can have multiple "text" and "image" objects.
                 // max image count is 10
            ]
        },
        {
            "role": "assistant",
            "candidates": [
                {
                    "content": [
                        {
                            "text": "..."
                        }
                    ],
                    "preferenceLabel": "preferred"
                },
                {
                    "content": [
                        {
                            "text": "..."
                        }
                    ],
                    "preferenceLabel": "non-preferred"
                }
            ]
        }
    ],
}
```

Other constraints on the input datasets apply. For more information, see [Dataset constraints](fine-tune-prepare-data-understanding.md#custom-fine-tune-constraints "fine-tune-prepare-data-understanding.md#custom-fine-tune-constraints"). We recommend that you include a minimum of 1,000 preference
pairs for effective training. High-quality preference data leads to more efficient
results.

We recommend using DPO in the following scenarios:

- Optimizing for subjective outputs that require alignment with specific human
  preferences.
- Adjusting the model’s tone, style, or content characteristics to match desired
  response patterns.
- Making targeted improvements to an existing model based on user feedback and error
  analysis.
- Maintaining consistent output quality across different use cases.
- Implementing safety guardrails through preferred response patterns.
- Training with reward-free reinforcement learning.
- Using only preference data instead of graded or labeled data.
- Improving the model in nuanced alignment tasks, such as helpfulness, harmlessness, or
  honesty.
  The Amazon Nova parameters that are available for full-rank DPO are as follows:

- **Run configuration**
  - `name`: A descriptive name for your training job. This helps
    identify your job in the AWS Management Console.
  - `model_type`: The Nova model variant to use. The available options
    are `amazon.nova-micro-v1:0:128k`,
    `amazon.nova-lite-v1:0:300k`, or
    `amazon.nova-pro-v1:0:300k`.
  - `model_name_or_path`: The path to the base model. Select the model
    to use from `nova-micro/prod`, `nova-lite/prod`,
    `nova-pro/prod`, or the S3 path for the post-training checkpoint
    (`s3://<escrow bucket>/<job
id>/outputs/checkpoints`).
  - `replicas`: The number of compute instances to use for distributed
    training. Available values vary based on the model chosen. Amazon Nova Micro supports 2,
    4, or 8 replicas. Amazon Nova Lite supports 4, 8, 16, or 32 replicas. Amazon Nova Pro supports
    6, 12, or 24 replicas.
  - `data_s3_path`: The S3 location of the training dataset, which is a
    JSONL file. This file must reside in the same account and Region as the cluster.
    All of the S3 locations provided must be in the same account and Region.
  - `validation_data_s3_path`: The S3 location of the validation
    dataset, which is a JSONL file. This file must reside in the same AWS account
    and Region as the cluster. All of the S3 locations provided must be in the same
    account and Region.

- **Training configuration**
  - `max_length`: The maximum sequence length in tokens. This
    determines the context window size for training. The maximum supported value are
    32,768 tokens for DPO.

  Longer sequences will improve training efficiencies at the cost of increased
  memory requirements. We recommend that you match the `max_length`
  parameter to your data distribution.

- **Trainer settings**
  - `max_epochs`: The number of complete passes through your training
    dataset.

  In general, larger datasets require fewer epochs to converge, while smaller
  datasets require more epochs to converge. We recommend that you adjust the number
  of epochs based on the size of your data.

- **Model settings**
  - `hidden_dropout`: The probability of dropping hidden state outputs.
    Increase this value by approximately 0.0-0.2 to reduce overfitting on smaller
    datasets. Valid values are between 0-1, inclusive.
  - `attention_dropout`: The probability of dropping attention weights.
    This parameter can help with generalization. Valid values are between 0-1,
    inclusive.
  - `ffn_dropout`: The probability of dropping feed-forward network
    outputs. Valid values are between 0-1, inclusive.

- **Optimizer configuration**
  - `lr`: The learning rate, which controls the step size during
    optimization. We recommend values between 1e-6-1e-4 for good performance. Valid
    values are between 0-1, inclusive.
  - `name`: The optimizer algorithm. Currently, only
    `distributed_fused_adam` is supported.
  - `weight_decay`: The L2 regularization strength. Higher values
    (between 0.01-0.1) increase regularization.
  - `warmup_steps`: The number of steps to gradually increase learning
    rate. This improves training stability. Valid values are between 1-20,
    inclusive.
  - `min_lr`: The minimum learning rate at the end of decay. Valid
    values are between 0-1, inclusive, but must be less than learning rate.

- **DPO configuration**
  - `beta`: Determines how closely the model should fit the training
    data or the original model. Valid values are between 0.001-0.5, inclusive.

  Specify larger values (for example, 0.5) to preserve more of the reference
  model behavior while more slowly learning new preferences. Specify smaller values
  (for example, 0.01-0.05) to more quickly learn new preferences at the risk of
  diverging from the reference model behavior.

###### Full-rank DPO recipe

The following is a full-rank recipe for DPO

```
## Run config
run:
  name: "my-dpo-micro-job"             # A descriptive name for your training job
  model_type: "amazon.nova-micro-v1:0:128k"  # Model variant specification, do not change
  model_name_or_path: "nova-micro/prod"      # Base model path, do not change
  replicas: 2                     # Number of compute instances for training, allowed values are 2, 4, 8
  data_s3_path: s3:`Replace with your S3 bucket name`/input.jsonl
  validation_data_s3_path: `[OPTIONAL] s3:your S3 bucket name`/input.jsonl
  output_s3_path: `[S3_PATH_TO_STORE_MANIFEST]`

## Training specific configs
training_config:
  max_length: 32768               # Maximum context window size (tokens).
  global_batch_size: 64           # Global batch size, allowed values are 16, 32, 64.

  trainer:
    max_epochs: 2                # Number of training epochs

  model:
    hidden_dropout: 0.0          # Dropout for hidden states, must be between 0.0 and 1.0
    attention_dropout: 0.0       # Dropout for attention weights, must be between 0.0 and 1.0
    ffn_dropout: 0.0             # Dropout for feed-forward networks, must be between 0.0 and 1.0

    optim:
      lr: 1e-5                 # Learning rate
      name: distributed_fused_adam  # Optimizer algorithm, do not change
      adam_w_mode: true        # Enable AdamW mode
      eps: 1e-06               # Epsilon for numerical stability
      weight_decay: 0.0        # L2 regularization strength, must be between 0.0 and 1.0
      betas:                   # Adam optimizer betas, must be between 0.0 and 1.0
        - 0.9
        - 0.999
      sched:
        warmup_steps: 10     # Learning rate warmup steps
        constant_steps: 0    # Steps at constant learning rate
        min_lr: 1e-6         # Minimum learning rate, must be lower than lr

    dpo_cfg:
        beta: 0.1               # Strength of preference enforcement. Limits: [0.001, 0.5]

    peft:
        peft_scheme: null        # Disable LoRA, trigger full rank fine tuning
```

The Amazon Nova parameters that are available for low-rank adapter DPO are as
follows:

- **Run configuration**
  - `name`: A descriptive name for your training job. This helps
    identify your job in the AWS Management Console.
  - `model_type`: The Nova model variant to use. The available options
    are `amazon.nova-micro-v1:0:128k`,
    `amazon.nova-lite-v1:0:300k`, or
    `amazon.nova-pro-v1:0:300k`.
  - `model_name_or_path`: The path to the base model. Select the model
    to use from `nova-micro/prod`, `nova-lite/prod`,
    `nova-pro/prod`, or the S3 path for the post-training checkpoint
    (`s3://<escrow bucket>/<job
id>/outputs/checkpoints`).
  - `replicas`: The number of compute instances to use for distributed
    training. Available values vary based on the model chosen. Amazon Nova Micro supports 2,
    4, or 8 replicas. Amazon Nova Lite supports 4, 8, 16, or 32 replicas. Amazon Nova Pro supports
    6, 12, or 24 replicas.

- **Training configuration**
  - `max_length`: The maximum sequence length in tokens. This
    determines the context window size for training. The maximum supported value are
    32,768 tokens for DPO.

  Longer sequences will improve training efficiencies at the cost of increased
  memory requirements. We recommend that you match the `max_length`
  parameter to your data distribution.

- **Trainer settings**
  - `max_epochs`: The number of complete passes through your training
    dataset.

  In general, larger datasets require fewer epochs to converge, while smaller
  datasets require more epochs to converge. We recommend that you adjust the number
  of epochs based on the size of your data.

- **Model settings**
  - `hidden_dropout`: The probability of dropping hidden state outputs.
    Increase this value by approximately 0.0-0.2 to reduce overfitting on smaller
    datasets. Valid values are between 0-1, inclusive.
  - `attention_dropout`: The probability of dropping attention weights.
    This parameter can help with generalization. Valid values are between 0-1,
    inclusive.
  - `ffn_dropout`: The probability of dropping feed-forward network
    outputs. Valid values are between 0-1, inclusive.

- **Optimizer configuration**
  - `lr`: The learning rate, which controls the step size during
    optimization. We recommend values between 1e-6-1e-4 for good performance. Valid
    values are between 0-1, inclusive.
  - `name`: The optimizer algorithm. Currently, only
    `distributed_fused_adam` is supported.
  - `weight_decay`: The L2 regularization strength. Higher values
    (between 0.01-0.1) increase regularization.
  - `warmup_steps`: The number of steps to gradually increase learning
    rate. This improves training stability. Valid values are between 1-20,
    inclusive.
  - `min_lr`: The minimum learning rate at the end of decay. Valid
    values are between 0-1, inclusive, but must be less than learning rate.

- **DPO configuration**
  - `beta`: Determines how closely the model should fit the training
    data or the original model. Valid values are between 0.001-0.5, inclusive.

  Specify larger values (for example, 0.5) to preserve more of the reference
  model behavior while more slowly learning new preferences. Specify smaller values
  (for example, 0.01-0.05) to more quickly learn new preferences at the risk of
  diverging from the reference model behavior.

- **LoRA configuration parameters**
  - `peft_scheme`: Set to `lora` to enable Low-Rank
    Adaptation, which generates a more efficient, smaller output model. These
    LoRA-specific properties are also available:
    - `alpha`: The scaling factor for LoRA weights. This is typically
      set to same value as `adapter_dim`.
    - `adapter_dropout`: The regularization parameter for the LoRA
      parameters.

###### LoRA DPO recipe

The following is a recipe for LoRA DPO.

```
## Run config
run:
    name: "my-lora-run"             # A descriptive name for your training job
    model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification, do not change
    model_name_or_path: "nova-lite/prod"      # Base model path, do not change
    replicas: 4                     # Number of compute instances for training. All supported values: {4, 8, 16}
    data_s3_path: s3:`Replace with your S3 bucket name`/input.jsonl
    validation_data_s3_path: `[OPTIONAL] s3:your S3 bucket name`/input.jsonl
    output_s3_path: `[S3_PATH_TO_STORE_MANIFEST]`

## Training specific configs
training_config:
    max_length: 16384               # Maximum context window size (tokens). Should be between [1024, 32768] and multiple of 1024.
                                    # Note: Image dataset for DPO has a limit on 20k samples and 16384 max_length
    global_batch_size: 64           # Total samples per step. Limits: {16, 32, 64, 128, 256}

    trainer:
        max_epochs: 2               # Number of training epochs

    model:
        hidden_dropout: 0.0          # Dropout for hidden states. Limits: [0.0, 1.0]
        attention_dropout: 0.0       # Dropout for attention weights. Limits: [0.0, 1.0]
        ffn_dropout: 0.0             # Dropout for feed-forward networks. Limits: [0.0, 1.0]

        optim:
            lr: 1e-5                 # Learning rate
            name: distributed_fused_adam  # Optimizer algorithm, do not change
            adam_w_mode: true        # Enable AdamW mode
            eps: 1e-08               # Epsilon for numerical stability
            weight_decay: 0.01       # L2 regularization strength
            betas:                   # Adam optimizer betas. Limits: [0.0, 1.0]
                - 0.9
                - 0.999
            sched:
                warmup_steps: 10     # Learning rate warmup steps
                constant_steps: 0    # Steps at constant learning rate
                min_lr: 1e-6         # Minimum learning rate

        dpo_cfg:
            beta: 0.01               # Strength of preference enforcement. Limits: [0.001, 0.5]

        peft:
            peft_scheme: "lora"      # Enable LoRA for parameter-efficient fine-tuning
            lora_tuning:
                loraplus_lr_ratio: 20.0  # LoRA+ learning rate scaling factor. Limits: [0.0, 100.0]
                alpha: 64            # Scaling factor for LoRA weights. [32, 64, 96, 128, 160, 192]
                adapter_dropout: 0.01  # Regularization for LoRA parameters. Limits: [0.0, 1.0]
```

###### Limitations

DPO has the following limitations:

- Intermediate checkpoints are not saved for evaluation and you can't resume from an
  intermediate checkpoint. Only the last checkpoint is saved.
- To adjust the hyperparameters, follow the guidance in [Selecting
  hyperparameters](customize-fine-tune-hyperparameters.md "customize-fine-tune-hyperparameters.md").
