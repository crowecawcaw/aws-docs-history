

# Reinforcement fine-tuning (RFT) on Nova 2.0 on SageMaker HyperPod
<a name="nova-hp-rft-nova2"></a>

This section covers the sample recipe, starting a fine-tuning job, hyperparameter guidance, and training monitoring for RFT on Nova 2.0 Lite on SageMaker HyperPod. For information about the data format, supported features, constraints, and best practices for preparing RFT training data, see [Preparing data for RFT on Amazon Nova 2](nova-data-prep-rft-2.md).

To determine whether RFT is a good fit for your use case, see [Reinforcement fine-tuning (RFT)](nova-hp-rft.md).

**Topics**
+ [Starting a fine-tuning job on SageMaker HyperPod](#nova-rft-2-starting-job)
+ [Hyperparameter guidance](#nova-hp-rft-monitoring-hyperparams)
+ [Monitoring RFT training](nova-hp-rft-monitoring.md)

## Sample RFT recipe
<a name="nova-rft-2-sample-recipe"></a>

```
# Note:
# This recipe can run on p5.48xlarge, p5e.48xlarge, and p5en.48xlarge instance types.
run:
  name: "my-rft-run"                           # Unique run name (appears in logs and artifacts).
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  data_s3_path: s3://<bucket>/<data-file>      # Training dataset in JSONL format.
  replicas: 4                                   # Number of total training instances.
  generation_replicas: 2                        # Number of total instances dedicated to response generation.
  reward_lambda_arn: arn:aws:lambda:<region>:<account-id>:function:<function-name>

  ## MLFlow configs
  mlflow_tracking_uri: "" # Required for MLFlow
  mlflow_experiment_name: "my-rft-experiment" # Optional for MLFlow. Note: leave this field non-empty
  mlflow_run_name: "my-rft-run" # Optional for MLFlow. Note: leave this field non-empty

## SMHP RFT training configs
training_config:
  max_length: 8192                              # Context window (tokens) for inputs and prompt.
  global_batch_size: 32                         # Total samples per optimizer step across all replicas (16/32/64/128/256).
  reasoning_effort: high                        # Reasoning mode: high, low, or null for non-reasoning.

  data:
    shuffle: true                               # Shuffle training data each epoch.

  rollout:                                      # Controls how responses are generated for advantage calculation.
    rollout_strategy:
      type: off_policy_async                    # Asynchronous rollout for higher throughput.
      age_tolerance: 2                          # Maximum policy age before regeneration.
    advantage_strategy:
      number_generation: 4                      # Samples per prompt to estimate advantages (higher = lower variance but higher cost).
    generator:
      max_new_tokens: 6000                      # Cap on tokens generated per sample.
      set_random_seed: true                     # Seed generation for reproducibility across runs.
      temperature: 1                            # Softmax temperature for sampling.
      top_k: 1                                  # Sample only from top-K logits.
    rewards:
      preset_reward_function: null              # Preset reward functions: exact_match or null for custom.
      api_endpoint:
        lambda_arn: arn:aws:lambda:<region>:<account-id>:function:<function-name>
        lambda_concurrency_limit: 12             # Max concurrent Lambda invocations (throughput vs. throttling).
        lambda_batch_size: 128                  # Number of samples per Lambda invocation.

  trainer:
    max_steps: 2                                # Steps to train for. One step = global_batch_size samples.
    save_steps: 5                               # Save a checkpoint every N steps.
    test_steps: 1                               # Run validation every N reference model updates.
    refit_freq: 4                               # Frequency of reference model updates.
    clip_ratio_high: 0.2                        # PPO clip ratio for policy updates.
    loss_scale: 1.0                             # Scaling factor for the policy loss.

    # RL parameters
    ent_coeff: 0.0                              # Entropy bonus added to the policy loss (higher = more exploration).
    kl_loss_coef: 0.0                           # Weight on the KL penalty between the current and reference policy.

    optim_config:                               # Optimizer settings.
        lr: 1e-6                                # Learning rate.
        weight_decay: 0.0                       # L2 regularization strength (0.0 to 1.0).
        adam_beta1: 0.9
        adam_beta2: 0.95

    peft:                                       # Parameter-efficient fine-tuning (LoRA).
        peft_scheme: "lora"                     # Enable LoRA for PEFT.
        lora_tuning:
            alpha: 64                           # LoRA scaling factor.
            lora_plus_lr_ratio: 64.0            # LoRA+ learning rate scaling factor (0.0 to 100.0).
```

## Starting a fine-tuning job on SageMaker HyperPod
<a name="nova-rft-2-starting-job"></a>

### Preparing your data
<a name="nova-rft-2-preparing-data"></a>

For information about the data format, supported features, constraints, and best practices for preparing RFT training data, see [Preparing data for RFT on Amazon Nova 2](nova-data-prep-rft-2.md).

### Uploading your data
<a name="nova-rft-2-data-upload"></a>

Upload your training dataset to an S3 bucket. Specify its location in the recipe's `run` block:

```
## Run config
run:
  ...
  data_s3_path: "s3://<bucket-name>/<training-directory>/<training-file>.jsonl"
```

**Note**  
Replace `<bucket-name>`, `<training-directory>`, and `<training-file>` with actual S3 paths.

### Defining your config
<a name="nova-rft-2-defining-config"></a>

Define the base model using the `model_type` and `model_name_or_path` fields in the `run` block:

```
## Run config
run:
  ...
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: nova-lite-2/prod
  ...
```

## Hyperparameter guidance
<a name="nova-hp-rft-monitoring-hyperparams"></a>

Use the following recommended hyperparameters based on your training approach:

**General:**
+ Epochs: 1
+ Learning rate (lr): 1e-7
+ Number of generations: 8
+ Max new tokens: 8192
+ Batch size: 256

**LoRA (Low-Rank Adaptation):**
+ LoRA Rank: 32

**Note**  
Adjust these values based on your dataset size and validation performance. Monitor training metrics to prevent overfitting.