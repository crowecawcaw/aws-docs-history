# With Amazon SageMaker AI

###### Note

This documentation is for Amazon Nova Version 1. Amazon Nova 2 is now available with new models
and enhanced capabilities. For information on how to customize Amazon Nova 2, visit [Customizing Amazon Nova 2 models](../nova2-userguide/customization.md "../nova2-userguide/customization.md").

Developers sometimes require greater control and flexibility when customizing Amazon Nova
models. With SageMaker AI, you can leverage larger labeled datasets, perform deeper customization
(such as preference optimization or full rank fine-tuning), and access enhanced capabilities
for hyperparameter optimization and active train-loss curve analysis. You can perform these
advanced customization features on Amazon Nova models in the SageMaker AI platform.

With Amazon Nova customization using SageMaker AI, you can launch SageMaker training
jobs or launch jobs on SageMaker AI Hyperpod.

###### Topics

- [SageMaker AI Training Jobs](custom-fine-tune-models-sagemaker-tj.md "custom-fine-tune-models-sagemaker-tj.md")
- [SageMaker AI HyperPod training](customize-fine-tune-hyperpod.md "customize-fine-tune-hyperpod.md")
- [Evaluate your custom training jobs](customize-fine-tune-evaluate.md "customize-fine-tune-evaluate.md")
- [Amazon Amazon Nova Customization SDK](#customization-sdk "#customization-sdk")

## Amazon Amazon Nova Customization SDK

The Amazon Nova Customization SDK is a comprehensive Python SDK that provides a unified,
programmatic interface for the complete Amazon Amazon Nova model customization lifecycle. The SDK
simplifies model customization by offering a single, consistent API for training,
evaluation, monitoring, deployment, and inference across SageMaker AI and Amazon Bedrock platforms.
For more information, go to [Amazon Amazon Nova Customization SDK](../../../sagemaker/latest/dg/nova-customization-sdk.md "../../../sagemaker/latest/dg/nova-customization-sdk.md").
