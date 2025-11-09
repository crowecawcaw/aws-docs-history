# Custom Docker containers with SageMaker AI

You can adapt an existing Docker image to work with SageMaker AI. You may need to use an
existing, external Docker image with SageMaker AI when you have a container that satisfies
feature or safety requirements that are not currently supported by a pre-built SageMaker AI
image. There are two toolkits that allow you to bring your own container and adapt it to
work with SageMaker AI:

- [SageMaker Training
  Toolkit](https://github.com/aws/sagemaker-training-toolkit "https://github.com/aws/sagemaker-training-toolkit") – Use this toolkit for training models with SageMaker AI.
- [SageMaker AI Inference
  Toolkit](https://github.com/aws/sagemaker-inference-toolkit "https://github.com/aws/sagemaker-inference-toolkit") – Use this toolkit for deploying models with SageMaker AI.
  The following topics show how to adapt your existing image using the SageMaker Training and
  Inference toolkits:

###### Topics

- [Individual Framework
  Libraries](#docker-containers-adapt-your-own-frameworks "#docker-containers-adapt-your-own-frameworks")
- [SageMaker Training and Inference Toolkits](amazon-sagemaker-toolkits.md "amazon-sagemaker-toolkits.md")
- [Adapting your own training container](adapt-training-container.md "adapt-training-container.md")
- [Adapt your own inference container for
  Amazon SageMaker AI](adapt-inference-container.md "adapt-inference-container.md")

## Individual Framework

Libraries

In addition to the SageMaker Training Toolkit and SageMaker AI Inference Toolkit, SageMaker AI also
provides toolkits specialized for TensorFlow, MXNet, PyTorch, and Chainer. The
following table provides links to the GitHub repositories that contain the source
code for each framework and their respective serving toolkits. The instructions
linked are for using the Python SDK to run training algorithms and host models on
SageMaker AI. The functionality for these individual libraries is included in the SageMaker AI
Training Toolkit and SageMaker AI Inference Toolkit.

| Framework    | Toolkit Source Code                                                                                                                                                                                                                                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TensorFlow` | [SageMaker AI TensorFlow Training](https://github.com/aws/sagemaker-tensorflow-training-toolkit "https://github.com/aws/sagemaker-tensorflow-training-toolkit")<br>[SageMaker AI TensorFlow Serving](https://github.com/aws/sagemaker-tensorflow-serving-container "https://github.com/aws/sagemaker-tensorflow-serving-container") |
| `MXNet`      | [SageMaker AI MXNet Training](https://github.com/aws/sagemaker-mxnet-training-toolkit "https://github.com/aws/sagemaker-mxnet-training-toolkit")<br>[SageMaker AI MXNet Inference](https://github.com/aws/sagemaker-mxnet-inference-toolkit "https://github.com/aws/sagemaker-mxnet-inference-toolkit")                             |
| `PyTorch`    | [SageMaker AI PyTorch Training](https://github.com/aws/sagemaker-pytorch-training-toolkit "https://github.com/aws/sagemaker-pytorch-training-toolkit")<br>[SageMaker AI PyTorch Inference](https://github.com/aws/sagemaker-pytorch-inference-toolkit "https://github.com/aws/sagemaker-pytorch-inference-toolkit")                 |
| `Chainer`    | [SageMaker AI Chainer SageMaker AI Containers](https://github.com/aws/sagemaker-chainer-container "https://github.com/aws/sagemaker-chainer-container")                                                                                                                                                                             |
