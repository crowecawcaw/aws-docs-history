# Customizing Amazon Nova models on SageMaker AI

You can customize Amazon Nova models, including the enhanced Amazon Nova 2.0 models, through [recipes](nova-model-recipes.md#nova-model-get-recipes "nova-model-recipes.md#nova-model-get-recipes") and train them on SageMaker AI. These recipes support techniques such as supervised fine-tuning (SFT), Direct Preference Optimization (DPO), and Reinforcement Fine-Tuning (RFT), with both full-rank and low-rank adaptation (LoRA) options.

The end-to-end customization workflow involves stages like model training, model evaluation, and deployment for inference. This model customization approach on SageMaker AI provides greater flexibility and control to fine-tune its supported Amazon Nova models, optimize hyperparameters with precision, and implement techniques such as LoRA parameter-efficient fine-tuning (PEFT), full-rank SFT, DPO, RFT, Continued Pre-Training (CPT), Proximal Policy Optimization (PPO), etc.

## Customization approaches

SageMaker AI offers two approaches for customizing Amazon Nova models:

**UI-based experience** – Use to customize Amazon Nova models through a simple, guided interface. This approach provides an end-to-end workflow including training, evaluation, and deployment without writing code. The UI-based experience is ideal for rapid experimentation, proof-of-concept development, and users who prefer a visual workflow.

**Code-based experience** – Use the SageMaker AI Python SDK, Nova SDK and training recipes to customize models programmatically. This approach offers greater flexibility, allowing you to configure advanced hyperparameters, integrate with CI/CD pipelines, and automate training workflows. The code-based experience is recommended for production workloads, complex customization requirements, and teams with established MLOps practices.

| Approach   | Best for                                        | Key benefits                                            |
| ---------- | ----------------------------------------------- | ------------------------------------------------------- |
| UI-based   | Experimentation, prototyping, quick iterations  | Simple setup, guided workflow, no coding required       |
| Code-based | Production, automation, advanced configurations | Full flexibility, pipeline integration, version control |

## Customization platforms

AWS offers three platforms for customizing Amazon Nova models, each designed for different use cases and requirements:

**Amazon Bedrock** – Provides the easiest and fastest path to model customization with minimal setup. Bedrock handles all infrastructure management automatically, allowing you to focus on your data and use case. This platform is ideal when you need the quickest time-to-value and prefer a fully managed experience.

**SageMaker AI training jobs** – Provides a fully managed environment for customizing Amazon Nova models where you don't need to create or maintain any clusters. The service automatically handles all infrastructure provisioning, scaling, and resource management, allowing you to focus on configuring your training parameters and submitting your job. This platform offers a balance between ease of use and flexibility, supporting techniques like Parameter Efficient Fine-tuning (PEFT), Full rank fine tuning, Direct Preference Optimization (DPO), and Reinforcement Fine-Tuning (RFT).

**SageMaker AI HyperPod** – Offers a specialized environment for large-scale distributed training by requiring you to create and manage EKS clusters with restricted instance groups (RIGs). This platform gives you maximum flexibility in configuring your training environment with specialized GPU instances and integrated Amazon FSx for Lustre storage, making it particularly well-suited for advanced distributed training scenarios, ongoing model development, and enterprise-scale customization workloads.

| Platform                   | Complexity | Flexibility | Best for                                         |
| -------------------------- | ---------- | ----------- | ------------------------------------------------ |
| Amazon Bedrock             | Lowest     | Standard    | Fastest customization, minimal setup             |
| SageMaker AI training jobs | Medium     | High        | Balanced flexibility and ease of use             |
| SageMaker AI HyperPod      | Highest    | Maximum     | Large distributed training, enterprise workloads |

###### Note

If you provide a KMS key to your Amazon Nova model customization training job for encryption in the Amazon-owned output S3 bucket:

- You must provide the same KMS key when calling subsequent iterative training jobs, or when calling the Amazon Bedrock CreateCustomModel API leveraging the encrypted model.
- The identity calling the `CreateTrainingJob` API (rather than the execution role) must have permissions to `CreateGrant`, `RetireGrant`, `Encrypt`, and `GenerateDataKey` as defined in KMS key policy.
