# Features of DLAMI

The features of AWS Deep Learning AMIs (DLAMI) include preinstalled deep learning frameworks, GPU
software, model servers, and model visualization tools.

## Preinstalled frameworks

There are currently two primary flavors of DLAMI with other variations related to the
operating system (OS) and software versions:

- [Deep Learning AMI with Conda](overview-conda.md "overview-conda.md") – Frameworks installed separately using `conda`
  packages and separate Python environments.
- [Deep Learning Base AMI](overview-base.md "overview-base.md") – No frameworks installed; only [NVIDIA CUDA](https://developer.nvidia.com/cuda-zone "https://developer.nvidia.com/cuda-zone") and other
  dependencies.

The Deep Learning AMI with Conda uses `conda` environments to isolate each framework, so you can
switch between them at will and not worry about their dependencies conflicting. The Deep Learning AMI with Conda
supports the following frameworks:

- PyTorch
- TensorFlow 2

###### Note

DLAMI no longer supports the following deep learning frameworks: Apache MXNet, Microsoft
Cognitive Toolkit (CNTK), Caffe, Caffe2, Theano, Chainer, and Keras.

## Preinstalled GPU software

Even if you use a CPU-only instance, the DLAMIs will have [NVIDIA CUDA](https://developer.nvidia.com/cuda-zone "https://developer.nvidia.com/cuda-zone") and
[NVIDIA cuDNN](https://developer.nvidia.com/cudnn "https://developer.nvidia.com/cudnn"). The installed software is the same regardless of the instance type. Keep in
mind that GPU-specific tools work only on an instance that has at least one GPU. For more
information about instance types, see [Choosing a DLAMI instance type](instance-select.md "instance-select.md").

For more information about CUDA, see [CUDA Installations and Framework Bindings](overview-cuda.md "overview-cuda.md").

## Model serving and visualization

Deep Learning AMI with Conda comes preinstalled with model servers for TensorFlow, as well as TensorBoard
for model visualizations. For more information, see [TensorFlow Serving](tutorial-tfserving.md "tutorial-tfserving.md").
