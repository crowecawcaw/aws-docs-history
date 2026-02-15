# SFT on Nova 1.0

Supervised fine-tuning (SFT) is the process of providing a collection of prompt-response
pairs to a foundation model to improve the performance of a pre-trained foundation model on
a specific task. The labeled examples are formatted as prompt-response pairs and phrased as
instructions. This fine-tuning process modifies the weights of the model.

You should use SFT when you have domain-specific data that requires providing specific
prompt-response pairs for optimal results.

Note that your training and validation input datasets must reside in customer-owned
buckets, not in escrow, or service-managed S3 buckets.

## Data requirements

For full-rank SFT and low-rank adapter (LoRA) SFT, the data should follow the [Amazon Bedrock
Converse operation format](../../../bedrock/latest/APIReference/API_runtime_Converse.md "../../../bedrock/latest/APIReference/API_runtime_Converse.md"). For examples and constraints of this format, see
[Preparing data for
fine-tuning Understanding models](fine-tune-prepare-data-understanding.md "fine-tune-prepare-data-understanding.md").

To validate your dataset format before submission, we recommend using [the validation script from the Amazon Bedrock samples repository](https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/bedrock-finetuning/understanding/dataset_validation/nova_ft_dataset_validator.py "https://github.com/aws-samples/amazon-nova-samples/blob/main/customization/bedrock-finetuning/understanding/dataset_validation/nova_ft_dataset_validator.py"). This validation tool
helps ensure that your JSONL files adhere to the required format specifications and
identify any potential issues before you submit your fine-tuning job.

The Amazon Nova parameters that are available for tuning with SFT are as follows:

- **Run configuration**
  - `name`: A descriptive name for your training job. This helps
    identify your job in the AWS Management Console.
  - `model_type`: The Amazon Nova model variant to use. The available
    options are `amazon.nova-micro-v1:0:128k`,
    `amazon.nova-lite-v1:0:300k`, or
    `amazon.nova-pro-v1:0:300k`.
  - `model_name_or_path`: The path to the base model to use for your
    training. Select the model to use from `nova-micro/prod`,
    `nova-lite/prod`, `nova-pro/prod`, or the S3 path for the
    post-training checkpoint (`s3://<escrow bucket>/<job
id>/outputs/checkpoints`).
  - `replicas`: The number of compute instances to use for distributed
    training. Available values vary based on the model chosen. Amazon Nova Micro supports 2,
    4, or 8 replicas. Amazon Nova Lite supports 4, 8, 16, or 32 replicas. Amazon Nova Pro supports
    6, 12, or 24 replicas.
  - `data_s3_path`: The S3 location of the training dataset, which is a
    JSONL file. This file must reside in the same AWS account and Region as the
    cluster. All of the S3 locations within the provided S3 path must be in the same
    account and Region.
  - `validation_data_s3_path`: (Optional) The S3 location of the
    validation dataset, which is a JSONL file. This file must reside in the same
    account and Region as the cluster. All of the S3 locations within the provided S3
    path must be in the same account and Region.
  - `output_s3_path`: The S3 location where the manifest and
    TensorBoard logs are stored. All of the S3 locations within the provided S3 path
    must be in the same account and region.

- **Training configuration**
  - `max_length`: The maximum sequence length in tokens. This
    determines the context window size for training. The maximum supported value are
    65,536 tokens for SFT.

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
    Increase this value by approximately 0.0-0.2 to reduce over-fitting on smaller
    datasets. Valid values are between 0-1, inclusive.
  - `attention_dropout`: The probability of dropping attention weights.
    This parameter can help with generalization. Valid values are between 0-1,
    inclusive.
  - `ffn_dropout`: The probability of dropping feed-forward network
    outputs. Valid values are between 0-1, inclusive.

- **Optimizer configuration**
  - `lr`: The learning rate, which controls the step size during
    optimization. Valid values are between 1e-6-1e-3, inclusive. We recommend values
    between 1e-6-1e-4 for good performance.
  - `name`: The optimizer algorithm. Currently, only
    `distributed_fused_adam` is supported.
  - `weight_decay`: The L2 regularization strength. Higher values
    (between 0.01-0.1) increase regularization.
  - `warmup_steps`: The number of steps to gradually increase learning
    rate. This improves training stability. Valid values are between 1-20,
    inclusive.
  - `min_lr`: The minimum learning rate at the end of decay. Valid
    values are between 0-1, inclusive, but must be less than learning rate.

The following is a recipe for full-rank SFT that's intended for you to quickly start
an SFT job on a SageMaker AI HyperPod cluster. This recipe also assumes that you have
connected to your SageMaker AI HyperPod cluster using the correct AWS credentials.

