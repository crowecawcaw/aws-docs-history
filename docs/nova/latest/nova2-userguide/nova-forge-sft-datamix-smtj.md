# Data mixing on SageMaker Training Jobs

With Amazon Nova Forge data mixing, you can combine your custom training data with Amazon Nova's
proprietary training data during supervised fine-tuning (SFT). This helps preserve the
model's general capabilities while specializing it to your target domain.

###### Note

Data mixing on SageMaker Training Jobs (serverless) is currently supported for
Nova 2 Lite text-only SFT, with both LoRA and full-rank fine-tuning.

## Prerequisites

- Amazon Nova Forge subscription. Contact your AWS point of contact for access.
- An IAM execution role with `AmazonSageMakerFullAccess` and
  permissions to access Amazon Nova Forge Amazon S3 buckets and your training data bucket.
  The execution role must have Amazon S3 read access to the Amazon Nova Forge subscription
  buckets so that the service can validate your subscription status. For the
  required IAM policy, see [IAM policy requirements for Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md").
- Training data uploaded to Amazon S3 in Converse API format. For data format
  details, see [Preparing training data for Nova 2.0](nova-sft-2-smtj.md#nova-2-data-preparation "nova-sft-2-smtj.md#nova-2-data-preparation").
- A model package group ARN in your account.
- A base model ARN from the SageMaker AI Hub.
- (Optional) The SageMaker Python SDK installed. For
  installation instructions, see [Installation](nova-forge-sdk.md#nova-forge-sdk-installation "nova-forge-sdk.md#nova-forge-sdk-installation").

## Hyperparameters

When using the API or CLI directly, all hyperparameter values must be passed as
strings. The SDKs handle type conversion internally. Data mixing is enabled by including
the `customer_data_percent` hyperparameter.

### Data mixing parameter

| Parameter               | Type           | Description                                                                                                                      |
| ----------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `customer_data_percent` | String (0–100) | Percentage of the overall training mix drawn from your data.<br>The remainder comes from Amazon Nova's curated training<br>data. |

Setting `customer_data_percent` to `"50"` means 50% of
training samples come from your JSONL file and 50% from Amazon Nova. Set to
`"100"` to disable mixing (customer data only). Set to
`"0"` for Amazon Nova data only.

You can also control the distribution of Amazon Nova data across categories by
passing individual `nova_<category>_percent` hyperparameters.
When provided, the `nova_*_percent` values must sum to 100.
If you omit them, the default distribution is used.

###### Important

When you customize category percentages, you must specify values for
_all 23 categories_ and they must sum to 100.
Set unused categories to `"0"` explicitly.

**Example: default category distribution**

```
{
  "customer_data_percent": "50",
  "nova_agents_percent": "1",
  "nova_baseline_percent": "10",
  "nova_chat_percent": "0.5",
  "nova_code_percent": "10",
  "nova_factuality_percent": "0.1",
  "nova_identity_percent": "1",
  "nova_long-context_percent": "1",
  "nova_math_percent": "2",
  "nova_rai_percent": "1",
  "nova_instruction-following_percent": "13",
  "nova_stem_percent": "0.5",
  "nova_planning_percent": "10",
  "nova_reasoning-chat_percent": "0.5",
  "nova_reasoning-code_percent": "0.5",
  "nova_reasoning-factuality_percent": "0.5",
  "nova_reasoning-instruction-following_percent": "45",
  "nova_reasoning-math_percent": "0.5",
  "nova_reasoning-planning_percent": "0.5",
  "nova_reasoning-rag_percent": "0.4",
  "nova_reasoning-rai_percent": "0.5",
  "nova_reasoning-stem_percent": "0.4",
  "nova_rag_percent": "1",
  "nova_translation_percent": "0.1",
  "max_steps": "100",
  "global_batch_size": "32"
}
```

The following table lists all available category hyperparameters.

| Hyperparameter                                 | Description                                 |
| ---------------------------------------------- | ------------------------------------------- |
| `nova_agents_percent`                          | Agentic reasoning and task completion       |
| `nova_baseline_percent`                        | General language comprehension              |
| `nova_chat_percent`                            | Conversational fluency                      |
| `nova_code_percent`                            | Code generation and understanding           |
| `nova_factuality_percent`                      | Factual accuracy and verification           |
| `nova_identity_percent`                        | Consistent identity and persona             |
| `nova_instruction-following_percent`           | Instruction following                       |
| `nova_long-context_percent`                    | Long-context comprehension                  |
| `nova_math_percent`                            | Mathematics                                 |
| `nova_planning_percent`                        | Planning and task decomposition             |
| `nova_rag_percent`                             | Retrieval-augmented generation              |
| `nova_rai_percent`                             | Responsible AI alignment                    |
| `nova_stem_percent`                            | STEM                                        |
| `nova_translation_percent`                     | Multilingual comprehension and fluency      |
| `nova_reasoning-chat_percent`                  | Conversational reasoning                    |
| `nova_reasoning-code_percent`                  | Code reasoning                              |
| `nova_reasoning-factuality_percent`            | Factual reasoning and verification          |
| `nova_reasoning-instruction-following_percent` | Reasoning for complex instruction following |
| `nova_reasoning-math_percent`                  | Mathematical reasoning                      |
| `nova_reasoning-planning_percent`              | Reasoning for planning and strategy         |
| `nova_reasoning-rag_percent`                   | Reasoning with retrieved context            |
| `nova_reasoning-rai_percent`                   | Responsible AI reasoning                    |
| `nova_reasoning-stem_percent`                  | STEM reasoning                              |

###### Note

If you provide any `nova_*_percent` hyperparameters, you must
specify all 23 categories with values that sum to 100. If you don't provide any
`nova_*_percent` hyperparameters, the default distribution is
used.

### Training parameters

The following parameters apply to both LoRA and full-rank fine-tuning unless noted.

| Parameter                 | Type    | Default                         | Description                                                                                                                         |
| ------------------------- | ------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `max_steps`               | Integer | `10` (LoRA) / `100` (full-rank) | Number of training steps.                                                                                                           |
| `global_batch_size`       | Integer | `32`                            | Batch size. Options: 32, 64, 128, 256, 512, 1024.                                                                                   |
| `learning_rate`           | Float   | `1e-05`                         | Learning rate.                                                                                                                      |
| `warmup_steps`            | Integer | `15`                            | Learning rate warmup steps.                                                                                                         |
| `min_lr`                  | Float   | `1e-06`                         | Minimum learning rate for the scheduler.                                                                                            |
| `weight_decay`            | Float   | `0.0`                           | L2 regularization strength.                                                                                                         |
| `save_steps`              | Integer | `10` (LoRA) / `100` (full-rank) | How often to save checkpoints in training steps.<br>Must be an even number.                                                         |
| `max_context_length`      | Integer | `32768`                         | Maximum sequence length in tokens.                                                                                                  |
| `reasoning_enabled`       | Boolean | `true`                          | Enable reasoning mode. Set `true` if your data<br>contains `reasoningContent` fields,<br>`false` otherwise.                         |
| `validation_data_s3_path` | String  | –                               | Optional Amazon S3 path to a validation JSONL file. When provided,<br>validation loss is computed at `val_check_interval`<br>steps. |
| `val_check_interval`      | Integer | –                               | Run validation every N training steps.<br>Only applies when `validation_data_s3_path` is provided.                                  |
| `fine_tuned_model`        | Float   | `1.0`                           | Weight of the fine-tuned checkpoint in model merge<br>Set to `1.0` to disable model merging.                                        |

### LoRA parameters

| Parameter             | Type    | Default | Description                                                    |
| --------------------- | ------- | ------- | -------------------------------------------------------------- |
| `alpha`               | Integer | `64`    | LoRA alpha scaling factor. Options: 32, 64, 96, 128, 160, 192. |
| `learning_rate_ratio` | Float   | `64.0`  | LoRA+ learning rate scaling factor                             |

## Using the SageMaker Python SDK

You can submit serverless SFT jobs with data mixing using the SageMaker Python SDK
`SFTTrainer` class with `DataMixingConfig`. For installation
instructions, see [Installation](nova-forge-sdk.md#nova-forge-sdk-installation "nova-forge-sdk.md#nova-forge-sdk-installation").

```
from sagemaker.train import SFTTrainer
from sagemaker.train.data_mixing_config import DataMixingConfig

data_mixing = DataMixingConfig(
    customer_data_percent=50.0,
    nova_data_percentages={
        "agents": 60.0,
        "chat": 40.0,
    },
)

trainer = SFTTrainer(
    model="nova-textgeneration-lite-v2",
    training_dataset="s3://your-bucket/data/train.jsonl",
    s3_output_path="s3://your-bucket/output/",
    data_mixing_config=data_mixing,
)

job = trainer.train(wait=False)
```

For full-rank fine-tuning, pass `training_type=TrainingType.FULL` to
the trainer constructor.

###### Note

When `nova_data_percentages` is provided, only the specified
categories are used — all unspecified categories default to 0. The percentages
must sum to 100.

## Using the AWS CLI

The following command structure shows how to submit a serverless SFT job with
data mixing using the AWS CLI.

```
aws sagemaker create-training-job \
  --region <region> \
  --training-job-name <job-name> \
  --role-arn <execution-role-arn> \
  --hyper-parameters '<hyperparameters-json>' \
  --input-data-config '<input-config-json>' \
  --output-data-config '<output-config-json>' \
  --stopping-condition '{"MaxRuntimeInSeconds": 432000}' \
  --serverless-job-config '<serverless-config-json>' \
  --model-package-config '<model-package-config-json>'
```

### Serverless job configuration

Pass the following JSON as the value of `--serverless-job-config`.
This tells Amazon Nova Forge which model to fine-tune and which training method to use.

```
{
  "BaseModelArn": "<base-model-arn>",
  "AcceptEula": true,
  "JobType": "FineTuning",
  "CustomizationTechnique": "SFT",
  "Peft": "LORA"
}
```

| Field                    | Description                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------- |
| `BaseModelArn`           | ARN of the Nova 2 Lite model in SageMaker AI Hub.                                   |
| `AcceptEula`             | Must be `true` to accept the model EULA.                                            |
| `JobType`                | `FineTuning`                                                                        |
| `CustomizationTechnique` | `SFT`                                                                               |
| `Peft`                   | `LORA` for LoRA fine-tuning. Omit this field<br>entirely for full-rank fine-tuning. |

### Model package configuration

Pass the following JSON as the value of `--model-package-config`.
The trained model checkpoint is registered as a model package version in the
specified group.

```
{
  "ModelPackageGroupArn": "arn:aws:sagemaker:<region>:<account>:model-package-group/<group-name>"
}
```

### Input data configuration

###### Note

Data mixing on SageMaker Training Jobs (serverless) only supports text-only
converse format. Multimodal converse manifests (containing images or
videos) are not supported.

Pass the following JSON as the value of `--input-data-config`.

```
[{
  "ChannelName": "train",
  "DataSource": {
    "S3DataSource": {
      "S3DataType": "Converse",
      "S3Uri": "s3://<bucket>/<path>/training-data.jsonl",
      "S3DataDistributionType": "FullyReplicated"
    }
  },
  "CompressionType": "None",
  "RecordWrapperType": "None"
}]
```

`S3DataType` must be `Converse` for Amazon Nova SFT data.
The training data uses the same Converse API JSONL format as standard Nova 2 Lite
SFT. Set `CompressionType` to `None` because the training
data is plain JSONL and not compressed. Set `RecordWrapperType` to
`None` because the data is not wrapped in RecordIO format.

The following complete example submits a LoRA SFT job with 50% data mixing.

```
aws sagemaker create-training-job \
  --region us-east-1 \
  --training-job-name "my-sft-datamix-lora" \
  --role-arn "arn:aws:iam::<account>:role/<execution-role>" \
  --hyper-parameters '{
    "customer_data_percent": "50",
    "max_steps": "100",
    "global_batch_size": "32",
    "learning_rate": "1e-05",
    "warmup_steps": "15",
    "min_lr": "1e-06",
    "weight_decay": "0.0",
    "save_steps": "10",
    "reasoning_enabled": "true",
    "alpha": "64"
  }' \
  --input-data-config '[{
    "ChannelName": "train",
    "DataSource": {
      "S3DataSource": {
        "S3DataType": "Converse",
        "S3Uri": "s3://<bucket>/training-data.jsonl",
        "S3DataDistributionType": "FullyReplicated"
      }
    },
    "CompressionType": "None",
    "RecordWrapperType": "None"
  }]' \
  --output-data-config '{
    "S3OutputPath": "s3://<bucket>/output",
    "CompressionType": "NONE"
  }' \
  --stopping-condition '{"MaxRuntimeInSeconds": 432000}' \
  --serverless-job-config '{
    "BaseModelArn": "<base-model-arn>",
    "AcceptEula": true,
    "JobType": "FineTuning",
    "CustomizationTechnique": "SFT",
    "Peft": "LORA"
  }' \
  --model-package-config '{
    "ModelPackageGroupArn": "arn:aws:sagemaker:us-east-1:<account>:model-package-group/<group-name>"
  }' \
  --output text --query 'TrainingJobArn'
```

For full-rank fine-tuning, omit `"Peft": "LORA"` from
`--serverless-job-config` and remove `"alpha"` from
hyperparameters.

**Check job status**

```
aws sagemaker describe-training-job \
  --region us-east-1 \
  --training-job-name "my-sft-datamix-lora" \
  --query '{Status:TrainingJobStatus,Secondary:SecondaryStatus,Reason:FailureReason}' \
  --output json
```

## Best practices

- **Start with 50% customer data** as a balanced
  starting point. Higher percentages increase domain specialization but reduce
  general capability preservation.
- **Include reasoning-instruction-following**
  when using data mixing to maintain strong performance across general
  tasks.
- **Use default learning rates** – 1e-5 for LoRA,
  5e-6 for full-rank. Adjust only based on validation metrics.

## Limitations

- **Text-only SFT** – Multimodal data mixing is
  not supported on SageMaker Training Jobs.
- **Nova 2 Lite only** – Other model sizes are
  not supported for data mixing on SageMaker Training Jobs.
- **Category-level control** – When customizing
  category percentages, you must specify all 23 categories with values that
  sum to 100. Set unused categories to `"0"` explicitly.
- **No replicas parameter** –
  `ResourceConfig` is not supported on serverless.
  Replicas are not configurable.
