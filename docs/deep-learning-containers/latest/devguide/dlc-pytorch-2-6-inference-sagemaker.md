# AWS Deep Learning Containers for PyTorch 2.6 Inference on SageMaker

[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") (DLC) for Amazon SageMaker are now available with support for PyTorch 2.6 and support for CUDA 12.4 on Ubuntu 22.04. You can launch the new versions of the Deep Learning Containers on the SageMaker service. For a complete list of frameworks and versions supported by the AWS Deep Learning Containers, see the release notes below.

This release includes container images for inference on CPU and GPU, optimized for performance and scale on AWS. These Docker images have been tested with SageMaker services, and provide stable versions of NVIDIA CUDA, cuDNN, and other components to provide an optimized user experience for running deep learning workloads on AWS. All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices. These new DLC are designed to be used on SageMaker Inference services.

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). For latest updates, please also see the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers")to get launch announcements and post your questions.

## Release Notes

- Introduced containers for PyTorch 2.6.0 for inference supporting SageMaker services. For details about this release, check out our GitHub [release tag](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-sagemaker-2.6.0-inf-py312 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-sagemaker-2.6.0-inf-py312").
- Starting with PyTorch 2.6, we are removing Conda from the DLCs and installing all Python packages from PyPI.
- PyTorch 2.6 features multiple improvements for PT2: torch.compile can now be used with Python 3.13; new performance-related knob torch.compiler.set_stance; several AOTInductor enhancements. Besides the PT2 improvements, another highlight is FP16 support on X86 CPUs.
- Please refer to the official PyTorch 2.6.0 release notes [here](https://github.com/pytorch/pytorch/releases/tag/v2.6.0 "https://github.com/pytorch/pytorch/releases/tag/v2.6.0").
- The Dockerfile for CPU can be found [here](https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.6/py3/Dockerfile.cpu "https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.6/py3/Dockerfile.cpu"), and the Dockerfile for GPU can be found [here](https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.6/py3/cu124/Dockerfile.gpu "https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.6/py3/cu124/Dockerfile.gpu").

## Security Advisory

- AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python 3.12 Support

Python 3.12 is supported in the PyTorch Inference containers.

## CPU Instance Type Support

The containers support x86_64 CPU instance types.

## GPU Instance Type support

The containers support GPU instance types and contain the following software components for GPU support:

- CUDA 12.4.1
- cuDNN 9.1.0.70+cuda12.4
- NCCL 2.23.4+cuda12.4

## AWS Regions support

The containers are available in the following regions:

| Region                   | Code           |
| ------------------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)           | us-east-2      |
| US East (N. Virginia)    | us-east-1      |
| US West (Oregon)         | us-west-2      |
| US West (N. California)  | us-west-1      |
| AF South (Cape Town)     | af-south-1     |
| Asia Pacific (Hong Kong) | ap-east-1      |
| Asia Pacific (Hyderabad) | ap-south-2     |
| Asia Pacific (Mumbai)    | ap-south-1     |
| Asia Pacific (Osaka)     | ap-northeast-3 |
| Asia Pacific (Seoul)     | ap-northeast-2 |
| Asia Pacific (Tokyo)     | ap-northeast-1 |
| Asia Pacific (Melbourne) | ap-southeast-4 |
| Asia Pacific (Jakarta)   | ap-southeast-3 |
| Asia Pacific (Sydney)    | ap-southeast-2 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Malaysia)  | ap-southeast-5 |
| Canada (Central)         | ca-central-1   |
| Canada (Calgary)         | ca-west-1      |
| EU (Zurich)              | eu-central-2   |
| EU (Frankfurt)           | eu-central-1   |
| EU (Ireland)             | eu-west-1      |
| EU (London)              | eu-west-2      |
| EU (Paris)               | eu-west-3      |
| EU (Spain)               | eu-south-2     |
| EU (Milan)               | eu-south-1     |
| EU (Stockholm)           | eu-north-1     |
| Israel (Tel Aviv)        | il-central-1   |
| Middle East (Bahrain)    | me-south-1     |
| Middle East (UAE)        | me-central-1   |
| SA (Sau Paulo)           | sa-east-1      |
| China (Beijing)          | cn-north-1     |
| China (Ningxia)          | cn-northwest-1 | ## Build and Test <br>• Built on: c5.18xlarge <br>• Tested on: c5.18xlarge, g3.16xlarge, m5.16xlarge, t3.2xlarge, p3.16xlarge, p3dn.24xlarge, p4d.24xlarge, g4dn.xlarge, g5.24xlarge <br>• Tested with [MNIST](http://yann.lecun.com/exdb/mnist/ "http://yann.lecun.com/exdb/mnist/") on SageMaker. |
