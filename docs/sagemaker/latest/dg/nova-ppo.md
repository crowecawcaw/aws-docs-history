# Proximal policy optimization (PPO)

Proximal policy optimization (PPO) is the process of using several machine learning models
to train and score a model. The following models are part of the PPO process:

- **Actor train or policy model**: A supervised
  fine-tuning (SFT) model that gets fine-tuned and updated every epoch. The updates are made
  by sampling prompts, generating completions, and updating weights using a
  clipped-surrogate objective. This limits the per-token log-profitability change so that
  each policy step is _proximal_ to the previous one, preserving training
  stability.
- **Actor generation model**: A model that generates
  prompt completions or responses to be judged by the reward model and critic model. The
  weights of this model are updated from the actor train or policy model each epoch.
- **Reward model**: A model with frozen weights that's
  used to score the actor generation model.
- **Critic model**: A model with unfrozen weights
  that's used to score the actor generation model. This score is often viewed as an
  estimate of the total reward the actor receives when generating the remaining
  tokens.
- **Anchor model**: An SFT model with frozen weights
  that is used to calculate the KL divergence between the actor train model and the base
  model. The anchor model ensures that the updates to the actor model are not too drastic
  compared to the base model. Drastic changes can lead to instability or performance
  degradation.
  The training data must be in JSONL format where each line contains a single JSON object
  that represents a training example. Here is an example:

```
{
    "turns": ["string", "string", ...], // Required
    "turns_to_mask": [integer, integer, ...], // Required
    "reward_category": "string", // Required
    "meta_data": {} // Optional
}
```

- `turns` is an array of conversation string arrays that represent the
  dialog sequence. This line contains system prompts, user messages, and bot
  responses. User messages typically end with "Bot: " to indicate where the model
  output begins. For example, `[["System prompt"], ["User: Question Bot:"], ["Bot
response"]]`.
- `turns_to_mask` is an array of 0-based indices that identify which
  turns should not receive gradient updates. The masked turns are typically system
  prompts and user turns. For example, `[0, 1, 3]` masks the system prompt
  and user messages (the first and third messages).
- `reward_category` is a string that identifies what aspects of model
  performance to evaluate. It's used to select the appropriate reward model category
  during training. The reward category is available for the following reward
  categories: `default`, `math`, `coding`, `if`,
  `rag`, and `rai`.
- `meta_data` is an optional object that contains additional contextual
  or ground-truth information. This can include identifiers, source information, or
  conversation context. The structure is flexible based on your dataset needs.
  Here is an example record:

```
{
    "turns": ["You are a helpful AI assistant.",
        "User: What is ML? Bot:",
        "Machine learning is...", "User: Examples? Bot:",
        "Email spam filtering is..."
    ],
    "turns_to_mask": [0, 1, 3],
    "reward_category": "default",
    "meta_data": {
        "messages": [{
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": "What is ML?"
            },
            {
                "role": "assistant",
                "content": "Machine learning is..."
            },
            {
                "role": "user",
                "content": "Examples?"
            },
            {
                "role": "assistant",
                "content": "Email spam filtering is..."
            }
        ]
    }
}
```

The reward modeling framework implements multi-dimensional optimization across distinct
categorical objectives to facilitate robust model convergence. The reward category should be
selected based on the task that the model must be optimized for.

We recommend the following guidelines for selecting the right framework for your
tasks:

- `default`: A general purpose optimizer for standard conversational
  tasks and basic interactions. Used for general conversations and discussions, basic
  writing tasks, simple question answering, and non-specialized knowledge queries.

Here is an example:

```
{
    "turns": ["Write a summary of climate change"],
    "turns_to_mask": [0],
    "reward_category": "default"
}
```

- `math`: A specialized optimizer for mathematical computations and
  numerical reasoning tasks. Used for mathematical problem-solving, arithmetic
  calculations, algebraic equations, geometric problems, and statistical
  analysis.

Here is an example:

```
{
    "turns": ["Calculate the derivative of x²"],
    "turns_to_mask": [0],
    "reward_category": "math"
}
```

- `coding`: A dedicated category for programming and software
  development-related queries. Used for code implementation, debugging assistance,
  algorithm design, technical documentation, and system architecture questions.

Here is an example:

```
{
    "turns": ["Write a function to check if a string is palindrome"],
    "turns_to_mask": [0],
    "reward_category": "coding"
}
```

- `if`: A category for tasks that require precise procedural execution
  and step-by-step guidance. Used for multi-step procedures, sequential instructions,
  complex task decomposition, and process documentation.

