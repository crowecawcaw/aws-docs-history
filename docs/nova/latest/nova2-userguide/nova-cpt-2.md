

# Continued pre-training (CPT) on Nova 2.0 on SageMaker HyperPod
<a name="nova-cpt-2"></a>

Amazon Nova Lite 2.0 is a reasoning model trained on larger and more diverse datasets than Nova Lite 1.0. Despite being a larger model, Nova Lite 2.0 delivers faster inference than Nova Lite 1.0 while offering enhanced reasoning capabilities, longer context lengths, and improved multilingual performance.

With CPT on Nova 2.0 Lite, you can extend these advanced capabilities with your domain-specific data and develop deep expertise in specialized areas while maintaining the model's superior reasoning and analytical abilities.

## Sample CPT recipe
<a name="nova-cpt-2-sample-recipe"></a>

The following is a sample recipe for CPT. You can find this recipe and others in the [SageMaker HyperPod recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/training/nova) repository on GitHub.

```
# Note:
# This recipe can run on p5.48xlarge
# Run config
run:
  name: "my-cpt-run"                           # A descriptive name for your training job
  model_type: "amazon.nova-2-lite-v1:0:256k"   # Model variant specification, do not change
  model_name_or_path: "nova-lite-2/prod"        # Base model path, do not change
  replicas: 8                                   # Number of compute instances for training, allowed values are 4, 8, 16, 32
  data_s3_path: ""                              # Customer data paths
  validation_data_s3_path: ""                   # Customer validation data paths
  output_s3_path: ""                            # Output artifact path, SageMaker HyperPod job-specific configuration - not compatible with standard SageMaker Training Jobs
  mlflow_tracking_uri: ""                       # Required for MLFlow
  mlflow_experiment_name: "my-cpt-experiment"   # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-cpt-run"                 # Optional for MLFlow. Note: leave this field non-empty

## Training specific configs
training_config:
  task_type: cpt
  max_length: 8192                              # Maximum context window size (tokens)
  global_batch_size: 256                        # Global batch size, allowed values are 32, 64, 128, 256.

  trainer:
    max_steps: 10                               # The number of training steps to run total
    val_check_interval: 10                      # The number of steps between running validation. Integer count or float percentage
    limit_val_batches: 2                        # Batches of the validation set to use each trigger

  model:
    hidden_dropout: 0.0                         # Dropout for hidden states, must be between 0.0 and 1.0
    attention_dropout: 0.0                      # Dropout for attention weights, must be between 0.0 and 1.0

  optim:
    optimizer: adam
    lr: 1e-5                                    # Learning rate
    name: distributed_fused_adam                # Optimizer algorithm, do not change
    adam_w_mode: true                           # Enable AdamW mode
    eps: 1e-06                                  # Epsilon for numerical stability
    weight_decay: 0.0                           # L2 regularization strength, must be between 0.0 and 1.0
    adam_beta1: 0.9                             # Beta1 for Adam optimizer
    adam_beta2: 0.95                            # Beta2 for Adam optimizer
    sched:
      warmup_steps: 10                          # Learning rate warmup steps
      constant_steps: 0                         # Steps at constant learning rate
      min_lr: 1e-6                              # Minimum learning rate, must be lower than lr
```

## Starting a continued pre-training job on SageMaker HyperPod
<a name="nova-cpt-2-starting-job"></a>

### Preparing your data
<a name="nova-cpt-2-preparing-data"></a>

For information about the data format, supported features, constraints, and best practices for preparing CPT training data, see [Preparing data for CPT on Amazon Nova 2](nova-data-prep-cpt-2.md).

### Uploading your data
<a name="nova-cpt-2-data-upload"></a>

Upload training and validation datasets to an S3 bucket. Specify these locations in the recipe's `run` block:

```
## Run config
run:
  ...
  data_s3_path: "s3://<bucket-name>/<training-directory>/<training-file>.jsonl"
  validation_data_s3_path: "s3://<bucket-name>/<validation-directory>/<validation-file>.jsonl"
```

**Note**  
Replace `<bucket-name>`, `<training-directory>`, `<validation-directory>`, `<training-file>`, and `<validation-file>` with actual S3 paths.

### Defining your config
<a name="nova-cpt-2-defining-config"></a>

Define the base model using the `model_type` and `model_name_or_path` fields in the `run` block:

```
## Run config
run:
  ...
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  ...
```

## CPT tuning parameters
<a name="nova-cpt-2-tuning-parameters"></a>

The parameters that are available for fine-tuning with CPT include:

**Run configuration**  

+ **name**: A descriptive name for your training job. This helps identify your job in the AWS Management Console.
+ **model\_type**: The Amazon Nova model variant to use. The available options are `amazon.nova-2-lite-v1:0:256k`.
+ **model\_name\_or\_path**: The path to the base model to use for your training. The available options are `nova-lite-2/prod`, or the S3 path for the post-training checkpoint (`s3://customer-escrow-bucket-unique_id/training_run_name`).
+ **replicas**: The number of compute instances to use for distributed training. Available values vary based on the model you choose. Amazon Nova Lite 2.0 supports 4, 8, 16, or 32 replicas.
+ **data\_s3\_path**: The S3 location of the training dataset, which is a JSONL file. This file must reside in the same AWS account and Region as the cluster. All of the S3 locations provided must be in the same account and Region.
+ **validation\_data\_s3\_path**: (Optional) The S3 location of the validation dataset, which is a JSONL file. This file must reside in the same account and region as the cluster. All of the S3 locations provided must be in the same account and Region.
+ **output\_s3\_path**: The S3 location where the manifest and TensorBoard logs are stored. All of the S3 locations provided must be in the same AWS account and AWS Region.
+ **mlflow\_tracking\_uri**: The ARN of the MLFlow App to use for MLFlow logging
+ **mlflow\_experiment\_name**: MLFlow experiment name
+ **mlflow\_run\_name**: MLFlow run name

**Training configuration**  

+ **max\_length**: The maximum sequence length in tokens. This determines the context window size for training. The maximum supported value are 8192 tokens for CPT.

  Longer sequences will improve training efficiencies at the cost of increased memory requirements. We recommend that you match the max\_length parameter to your data distribution.
+ **global\_batch\_size**: The total number of training samples processed together in one forward or backward pass across all devices and workers.

  This value multiplies the per-device batch size and number of devices. It affects the stability of training and throughput. We recommend that you start with a batch size that fits comfortably within your memory and scale up from there. For domain-specific data, larger batches might over-smooth gradients.

**Trainer settings**  

+ **max\_steps**: The number of training steps to run. Each step will train the model with `global_batch_size` no. of elements

**Model settings**  

+ **hidden\_dropout**: The probability of dropping hidden state outputs. Increase this value by approximately 0.0-0.2 to reduce overfitting on smaller datasets. Valid values are between 0-1, inclusive.
+ **attention\_dropout**: The probability of dropping attention weights. This parameter can help with generalization. Valid values are between 0-1, inclusive.

**Optimizer configuration**  

+ **lr**: The learning rate, which controls the step size during optimization. We recommend values between 1e-6-1e-4 for good performance. Valid values are between 0-1, inclusive.
+ **name**: The optimizer algorithm. Currently, only `distributed_fused_adam` is supported.
+ **weight\_decay**: The L2 regularization strength. Higher values (between 0.01-0.1) increase regularization.
+ **warmup\_steps**: The number of steps to gradually increase learning rate. This improves training stability. Valid values are between 1-20, inclusive.
+ **min\_lr**: The minimum learning rate at the end of decay. Valid values are between 0-1, inclusive, but must be less than learning rate.