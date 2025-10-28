# MLCOST-12: Select an optimal ML framework

Organize, track, compare and evaluate machine learning (ML)
experiments and model versions. Identify the most cost-effective
and optimal combination of instance types and ML frameworks.
Examples of ML frameworks include TensorFlow, PyTorch, and
Scikit-learn.

## Implementation plan

- **Use Amazon SageMaker AI
  Experiments** -
  [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") lets you organize, track,
  compare, and evaluate your machine learning experiments.
  Using this service, you can experiment with various ML
  frameworks and see which one gives you the most
  cost-effective performance.
  [AWS Deep Learning](https://aws.amazon.com/machine-learning/amis/ "https://aws.amazon.com/machine-learning/amis/")
  [AMIs](https://aws.amazon.com/machine-learning/amis/ "https://aws.amazon.com/machine-learning/amis/")
  and
  [AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") enable you to use several
  open-source ML frameworks for training on your
  infrastructure. AWS Deep Learning AMIss have popular deep
  learning frameworks and interfaces preinstalled including
  TensorFlow, PyTorch, Apache MXNet, Chainer, Gluon,
  Horovod, and Keras. The AMI or container can be launched
  on powerful infrastructure that has been optimized for ML
  performance. SageMaker AI also allows you to bring your own
  container where you can use any framework you choose.

## Documents

- [Use
  Machine Learning Frameworks, Python, and R with Amazon SageMaker AI](../../../sagemaker/latest/dg/frameworks.md "../../../sagemaker/latest/dg/frameworks.md")

## Blogs

- [Right-sizing
  resources and avoiding unnecessary costs in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/right-sizing-resources-and-avoiding-unnecessary-costs-in-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/right-sizing-resources-and-avoiding-unnecessary-costs-in-amazon-sagemaker/")
- [Amazon SageMaker AI Experiments – Organize, Track and Compare your
  Machine Learning Trainings](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/")
