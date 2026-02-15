# Amazon Nova customization on SageMaker AI training jobs

SageMaker AI training jobs is an environment that enables you to train machine learning models
at scale. It automatically provisions and scales compute resources, loads training data from
sources like Amazon S3, executes your training code, and stores the resulting model
artifacts.

The purpose of training is to customize the base Amazon Nova model using your proprietary data.
The training process typically involves steps to prepare your data, choose a [recipe](../../../sagemaker/latest/dg/nova-model-recipes.md "../../../sagemaker/latest/dg/nova-model-recipes.md"), modify configuration parameters in YAML files, and submit a training
job. The training process will output trained model checkpoint in a service-managed Amazon S3
bucket. You can use this checkpoint location for evaluation jobs. Nova customization on SageMaker AI
training jobs stores model artifacts in a service-managed Amazon S3 bucket. Artifacts in the
service-managed bucket are encrypted with SageMaker AI-managed KMS keys. Service-managed Amazon S3
buckets don't currently support data encryption using customer-managed KMS keys.

For best practices, see [Best Practices](nova-forge-sft.md#best-practices "nova-forge-sft.md#best-practices").

###### Topics

- [Nova Customization SDK](nova-customization-sdk.md "nova-customization-sdk.md")
- [Fine-tune Nova 2.0](nova-fine-tune-2.md "nova-fine-tune-2.md")
- [Monitoring Progress Across Iterations](nova-model-monitor.md "nova-model-monitor.md")
- [Evaluating your SageMaker AI-trained model](nova-model-evaluation.md "nova-model-evaluation.md")
- [Reinforcement Fine-Tuning (RFT) with Amazon Nova models](nova-reinforcement-fine-tuning.md "nova-reinforcement-fine-tuning.md")
