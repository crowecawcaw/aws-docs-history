

# Core operations
<a name="training-sessions-primitives"></a>

The training session APIs expose a set of first-class operations that you compose into a training loop. Each operation is an API call against your active session. The model remains loaded on GPUs between calls, and gradient state persists within a training step.

## forward\_backward
<a name="training-sessions-primitives-forward-backward"></a>
+ Compute forward and backward passes in a single call.
+ Accumulate gradients across batches.
+ Specify your loss function (`cross_entropy`, `importance_sampling`, `ppo`, `cispo`, or a custom loss).

## forward
<a name="training-sessions-primitives-forward"></a>
+ Run a forward-only pass (no gradient computation).
+ Compute loss and metrics without updating optimizer state.
+ Useful for evaluation, importance weighting, and KL divergence calculation.
+ Same loss function options as `forward_backward`.

## optim\_step
<a name="training-sessions-primitives-optim-step"></a>
+ Update weights based on accumulated gradients.
+ Configure Adam hyperparameters (`learning_rate`, `beta1`, `beta2`, `eps`, `weight_decay`, `gradient_clip_norm`).
+ Full control over Adam optimization and LoRA\+ learning rate scaling.

## sample
<a name="training-sessions-primitives-sample"></a>
+ Generate tokens for evaluation, RL rollouts, or inference.
+ Generate multiple sequences per prompt (`num_samples`).
+ Optionally return per-token prompt log-probabilities.
+ Configurable `temperature`, `top_k`, `top_p`, `seed`, `max_tokens`, and stop sequences.

## compute\_logprobs
<a name="training-sessions-primitives-compute-logprobs"></a>
+ Score existing token sequences without generating new tokens.
+ Returns per-token log probabilities over the prompt.
+ Essential for RL reference policies, reranking, and importance sampling.
+ Works against the base model or any saved checkpoint.

## save\_weights
<a name="training-sessions-primitives-save-weights"></a>
+ Save inference-ready model weights as a model package.
+ Optionally merge LoRA adapters into full standalone weights.
+ Output is deployable directly, with no optimizer state overhead.
+ Distinct from `save_state`: export for serving versus checkpoint for resumption.

## save\_state
<a name="training-sessions-primitives-save-state"></a>
+ Checkpoint full training state (sharded weights and optimizer state).
+ Resume training from any checkpoint via `load_state`.
+ Registered as a versioned model package for lifecycle tracking.

## load\_state
<a name="training-sessions-primitives-load-state"></a>
+ Resume training from any previously saved checkpoint.
+ `load_state` restores weights only; the optimizer starts fresh.
+ `load_state_with_optimizer` restores weights and optimizer state, so training resumes exactly where the checkpoint left off.
+ Use it to resume after an interruption or to branch a new experiment from a saved point.