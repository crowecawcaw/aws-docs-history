

# Hyperparameters reference
<a name="model-customize-mtrl-hyperparams"></a>

The following table lists all configurable hyperparameters for multi-turn RL training jobs. Recipe defaults are included below.


| Category | Params | Default | Choice | Explanation | 
| --- | --- | --- | --- | --- | 
| Batch | global\_batch\_size | 128 | {32, 64, 128} | Number of unique prompts per training step. | 
| Batch | group\_size | 8 | [2, 32] | Rollouts per prompt used to compute group-based advantages (GRPO / RLOO). | 
| RL | advantage\_method | group\_based | monte\_carlo, group\_based, group\_based\_per\_turn, rloo, reinforce\_pp, reinforce\_pp\_baseline, opo, grpo\_passk, gpg | Method for computing advantages for rollouts. | 
| RL | loss\_fn | ppo | importance\_sampling, ppo, cispo | RL loss formulation. | 
| RL | clip\_low\_threshold | 0.8 | [0, 1] | Lower bound for clipping the policy probability ratio π\_new/π\_old in the PPO-style surrogate loss. | 
| RL | clip\_high\_threshold | 1.2 | [1, 10] | Upper bound for clipping the policy probability ratio in the loss. | 
| sampling\_params | temperature | 1 | [0, 2] | Sampling temperature applied to logits before sampling. | 
| sampling\_params | sampling\_top\_p | 1 | [0, 1] | Nucleus-sampling cutoff. Samples only from the smallest set of tokens whose cumulative probability ≥ top\_p. | 
| sampling\_params | sampling\_max\_tokens | 4096 | [512, 8192] | Max tokens the model can generate per turn during rollout. | 
| val\_sampling\_params | sampling\_max\_tokens | 4096 | [512, 8192] | Max tokens the model can generate per turn during evaluation. | 
| val\_metrics\_config | pass\_k\_values | [1, 2, 4, 8, 16, 32] | n/a | List of k values for computing pass@k metrics. | 
| val\_metrics\_config | success\_threshold | 1 | n/a | Reward threshold for counting a rollout as "successful". | 
| Schedule | max\_epochs | 1 | [1, 30] | Total passes over the data. | 
| Schedule | max\_steps | 50 | [1, 1000] | Total training iterations. | 
| Schedule | val\_every | 10 | [0, 100] | Eval interval (steps). | 
| Model | model\_name\_or\_path | required |  | Model to fine-tune (e.g., "GPT-OSS-20B"). | 
| Model | lora\_rank | 32 | [16,64] | The rank of LoRA adapter that controls adapter capacity. | 
| Model | lora\_alpha | 64 | [16,128] | LoRA scaling factor. Effective update magnitude ∝ alpha / rank. | 
| Model | learning\_rate | 4.00E-05 | (0, 1e-2] | Adam learning rate. | 
| Model | adam\_beta1 | 0.9 | [0, 0.999999] | Exponential decay rate for the running average of the gradient (first moment) in Adam. | 
| Model | adam\_beta2 | 0.95 | [0, 0.999999] | Exponential decay rate for the running average of the squared gradient (second moment) in Adam. | 
| Model | adam\_eps | 1.00E-08 | [1e-16, 1e-2] | Small constant added to the denominator for numerical stability in Adam's update rule. | 
| Model | adam\_weight\_decay | 0 | [0, 1] | Decoupled weight-decay coefficient (AdamW-style). | 
| Model | adam\_grad\_clip\_norm | 1 | [0, 100] | Maximum global gradient norm. | 
| Rollout | rollout\_max\_concurrency | 96 | [32, 96] | The max in-flight rollout processes can happen in parallel. | 
| Rollout | rollout\_timeout | 600 | [300, 86400] | Failure handling: time after which we treat as the rollout failure. | 
| Rollout | rollout\_max\_retries | 3 | [1, 10] | Number of retry attempts for failed rollouts. | 
| async\_config | max\_steps\_off\_policy | 3 | [0, 10] | Staleness threshold in asynchronous training. When 0, it is synchronous training. | 

## Best practices for tuning hyperparameters
<a name="model-customize-mtrl-hyperparams-best-practices"></a>

When a run is flat or collapsing, the following six parameters account for almost all of the explanation.

### Learning rate
<a name="model-customize-mtrl-hp-bp-lr"></a>

The `learning_rate` controls how large a step the optimizer takes at each training iteration. In multi-turn RL, the gradient signal per step varies depending on the task: a sparse-reward environment with binary outcomes produces many groups where all rollouts score identically, yielding zero advantage for the entire group. Only groups with mixed outcomes produce gradient signal, so each step's useful gradient is diluted. The learning rate needs to be lower to align with weaker signal, or the run needs more steps.

A dense-reward environment where trajectories within a group reliably get different scores produces consistent, non-zero advantages across most groups, and the default learning rate is often already sufficient.

The effective step size also depends on LoRA configuration — the actual update magnitude is `learning_rate × alpha/rank` — so a fixed learning rate hits differently depending on adapter capacity.

### Loss function and clipping range
<a name="model-customize-mtrl-hp-bp-loss"></a>

If you are new to MTRL, importance sampling (`importance_sampling`) is a good starting point before moving to advanced clipping-based algorithms. PPO and CISPO use `clip_low_threshold` and `clip_high_threshold` to constrain the probability ratio `policy_new(action|state) / policy_old(action|state)` — how much the policy is allowed to change in a single training step.

