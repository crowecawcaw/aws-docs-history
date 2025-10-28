# Pre-built SageMaker AI Docker images

Amazon SageMaker AI provides containers for its built-in algorithms and pre-built Docker images
for some of the most common machine learning frameworks, such as Apache MXNet,
TensorFlow, PyTorch, and Chainer. It also supports machine learning libraries such as
scikit-learn and SparkML.

You can use these images from your SageMaker notebook instance or SageMaker Studio. You can also
extend the pre-built SageMaker images to include libraries and needed functionality. The
following topics give information about the available images and how to use them.

For the Docker registry path and other parameters for each of the Amazon SageMaker AI provided
algorithms and Deep Learning Containers (DLC), see [Docker
Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md").

For information on Docker images for developing reinforcement learning (RL)
solutions in SageMaker AI, see [SageMaker AI RL Containers](https://github.com/aws/sagemaker-rl-container "https://github.com/aws/sagemaker-rl-container").

###### Note

Pre-built container images are owned by SageMaker AI, and in some cases include proprietary code.
Capabilities such as training and processing jobs, batch transform, and real-time inference
use service-owned credentials to pull and run images on managed SageMaker AI instances. Because customer
credentials aren't used, any AWS IAM policies (including service control policies and resource
control policies) that deny Amazon ECR permissions don't prevent the use of pre-built images.

###### Topics

- [Prebuilt SageMaker image support policy](pre-built-containers-support-policy.md "pre-built-containers-support-policy.md")
- [Prebuilt SageMaker AI Docker images
  for deep learning](pre-built-containers-frameworks-deep-learning.md "pre-built-containers-frameworks-deep-learning.md")
- [Accessing Docker
  Images for Scikit-learn and Spark ML](pre-built-docker-containers-scikit-learn-spark.md "pre-built-docker-containers-scikit-learn-spark.md")
- [Deep Graph Networks](deep-graph-library.md "deep-graph-library.md")
- [Extend a Pre-built
  Container](prebuilt-containers-extend.md "prebuilt-containers-extend.md")
