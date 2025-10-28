# Customizing Amazon Nova models on Amazon SageMaker AI

You can customize [Amazon Nova models](../../../nova/latest/userguide/what-is-nova.md "../../../nova/latest/userguide/what-is-nova.md") through [recipes](nova-model-recipes.md#nova-model-get-recipes "nova-model-recipes.md#nova-model-get-recipes") and train them on SageMaker AI. These recipes
support techniques such as supervised fine-tuning (SFT) and Direct Preference Optimization
(DPO), with both full-rank and low-rank adaptation (LoRA) options.

The end-to-end customization workflow involves stages like model training, model
evaluation, and deployment for inference. This model customization approach on SageMaker AI provides
greater flexibility and control to fine-tune its supported Amazon Nova models, optimize
hyperparameters with precision, and implement techniques such as LoRA parameter-efficient
fine-tuning (PEFT), full-rank SFT, DPO, Continued Pre-Training (CPT), Proximal Policy
Optimization (PPO), etc.

SageMaker AI offers two environments for customizing Amazon Nova models.

- [**Amazon SageMaker training jobs**](how-it-works-training.md "how-it-works-training.md") provides a
  fully managed environment for customizing Nova models where you don't need to create
  or maintain any clusters. The service automatically handles all infrastructure
  provisioning, scaling, and resource management, allowing you to focus solely on
  configuring your training parameters and submitting your job. You can customize Nova
  models on SageMaker training jobs with techniques like Parameter Efficient
  Fine-tuning (PEFT), Full rank fine tuning as well as Direct Preference Optimization
  (DPO). For more information, see [Amazon Nova customization on SageMaker training
  jobs](nova-model-training-job.md "nova-model-training-job.md").
- [**Amazon SageMaker HyperPod**](sagemaker-hyperpod.md "sagemaker-hyperpod.md") offers a
  specialized environment to train Nova models by requiring you to create and manage
  SageMaker HyperPod EKS clusters with restricted instance groups (RIGs). This environment
  gives you flexibility in configuring your training environment with specialized GPU
  instances and integrated Amazon FSx for Lustre storage, making it particularly well-suited
  for advanced distributed training scenarios and ongoing model development. For more
  information, see [Amazon Nova customization on Amazon SageMaker HyperPod](nova-hp.md "nova-hp.md").

###### In this chapter

- [General prerequisites](nova-model-general-prerequisites.md "nova-model-general-prerequisites.md")
- [Amazon Nova recipes](nova-model-recipes.md "nova-model-recipes.md")
- [Amazon Nova customization on SageMaker training
  jobs](nova-model-training-job.md "nova-model-training-job.md")
- [Amazon Nova customization on Amazon SageMaker HyperPod](nova-hp.md "nova-hp.md")
- [Iterative training](nova-hp-iterative-training.md "nova-hp-iterative-training.md")
- [Amazon Bedrock inference](nova-model-bedrock-inference.md "nova-model-bedrock-inference.md")
- [Limitations](nova-model-limitations.md "nova-model-limitations.md")
- [Amazon Nova customization FAQs](nova-model-faqs.md "nova-model-faqs.md")