Here is an example:

```
{
    "turns": ["Provide steps to deploy a web application"],
    "turns_to_mask": [0],
    "reward_category": "if"
}
```

- `rag`: A reward category for tasks that require answering queries based
  specifically on retrieved contextual information. Used when responses should be
  derived directly from provided reference materials, synthesizing factual content
  without going beyond the scope of retrieved information, ensuring answers are
  grounded in the supplied context rather than general knowledge.

Here is an example:

```
{
            "turns": ["The Synthesis Report integrates findings from all six IPCC assessment cycles, revealing that global surface temperature has increased 1.1°C from 1850-1900 to 2011-2020, with human activities unequivocally identified as the cause of this warming. Alarmingly, current policies put the world on track for 3.2°C warming by 2100. The document identifies 5 key climate system "tipping points" approaching and emphasizes that greenhouse gas emissions must decline 43% by 2030 (compared to 2019 levels) to limit warming to 1.5°C. Climate-related risks will escalate with every increment of warming, with loss and damage disproportionately affecting vulnerable populations. Despite some progress, climate adaptation remains uneven with significant gaps, and financial flows continue to fall below levels needed for mitigation goals.",
            "What were the key findings of the latest IPCC climate report?"],
            "turns_to_mask": [0, 0],
            "reward_category": "rag"
            }
```

- `rai`: A reward category for tasks that require applying responsible AI
  principles such as fairness, transparency, and ethics. Used for evaluating potential
  biases in AI systems, ensuring privacy considerations, addressing ethical dilemmas,
  and promoting inclusive design principles.

Here is an example:

```
{
            "turns": ["Identify potential bias concerns when developing a loan approval algorithm and suggest mitigation strategies"],
            "turns_to_mask": [0],
            "reward_category": "rai"
            }
```

###### Masking turns

In training datasets, the `turns_to_mask` parameter is crucial for
controlling which conversation turns receive gradient updates during training. This
array of indices determines which parts of the dialogue the model should learn to
generate versus which parts should be treated as context only. Proper masking ensures
the model learns appropriate response patterns while avoiding training on system prompts
or user inputs that could degrade performance.

We recommend the following guidance for masking:

- **Always mask index 0** - System prompts should never
  receive gradient updates.
- **Always mask user turns** - Prevent the model from
  learning to generate user inputs.
- **Pattern consistency** - Use identical masking
  patterns for similar conversation structures, such as (0, 1, 3, 5) for multi-turn
  dialogues.
- **Selective training** - Mask early bot responses to
  focus training on improved final responses.
- **Chain-of-thought preservation** - Only mask system
  and user turns when training on reasoning sequences.
- **Quality filtering** - Mask low-quality assistant
  responses to prevent performance degradation.
- **Context optimization** - Ensure masked turns don't
  remove essential context needed for subsequent responses.
  The key to effective masking is monitoring training metrics and validation performance to
  identify whether your masking strategy preserves necessary context while focusing gradient
  updates on the desired model outputs.

###### Enable KL-divergence loss

For enabling KL-divergence loss, the anchor
server
needs to be enabled to compute the divergence of the current policy from the original
distribution. The KL loss type needs to be specified, and coefficients need to be a
value other than zero. Higher coefficient values help the model not deviate much from
the original policy which results in lesser changes to general performance. Lower
coefficient values allow larger deviations from previous policy, leading to better
performance of target metrics but impacting the general performance.

```
ppo_anchor:
  max_length: 8192
  trainer:
    num_nodes: ${recipes.run.cm_replicas}
  model:
    global_batch_size: 32

ppo_actor_train:
  model:
    ######## Use KL in actor loss ########
    kl_loss_type: low_var_kl
    kl_loss_coeff: 0.1

    ######## Use KL in reward model ######
    kl_reward_penalty_coeff: 0.1
```

###### Learning rate

The learning rate for the critic and policy models can be adjusted, with 3e-6 being
the default balanced choice. Higher learning rates typically lead to training
instabilities, which can be identified through KL divergence spikes and erratic policy
behavior. Lower learning rates may cause convergence issues and slow learning, indicated
by stagnant rewards and minimal policy updates. Regular monitoring of KL divergence,
reward score, and value loss helps in determining whether to adjust the learning rate
during training.

```
ppo_critic:
  model:
    optim:
      lr: 3e-6

ppo_actor_train:
  model:
    optim:
      lr: 3e-06
```

