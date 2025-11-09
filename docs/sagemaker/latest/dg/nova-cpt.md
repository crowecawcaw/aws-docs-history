# Continued pre-training (CPT)

Continued pre-training (CPT) is the process of further training a pre-trained foundation
model on new data using the same unsupervised objectives (such as masked language modeling
or causal language modeling). It preserves the previously learned general language
capabilities while adapting to new domains or distributional shifts.

CPT does not involve architectural changes or fine-tuning for specific downstream tasks.
Instead, it extends the model’s language understanding capacity in a domain-aware
manner.

You should use CPT in the following scenarios:

- You have large-scale, unlabeled data that's specific to a domain (for example
  medicine or finance).
- You want the model to retain general language capabilities while improving on
  domain-specific content.
- You want to improve zero-shot and few-shot performance in specialized areas
  without performing extensive, task-specific fine-tuning.

###### Data format requirements

We recommend adhering to the following dataset characteristics when performing
CPT:

- **Diversity**: Your data should cover a broad range
  of expressions within the target domain to avoid over-fitting.
- **Representation**: Your data should reflect the
  distribution that the model will face during inference.
- **Cleanliness**: Noise and redundancy in your data
  can degrade performance. Deduplication and text normalization improve model
  training.
- **Scale**: Larger datasets help, but beyond a certain
  threshold (such as running multiple epochs on limited data), over-fitting risks
  increase.
  Training and validation datasets must be JSONL files following the Converse format, where
  each line contains a JSON object representing a conversation with the required fields and
  structure. Here is an example:

```
{"text": "AWS stands for Amazon Web Services"}
{"text": "Amazon SageMaker is a fully managed machine learning service"}
{"text": "Amazon Bedrock is a fully managed service for foundation models"}
```

Text entries should contain naturally flowing, high-quality content that represents your
target domain.

###### Dataset validation

To validate your dataset before submitting your CPT job, check for the following
conditions:

- Each line must contain a valid JSON object.
- Each object has a "text" field that contains string data.
- No fields other than "text" are present.
- The file is a `.jsonl` extension.

###### Training times

The amount of time spent training depends heavily on the size of the dataset, the
number of instances use, and the model being trained. Training times are expected to
scale linearly. The following table provides some example training times for various
models.

| Model Type        | GBS | Number of Samples in Dataset | Number of P5 Instances | `max_length` value | Approximate training time in hours |
| ----------------- | --- | ---------------------------- | ---------------------- | ------------------ | ---------------------------------- |
| Amazon Nova Micro | 256 | 100,000                      | 8                      | 8,192              | 4                                  |
| Amazon Nova Lite  | 256 | 100,000                      | 16                     | 8,192              | 4                                  |
| Amazon Nova Pro   | 256 | 100,000                      | 24                     | 8,192              | 10                                 |

Training and validation datasets must be JSONL files following the [Amazon Bedrock
Converse operation format](../../../bedrock/latest/APIReference/API_runtime_Converse.md "../../../bedrock/latest/APIReference/API_runtime_Converse.md"), where each line contains a JSON object representing a
conversation with the required fields and structure.

The Amazon Nova parameters that are available for tuning with CPT include:

- **Run configuration**
  - `name`: A descriptive name for your training job. This helps
    identify your job in the AWS Management Console.
  - `model_type`: The Amazon Nova model variant to use. The available
    options are `amazon.nova-micro-v1:0:128k`,
    `amazon.nova-lite-v1:0:300k`, or
    `amazon.nova-pro-v1:0:300k`.
  - `model_name_or_path`: The path to the base model to use for
    your training. The available options are
    `nova-micro/prod`,
    `nova-lite/prod`,
    `nova-pro/prod`, or the S3 path for the
    post-training checkpoint
    (`s3://customer-escrow-bucket-unique_id/training_run_name`).
  - `replicas`: The number of compute instances to use for
    distributed training. Available values vary based on the model you choose.
    Amazon Nova Micro supports 2, 4, or 8 replicas. Amazon Nova Lite supports 4, 8, 16, or
    32 replicas. Amazon Nova Pro supports 6, 12, or 24 replicas.
  - `data_s3_path`: The S3 location of the training dataset, which
    is a JSONL file. This file must reside in the same AWS account and Region
    as the cluster. All of the S3 locations provided must be in the same account
    and Region.
  - `validation_data_s3_path`: (Optional) The S3 location of the
    validation dataset, which is a JSONL file. This file must reside in the same
    account and region as the cluster. All of the S3 locations provided must be
    in the same account and Region.
  - `output_s3_path`: The S3 location where the manifest and
    TensorBoard logs are stored. All of the S3 locations provided must be in the same
    AWS account and AWS Region.

