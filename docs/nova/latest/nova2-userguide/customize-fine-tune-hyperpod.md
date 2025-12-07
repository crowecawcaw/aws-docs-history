# SageMaker AI HyperPod training

You can customize Amazon Nova models using [Amazon Nova recipes](../../../sagemaker/latest/dg/nova-model-recipes.md "../../../sagemaker/latest/dg/nova-model-recipes.md") and train them on SageMaker AI HyperPod. A recipe is a YAML configuration file that provides details to SageMaker AI on how to run your model customization job.

SageMaker AI HyperPod offers high-performance computing with optimized GPU instances and Amazon FSx for Lustre storage, robust monitoring through integration with tools like TensorBoard, flexible checkpoint management for iterative improvement, seamless deployment to Amazon Bedrock for inference and efficient scalable multi-node distributed training-all working together to provide organizations with a secure, performant and flexible environment to tailor Amazon Nova models to their specific business requirements.

Amazon Nova customization on SageMaker AI HyperPod stores model artifacts including model checkpoints in a service-managed Amazon S3 bucket. Artifacts in the service-managed bucket are encrypted with SageMaker-managed KMS keys. Service-managed Amazon S3 buckets don't currently support data encryption using customer managed keys. You can use this checkpoint location for evaluation jobs or Amazon Bedrock inference.

This section provides details about the Amazon Nova model parameters that you can tune with
SageMaker AI
HyperPod, when you might want to tune them and how they might affect
model performance. The parameters are presented by training technique. For information on how to submit a job, see [Running a SageMaker training job](../../../sagemaker/latest/dg/cluster-specific-configurations-run-sagemaker-training-job.md "../../../sagemaker/latest/dg/cluster-specific-configurations-run-sagemaker-training-job.md").

Continued Pre-Training (CPT) is a technique that extends a pre-trained language model's capabilities by training it on new domain-specific data while preserving its general language understanding. Unlike fine-tuning, CPT uses the same unsupervised objectives as the original pre-training (such as masked or causal language modeling) and doesn't modify the model's architecture.

CPT is particularly valuable when you have large amounts of unlabeled domain-specific data (like medical or financial text) and want to improve the model's performance in specialized areas without losing its general capabilities. This approach enhances zero-shot and few-shot performance in targeted domains without requiring extensive task-specific fine-tuning.

For detailed instructions about using CPT with Amazon Nova model customization, see the [Continued Pre-Training (CPT)](../../../sagemaker/latest/dg/nova-cpt.md "../../../sagemaker/latest/dg/nova-cpt.md") section from SageMaker user guide.

Supervised fine-tuning (SFT) is the process of providing a collection of
prompt-response pairs to a foundation model to improve the performance of a pre-trained
foundation model on a specific task. The labeled examples are formatted as
prompt-response pairs and phrased as instructions. This fine-tuning process modifies the
weights of the model.

You should use SFT when you have domain-specific data that requires providing specific
prompt-response pairs for optimal results. Both full-rank
SFT and parameter-efficient SFT are available.

For detailed instructions about using SFT with Amazon Nova model customization, see the [Supervised Fine-Tuning (Full FT, PEFT)](../../../sagemaker/latest/dg/nova-fine-tune.md "../../../sagemaker/latest/dg/nova-fine-tune.md") section from SageMakeruser guide.

DPO is an advanced technique that fine-tunes models based on human preferences rather than fixed labels. It uses paired examples where humans have indicated which response is better for a given prompt. The model learns to generate outputs that align with these preferences, helping to improve response quality, reduce harmful outputs and better align with human values. DPO is particularly valuable for refining model behavior after initial SFT.

Both full-rank DPO and low-rank adapter (LoRA) DPO are available.

For detailed instructions about using DPO with Amazon Nova model customization, see the [Direct Preference Optimization (DPO)](../../../sagemaker/latest/dg/nova-dpo.md "../../../sagemaker/latest/dg/nova-dpo.md") section from SageMakeruser guide.

Proximal policy optimization (PPO) is the process of using several machine learning models
to train and score a model. The PPO process involves five key components:

- **Actor train model** (or policy model): A
  supervised
  fine-tuning (SFT) model that gets fine-tuned and updated every
  epoch. The updates are made by sampling prompts, generating completions and updating weights using a clipped-surrogate objective. This limits the per-token
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

Iterative training allows you to develop more sophisticated training pipelines to tune
Amazon Nova models. By chaining training modules, you're able to layer training techniques to
customize your models exactly to your needs.

To begin, you start by training Amazon Nova using one of the techniques described in [SageMaker AI HyperPod training](customize-fine-tune-hyperpod.md "customize-fine-tune-hyperpod.md").
In the output S3 location defined during training, locate the `manifest.json`
file. This file contains the value `checkpoint_s3_bucket` that indicates where
the output model is defined. You can utilize this output location as the
`model_name_or_path` value in future training runs.

For detailed instructions about using iterative training with Amazon Nova model customization, see the [Iterative training](../../../sagemaker/latest/dg/nova-hp-iterative-training.md "../../../sagemaker/latest/dg/nova-hp-iterative-training.md") section from SageMakeruser guide.