###### Global batch size

Global batch size significantly impacts PPO performance in Amazon Nova, with larger batches
generally improving training stability and gradient estimation while enabling more efficient
parallel processing. However, very large batch sizes can lead to diminishing returns and may
be constrained by available memory, requiring careful balance with learning rate and other
hyperparameters.

```
ppo_actor_train:
  model:
    global_batch_size: 160
```

The Amazon Nova parameters that are available for tuning with PPO include:

- **Run configuration**
  - `actor_train_replicas`: The number of compute instances to be
    used for the actor train model. Available values vary based on the model
    chosen. Amazon Nova Micro supports 1 or 2 replicas. Amazon Nova Lite supports 1, 2, or 4
    replicas. Amazon Nova Pro supports 3, 6, or 12 replicas.
  - `rm_replicas`: The number of compute instances used for the
    reward model. We recommend that you use one replica for any model
    size.
  - `cm_replicas`: The number of compute instances used for the
    critic model. We recommend that you use one replica for any model
    size.
  - `actor_generation_replicas`: The number of compute instances
    used for the actor generation. Available values vary based on the model
    chosen. Amazon Nova Micro supports 1 replica. Amazon Nova Lite supports 1 or 2 replicas.
    Amazon Nova Pro supports 1 or 2 replicas.
  - `am_replicas`: The number of compute instances used for the
    anchor model. We recommend that you use one replica for any model
    size.

- **Actor train configuration (policy config)**
  - `max_steps`: The maximum number of steps to fine-tune or train
    the actor train model. Here, one step is defined as rollout, followed by training the
    actor train model with `global_batch_size` number of samples. One epoch is
    defined as `global_batch_size * trajectory_buffer_scale`.

  The value chosen here will vary based on your use case and dataset
  complexity. We recommend starting with 65 epochs or 520 steps, which is the
  number of epochs multiplied by the value of the
  `trajectory_buffer_scale`. However, some tasks require a
  longer PPO training time to achieve the same performance.

  For PPO, the training metrics, such as saturating reward model score and
  average action length from the [ml-flow](mlflow-create-tracking-server.md "mlflow-create-tracking-server.md")
  console, can help in identifying the optimal points for evaluation.
  - `actor_model_max_length`: The maximum length of the input data
    that is sent to the actor generation component to generate
    completions.
  - `reward_model_max_length`: The maximum length of the input data
    that is sent to the reward server to score completions.
  - `trajectory_buffer_scale`: This buffer represents the number of
    rollouts generated using the old actor train (policy) model before updating the
    weights and generating the new rollouts. The supported values are 1, 2, 4, 8, and
  16.

  If `trajectory_buffer_scale` is 1, then the training is on
  policy. That means the rollouts are generated with the most updated model
  weights, but throughput suffers. If it's 16, then the model is slightly
  off-policy but throughput is higher. We recommend starting with 8 for each
  model.
  - `kl_reward_penalty_coeff`: This is the KL divergence term that
    ensures updates are not too drastic and the policy does not draft from the
    base or SFT model.
  - `kl_loss_coeff`: This value controls how much the KL divergence
    penalty influences the overall training objective in PPO.
  - `kl_loss_type`: This value specifies how to compute the
    divergence between current and reference policy distributions. The
    `kl_loss_types` available are `kl` (Standard KL
    divergence), `mse` (Mean squared error), `abs`
    (Absolute difference between log probabilities), and `low_var_kl`
    (low-variance KL approximation).
  - `model.clip_ratio`: The actor clip ratio (ε) in PPO is a
    hyperparameter that limits how much the policy can change during each update.
  - `model.optim.lr`: The learning rate used for surrogate model
    loss training in the actor model.
  - `model.lam`: Part of the advantage estimation process. Higher λ
    gives more weight to longer-term rewards but with higher variance, while a
    lower λ focuses more on immediate rewards with lower variance but more
    bias.
  - `model.ent_coeff`: Entropy loss in PPO encourages exploration
    by penalizing the policy when it becomes too deterministic (that is, always
    picking the same actions with high confidence).

- **Reward model configuration**
  - `global_batch_size`: The batch size for scoring the completions
    using the reward model. If
    `ppo_actor_train.model.global_batch_size` is greater than
    `ppo_reward.model.global_batch_size`, they are processed in
    multiple batches. Note that `ppo_actor_train.model.global_batch_size %
ppo_reward.model.global_batch_size` must equal 0.
  - `max_length`: The maximum context length of the reward model.
    This should be same as `ppo_actor_train.model.max_length`.

