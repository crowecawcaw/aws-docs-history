# Direct Preference Optimization (DPO)

## Overview

Direct Preference Optimization (DPO) is an alignment technique that fine-tunes
foundation models using paired comparison data to align model outputs with human
preferences. Unlike reinforcement learning methods, DPO directly optimizes model
behavior based on human feedback about which responses are more desirable, offering
a more stable and scalable approach.

**Why use DPO**

Foundation models may generate outputs that are factually correct but fail to align
with specific user needs, organizational values, or safety requirements. DPO addresses
this by enabling you to:

- Fine-tune models toward desired behavior patterns
- Reduce unwanted or harmful outputs
- Align model responses with brand voice and communication guidelines
- Improve response quality based on domain expert feedback
- Implement safety guardrails through preferred response patterns

**How DPO works**

DPO uses paired examples where human evaluators indicate which of two possible
responses is preferred. The model learns to maximize the likelihood of generating
preferred responses while minimizing undesired ones.

**When to use DPO**

Use DPO in the following scenarios:

- Optimizing for subjective outputs that require alignment with specific human preferences
- Adjusting the model's tone, style, or content characteristics
- Making targeted improvements based on user feedback and error analysis
- Maintaining consistent output quality across different use cases
- Training with reward-free reinforcement learning using only preference data

## Supported models and techniques

DPO supports both full-parameter fine-tuning and LoRA (Low-Rank Adaptation):

| Model             | Supported inputs | Instance type  | Recommended instance count | Allowed instance count |
| ----------------- | ---------------- | -------------- | -------------------------- | ---------------------- |
| Amazon Nova Micro | Text             | ml.p5.48xlarge | 2                          | 2, 4, 8                |
| Amazon Nova Lite  | Text, image      | ml.p5.48xlarge | 4                          | 2, 4, 8, 16            |
| Amazon Nova Pro   | Text, image      | ml.p5.48xlarge | 6                          | 6, 12, 24              |

**Training approaches**

- **Full-rank DPO**: Updates all model
  parameters. Potentially delivers better alignment quality but requires more compute
  resources and produces larger models.
- **LoRA DPO**: Uses lightweight adapters
  for parameter-efficient fine-tuning. Offers more efficient training and deployment
  with smaller output models while maintaining good alignment quality.

For most use cases, the LoRA approach provides sufficient adaptation capability with
significantly improved efficiency.

## Data format

DPO training data follows the same format as SFT, except the last assistant turn
must contain preference pairs with `preferred` and
`non-preferred` labels.

### Basic structure

The final assistant turn uses a `candidates` array instead of
`content`:

```
{
  "role": "assistant",
  "candidates": [
    {
      "content": [
        {
          "text": "This is the preferred response."
        }
      ],
      "preferenceLabel": "preferred"
    },
    {
      "content": [
        {
          "text": "This is the non-preferred response."
        }
      ],
      "preferenceLabel": "non-preferred"
    }
  ]
}
```

### Complete text example

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
          "text": "What is the capital of France?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "The capital of France is Paris."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "text": "Tell me more about it."
        }
      ]
    },
    {
      "role": "assistant",
      "candidates": [
        {
          "content": [
            {
              "text": "Paris is the capital and largest city of France, known for the Eiffel Tower, world-class museums like the Louvre, and its rich cultural heritage."
            }
          ],
          "preferenceLabel": "preferred"
        },
        {
          "content": [
            {
              "text": "Paris is a city in France."
            }
          ],
          "preferenceLabel": "non-preferred"
        }
      ]
    }
  ]
}
```

### Example with images

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
          "text": "Describe this image."
        },
        {
          "image": {
            "format": "jpeg",
            "source": {
              "s3Location": {
                "uri": "s3://`your-bucket`/`your-path`/image.jpg",
                "bucketOwner": "`your-aws-account-id`"
              }
            }
          }
        }
      ]
    },
    {
      "role": "assistant",
      "candidates": [
        {
          "content": [
            {
              "text": "The image shows a detailed description with relevant context and observations."
            }
          ],
          "preferenceLabel": "preferred"
        },
        {
          "content": [
            {
              "text": "This is a picture."
            }
          ],
          "preferenceLabel": "non-preferred"
        }
      ]
    }
  ]
}
```

### Dataset requirements

- **Format**: Single JSONL file for
  training, single JSONL file for validation (optional)
- **Minimum size**: 1,000 preference
  pairs recommended for effective training
- **Quality**: High-quality preference
  data produces more effective results
- **Other constraints**: Same as SFT.
  For more information, see Dataset constraints.

**Uploading data**

```
aws s3 cp /path/to/training-data/ s3://`your-bucket`/train/ --recursive
aws s3 cp /path/to/validation-data/ s3://`your-bucket`/val/ --recursive
```

## Recipe configuration

### General run configuration

```
run:
  name: "my-dpo-run"
  model_type: "amazon.nova-lite-v1:0:300k"
  model_name_or_path: "nova-lite/prod"
  replicas: 4
```

| Parameter            | Description                                          |
| -------------------- | ---------------------------------------------------- |
| `name`               | Descriptive name for your training job               |
| `model_type`         | Nova model variant (do not modify)                   |
| `model_name_or_path` | Base model path (do not modify)                      |
| `replicas`           | Number of compute instances for distributed training |

