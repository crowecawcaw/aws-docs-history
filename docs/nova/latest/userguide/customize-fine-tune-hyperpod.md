# SageMaker AI HyperPod training

You can customize Amazon Nova models using [Amazon Nova recipes](../../../sagemaker/latest/dg/nova-model-recipes.md "../../../sagemaker/latest/dg/nova-model-recipes.md") and train them on SageMaker AI HyperPod. A recipe is a YAML configuration file that provides details to SageMaker AI on how to run your model customization job.

SageMaker AI HyperPod offers high-performance computing with optimized GPU instances and Amazon FSx for Lustre storage, robust monitoring through integration with tools like TensorBoard, flexible checkpoint management for iterative improvement, seamless deployment to Amazon Bedrock for inference, and efficient scalable multi-node distributed training-all working together to provide organizations with a secure, performant, and flexible environment to tailor Amazon Nova models to their specific business requirements.

Amazon Nova customization on SageMaker AI HyperPod stores model artifacts including model checkpoints in a service-managed Amazon S3 bucket. Artifacts in the service-managed bucket are encrypted with SageMaker-managed KMS keys. Service-managed Amazon S3 buckets don't currently support data encryption using customer managed keys. You can use this checkpoint location for evaluation jobs or Amazon Bedrock inference.

This section provides details about the Amazon Nova model parameters that you can tune with
SageMaker AI
HyperPod, when you might want to tune them, and how they might affect
model performance. The parameters are presented by training technique. For information on how to submit a job, see [Running a SageMaker training job](../../../sagemaker/latest/dg/cluster-specific-configurations-run-sagemaker-training-job.md "../../../sagemaker/latest/dg/cluster-specific-configurations-run-sagemaker-training-job.md").

###### Topics

- [Continued pre-training (CPT)](customize-fine-tune-hyperpod-cpt.md "customize-fine-tune-hyperpod-cpt.md")
- [Supervised fine-tuning (Full FT, PEFT)](customize-fine-tune-hyperpod-sft.md "customize-fine-tune-hyperpod-sft.md")
- [Direct preference optimization (DPO)](customize-fine-tune-hyperpod-dpo.md "customize-fine-tune-hyperpod-dpo.md")
- [Proximal policy optimization (PPO)](customize-fine-tune-hyperpod-ppo.md "customize-fine-tune-hyperpod-ppo.md")
- [Iterative training](customize-fine-tune-hyperpod-iterate.md "customize-fine-tune-hyperpod-iterate.md")
