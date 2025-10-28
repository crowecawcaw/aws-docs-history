# Using the DLAMI with AWS Neuron

A typical workflow with the AWS Neuron SDK is to compile a previously trained machine
learning model on a compilation server. After this, distribute the artifacts to the Inf1
instances for execution. AWS Deep Learning AMIs (DLAMI) comes pre-installed with everything you need to
compile and run inference in an Inf1 instance that uses Inferentia.

The following sections describe how to use the DLAMI with Inferentia.

###### Contents

- [Using TensorFlow-Neuron and the AWS Neuron Compiler](tutorial-inferentia-tf-neuron.md "tutorial-inferentia-tf-neuron.md")
- [Using AWS Neuron TensorFlow Serving](tutorial-inferentia-tf-neuron-serving.md "tutorial-inferentia-tf-neuron-serving.md")
- [Using MXNet-Neuron and the AWS Neuron Compiler](tutorial-inferentia-mxnet-neuron.md "tutorial-inferentia-mxnet-neuron.md")
- [Using MXNet-Neuron Model Serving](tutorial-inferentia-mxnet-neuron-serving.md "tutorial-inferentia-mxnet-neuron-serving.md")
- [Using PyTorch-Neuron and the AWS Neuron
  Compiler](tutorial-inferentia-pytorch-neuron.md "tutorial-inferentia-pytorch-neuron.md")
