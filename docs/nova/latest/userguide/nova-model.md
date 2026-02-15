# Customizing Amazon Nova models on SageMaker AI

You can customize [Amazon Nova models](what-is-nova.md "what-is-nova.md"), including the enhanced Amazon Nova 2.0 models, through [recipes](nova-model-recipes.md#nova-model-get-recipes "nova-model-recipes.md#nova-model-get-recipes") and train them on SageMaker AI. These recipes
support techniques such as supervised fine-tuning (SFT), Direct Preference Optimization
(DPO), and Reinforcement Fine-Tuning (RFT), with both full-rank and low-rank adaptation (LoRA) options.

The end-to-end customization workflow involves stages like model training, model
evaluation, and deployment for inference. This model customization approach on SageMaker AI provides
greater flexibility and control to fine-tune its supported Amazon Nova models, optimize
hyperparameters with precision, and implement techniques such as LoRA parameter-efficient
fine-tuning (PEFT), full-rank SFT, DPO, RFT, Continued Pre-Training (CPT), Proximal Policy
Optimization (PPO), etc.

SageMaker AI offers two environments for customizing Amazon Nova models.

- [**SageMaker AI training jobs**](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md") provides a
  fully managed environment for customizing Amazon Nova models where you don't need to create
  or maintain any clusters. The service automatically handles all infrastructure
  provisioning, scaling, and resource management, allowing you to focus solely on
  configuring your training parameters and submitting your job. You can customize Nova
  models on SageMaker AI training jobs with techniques like Parameter Efficient
  Fine-tuning (PEFT), Full rank fine tuning, Direct Preference Optimization
  (DPO), and Reinforcement Fine-Tuning (RFT). For more information, see [Amazon Nova customization on SageMaker AI training jobs](nova-model-training-job.md "nova-model-training-job.md").

###### Note

If you provide a KMS key to your Amazon Nova model customization training job for encryption in the Amazon-owned output S3 bucket:

    + You must provide the same KMS key when calling subsequent [iterative
     training jobs](../../../sagemaker/latest/dg/nova-iterative-training.md "../../../sagemaker/latest/dg/nova-iterative-training.md"), or when calling the Amazon Bedrock [CreateCustomModel](../../../bedrock/latest/APIReference/API_CreateCustomModel.md#bedrock-CreateCustomModel-request-modelKmsKeyArn "../../../bedrock/latest/APIReference/API_CreateCustomModel.md#bedrock-CreateCustomModel-request-modelKmsKeyArn") API leveraging the encrypted model.
    + The identity calling the `CreateTrainingJob` API (rather than the execution role) must have permissions to `CreateGrant`, `RetireGrant`, `Encrypt`, and `GenerateDataKey` as defined in KMS key policy.

- [**SageMaker AI HyperPod**](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md") offers a
  specialized environment to train Amazon Nova models by requiring you to create and manage
  EKS clusters with restricted instance groups (RIGs). This environment
  gives you flexibility in configuring your training environment with specialized GPU
  instances and integrated Amazon FSx for Lustre storage, making it particularly well-suited
  for advanced distributed training scenarios and ongoing model development. For more
  information, see [Amazon Nova customization on SageMaker AI Hyperpod](nova-hp.md "nova-hp.md") .

###### In this chapter

- [General prerequisites](nova-model-general-prerequisites.md "nova-model-general-prerequisites.md")
- [Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md")
- [Amazon Nova customization on SageMaker AI training jobs](nova-model-training-job.md "nova-model-training-job.md")
- [Amazon Nova customization on SageMaker AI Hyperpod](nova-hp.md "nova-hp.md")
- [Iterative Training](nova-iterative-training.md "nova-iterative-training.md")
