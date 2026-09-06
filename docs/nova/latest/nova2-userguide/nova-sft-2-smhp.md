

# Supervised fine-tuning (SFT) on Nova 2.0 on SageMaker HyperPod
<a name="nova-sft-2-smhp"></a>

Amazon Nova Lite 2.0 brings enhanced capabilities for supervised fine-tuning, including advanced reasoning mode, improved multimodal understanding, and extended context handling. SFT on Nova Lite 2.0 enables you to adapt these powerful capabilities to your specific use cases while maintaining the model's superior performance on complex tasks.

The key features of SFT on Nova Lite 2.0 are summarized in [Supported features](nova-data-prep-sft-2.md#nova-2-supported-features).

To determine whether SFT is a good fit for your use case, see [Supervised fine-tuning (SFT)](nova-fine-tune.md).

**Topics**
+ [Reasoning mode selection (Nova 2.0 only)](#nova-sft-2-reasoning-mode)
+ [Starting a fine-tuning job on SageMaker HyperPod](#nova-sft-2-creating-job)
+ [SFT tuning parameters](#nova-sft-2-tuning-parameters)
+ [Hyperparameter guidance](#nova-sft-2-hyperparameters)

## Sample SFT recipe
<a name="nova-sft-2-sample-recipe"></a>

Below is a sample recipe for SFT. You can find this recipe and others in the [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova) repository on GitHub.

```
run:
  name: my-full-rank-sft-run
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://my-bucket-name/train.jsonl  # SageMaker HyperPod only and not compatible with SageMaker Training Jobs
  replicas: 4                                     # Number of compute instances for training, allowed values are 4, 8, 16, 32
  output_s3_path: s3://my-bucket-name/outputs/    # Output artifact path (HyperPod job-specific; not compatible with standard SageMaker Training Jobs)
  mlflow_tracking_uri: ""                         # Required for MLFlow
  mlflow_experiment_name: "my-full-rank-sft-experiment"  # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-full-rank-sft-run"         # Optional for MLFlow. Note: leave this field non-empty

training_config:
  max_steps: 100                    # Maximum training steps. Minimal is 4.
  save_steps: ${oc.select:training_config.max_steps}  # How many training steps the checkpoint will be saved
  save_top_k: 5                     # Keep top K best checkpoints. Note supported only for SageMaker HyperPod jobs. Minimal is 1.
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

## Reasoning mode selection (Nova 2.0 only)
<a name="nova-sft-2-reasoning-mode"></a>

Amazon Nova 2.0 supports reasoning mode for enhanced analytical capabilities:
+ **Reasoning Mode (enabled)**:
  + Set `reasoning_enabled: true` in the training configuration
  + Model trains to generate reasoning traces before final answers
  + Improves performance on complex reasoning tasks
+ **Non-Reasoning Mode (disabled)**:
  + Set `reasoning_enabled: false` or omit the parameter (default)
  + Standard SFT without explicit reasoning
  + Suitable for tasks that don't benefit from step-by-step reasoning

**Note**  
When reasoning is enabled, it operates at high reasoning effort. There is no low reasoning option for SFT.
Multimodal reasoning content is not supported for SFT. Reasoning mode applies to text-only inputs.

### Using reasoning mode with non-reasoning datasets
<a name="nova-sft-2-reasoning-non-reasoning-data"></a>

Training Amazon Nova on a non-reasoning dataset with `reasoning_enabled: true` is permitted. However, doing so may cause the model to lose its reasoning capabilities, as Amazon Nova primarily learns to generate the responses presented in the data without applying reasoning.

If training Amazon Nova on a non-reasoning dataset but still want to use reasoning during inference:

1. Disable reasoning during training (`reasoning_enabled: false`)

1. Enable reasoning later during inference

While this approach allows reasoning at inference time, it does not guarantee improved performance compared to inference without reasoning.

**Best practice:** Enable reasoning for both training and inference when using reasoning datasets, and disable it for both when using non-reasoning datasets.

**Note**  
For more information about container images and example recipes, see [Amazon Nova recipes](nova-model-recipes.md).

## Starting a fine-tuning job on SageMaker HyperPod
<a name="nova-sft-2-creating-job"></a>

### Preparing your data
<a name="nova-sft-2-preparing-data"></a>

For information about the data format, supported features, constraints, and best practices for preparing SFT training data, see [Preparing data for SFT on Amazon Nova 2](nova-data-prep-sft-2.md).

### Uploading your data
<a name="nova-sft-2-data-upload"></a>

Upload training and validation datasets to an S3 bucket. Specify these locations in the recipe's `run` block:

```
## Run config
run:
  ...
  data_s3_path: "s3://<bucket-name>/<training-directory>/<training-file>.jsonl"
```

**Note**  
Replace `<bucket-name>`, `<training-directory>`, `<validation-directory>`, `<training-file>`, and `<validation-file>` with actual S3 paths.

**Note**  
Validation datasets are not currently supported for SFT with Amazon Nova 2.0. If a validation dataset is provided, it will be ignored.

### Defining your config
<a name="nova-sft-2-defining-config"></a>

Define the base model using the `model_type` and `model_name_or_path` fields in the `run` block:

```
## Run config
run:
  ...
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  ...
```

## SFT tuning parameters
<a name="nova-sft-2-tuning-parameters"></a>

The parameters that are available for tuning with SFT include:

**Run configuration**  

+ **name**: A descriptive name for your training job. This helps identify your job in the AWS Management Console.
+ **model\_type**: The Amazon Nova model variant to use. The available options are `amazon.nova-2-lite-v1:0:256k`.
+ **model\_name\_or\_path**: The path to the base model to use for your training. The available options are `nova-lite-2/prod`, or the S3 path for the post-training checkpoint (`s3://customer-escrow-bucket-unique_id/training_run_name`).
+ **replicas**: The number of compute instances to use for distributed training. Available values vary based on the model you choose. Amazon Nova Lite 2.0 supports 4, 8, 16, or 32 replicas.
+ **data\_s3\_path**: The S3 location of the training dataset, which is a JSONL file. This file must reside in the same AWS account and Region as the cluster. All of the S3 locations provided must be in the same account and Region.
+ **validation\_data\_s3\_path**: (Optional) The S3 location of the validation dataset, which is a JSONL file. This file must reside in the same account and region as the cluster. All of the S3 locations provided must be in the same account and Region.
+ **output\_s3\_path**: The S3 location where the manifest and TensorBoard logs are stored. All of the S3 locations provided must be in the same AWS account and AWS Region.
+ **mlflow\_tracking\_uri**: The ARN of the MLFlow App to use for MLFlow logging.
+ **mlflow\_experiment\_name**: MLFlow experiment name.
+ **mlflow\_run\_name**: MLFlow run name.

**Training configuration**  

+ **max\_steps**: The number of training steps to run. Each step will train the model with `global_batch_size` number of elements.
+ **save\_steps**: The frequency (in steps) at which to save model checkpoints during training.
+ **save\_top\_k**: The maximum number of best checkpoints to retain based on validation metrics.
+ **max\_length**: The maximum sequence length in tokens. This determines the context window size for training. The maximum supported value is 32768 tokens for SFT.

  Longer sequences will improve training efficiencies at the cost of increased memory requirements. We recommend that you match the max\_length parameter to your data distribution.
+ **global\_batch\_size**: The total number of training samples processed together in one forward or backward pass across all devices and workers.

  This value multiplies the per-device batch size and number of devices. It affects the stability of training and throughput. We recommend that you start with a batch size that fits comfortably within your memory and scale up from there. For domain-specific data, larger batches might over-smooth gradients.
+ **reasoning\_enabled**: Boolean flag to enable reasoning capabilities during training.

**Learning rate scheduler**  

+ **warmup\_steps**: The number of steps to gradually increase learning rate. This improves training stability.
+ **min\_lr**: The minimum learning rate at the end of decay. Valid values are between 0-1, inclusive, but must be less than learning rate.

**Optimizer configuration**  

+ **lr**: The learning rate, which controls the step size during optimization. We recommend values between 1e-6-1e-4 for good performance. Valid values are between 0-1, inclusive.
+ **weight\_decay**: The L2 regularization strength. Higher values (between 0.01-0.1) increase regularization.
+ **adam\_beta1**: The exponential decay rate for the first moment estimates in Adam optimizer. Default is 0.9.
+ **adam\_beta2**: The exponential decay rate for the second moment estimates in Adam optimizer. Default is 0.95.

**PEFT configuration**  

+ **peft\_scheme**: The parameter-efficient fine-tuning scheme to use. Options are `'null'` for full-rank fine-tuning or `lora` for LoRA-based fine-tuning.

**LoRA tuning (when peft\_scheme is 'lora')**  

+ **alpha**: The LoRA scaling parameter. Controls the magnitude of the low-rank adaptation. Typical values range from 8 to 128.
+ **lora\_plus\_lr\_ratio**: The learning rate ratio for LoRA\+ optimization. This multiplier adjusts the learning rate specifically for LoRA parameters.

## Hyperparameter guidance
<a name="nova-sft-2-hyperparameters"></a>

Use the following recommended hyperparameters based on the training approach:

**Full Rank Training**
+ **Epochs**: 1
+ **Learning rate (lr)**: 1e-5
+ **Minimum learning rate (min\_lr)**: 1e-6

**LoRA (Low-Rank Adaptation)**
+ **Epochs**: 2
+ **Learning rate (lr)**: 5e-5
+ **Minimum learning rate (min\_lr)**: 1e-6

**Note**  
Adjust these values based on dataset size and validation performance. Monitor training metrics to prevent overfitting.