- **Training configuration**
  - `max_length`: The maximum sequence length in tokens. This
    determines the context window size for training. The maximum supported value
    are 8192 tokens for CPT.

  Longer sequences will improve training efficiencies at the cost of
  increased memory requirements. We recommend that you match the
  `max_length` parameter to your data distribution.

- **Trainer settings**
  - `global_batch_size`: The total number of training samples
    processed together in one forward or backward pass across all devices and
    workers.

  This value multiplies the per-device batch size and number of devices. It
  affects the stability of training and throughput. We recommend that you
  start with a batch size that fits comfortably within your memory and scale
  up from there. For domain-specific data, larger batches might over-smooth
  gradients.
  - `max_epochs`: The number of complete passes through your
    training dataset.

  In general, larger datasets require fewer epochs to converge, while
  smaller datasets require more epochs to converge. We recommend that you
  adjust the number of epochs based on the size of your data to prevent
  over-fitting.

- **Model settings**
  - `hidden_dropout`: The probability of dropping hidden state
    outputs. Increase this value by approximately 0.0-0.2 to reduce overfitting
    on smaller datasets. Valid values are between 0-1, inclusive.
  - `attention_dropout`: The probability of dropping attention
    weights. This parameter can help with generalization. Valid values are
    between 0-1, inclusive.
  - `ffn_dropout`: The probability of dropping feed-forward network
    outputs. Valid values are between 0-1, inclusive.

- **Optimizer configuration**
  - `lr`: The learning rate, which controls the step size during
    optimization. We recommend values between 1e-6-1e-4 for good performance.
    Valid values are between 0-1, inclusive.
  - `name`: The optimizer algorithm. Currently, only
    `distributed_fused_adam` is supported.
  - `weight_decay`: The L2 regularization strength. Higher values
    (between 0.01-0.1) increase regularization.
  - `warmup_steps`: The number of steps to gradually increase
    learning rate. This improves training stability. Valid values are between
    1-20, inclusive.
  - `min_lr`: The minimum learning rate at the end of decay. Valid
    values are between 0-1, inclusive, but must be less than learning
    rate.

###### CPT recipe

The following is a recipe for CPT.

```
## Run config
run:
  name: "my-cpt-run"             # A descriptive name for your training job
  model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification, do not change
  model_name_or_path: "nova-lite/prod"      # Base model path, do not change
  replicas: 4                     # Number of compute instances for training, allowed values are 4, 8, 16
  data_s3_path: `[S3_PATH_TO_TRAIN_DATASET]`
  validation_data_s3_path: `(OPTIONAL)[S3_PATH_TO_VALIDATION_DATASET]`
  output_s3_path: `[S3_PATH_TO_STORE_MANIFEST]`

## Training specific configs
training_config:
  max_length: 8192               # Maximum context window size (tokens).
  global_batch_size: 256           # Global batch size, allowed values are 32, 64, 128, 256.

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
```

###### Limitations

CPT has the following limitations:

- Multimodal datasets aren't supported.
- Intermediate checkpoints aren't saved for evaluation and you can't resume from an
  intermediate checkpoint. Only the last checkpoint is saved.
- MLflow logging isn't supported.
