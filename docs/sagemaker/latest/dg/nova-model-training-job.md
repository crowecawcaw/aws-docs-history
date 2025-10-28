# Amazon Nova customization on SageMaker training

jobs

Amazon SageMaker training jobs is an environment that enables you to train machine learning
models at scale. It automatically provisions and scales compute resources, loads
training data from sources like Amazon S3, executes your training code, and stores the
resulting model artifacts.

The purpose of training is to customize the base Amazon Nova model using your proprietary
data. The training process typically involves steps to prepare your data, choose a
recipe, modify configuration parameters in YAML files, and submit a training job. The
training process will output trained model checkpoint in a service-managed Amazon S3 bucket.
You can use this checkpoint location for evaluation jobs. Nova customization on SageMaker
training jobs stores model artifacts in a service-managed Amazon S3 bucket. Artifacts in the
service-managed bucket are encrypted with SageMaker-managed KMS keys. Service-managed Amazon S3
buckets don't currently support data encryption using customer-managed
KMS keys.

###### Topics

- [Amazon Nova distillation](nova-distillation.md "nova-distillation.md")
- [Fine-tuning Amazon Nova models using SageMaker training
  jobs](nova-fine-tuning-training-job.md "nova-fine-tuning-training-job.md")
- [Evaluating your SageMaker AI-trained model](nova-model-evaluation.md "nova-model-evaluation.md")
