

# Customizing Amazon Nova models on SageMaker AI
<a name="nova-model"></a>

**Note**  
This documentation is for Amazon Nova Version 1. Amazon Nova 2 is now available with new models and enhanced capabilities. For information on how to customize Amazon Nova 2, visit [Customizing Amazon Nova 2 models](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model.html).

You can customize [Amazon Nova models](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html), including the enhanced Amazon Nova 2.0 models, through [recipes](nova-model-recipes.md#nova-model-get-recipes) and train them on SageMaker. These recipes support techniques such as supervised fine-tuning (SFT), Direct Preference Optimization (DPO), and Reinforcement Fine-Tuning (RFT), with both full-rank and low-rank adaptation (LoRA) options.

The end-to-end customization workflow involves stages like model training, model evaluation, and deployment for inference. This model customization approach on SageMaker provides greater flexibility and control to fine-tune its supported Amazon Nova models, optimize hyperparameters with precision, and implement techniques such as LoRA parameter-efficient fine-tuning (PEFT), full-rank SFT, DPO, RFT, Continued Pre-Training (CPT), Proximal Policy Optimization (PPO), etc.

SageMaker offers two environments for customizing Amazon Nova models.
+ [**SageMaker training jobs**](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) provides a fully managed environment for customizing Amazon Nova models where you don't need to create or maintain any clusters. The service automatically handles all infrastructure provisioning, scaling, and resource management, allowing you to focus solely on configuring your training parameters and submitting your job. You can customize Nova models on SageMaker training jobs with techniques like Parameter Efficient Fine-tuning (PEFT), Full rank fine tuning, Direct Preference Optimization (DPO), and Reinforcement Fine-Tuning (RFT). For more information, see [Amazon Nova customization on SageMaker Training Jobs](nova-model-training-job.md).
**Note**  
If you provide a KMS key to your Amazon Nova model customization training job for encryption in the Amazon-owned output S3 bucket:  
You must provide the same KMS key when calling subsequent [iterative training jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-iterative-training.html), or when calling the Amazon Bedrock [CreateCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModel.html#bedrock-CreateCustomModel-request-modelKmsKeyArn) API leveraging the encrypted model.
The identity calling the `CreateTrainingJob` API (rather than the execution role) must have permissions to `CreateGrant`, `RetireGrant`, `Encrypt`, and `GenerateDataKey` as defined in KMS key policy.
+ [**SageMaker HyperPod**](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) offers a specialized environment to train Amazon Nova models by requiring you to create and manage SageMaker HyperPod EKS clusters with restricted instance groups (RIGs). This environment gives you flexibility in configuring your training environment with specialized GPU instances and integrated Amazon FSx for Lustre storage, making it particularly well-suited for advanced distributed training scenarios and ongoing model development. For more information, see [Amazon Nova customization on SageMaker HyperPod](nova-hp.md).

**Topics**
+ [General prerequisites](nova-model-general-prerequisites.md)
+ [Amazon Nova recipes](nova-model-recipes.md)
+ [Amazon Nova customization on SageMaker Training Jobs](nova-model-training-job.md)
+ [Amazon Nova customization on SageMaker HyperPod](nova-hp.md)
+ [Iterative Training](nova-iterative-training.md)
+ [Model Merge](nova-model-merge.md)
+ [SageMaker Inference](nova-model-sagemaker-inference.md)
+ [Amazon Bedrock inference](nova-model-bedrock-inference.md)
+ [Evaluation with Inspect AI](nova-eval-inspect-ai.md)