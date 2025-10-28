# MLCOST-25: Explore cost effective hardware options

Machine learning models that power AI applications are becoming
increasingly complex resulting in rising underlying compute
infrastructure costs. Up to 90% of the infrastructure spend for
developing and running ML applications is often on inference.
Look for cost-effective infrastructure solutions for deploying
their ML applications in production.

## Implementation plan

- **Use Amazon SageMaker AI
  Neo** - Please see details of Amazon SageMaker AI
  Neo under “MLPER-10: Evaluate machine learning deployment
  option (cloud versus edge)”. For inference in the cloud,
  SageMaker AI Neo speeds up inference and saves cost by
  creating an inference optimized container in SageMaker AI
  hosting. For inference at the edge, SageMaker AI Neo saves
  developers months of manual tuning by automatically tuning
  the model for the selected operating system and processor
  hardware.
- **Use Amazon SageMaker AI Elastic Inference** - Amazon Elastic Inference (EI) is a
  service that lets you attach just the right amount of
  GPU-powered inference acceleration to any EC2 instance. By
  using Amazon EI, you can speed up the throughput and
  decrease the latency of getting real-time inferences from
  your deep learning models that are deployed as
  [Amazon SageMaker AI hosted models](../../../sagemaker/latest/dg/deploy-model.md "../../../sagemaker/latest/dg/deploy-model.md"), but at a fraction of the
  cost of using a GPU instance for your endpoint. Add an
  Amazon EI accelerator in one of the available sizes to a
  deployable model in addition to a CPU instance type, and
  then add that model as a production variant to an endpoint
  configuration that you use to deploy a hosted endpoint.
  You can also add an Amazon EI accelerator to a SageMaker AI
  [notebook
  instance](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md") so that you can test and evaluate
  inference performance when you are building your models.
- **Use Amazon EC2 Inf1
  Instances** - Amazon EC2 Inf1 instances deliver
  high-performance ML inference at the lowest cost in the
  cloud. They deliver up to 2.3-times higher throughput and
  up to 70% lower cost per inference than comparable current
  generation GPU-based Amazon EC2 instances. Inf1 instances
  are built from the ground up to support machine learning
  inference applications. They feature up to 16 AWS
  Inferentia chips, high-performance machine learning
  inference chips designed and built by AWS. Additionally,
  Inf1 instances include second generation Intel Xeon
  Scalable processors and up to 100 Gbps networking to
  deliver high throughput inference.

## Documents

- [Use
  Amazon SageMaker AI Elastic Inference](../../../sagemaker/latest/dg/ei.md "../../../sagemaker/latest/dg/ei.md")
- [What
  Is Amazon Elastic Inference?](../../../elastic-inference/latest/developerguide/what-is-ei.md "../../../elastic-inference/latest/developerguide/what-is-ei.md")
- [Optimize
  model performance using Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md")
- [Amazon EC2 Inf1 Instances](https://aws.amazon.com/ec2/instance-types/inf1/ "https://aws.amazon.com/ec2/instance-types/inf1/")

## Blogs

- [Increasing
  performance and reducing the cost of MXNet inference using
  Amazon SageMaker AI Neo and Amazon Elastic Inference](https://aws.amazon.com/blogs/machine-learning/increasing-performance-and-reducing-the-cost-of-mxnet-inference-using-amazon-sagemaker-neo-and-amazon-elastic-inference/ "https://aws.amazon.com/blogs/machine-learning/increasing-performance-and-reducing-the-cost-of-mxnet-inference-using-amazon-sagemaker-neo-and-amazon-elastic-inference/")
- [Reduce
  ML inference costs on Amazon SageMaker AI with hardware and
  software acceleration](https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/ "https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/")
- [Announcing
  availability of Inf1 instances in Amazon SageMaker AI for
  high performance and cost-effective machine learning inference](https://aws.amazon.com/blogs/machine-learning/announcing-availability-of-inf1-instances-in-amazon-sagemaker-for-high-performance-and-cost-effective-machine-learning-inference/ "https://aws.amazon.com/blogs/machine-learning/announcing-availability-of-inf1-instances-in-amazon-sagemaker-for-high-performance-and-cost-effective-machine-learning-inference/")

## Examples

- [Increasing
  performance and reducing cost of deep learning inference using Amazon SageMaker AI Neo and Amazon Elastic Inference](https://github.com/dheepanr/MxNet-Sagemaker-Deployments "https://github.com/dheepanr/MxNet-Sagemaker-Deployments")
