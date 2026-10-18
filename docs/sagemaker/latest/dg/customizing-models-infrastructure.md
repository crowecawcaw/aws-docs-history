

# Infrastructure options
<a name="customizing-models-infrastructure"></a>

Amazon SageMaker AI offers three infrastructure options for model customization. Choose based on your requirements for control, scale, and capacity access. For example, if you have reserved compute capacity through [SageMaker AI Flexible Training Plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html), you can use the customization Recipes to run customization jobs on your reserved capacity. The difference is in how compute resources are managed.

**Recipes** are pre-configured training configurations that work with both SageMaker AI Training Jobs and HyperPod. They automate dataset loading, distributed training, and checkpoint management. See [SageMaker Recipes](https://github.com/aws/sagemaker-hyperpod-recipes) on the GitHub website on GitHub.



- **[Serverless model customization](customize-model.md)**
  - **What it is:** Job APIs: Fully managed, no instance selection. Infrastructure provisioned and released automatically. / **Interfaces:** Studio UI, Python SDK (SFTTrainer, DPOTrainer, etc.) / **Best for:** Quick experimentation, production jobs without ops overhead
  - **What it is:** [Training session APIs](customizing-models-training-sessions.md): Interactive, long-lived sessions that expose low-level training primitives as API calls, so you drive the training loop from your own code. / **Interfaces:** Python SDK (ServiceClient), API / **Best for:** Custom training loops, multi-turn reinforcement learning (RL), multi-stage pipelines

- **[SageMaker AI Training Jobs](customizing-models-training-jobs.md)**
  - **What it is:** Ephemeral jobs where you select instance type and count. Instances released after training.
  - **Interfaces:** Recipes, Python SDK (ModelTrainer)
  - **Best for:** Custom instance configs, advanced distributed setups

- **[HyperPod](customizing-models-hyperpod.md)**
  - **What it is:** Persistent clusters with automatic fault detection and recovery. Clusters remain available across jobs.
  - **Interfaces:** Recipes, HP-CLI
  - **Best for:** Large-scale training, long-running jobs, multi-job workflows