```
run:
  name: "my-sft-micro-job" # gets appended with a unique ID for HP jobs
  model_type: "amazon.nova-micro-v1:0:128k"
  model_name_or_path: "nova-micro/prod"
  replicas: 2
  data_s3_path: s3:`Replace with your S3 bucket name`/input.jsonl
  validation_data_s3_path: `[OPTIONAL] s3:your S3 bucket name`/input.jsonl
  output_s3_path: `[S3_PATH_TO_STORE_MANIFEST]`

## training specific configs
training_config:
  max_length: 32768
  save_steps: 100000
  replicas: ${recipes.run.replicas}
  micro_batch_size: 1
  task_type: sft
  global_batch_size: 64
  weights_only: True
  allow_percentage_invalid_samples: 10

  exp_manager:
    exp_dir: null
    create_wandb_logger: False
    create_tensorboard_logger: True
      project: null
      name: null
    checkpoint_callback_params:
      monitor: step
      save_top_k: 10
      mode: max
      every_n_train_steps: ${recipes.training_config.save_steps}
      save_last: True
    create_early_stopping_callback: True
    early_stopping_callback_params:
      min_delta: 0.001
      mode: min
      monitor: "val_loss"
      patience: 2

  trainer:
    log_every_n_steps: 1
    max_epochs: -1
    max_steps: 16
    val_check_interval: 100
    limit_test_batches: 0
    gradient_clip_val: 1.0
    num_nodes: ${recipes.training_config.replicas}

  model:
    hidden_dropout: 0.0 # Dropout probability for hidden state transformer.
    attention_dropout: 0.0 # Dropout probability in the attention layer.
    ffn_dropout: 0.0 # Dropout probability in the feed-forward layer.
    sequence_parallel: True
    optim:
      lr: 1e-5
      name: distributed_fused_adam
      bucket_cap_mb: 10
      contiguous_grad_buffer: False
      overlap_param_sync: False
      contiguous_param_buffer: False
      overlap_grad_sync: False
      adam_w_mode: true
      eps: 1e-06
      weight_decay: 0.0
      betas:
        - 0.9
        - 0.999
      sched:
        name: CosineAnnealing
        warmup_steps: 10
        constant_steps: 0
        min_lr: 1e-6

    mm_cfg:
      llm:
        freeze: false
      image_projector:
        freeze: true
        require_newline: true
      video_projector:
        freeze: true
        require_newline: false

    peft:
      peft_scheme: null

    training_validation:
      loader:
        args:
          data_loader_workers: 1
          prefetch_factor: 2
      collator:
        args:
          force_image_at_turn_beginning: false
```

The following is a sample full-rank recipe for SFT with all components properly
configured.

```
## Run config
run:
    name: "my-sft-run"              # A descriptive name for your training job
    model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification
    model_name_or_path: "nova-lite/prod"      # Base model path
    replicas: 4                     # Number of compute instances for training
    data_s3_path: s3:`Replace with your S3 bucket name`/input.jsonl
    validation_data_s3_path: `[OPTIONAL] s3:your S3 bucket name`/input.jsonl
    output_s3_path: `[S3_PATH_TO_STORE_MANIFEST]`

## Training specific configs
training_config:
    max_length: 32768               # Maximum context window size (tokens)

    trainer:
        max_epochs: 2               # Number of training epochs

    model:
        hidden_dropout: 0.0          # Dropout for hidden states
        attention_dropout: 0.0       # Dropout for attention weights
        ffn_dropout: 0.0             # Dropout for feed-forward networks

        optim:
            lr: 1e-5                 # Learning rate
            name: distributed_fused_adam  # Optimizer algorithm
            adam_w_mode: true        # Enable AdamW mode
            eps: 1e-06               # Epsilon for numerical stability
            weight_decay: 0.0        # L2 regularization strength
            betas:                   # Adam optimizer betas
                - 0.9
                - 0.999
            sched:
                warmup_steps: 10     # Learning rate warmup steps
                constant_steps: 0    # Steps at constant learning rate
                min_lr: 1e-6         # Minimum learning rate

        peft:
            peft_scheme: null        # Set to null for full-parameter fine-tuning
```

## Limitations

Publishing metrics to Weights & Biases is not supported.

To adjust the hyperparameters, follow the guidance in [Selecting
hyperparameters](customize-fine-tune-hyperparameters.md "customize-fine-tune-hyperparameters.md").

## Parameter-efficient fine-tuning (PEFT)

Parameter-efficient fine-tuning (PEFT) involves retraining a small number of
additional weights to adapt a foundation model to new tasks or domains. Specifically,
low-rank adapter (LoRA) PEFT efficiently fine-tunes foundation models by introducing
low-rank trainable weight matrices into specific model layers, reducing the number of
trainable parameters while maintaining model quality.

A LoRA PEFT adapter augments the base foundation model by incorporating lightweight
adapter layers that modify the model’s weights during inference while keeping the original
model parameters intact. This approach is also considered one of the most cost-effective
fine-tuning techniques. For more information, see [Fine-tune models with adapter
inference components](../../../sagemaker/latest/dg/realtime-endpoints-adapt.md "../../../sagemaker/latest/dg/realtime-endpoints-adapt.md").

You should use LoRA PEFT in the following scenarios:

