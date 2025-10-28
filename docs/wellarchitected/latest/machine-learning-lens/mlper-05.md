# MLPER-05: Optimize training and inference instance types

Determine how the model type and data velocity affect the choice
of training and inference instance types. Identify the right
instance type that supports memory intensive training, or
compute intensive training with high throughput and low latency
real-time inference. The speed of model inferences is directly
impacted by model complexity. Selection of high compute
instances can accelerate inference speed. GPUs are often the
preferred processor type to train many deep learning models.
CPUs are often sufficient for the inference workloads.

## Implementation plan

- **Experiment with alternative
  instance types to train and deploy** - Determine
  which instance types are most appropriate for your ML
  algorithm and use case. Use multiple instances for
  training for large datasets to take advantage of scale.

## Documents

- [Use
  Amazon SageMaker AI Notebook Instances](../../../sagemaker/latest/dg/nbi.md "../../../sagemaker/latest/dg/nbi.md")
- [Train
  a Model with Amazon SageMaker AI](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md")
- [Distributed
  training libraries](https://aws.amazon.com/sagemaker/distributed-training/ "https://aws.amazon.com/sagemaker/distributed-training/")

## Blogs

- [Learn
  how to select ML instances on the fly in Amazon SageMaker AI
  Studio](https://aws.amazon.com/blogs/machine-learning/learn-how-to-select-ml-instances-on-the-fly-in-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/learn-how-to-select-ml-instances-on-the-fly-in-amazon-sagemaker-studio/")
- [Optimizing
  I/O for GPU performance tuning of deep learning training
  in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-i-o-for-gpu-performance-tuning-of-deep-learning-training-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/optimizing-i-o-for-gpu-performance-tuning-of-deep-learning-training-in-amazon-sagemaker/")
- [Right-sizing
  resources and avoiding unnecessary costs in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/right-sizing-resources-and-avoiding-unnecessary-costs-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/right-sizing-resources-and-avoiding-unnecessary-costs-in-amazon-sagemaker/")

## Videos

- [How
  to choose the right instance type for ML inference](https://www.youtube.com/watch?v=0DSgXTN7ehg "https://www.youtube.com/watch?v=0DSgXTN7ehg")
- [The
  right instance type in Amazon SageMaker AI](https://www.youtube.com/watch?v=vRB9Uncsia8 "https://www.youtube.com/watch?v=vRB9Uncsia8")

## Examples

- [Amazon SageMaker AI End-to-End Example](https://github.com/aws/amazon-sagemaker-examples/tree/master/end_to_end "https://github.com/aws/amazon-sagemaker-examples/tree/master/end_to_end")
