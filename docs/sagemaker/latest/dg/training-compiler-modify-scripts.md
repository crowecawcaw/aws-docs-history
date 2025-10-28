# Bring Your Own Deep Learning

Model

###### Important

Amazon Web Services (AWS) announces that there will be no new releases or
versions of SageMaker Training Compiler. You can continue to utilize SageMaker Training Compiler through the existing AWS
Deep Learning Containers (DLCs) for SageMaker Training. It is important to note that
while the existing DLCs remain accessible, they will no longer receive patches or
updates from AWS, in accordance with the [AWS Deep Learning Containers Framework Support Policy](../../../deep-learning-containers/latest/devguide/support-policy.md "../../../deep-learning-containers/latest/devguide/support-policy.md").

This guide walks you through how to adapt your training script for a
compiler-accelerated training job. The preparation of your training script depends on
the following:

- Training settings such as single-core or distributed training.
- Frameworks and libraries that you use to create the training script.
  Choose one of the following topics depending on the framework you use.

###### Topics

- [PyTorch](training-compiler-pytorch-models.md "training-compiler-pytorch-models.md")
- [TensorFlow](training-compiler-tensorflow.md "training-compiler-tensorflow.md")

###### Note

After you finish preparing your training script, you can run a SageMaker training job
using the SageMaker AI framework estimator classes. For more information, see the previous
topic at [Enable SageMaker Training Compiler](training-compiler-enable.md "training-compiler-enable.md").