- You want to start with a fast training procedure.
- The base model's performance is already satisfactory. In this case, the goal of
  LoRA PEFT is to enhance its capabilities across multiple related tasks, such as text
  summarization or language translation. LoRA PEFT's regularization properties help
  prevent overfitting and mitigate the risks of the model "forgetting" the source
  domain. This ensures the model remains versatile and adaptable to various
  applications.
- You want to perform instruction fine-tuning scenarios with relatively small
  datasets. LoRA PEFT performs better with smaller, task-specific datasets than broader,
  larger datasets.
- You have large, labeled datasets that exceed the Amazon Bedrock customization data
  limits. In this case, you can use LoRA PEFT on SageMaker AI to generate better results.
- If you have already achieved promising results through Amazon Bedrock fine-tuning, LoRA PEFT
  in SageMaker AI can help further optimize the model hyperparameters.

The Amazon Nova parameters that are available for with LoRA PEFT include:

- **Run configuration**
  - `name`: A descriptive name for your training job. This helps
    identify your job in the AWS Management Console.
  - `model_type`: The Nova model variant to use. The available options
    are `amazon.nova-micro-v1:0:128k`,
    `amazon.nova-lite-v1:0:300k`, or
    `amazon.nova-pro-v1:0:300k`.
  - `model_name_or_path`: The path to the base model to use for your
    training. Select the model to use. The available options are
    `nova-micro/prod`, `nova-lite/prod`,
    `nova-pro/prod`, or the S3 path for the post-training checkpoint
    (`s3://<escrow bucket>/<job
id>/outputs/checkpoints`).
  - `replicas`: The number of compute instances to use for distributed
    training. Available values vary based on the model you use. Amazon Nova Micro supports
    2, 4, or 8 replicas. Amazon Nova Lite supports 4, 8, 16, or 32 replicas. Amazon Nova Pro
    supports 6, 12, or 24 replicas.
  - `output_s3_path`: The S3 location where the manifest and
    TensorBoard logs are stored. All of the S3 locations within the provided S3 path
    must be in the same account and region.

- **Training configuration**
  - `max_length`: The maximum sequence length in tokens. This
    determines the context window size for training. The maximum supported value are
    65,536 tokens for LoRA PEFT.

  Longer sequences will improve training efficiencies at the cost of increased
  memory requirements. We recommend that you match the `max_length`
  parameter to your data distribution.

- **Trainer settings**
  - `max_epochs`: The number of complete passes through your training
    dataset. You can set either `max_steps` or `max_epochs`, but
    we do not recommend setting both. The maximum value is 5.

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

- **LoRA configuration parameters**
  - `peft_scheme`: Set to `lora` to enable low-rank
    adaptation.
  - `alpha`: The scaling factor for LoRA weights. This is typically set
    to same value as `adapter_dim`.
  - `adaptor_dropout`: The regularization parameter for LoRA.

The following is a recipe for LoRA PEFT.

```
## Run config
run:
    name: "my-lora-run"             # A descriptive name for your training job
    model_type: "amazon.nova-lite-v1:0:300k"  # Model variant specification
    model_name_or_path: "nova-lite/prod"      # Base model path
    replicas: 4                     # Number of compute instances for training
    output_s3_path: `[S3_PATH_TO_STORE_MANIFEST]`

## Training specific configs
training_config:
    max_length: 32768               # Maximum context window size (tokens)

    trainer:
        max_epochs: 2               # Number of training epochs

    model:
        hidden_dropout: 0.0          # Dropout for hidden states
        attention_dropout: 0.0       # Dropout for attention weights
        ffn_dropout: 0.0             # Dropout for feed-forward networks

        optim:
            lr: 1e-5                 # Learning rate
            name: distributed_fused_adam  # Optimizer algorithm
            adam_w_mode: true        # Enable AdamW mode
            eps: 1e-06               # Epsilon for numerical stability
            weight_decay: 0.0        # L2 regularization strength
            betas:                   # Adam optimizer betas
                - 0.9
                - 0.999
            sched:
                warmup_steps: 10     # Learning rate warmup steps
                constant_steps: 0    # Steps at constant learning rate
                min_lr: 1e-6         # Minimum learning rate

        peft:
            peft_scheme: "lora"      # Enable LoRA for parameter-efficient fine-tuning
            lora_tuning:
                loraplus_lr_ratio: 8.0  # LoRA+ learning rate scaling factor
                alpha: 32            # Scaling factor for LoRA weights
                adapter_dropout: 0.01  # Regularization for LoRA parameters
```

Use the following information to help resolve issues that you might
encounter:

- The input dataset for both training and validation should reside in
  customer-owned buckets, not in escrow, or service-managed S3 buckets.
- If you receive a Region not found error in the AWS CLI, resubmit the job with
  the region prepended to the start-job command. For example:
  `AWS_REGION=us-east-1 hyperpod start-job ...`Job
  Parameters``.
- To adjust the hyperparameters, follow the guidance in [Selecting
  hyperparameters](customize-fine-tune-hyperparameters.md "customize-fine-tune-hyperparameters.md").