### Training configuration

```
training_config:
  max_length: 16384
  global_batch_size: 32

  trainer:
    max_epochs: 3

  model:
    hidden_dropout: 0.0
    attention_dropout: 0.0
    ffn_dropout: 0.0
```

| Parameter           | Description                       | Range                                            |
| ------------------- | --------------------------------- | ------------------------------------------------ |
| `max_length`        | Maximum sequence length in tokens | 1024–32768                                       |
| `global_batch_size` | Samples per optimizer step        | Micro/Lite/Pro: 16, 32, 64, 128. Micro/Lite: 256 |
| `max_epochs`        | Training passes through dataset   | Min: 1                                           |
| `hidden_dropout`    | Dropout for hidden states         | 0.0–1.0                                          |
| `attention_dropout` | Dropout for attention weights     | 0.0–1.0                                          |
| `ffn_dropout`       | Dropout for feed-forward layers   | 0.0–1.0                                          |

### Optimizer configuration

```
model:
  optim:
    lr: 1e-5
    name: distributed_fused_adam
    adam_w_mode: true
    eps: 1e-08
    weight_decay: 0.0
    betas:
      - 0.9
      - 0.999
    sched:
      warmup_steps: 10
      constant_steps: 0
      min_lr: 1e-6
```

| Parameter      | Description                               | Range                        |
| -------------- | ----------------------------------------- | ---------------------------- |
| `lr`           | Learning rate                             | 0–1 (typically 1e-6 to 1e-4) |
| `weight_decay` | L2 regularization strength                | 0.0–1.0                      |
| `warmup_steps` | Steps to gradually increase learning rate | 0–20                         |
| `min_lr`       | Minimum learning rate at end of decay     | 0–1 (must be < lr)           |

### DPO-specific configuration

```
model:
  dpo_cfg:
    beta: 0.1
```

| Parameter | Description                                                                  | Range     |
| --------- | ---------------------------------------------------------------------------- | --------- |
| `beta`    | Balance between fitting training data and staying close to<br>original model | 0.001–0.5 |

- **Higher beta (0.1)**: Preserves more
  reference model behavior but may learn preferences more slowly
- **Lower beta (0.01–0.05)**: More
  aggressive preference learning but risks divergence from reference

**Recommendation**: Start with
`beta: 0.1` and adjust downward if preference learning seems
insufficient.

### LoRA PEFT configuration

```
model:
  peft:
    peft_scheme: "lora"
    lora_tuning:
      loraplus_lr_ratio: 64.0
      alpha: 32
      adapter_dropout: 0.01
```

| Parameter           | Description                        | Allowed values                 |
| ------------------- | ---------------------------------- | ------------------------------ |
| `peft_scheme`       | Fine-tuning method                 | `"lora"` or `null` (full-rank) |
| `alpha`             | Scaling factor for LoRA weights    | 32, 64, 96, 128, 160, 192      |
| `loraplus_lr_ratio` | LoRA+ learning rate scaling factor | 0.0–100.0                      |
| `adapter_dropout`   | Regularization for LoRA parameters | 0.0–1.0                        |

## Starting a training job

**Container image**

```
708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest
```

**Example code**

```
from sagemaker.pytorch import PyTorch
from sagemaker.inputs import TrainingInput

instance_type = "ml.p5.48xlarge"
instance_count = 4

image_uri = "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest"

recipe_overrides = {
    "training_config": {
        "trainer": {"max_epochs": 2},
        "model": {
            "dpo_cfg": {"beta": 0.1},
            "peft": {
                "peft_scheme": "lora",
                "lora_tuning": {
                    "loraplus_lr_ratio": 64.0,
                    "alpha": 32,
                    "adapter_dropout": 0.01,
                },
            },
        },
    },
}

estimator = PyTorch(
    output_path=f"s3://{bucket_name}/{job_name}",
    base_job_name=job_name,
    role=role,
    instance_count=instance_count,
    instance_type=instance_type,
    training_recipe="fine-tuning/nova/nova_lite_p5_gpu_lora_dpo",
    recipe_overrides=recipe_overrides,
    max_run=18000,
    sagemaker_session=sagemaker_session,
    image_uri=image_uri,
    disable_profiler=True,
    debugger_hook_config=False,
)

train_input = TrainingInput(
    s3_data=train_dataset_s3_path,
    distribution="FullyReplicated",
    s3_data_type="Converse",
)

val_input = TrainingInput(
    s3_data=val_dataset_s3_path,
    distribution="FullyReplicated",
    s3_data_type="Converse",
)

estimator.fit(inputs={"train": train_input, "validation": val_input}, wait=True)
```

## Deploying the model

After training completes, deploy the customized model to Amazon Bedrock using the Custom Model
Import functionality. The model supports both provisioned throughput and on-demand
inference. LoRA-trained models support on-demand inference.

For deployment instructions, see [Deploying
customized models](deploy-custom-model.md "deploy-custom-model.md").

## Limitations

- **Input modalities**: DPO accepts text
  and images only. Video input is not supported.
- **Output modality**: Text
  only
- **Preference pairs**: The final assistant
  turn must contain exactly two candidates with `preferred` and
  `non-preferred` labels
- **Image limit**: Maximum 10 images per
  content block
- **Mixed modalities**: Cannot combine text,
  image, and video in the same training job
