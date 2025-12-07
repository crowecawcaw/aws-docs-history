# Fine-tune Nova 1.0

## Prerequisites

Before you start a training job, note the following.

- Amazon S3 buckets to store your input data and output of training jobs. You can
  either use one bucket for both or separate buckets for each type of the
  data. Make sure your buckets are in the same AWS Region where you create
  all the other resources for training. For more information, see [Creating a
  general purpose bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").
- An IAM role with permissions to run a training job. Make sure you attach
  an IAM policy with `AmazonSageMakerFullAccess`. For more
  information, see [How to use SageMaker execution roles](sagemaker-roles.md "sagemaker-roles.md").
- Base Amazon Nova recipes, see [Getting Amazon Nova recipes](nova-model-recipes.md#nova-model-get-recipes "nova-model-recipes.md#nova-model-get-recipes").

## Data preparation

Preparing high-quality, properly formatted data is a critical first step in the
fine-tuning process for large language models. Whether you're using supervised
fine-tuning (SFT) or Direct Preference Optimization (DPO), with either full-rank or
low-rank adaptation (LoRA) approaches, your data must adhere to specific format
requirements to ensure successful model training. This section outlines the
necessary data formats, validation methods, and best practices to help you prepare
your datasets effectively for fine-tuning Amazon Nova models.

**SFT**

SFT data format requirements - For both full-rank SFT and LoRA SFT, data
should follow the Converse format. For examples and constraints of this
format, see [Preparing data for fine-tuning Understanding models](../../../nova/latest/userguide/fine-tune-prepare-data-understanding.md "../../../nova/latest/userguide/fine-tune-prepare-data-understanding.md").

SFT data validation - To validate your dataset format before submission, we
recommend using the following validation script from the [Amazon Bedrock samples repository](https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/bedrock-fine-tuning/nova/understanding/dataset_validation/nova_ft_dataset_validator.py "https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/bedrock-fine-tuning/nova/understanding/dataset_validation/nova_ft_dataset_validator.py"). This validation tool will help ensure
your `jsonl` files adhere to the required format specifications
and identify any potential issues before submitting your fine-tuning
job.

**DPO**

DPO data format requirements - For both DPO in full-rank and DPO with
LoRA, data should follow the Converse format. The dataset also needs to be
in the similar format as SFT except the last turn needs to have preference
pairs.

DPO dataset other constraints - Other constraints on datasets are the same for
SFT. For more information, see [Dataset constraints](../../../nova/latest/userguide/fine-tune-prepare-data-understanding.md "../../../nova/latest/userguide/fine-tune-prepare-data-understanding.md"). A single JSONL file for training and a single
JSONL file for validation is expected. Validation set is optional.

DPO dataset recommendations - A minimum of 1,000 preference pairs for
effective training. High-quality preference data will result in more efficient
results.

**Sample DPO data format**

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

**Sample DPO data format (multi-turn)**

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

**Sample DPO data format (with images)**

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

Training jobs default to a 1-day time limit, though the estimates in the
tables below assume a 5-day training duration for illustration purposes. As
a best practice, we recommend increasing your training time limit to 28 days
maximum to accommodate longer training workloads. To request a limit
increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").

**SFT dataset limits**

| Context length          | Model                                                                                                                                    | Method                                                                                                                                    | Datasets                                                                                                                                  | Description                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 32k context length jobs | Amazon Nova Micro                                                                                                                        | Full rank and LoRA                                                                                                                        | Text only                                                                                                                                 | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>only have up to 100k records. |
| Amazon Nova Lite        | Full rank                                                                                                                                | Text only                                                                                                                                 | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 100k records. |
| Image and video         | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 50k records. |
| LoRA                    | Text only                                                                                                                                | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 100k records. |
| Image and video         | If you use a dataset where all records have 32k context length,<br>and for example, run for 5 epochs, you can have up to<br>90k records. |
| Amazon Nova Pro         | Full rank                                                                                                                                | Text only                                                                                                                                 | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 40k records.  |
| Image and video         | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 30k records. |
| LoRA                    | Text only                                                                                                                                | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 40k records.  |
| Image and video         | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 35k records. |
| 64k context length jobs | Amazon Nova Micro                                                                                                                        | Full rank and LoRA                                                                                                                        | Text only                                                                                                                                 | If you use a dataset where all records have 64k context<br>length, and for example, run for 5 epochs, you can<br>only have up to 50k records.  |
| Amazon Nova Lite        | Full rank                                                                                                                                | Text only                                                                                                                                 | If you use a dataset where all records have 64k context<br>length, and for example, run for 5 epochs, you can<br>have up to 50k records.  |
| Image and video         | If you use a dataset where all records have 64k context<br>length, and for example, run for 5 epochs, you can<br>have up to 30k records. |
| LoRA                    | -                                                                                                                                        | LoRA is not supported at 64k for Nova Lite.                                                                                               |
| Amazon Nova Pro         | Full rank and LoRA                                                                                                                       | Text only                                                                                                                                 | If you use a dataset where all records have 64k context<br>length, and for example, run for 5 epochs, you can<br>have up to 17k records.  |
| Image and video         | If you use a dataset where all records have 64k context length,<br>and for example, run for 5 epochs, you can have up to<br>15k records. |

DPO dataset limits

| Context length          | Model                                                                                                                                                | Method                                                                                                                                         | Datasets                                                                                                                                  | Description                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 16k context length jobs | Amazon Nova Micro                                                                                                                                    | Full rank                                                                                                                                      | Text only                                                                                                                                 | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>only have up to 120k records. |
| LoRA                    | Text only                                                                                                                                            | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>only have up to 125k records. |
| Amazon Nova Lite        | Full rank                                                                                                                                            | Text only                                                                                                                                      | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>have up to 130k records. |
| Image                   | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>complete 20k samples within 2 days  |
| LoRA                    | Text only                                                                                                                                            | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>have up to 140k records.      |
| Image                   | if you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>complete 20k samples within 2 days. |
| Amazon Nova Pro         | Full rank                                                                                                                                            | Text only                                                                                                                                      | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>have up to 45k records.  |
| Image                   | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>complete 20k samples within 4 days  |
| LoRA                    | Text only                                                                                                                                            | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>have up to 55k records.       |
| Image                   | If you use a dataset where all records have 16k context<br>length, and for example, run for 5 epochs, you can<br>complete 20k samples within 4 days  |
| 32k context length jobs | Amazon Nova Micro                                                                                                                                    | Full rank                                                                                                                                      | Text only                                                                                                                                 | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>only have up to 45k records.  |
| LoRA                    | Text only                                                                                                                                            | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>only have up to 50k records.  |
| Amazon Nova Lite        | Full rank                                                                                                                                            | Text only                                                                                                                                      | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 55k records.  |
| Image                   | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 35k records.             |
| LoRA                    | Text only                                                                                                                                            | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 60k records.       |
| Image                   | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 35k records.             |
| Amazon Nova Pro         | Full rank                                                                                                                                            | Text only                                                                                                                                      | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 20k records.  |
| Image                   | If you use a dataset where all records have 64k context<br>length, and for example, run for 5 epochs, you can<br>have up to 16k records.             |
| LoRA                    | Text only                                                                                                                                            | If you use a dataset where all records have 32k context<br>length, and for example, run for 5 epochs, you can<br>have up to 22k records.       |
| Image                   | If you use a dataset where all records have 64k context<br>length, and for example, run for 5 epochs, you can<br>have up to 18k records.             |

By reducing the number of epochs or the context length of your records, you could provide more records.

## Full-rank SFT and LoRA PEFT

configurations

This section covers guidance on recipe configurations for both full-rank
supervised fine-tuning (SFT) and low-rank adaptation parameter-efficient fine-tuning
(LoRA PEFT) approaches. These recipe files serve as the blueprint for your model
customization jobs, allowing you to specify training parameters, hyperparameters,
and other critical settings that determine how your model learns from your data. To
adjust the hyperparameters, follow the guidelines in [Selecting
hyperparameters](../../../nova/latest/userguide/customize-fine-tune-hyperparameters.md "../../../nova/latest/userguide/customize-fine-tune-hyperparameters.md").

### Fine-tuning

configurations (Full-rank SFT and LoRA PEFT)

The only difference between full-rank SFT and LoRA PEFT in terms of recipe is the
LoRA PEFT configuration, which is set to 'null' for full rank and set to
appropriate values if using LoRA PEFT-based fine-tuning. Example recipes are
available in the [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes") GitHub repository. The following tables show
detailed configurations that you might find helpful.

About **"run" configuration**.

|                   | Key                | Definition                                                            | Micro                         | Lite                         | Pro                         |
| ----------------- | ------------------ | --------------------------------------------------------------------- | ----------------------------- | ---------------------------- | --------------------------- |
| Run configuration | model_type         | Specifies the Nova model variant to use. Do not modify this<br>field. | "amazon.nova-micro-v1:0:128k" | "amazon.nova-lite-v1:0:300k" | "amazon.nova-pro-v1:0:300k" |
|                   | model_name_or_path | The path to the base model.                                           | "nova-micro/prod"             | "nova-lite/prod"             | "nova-pro/prod"             |
|                   | replicas           | The number of compute instances to use for distributed<br>training.   | 2, 4 or 8                     | 4, 8 or 16                   | 6, 12 or 24                 |

About **“training_config” configuration**.

|                                | Root key                      | Child keys                                                                                                         | Definition                                                                                                                                                                   | Min      | Max                                           |
| ------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------- |
|                                |                               | max_length                                                                                                         | The maximum sequence length in tokens. This determines the context<br>window size for training. Tunable to nearest 1024<br>multiple, max value: 65536 (for Lite Lora 32768). | 1024     | 65536, except Lite LoRA which supports 32768. |
|                                |                               | global_batch_size                                                                                                  | Total samples per step, allowed values are 16, 32, 64. Max value:<br>32 for Nova Pro, 64 for Nova Lite and Micro.                                                            | 16       | 32 for Nova Pro, 64 for Nova Lite and Micro.  |
| **Trainer configuration**      | trainer                       | max_epochs                                                                                                         | The number of complete passes through your training dataset. For<br>most customization tasks, 1-5 epochs are typically<br>sufficient. Recommended to keep up to 5.           | 1        | -                                             |
| **Model<br>configuration**     | model                         | hidden_dropout                                                                                                     | Probability of dropping hidden state outputs. Increase (0.0-0.2)<br>to reduce overfitting on smaller datasets. The bounds are between 0<br>• 1.                              | 0        | 1                                             |
| model                          | attention_dropout             | Probability of dropping attention weights. Can help with<br>generalization. The bounds are between 0<br>• 1.       | 0                                                                                                                                                                            | 1        |
| model                          | ffn_dropout                   | Probability of dropping feed-forward network outputs. The bounds<br>are between 0<br>• 1.                          | 0                                                                                                                                                                            | 1        |
| **Optimizer<br>configuration** | model.optim                   | lr                                                                                                                 | Learning rate, controls step size during optimization. The limits<br>are between 0 and 1. Typically set between 1e-6 and 1e-4. for good<br>performance.                      | 0        | 1                                             |
| model.optim                    | name                          | Optimizer algorithm. Currently, only<br>`distributed_fused_adam`is supported.                                      | -                                                                                                                                                                            | -        |
| model.optim                    | adam_w_mode                   | Enable AdamW mode (true/false).                                                                                    | -                                                                                                                                                                            | -        |
| model.optim                    | eps                           | Epsilon for numerical stability.                                                                                   |                                                                                                                                                                              |          |
| model.optim                    | weight_decay                  | L2 regularization strength, must be between 0.0 and 1.0.                                                           | 0                                                                                                                                                                            | 1        |
| model.optim                    | betas                         | Adam optimizer betas, must be between 0.0 and 1.0.                                                                 | 0                                                                                                                                                                            | 1        |
| model.optim                    | sched_warmup_steps            | Number of steps to gradually increase learning rate. This improves<br>training stability. Between 1 and 20.        | 1                                                                                                                                                                            | 20       |
| model.optim                    | sched_constant_steps          | Steps at constant learning rate.                                                                                   | 1.00E-10                                                                                                                                                                     | 1.00E-06 |
| model.optim                    | sched.min_lr                  | Minimum learning rate at the end of decay. The limits are between<br>0 and 1, but must be less than learning rate. | 0                                                                                                                                                                            | 1        |
| **LoRA PEFT<br>configuration** | model.peft                    | peft_scheme                                                                                                        | Use "lora" or "null". "lora" uses LoRA PEFT method for<br>parameter-efficient fine-tuning. "null" kicks off a full rank fine<br>tuning.                                      | -        | -                                             |
| model.peft                     | lora_tuning.loraplus_lr_ratio | LoRA+ learning rate scaling factor, must be between 0.0 and<br>100.0.                                              | 0                                                                                                                                                                            | 100      |
| model.peft                     | lora_tuning.alpha             | Scaling factor for LoRA weights. Allowed values are 32, 64, 96,<br>128, 160 and 192.                               | 32                                                                                                                                                                           | 192      |
| model.peft                     | lora_tuning.adapter_dropout   | Regularization for LoRA parameters.Must be between 0.0 and<br>1.0.                                                 | 0                                                                                                                                                                            | 1        |

### Fine-tuning specific

configurations (DPO)

The only difference between Direct Preference Optimization (DPO) as compared to
LoRA PEFT and FullRank SFT is in terms of dpo_cfg configuration and allowed
values. Refer to the table below the example for allowed specifically for
DPO. Example recipes are available in the [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes") GitHub repository. The following table
shows detailed configurations that you might find helpful.

|                                | Root key                      | Child keys                                                                                                         | Definition                                                                                                                                              | Min      | Max   |
| ------------------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----- |
|                                |                               | max_length                                                                                                         | The maximum sequence length in tokens. This determines the context<br>window size for training. Tunable to nearest 1024 multiple, max<br>value: 32,768. | 1024     | 32768 |
|                                |                               | global_batch_size                                                                                                  | Global batch size, allowed values are {16, 32, 64, 128,<br>256}.                                                                                        | 16       | 256   |
| **Trainer configuration**      | trainer                       | max_epochs                                                                                                         | The number of complete passes through your training<br>dataset. For most customization tasks, 1-5 epochs are<br>typically sufficient. Max epochs is 5.  | 1        | 5     |
| **Model<br>configuration**     | model                         | hidden_dropout                                                                                                     | Probability of dropping hidden state outputs. Increase<br>(0.0-0.2) to reduce overfitting on smaller datasets. The<br>bounds are between 0<br>• 1.      | 0        | 1     |
| model                          | attention_dropout             | Probability of dropping attention weights. Can help with<br>generalization. The bounds are between 0<br>• 1.       | 0                                                                                                                                                       | 1        |
| model                          | ffn_dropout                   | Probability of dropping feed-forward network outputs. The bounds<br>are between 0<br>• 1.                          | 0                                                                                                                                                       | 1        |
| **Optimizer<br>configuration** | model.optim                   | lr                                                                                                                 | Learning rate, controls step size during optimization. The limits<br>are between 0 and 1. Typically set between 1e-6 and 1e-4. for good<br>performance. | 0        | 1     |
| model.optim                    | name                          | Optimizer algorithm. Currently, only<br>`distributed_fused_adam` is supported.                                     | -                                                                                                                                                       | -        |
| model.optim                    | adam_w_mode                   | Enable AdamW mode (true/false).                                                                                    | -                                                                                                                                                       | -        |
| model.optim                    | eps                           | Epsilon for numerical stability.                                                                                   | 1.00E-10                                                                                                                                                | 1.00E-06 |
| model.optim                    | weight_decay                  | L2 regularization strength, must be between 0.0 and 1.0.                                                           | 0                                                                                                                                                       | 1        |
| model.optim                    | betas                         | Adam optimizer betas, must be between 0.0 and 1.0.                                                                 | 0                                                                                                                                                       | 1        |
| model.optim                    | sched_warmup_steps            | Number of steps to gradually increase learning rate. This improves<br>training stability. Between 1 and 20.        | 1                                                                                                                                                       | 20       |
| model.optim                    | sched_constant_steps          | Steps at constant learning rate.                                                                                   |                                                                                                                                                         |          |
| model.optim                    | sched.min_lr                  | Minimum learning rate at the end of decay. The limits are between<br>0 and 1, but must be less than learning rate. | 0                                                                                                                                                       | 1        |
| **LoRA PEFT<br>configuration** | model.peft                    | peft_scheme                                                                                                        | Use "lora" or "null". "lora" uses LoRA PEFT method for<br>parameter-efficient fine-tuning. "null" kicks off a full rank fine<br>tuning.                 | -        | -     |
| model.peft                     | lora_tuning.loraplus_lr_ratio | LoRA+ learning rate scaling factor, must be between 0.0 and<br>100.0.                                              | 0                                                                                                                                                       | 100      |
| model.peft                     | lora_tuning.alpha             | Scaling factor for LoRA weights. Allowed values are 32, 64, 96,<br>128, 160 and 192.                               | 32                                                                                                                                                      | 192      |
| model.peft                     | lora_tuning.adapter_dropout   | Regularization for LoRA parameters. Must be between 0.0 and<br>1.0.                                                | 0                                                                                                                                                       | 1        |
| **DPO configuration**          | model-dpo_cfg                 | beta                                                                                                               | Strength of preference enforcement.                                                                                                                     | 0.001    | 0.1   |

## Running customized Nova model on

SageMaker training jobs

This section demonstrates how to run a customized Nova model on SageMaker training jobs
through a Jupyter notebook environment. You'll find a complete example that walks
through the process of configuring and launching a training job, along with
reference tables for selecting the appropriate container image URIs and instance
configurations. This approach gives you programmatic control over your fine-tuning
workflows while leveraging SageMaker's managed infrastructure for model customization.
For more information, see [Use a SageMaker AI estimator to run a training job](docker-containers-adapt-your-own-private-registry-estimator.md "docker-containers-adapt-your-own-private-registry-estimator.md").

### Reference

tables

Before running the sample notebook, refer to the following tables for selecting
the appropriate container image URIs and instance configurations.

**Selecting image URI**

| Recipe        | Image URI                                                                           |
| ------------- | ----------------------------------------------------------------------------------- |
| SFT image URI | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-SFT-latest` |
| DPO image URI | `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-DPO-latest` |

**Selecting instance type and count**

| Model             | Job type                    | Instance type                                           | Recommended instance count | Allowed instance count |
| ----------------- | --------------------------- | ------------------------------------------------------- | -------------------------- | ---------------------- |
| Amazon Nova Micro | Fine-tuning (SFT/DPO, LoRA) | `g5.12xlarge, g6.12xlarge, g5.48xlarge,<br>g6.48xlarge` | 1                          | 1                      |
| Amazon Nova Micro | Fine-tuning (SFT, FFT)      | `g5.48xlarge, g6.48xlarge`                              | 1                          | 1                      |
| Amazon Nova Lite  | Fine-tuning (SFT, LoRA)     | `g5.12xlarge, g6.12xlarge, g5.48xlarge,<br>g6.48xlarge` | 1                          | 1                      |
| Amazon Nova Lite  | Fine-tuning (DPO, LoRA)     | `g5.48xlarge, g6.48xlarge`                              | 1                          | 1                      |
| Amazon Nova Micro | Fine-tuning (SFT)           | `p5.48xlarge, p5en.48xlarge`                            | 2                          | 1,2,4,8                |
| Amazon Nova Lite  | Fine-tuning (SFT)           | `p5.48xlarge, p5en.48xlarge`                            | 4                          | 2,4,8,16               |
| Amazon Nova Pro   | Fine-tuning (SFT)           | `p5.48xlarge, p5en.48xlarge`                            | 6                          | 3,6,12,24              |
| Amazon Nova Micro | Fine-tuning (DPO)           | `p5.48xlarge, p5en.48xlarge`                            | 2                          | 2,4,8                  |
| Amazon Nova Lite  | Fine-tuning (DPO)           | `p5.48xlarge, p5en.48xlarge`                            | 4                          | 4,8,16                 |
| Amazon Nova Pro   | Fine-tuning (DPO)           | `p5.48xlarge, p5en.48xlarge`                            | 6                          | 6,12,24                |

### Sample notebook

The following sample notebook demonstrates how to run a training job. For
additional getting started notebooks on how to customize Nova models using
SageMaker AI training jobs, see [Use a SageMaker AI estimator to run a training job](docker-containers-adapt-your-own-private-registry-estimator.md "docker-containers-adapt-your-own-private-registry-estimator.md").

```
# 1. Install dependencies

!pip install sagemaker==2.254.1

# 2. Import dependencies and initialize sagemaker session

import sagemaker,boto3

sm = boto3.client('sagemaker', region_name='us-east-1')
sagemaker_session = sagemaker.session.Session(boto_session=boto3.session.Session(), sagemaker_client=sm)

# 3. Configure your job
# Define the core configuration for launching a SageMaker Training Job. This includes input/output S3 URIs, container image, hardware setup, and other runtime parameters. Update the placeholders below before submitting the job.

job_name = "<Your Job Name>"

input_s3_uri = "<S3 path to input data>"
validation_s3_uri = "<S3 path to validation data>" # optional, leave blank if no validation data

output_s3_uri = "<S3 path to output location>"

image_uri = "<Image URI from documentation>" # you can choose the image for SFT/DPO
instance_type = "ml.p5.48xlarge" # do not change
instance_count = <Integer number of hosts> # change hosts as needed. Refer to documentation for allowed values based on model type.
role_arn = "<IAM Role you want to use to run the job>"
recipe_path = "<Local path to the recipe file>"

# 4. Launch SageMaker Training Job
# This block sets up and runs the SageMaker training job using the PyTorch estimator. It configures the training image, hardware, input channels, and TensorBoard integration. Validation data is included if provided.

from sagemaker.debugger import TensorBoardOutputConfig
from sagemaker.pytorch import PyTorch
from sagemaker.inputs import TrainingInput

tensorboard_output_config = TensorBoardOutputConfig(
    s3_output_path=output_s3_uri,
)

estimator = PyTorch(
    output_path=output_s3_uri,
    base_job_name=job_name,
    role=role_arn,
    instance_count=instance_count,
    instance_type=instance_type,
    training_recipe=recipe_path,
    sagemaker_session=sagemaker_session,
    image_uri=image_uri,
    tensorboard_output_config=tensorboard_output_config, # Add the setting for using TensorBoard.
    disable_profiler=True,
    debugger_hook_config=False
)

trainingInput = TrainingInput(
    s3_data=input_s3_uri,
    distribution='FullyReplicated',
    s3_data_type='Converse'
)

if (validation_s3_uri):
    validationInput = TrainingInput(
        s3_data=validation_s3_uri,
        distribution='FullyReplicated',
        s3_data_type='Converse'
    )

    estimator.fit(inputs={"train": trainingInput, "validation": validationInput}) # inputs must be called "train" and "validation", do not change
else:
    estimator.fit(inputs={"train": trainingInput})

# 5. Monitor your training job
# To monitor your training job, you can either:
#  * Go to your AWS console -> Amazon Sagemaker AI -> Training -> Training Jobs
#  * run the following command

# sm.describe_training_job(TrainingJobName="<complete training job name>")
```

## Hyperparameter optimization guidance

Fine-tuning your Nova LLM model effectively requires careful selection of
hyperparameters. While this section explains the basic recipe structure and
components, optimizing hyperparameters for your specific use case often requires
additional guidance. For comprehensive recommendations on hyperparameter selection,
best practices, and optimization strategies, see [Selecting
hyperparameters](../../../nova/latest/userguide/customize-fine-tune-hyperparameters.md "../../../nova/latest/userguide/customize-fine-tune-hyperparameters.md"). This resource provides detailed guidance on selecting
appropriate learning rates, batch sizes, training epochs, and other critical
parameters based on your dataset characteristics and training objectives. We
recommend consulting this guide when fine-tuning your recipe configuration to
achieve optimal model performance.

For details about minimum, maximum, and default values for epochs, learning rate,
and learning warmup steps, see [Hyperparameters for Understanding models](../../../nova/latest/userguide/fine-tune-hyperparameters-understanding-models.md "../../../nova/latest/userguide/fine-tune-hyperparameters-understanding-models.md").

**Common recipe modifications**

Here are some common recipe adjustments based on specific use cases:

- **For smaller datasets (< 1,000
  examples)**

```
training_config:
    max_epochs: 2  # More passes through a smaller dataset
model:
    hidden_dropout: 0.1  # Increase regularization
    weight_decay: 0.01   # Increase regularization
```

- **For efficiency with limited
  compute**

```
peft:
    peft_scheme: "lora"
    lora_tuning:
```

- **For complex instruction tuning**

```
optim:
    lr: 5e-6  # Lower learning rate for more stable learning
    sched:
        warmup_steps: 100  # Longer warmup for stability
```