- **Critic model configuration**
  - `global_batch_size`: The batch size of the critic model value.
    The critic model will provide value estimates for each token in the
    responses provided by the actor model. The batch size is used for both
    inference and training.

  Note that `ppo_actor_train.model.global_batch_size %
 ppo_critic.model.global_batch_size` must equal 0 and
  `ppo_actor_train.model.global_batch_size *
 ppo_actor_train.model.trajectory_buffer_size %
 ppo_critic.model.global_batch_size == 0`.
  - `max_length`: The maximum context length of the critic model.
    This should be same as `ppo_actor_train.model.max_length`.
  - `model.optim.lr`: The learning rate used for surrogate model
    loss training in the actor model.

- **Anchor model configuration**
  - `global_batch_size`: The batch size for generating the logp of
    the frozen SFT or anchor model. Note that
    `ppo_actor_train.model.global_batch_size %
ppo_anchor.model.global_batch_size` must equal 0.
  - `max_length`: The maximum context length of the reward model.
    This should be same as `ppo_actor_train.model.max_length`.

- **Actor generation model configuration**
  - `actor_model_max_length`: The maximum context length of the
    actor model generation component. This should be the same as
    `ppo_actor_train.model.max_length`.

###### PPO recipe

The following is a recipe for PPO.

```
## Run config
run:
  name: ndry-ppo-pro
  model_type: amazon.nova-pro-v1:0:300k
  model_name_or_path: nova-pro/prod
  data_s3_path: s3://testing/train.jsonl # Your training data S3 path

  actor_train_replicas: 6 # Actor train model replicas
  rm_replicas: 1 # Reward model replicas
  cm_replicas: 1 # Critic model replicas
  actor_generation_replicas: 2 # Actor generation model replicas
  am_replicas: 1 # Anchor model replicas

## Training config for each PPO component
ppo_reward:
  max_length: 8192 # model architecture max length
  trainer:
    num_nodes: ${recipes.run.rm_replicas}
  model:
    global_batch_size: 16

ppo_critic:
  max_length: 8192
  trainer:
    num_nodes: ${recipes.run.cm_replicas}
  model:
    global_batch_size: 16
    optim:
      lr: 3e-6
      name: distributed_fused_adam
      adam_w_mode: true
      eps: 1e-06
      weight_decay: 0.0
      betas:
        - 0.9
        - 0.999

ppo_anchor:
  max_length: 8192
  trainer:
    num_nodes: ${recipes.run.am_replicas}
  model:
    global_batch_size: 16

ppo_actor_generation:
  actor_model_max_length: 8192
  trainer:
    num_nodes: ${recipes.run.actor_generation_replicas}

ppo_actor_train:
  max_length: 8192
  max_steps: 520 # Stopping criteria Desired epoch num * trajectory_buffer_scale
  actor_model_max_length: 8192 # truncate input data to max length
  reward_model_max_length: 8192 # truncate input data to max length
  trajectory_buffer_scale: 8
  trainer:
    num_nodes: ${recipes.run.actor_train_replicas}
  model:
    global_batch_size: 160
    ent_coeff: 0
    clip_ratio: 0.2
    lam: 1
    kl_loss_coeff: 0.0
    kl_loss_type: low_var_kl
    kl_reward_penalty_coeff: 0.0
    hidden_dropout: 0.0 # Dropout probability for hidden state transformer.
    attention_dropout: 0.0 # Dropout probability in the attention layer.
    ffn_dropout: 0.0 # Dropout probability in the feed-forward layer.
    optim:
      lr: 3e-06
      name: distributed_fused_adam # only this one is available for p0.
      adam_w_mode: true
      eps: 1e-08
      weight_decay: 0.0
      betas:
        - 0.9
        - 0.999
```

###### Limitations

PPO has the following limitations:

- Intermediate checkpoints are not saved for evaluation and you can't resume from an
  intermediate checkpoint. Only the last checkpoint is saved.
- Multimodal datasets aren't supported.
- Training jobs aren't automatically stopped. You have to stop the job using the
  HyperPod CLI.
- MLflow logging isn't supported.
- Critic training metrics are not supported on TensorBoard.
- To adjust the hyperparameters, follow the guidance in [Selecting
  hyperparameters](../../../nova/latest/userguide/customize-fine-tune-hyperparameters.md "../../../nova/latest/userguide/customize-fine-tune-hyperparameters.md").
