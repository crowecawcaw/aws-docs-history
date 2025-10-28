# MLCOST-14: Use managed training capabilities

Machine learning model training can be an iterative, compute
intensive, and time-consuming process. Instead of using the
notebook itself, which might be running on a small instance,
consider offloading the training to a managed cluster of compute
resources including both CPUs and GPUs to train the model. 

## Implementation plan

- **Use Amazon SageMaker AI managed
  training capabilities** - Amazon SageMaker AI
  reduces the time and cost to train and tune ML models
  without the need to manage infrastructure. With SageMaker AI,
  easily train and tune ML models using built-in tools to
  manage and track training experiments, automatically
  choose optimal hyperparameters, debug training jobs, and
  monitor the utilization of system resources such as GPUs,
  CPUs, and network bandwidth. SageMaker AI can automatically
  scale infrastructure up or down based on your training job
  requirements, from one GPU to thousands, or from terabytes
  to petabytes of storage. SageMaker AI also offers the
  highest-performing ML compute infrastructure currently
  available, which can
  reduce ML training costs by up to 60% compared with
  previous generations. And, since you pay only for what you
  use, you can manage your training costs more effectively.
- **Use the
  [Amazon SageMaker AI Training Compiler](../../../sagemaker/latest/dg/training-compiler.md "../../../sagemaker/latest/dg/training-compiler.md")** - To train
  deep learning (DL) models faster, you can use the Amazon SageMaker AI Training Compiler to accelerate the model
  training process by up to 50% through graph- and
  kernel-level optimizations that make more efficient use of
  GPUs. Moreover, you can add either data parallelism or
  model parallelism to your training script with a few lines
  of code, and the SageMaker AI distributed training libraries
  will automatically split models and training datasets
  across GPU instances to help you complete distributed
  training faster.
- **Use Amazon SageMaker AI managed Spot
  training** - Amazon SageMaker AI makes it easy to
  train machine learning models using managed Amazon EC2
  Spot Instances. Managed Spot training can optimize the
  cost of training models up to 90% over On-demand
  Instances. SageMaker AI manages the Spot interruptions on
  your behalf. You can specify which training jobs use Spot
  Instances and a stopping condition that specifies how long
  SageMaker AI waits for a job to run using Spot Instances.
  Metrics and logs generated during training runs are
  available in CloudWatch.

## Documents

- [Train
  a Model with Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md")
- [SageMaker AI
  Model Training](../../../sagemaker/latest/dg/train-model.md "../../../sagemaker/latest/dg/train-model.md")
- [Managed
  Spot Training in Amazon SageMaker AI](../../../sagemaker/latest/dg/model-managed-spot-training.md "../../../sagemaker/latest/dg/model-managed-spot-training.md")
- [Amazon SageMaker AI Training Compiler](../../../sagemaker/latest/dg/training-compiler.md "../../../sagemaker/latest/dg/training-compiler.md")

## Blogs

- [Amazon SageMaker AI Simplifies Training Deep Learning Models with
  Billions of Parameters](https://aws.amazon.com/blogs/aws/amazon-sagemaker-simplifies-training-deep-learning-models-with-billions-of-parameters/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-simplifies-training-deep-learning-models-with-billions-of-parameters/")
- [Choose
  the best data source for your Amazon SageMaker AI training
  job](https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/ "https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/")
- [Managed
  Spot Training: Save Up to 90% On Your Amazon SageMaker AI
  Training Jobs](https://aws.amazon.com/blogs/aws/managed-spot-training-save-up-to-90-on-your-amazon-sagemaker-training-jobs/ "https://aws.amazon.com/blogs/aws/managed-spot-training-save-up-to-90-on-your-amazon-sagemaker-training-jobs/")
- [Cinnamon
  AI saves 70% on ML model training costs with Amazon SageMaker AI Managed Spot Training](https://aws.amazon.com/blogs/machine-learning/cinnamon-ai-saves-70-on-ml-model-training-costs-with-amazon-sagemaker-managed-spot-training/ "https://aws.amazon.com/blogs/machine-learning/cinnamon-ai-saves-70-on-ml-model-training-costs-with-amazon-sagemaker-managed-spot-training/")

## Examples

- [Optimizing
  and Scaling Machine Learning Training](https://aws.amazon.com/getting-started/hands-on/managed-spot-training-sagemaker/ "https://aws.amazon.com/getting-started/hands-on/managed-spot-training-sagemaker/")
