

# Reinforcement fine-tuning (RFT) on Nova 2.0 on SageMaker Training Jobs
<a name="nova-rft-2-smtj"></a>

## Overview
<a name="nova-rft-overview"></a>

**What is RFT?**

Reinforcement fine-tuning (RFT) improves model performance by training on feedback signals—measurable scores or rewards indicating how well the model performed—rather than exact correct answers. Unlike supervised fine-tuning (SFT) that learns from input-output pairs, RFT uses reward functions to evaluate model responses and iteratively optimizes the model to maximize these rewards. This approach excels when defining the exact correct output is challenging, but you can reliably measure response quality.

To determine whether RFT is a good fit for your use case, see [Reinforcement fine-tuning (RFT)](nova-hp-rft.md).

## Creating and running jobs
<a name="nova-rft-creating-jobs"></a>

### Preparing your data
<a name="nova-rft-preparing-data"></a>

For information about the data format, supported features, constraints, and best practices for preparing RFT training data, see [Preparing data for RFT on Amazon Nova 2](nova-data-prep-rft-2.md).

### Starting a training job
<a name="nova-rft-starting-job"></a>

Use the SageMaker training job notebook template: [Use a SageMaker AI estimator to run a training job](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-fine-tuning-training-job.html#nova-model-training-jobs-notebook).

### Instance requirements
<a name="nova-rft-instance-requirements"></a>

The container supports both Full-Rank and LoRA training:
+ **LoRA training** – 2/4/6/8 × p5.48xlarge or p5en.48xlarge instances
+ **Full-Rank training** – 2/4/6/8 × p5.48xlarge instances (required)

### Selecting hyperparameters and updating the recipe
<a name="nova-rft-training-config"></a>

Once the input data has been uploaded to S3, use the recipe from [SageMaker HyperPod Recipes](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection/recipes/fine-tuning/nova) on GitHub under the Fine tuning folder. For the container image URI, use `708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-TJ-RFT-V2-latest` to run an RFT training job.

**Sample recipe**

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

## SMTJ RFT training configs
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

## Monitoring training
<a name="nova-rft-monitoring"></a>

Training logs include comprehensive metrics at each step. Key metric categories:

**Reward metrics**
+ `critic/rewards/mean`, `critic/rewards/max`, `critic/rewards/min` – Reward distribution
+ `val-score/rewards/mean@1` – Validation rewards

**Model behavior**
+ `actor/entropy` – Policy variation (higher = more exploratory)

**Training health**
+ `actor/pg_loss` – Policy gradient loss
+ `actor/pg_clipfrac` – Frequency of clipped updates
+ `actor/grad_norm` – Gradient magnitude

**Response characteristics**
+ `prompt_length/mean`, `prompt_length/max`, `prompt_length/min` – Input token statistics
+ `response_length/mean`, `response_length/max`, `response_length/min` – Output token statistics
+ `response/aborted_ratio` – Incomplete generation rate (0 = all completed)

**Performance**
+ `perf/throughput` – Training throughput
+ `perf/time_per_step` – Time per training step
+ `timing_per_token_ms/*` – Per-token processing times

**Resource usage**
+ `perf/max_memory_allocated_gb`, `perf/max_memory_reserved_gb` – GPU memory
+ `perf/cpu_memory_used_gb` – CPU memory

## Using fine-tuned models
<a name="nova-rft-using-models"></a>

After training completes, the final model checkpoint is saved to your specified output location. The checkpoint path is available in:
+ Training logs
+ `manifest.json` file in the output Amazon S3 location (defined by `output_s3_uri` in your notebook)

## Limitations and best practices
<a name="nova-rft-limitations"></a>

**Limitations**
+ **Lambda timeout** – Reward functions must complete within 15 minutes (prevents runaway processes and manages costs)
+ **Single-turn only** – Multi-turn conversations are not supported
+ **Data requirements** – Needs sufficient diversity; struggles with sparse rewards (<5% positive examples)
+ **Computational cost** – More expensive than supervised fine-tuning
+ **No multi-modal data** – Only text data type is supported

**Best practices**

**Start small**
+ Begin with 100-200 examples
+ Validate reward function correctness
+ Scale gradually based on results

**Pre-training evaluation**
+ Test baseline model performance before RFT
+ If rewards are consistently 0%, use SFT first to establish basic capabilities
+ If rewards are >95%, RFT may be unnecessary

**Monitor training**
+ Track average reward scores and distribution
+ Watch for overfitting (training rewards increase while validation rewards decrease)
+ Look for concerning patterns:
  + Rewards plateauing below 0.15
  + Increasing reward variance over time
  + Declining validation performance

**Optimize reward functions**
+ Execute within seconds (not minutes)
+ Minimize external API calls
+ Use efficient algorithms
+ Implement proper error handling
+ Take advantage of Lambda's parallel scaling

**Iteration strategy**

If rewards aren't improving:
+ Adjust reward function design
+ Increase dataset diversity
+ Add more representative examples
+ Verify reward signals are clear and consistent