A ratio of `1.0` means no change. The lower threshold (for example, `0.8`) prevents the policy from aggressively unlearning actions it previously favored. The upper threshold (for example, `1.2`) prevents it from overcommitting to actions that looked good in one batch.
+ **PPO** with `(clip_low_threshold, clip_high_threshold) = (0.8, 1.2)` is the safe baseline for any first run.
+ **CISPO** requires wide asymmetric clipping. Start with `clip_low_threshold = 1.0`, `clip_high_threshold = 6.0`. CISPO allows bad-action probabilities to decrease freely and relies solely on the upper clip to prevent instability.

Tweaking clipping thresholds is recommended if training collapse or under-training is observed.

### Batch size and group size
<a name="model-customize-mtrl-hp-bp-batch"></a>

These two parameters jointly determine how much useful gradient signal each training step receives.

`global_batch_size` controls how many unique prompts are included in one optimizer step. Larger batches (128) average gradients over more prompts, producing smoother reward curves and more stable updates. Smaller batches (32) are cheaper per step and useful for fast iteration, but produce noisier gradients. For production runs, 128 is a good default; for debugging or hyperparameter screening, 32 is fine.

`group_size` determines how many independent rollouts are generated for each prompt. These rollouts are compared against each other to compute advantages. If all rollouts receive the same reward (all succeed or all fail), the advantage is zero and the group produces no gradient signal. The default is `group_size = 8`. Reduce it if you have enough diversity in the group, increase it if the environment demands more diversity.

Total rollouts per step = `global_batch_size × group_size`. In sparse-reward settings where most groups yield zero signal, it is often more efficient to keep group size moderate and increase batch size or step count instead.

### Off-policy staleness
<a name="model-customize-mtrl-hp-bp-offpolicy"></a>

In asynchronous training, `max_steps_off_policy` controls how stale a rollout is allowed to be before it is discarded. The default of `3` hides rollout-server tail latency. But stale rollouts have importance ratios that deviate substantially from `1.0`, and when those ratios hit clip bounds they contribute no gradient signal.

**Set to 0 when debugging collapse.** Async staleness compounds with importance-weighted updates and can obscure root causes. Set to `0`, stabilize, then re-enable once the issue is understood. For environments where rollouts are fast, `max_steps_off_policy = 1` may be a better default.

### Sampling max tokens
<a name="model-customize-mtrl-hp-bp-maxtokens"></a>

`sampling_max_tokens` is the per-turn generation cap. If the cap is too low, the model's responses get truncated mid-thought, and it receives reward for an incomplete attempt. The policy then learns to associate those truncated prefixes with bad outcomes, suppressing exploratory behaviors that would have succeeded given more room.

The default of 4096 works for most tasks. Raise to 8192 for models with overlong thinking/reasoning responses. The sizing rule is: `max_turns × (sampling_max_tokens + expected_tool_output) + prompt ≤ max_sequence_length` with some margin.

**Diagnostic:** monitor `rollout/tokens/response_max`. If trajectories cluster at exactly the cap, the model is being silently truncated and likely losing signal. `val_sampling_params.sampling_max_tokens` should match training.

### Rollout configuration
<a name="model-customize-mtrl-hp-bp-rollout"></a>

These parameters control how rollouts are produced and how the trainer handles slow or failed rollouts.
+ `rollout_max_concurrency` — Controls how many rollouts are in flight at once. The default of 96 works well for most setups. Setting it too high in async mode produces stale rollouts and can overwhelm the inference engine.
+ `rollout_timeout` — How long (in seconds) to wait for a single rollout before treating it as failed. The default of 600 is sized for typical tool-using environments. Setting it too low truncates rollouts that would have succeeded given more time.
+ `rollout_max_retries` — Controls retry attempts for failed rollouts. If the permanent failure rate exceeds approximately 1%, the problem is in the environment setup, not retry count.

### Supporting parameters
<a name="model-customize-mtrl-hp-bp-supporting"></a>
+ **LoRA capacity (`lora_rank` and `lora_alpha`).** The effective update magnitude per step is proportional to `alpha/rank`, which acts as a multiplier on the learning rate. The default is `lora_rank = 32, lora_alpha = 64` (a 2:1 ratio). Consider increasing only if everything else is well-tuned and the reward curve still plateaus — double both together (64/128) to add capacity while preserving the same effective learning rate.
+ **temperature = 1.0, sampling\_top\_p = 1.0 for training.** For RL training you want diversity across rollouts within a group so that the group baseline has signal. Temperature 1.0 is a good default. For evaluation, use temperature = 0.0 (greedy decoding) so that eval curves are deterministic and comparable across runs.
+ **pass\_k\_values.** Pass@1 is the headline evaluation metric. Pass@G (where G = group\_size) is a useful sanity check: if pass@G is very high, most prompts are too easy; if pass@G is very low, most prompts are too hard and the group signal is sparse.
+ **max\_steps and max\_epochs.** `max_steps = 50` for screening (enough to see whether the curve is moving), 100 for production. CISPO collapse tends to appear between steps 40–80. `max_epochs = 1` is the default; multiple epochs re-use the same prompts with fresh rollouts, which can help if the prompt set is small but risks overfitting to a narrow prompt distribution.
+ **adam\_beta2 = 0.95.** Lower than the SFT default of 0.999. In RL, gradient statistics are non-stationary, so the optimizer needs to track recent gradient variance more aggressively.
+ **weight\_decay = 0.0.** LoRA already constrains updates via low-rank parameterization. Adding weight decay compounds the regularization in ways that have not been well-characterized for RL fine-tuning.
+ **adam\_grad\_clip\_norm = 1.0.** Caps the global gradient norm. If collapse correlates with large pre-clip spikes, drop to 0.5. If the norm sits at exactly 1.0 for many steps and reward is flat, the clip may be the bottleneck — raise to 2.0 cautiously.