# MLCOST-09: Select optimal computing instance size

Right size the training instances according to the ML algorithm
used for maximum efficiency and cost reduction. Use debugging
capabilities to understand the right resources to use during
training. Simple models might not train faster on larger
instances because they might not be able to benefit from
additional compute resources. These models might even train
slower due to the high GPU communication overhead. Start with
smaller instances and scale as necessary.

## Implementation plan

- **Use Amazon SageMaker AI
  Experiments** -
  [Amazon EC2](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") provides a wide selection of instance types
  optimized to fit different use cases. Machine learning
  workloads can use either a CPU or a GPU instance. Select
  an instance type from
  [the
  available EC2 instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") depending on the needs
  of your ML algorithm. Experiment with both CPU and GPU
  instances to learn which one gives you the best cost
  configuration. Amazon SageMaker AI lets you use a single
  instance or a distributed cluster of GPU instances. Use
  [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to evaluate alternative
  options, and identify the size resulting in optimal
  outcome. With the pricing broken down by time and
  resources, you can optimize the cost of Amazon SageMaker AI
  and only pay for what is needed.
- **Use Amazon SageMaker AI
  Debugger** -
  [Amazon SageMaker AI Debugger](https://aws.amazon.com/sagemaker/debugger/ "https://aws.amazon.com/sagemaker/debugger/") automatically monitors the
  utilization of system resources, such as GPUs, CPUs,
  network, and memory, and profiles your training jobs to
  collect detailed ML framework metrics. You can inspect all
  resource metrics visually through SageMaker AI Studio and
  take corrective actions if the resource is under-utilized
  to optimize cost.

## Documents

- [Amazon SageMaker AI Debugger](../../../sagemaker/latest/dg/train-debugger.md "../../../sagemaker/latest/dg/train-debugger.md")

## Blogs

- [Right-sizing
  resources and avoiding unnecessary costs in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/right-sizing-resources-and-avoiding-unnecessary-costs-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/right-sizing-resources-and-avoiding-unnecessary-costs-in-amazon-sagemaker/")
- [Identify
  bottlenecks, improve resource utilization, and reduce ML
  training costs with the deep profiling feature in Amazon SageMaker AI Debugger](https://aws.amazon.com/blogs/machine-learning/identify-bottlenecks-improve-resource-utilization-and-reduce-ml-training-costs-with-the-new-profiling-feature-in-amazon-sagemaker-debugger/ "https://aws.amazon.com/blogs/machine-learning/identify-bottlenecks-improve-resource-utilization-and-reduce-ml-training-costs-with-the-new-profiling-feature-in-amazon-sagemaker-debugger/")

## Videos

- [AWS re:Invent 2019: Choose the right instance type in Amazon SageMaker AI, with Texas Instruments](https://www.youtube.com/watch?v=vRB9Uncsia8&ab_channel=AWSEvents "https://www.youtube.com/watch?v=vRB9Uncsia8&ab_channel=AWSEvents")
