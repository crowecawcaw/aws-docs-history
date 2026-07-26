# Infrastructure options

Amazon SageMaker AI offers three infrastructure options for model customization. Choose based on
your requirements for control, scale, and capacity access. For example, if you have
reserved compute capacity through [SageMaker AI Flexible Training
Plans](reserve-capacity-with-training-plans.md "reserve-capacity-with-training-plans.md"), you can use the customization Recipes to run customization jobs on your
reserved capacity. The difference is in how compute resources are managed.

**Recipes** are pre-configured training configurations
that work with both SageMaker AI Training Jobs and HyperPod. They automate dataset loading,
distributed training, and checkpoint management. See
[SageMaker Recipes](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes") on the GitHub website
on GitHub.

| Option                                                                                                  | What it is                                                                                                 | Interfaces                                           | Best for                                                     |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| [Serverless model customization](customize-model.md "customize-model.md")                               | Fully managed, no instance selection. Infrastructure provisioned<br>and released automatically.            | Studio UI, Python SDK (SFTTrainer, DPOTrainer, etc.) | Quick experimentation, production jobs without ops overhead  |
| [SageMaker AI Training Jobs](customizing-models-training-jobs.md "customizing-models-training-jobs.md") | Ephemeral jobs where you select instance type and count.<br>Instances released after training.             | Recipes, Python SDK (ModelTrainer)                   | Custom instance configs, advanced distributed setups         |
| [HyperPod](customizing-models-hyperpod.md "customizing-models-hyperpod.md")                             | Persistent clusters with automatic fault detection and recovery.<br>Clusters remain available across jobs. | Recipes, HP-CLI                                      | Large-scale training, long-running jobs, multi-job workflows |
