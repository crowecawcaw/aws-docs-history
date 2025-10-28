# MLOE-13: Establish reliable packaging patterns to access approved public libraries

Establish reliable packaging patterns for data scientists, which
include (a) the use of internal repositories that provide access
to public libraries and (b) the creation of separate kernels for
common ML frameworks. Examples of such common ML frameworks
include TensorFlow, PyTorch, Scikit-learn, and Keras.

## Implementation plan

- **Use container
  technology** - Use or alternatively bring custom
  containers and store them in
  [Amazon Elastic Container Registry](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md") (Amazon ECR). Using
  containers, you can train machine learning algorithms and
  deploy models quickly and reliably at any scale.
- **Use artifact repository**

* Set up
  [AWS CodeArtifact](../../../codeartifact/latest/ug/welcome.md "../../../codeartifact/latest/ug/welcome.md") to be used as a central internal
  artifact repository. This will enable pulling artifacts
  from internal repositories and reusing them.

## Documents

- [Train
  a Deep Learning model with AWS Deep Learning Containers on
  Amazon EC2](https://aws.amazon.com/getting-started/hands-on/train-deep-learning-model-aws-ec2-containers/ "https://aws.amazon.com/getting-started/hands-on/train-deep-learning-model-aws-ec2-containers/")

## Blogs

- [Private
  package installation in Amazon SageMaker AI running in
  internet-free mode](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/ "https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/")
- [Bringing
  your own custom container image to Amazon SageMaker AI Studio
  notebooks](https://aws.amazon.com/blogs/machine-learning/bringing-your-own-custom-container-image-to-amazon-sagemaker-studio-notebooks/ "https://aws.amazon.com/blogs/machine-learning/bringing-your-own-custom-container-image-to-amazon-sagemaker-studio-notebooks/")
- [Integrating
  Jenkins with AWS CodeArtifact to publish and consume
  Python artifacts](https://aws.amazon.com/blogs/devops/using-jenkins-with-codeartifact/ "https://aws.amazon.com/blogs/devops/using-jenkins-with-codeartifact/")
