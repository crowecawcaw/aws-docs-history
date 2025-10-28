# Proximal policy optimization (PPO)

Proximal policy optimization (PPO) is the process of using several machine learning models
to train and score a model. The PPO process involves five key components:

- **Actor train model** (or policy model): A
  supervised
  fine-tuning (SFT) model that gets fine-tuned and updated every
  epoch. The updates are made by sampling prompts, generating completions, and
  updating weights using a clipped-surrogate objective. This limits the per-token
  log-profitability change so that each policy step is _proximal_
  to the previous one, preserving training stability.
- **Actor generation model**: A model that generates
  prompt completions or responses to be judged by the reward model and critic model.
  The weights of this model are updated from the
  actor
  train or policy model each epoch.
- **Reward model**: A model with fixed (frozen) weights that's
  used to score the actor generation model, providing feedback on response quality.
- **Critic model**: A model with trainable (unfrozen) weights
  that's used to score the actor generation model. This score is often viewed as an
  estimate of the total reward the actor receives when generating the remaining
  tokens in a sequence.
- **Anchor model**: An SFT model with frozen weights
  that is used to calculate the Kullback-Leibler (KL) divergence between the actor train model and the
  original base model. The anchor model ensures that the updates to the actor
  model are not too drastic compared to the base model. Drastic changes can lead to
  instability or performance degradation.
  Together, these components create a sophisticated reinforcement learning system that can optimize language model outputs based on defined reward criteria while maintaining stable training dynamics.

For detailed instructions about using PPO with Amazon Nova model customization, see the [Proximal Policy Optimization (PPO)](../../../sagemaker/latest/dg/nova-ppo.md "../../../sagemaker/latest/dg/nova-ppo.md") section from SageMakeruser guide.
