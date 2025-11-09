# AWS Deep Learning Containers for PyTorch 2.7 Training on EC2, ECS and EKS

[AWS Deep Learning Containers (DLCs)](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") for Amazon EC2, ECS and EKS are now available with PyTorch 2.7 and support for CUDA 12.8 on Ubuntu 22.04. You can launch the new versions of the Deep Learning Containers on any of the EC2, ECS and EKS service(s). For a complete list of frameworks and versions supported by the AWS Deep Learning Containers, see below.

This release includes container images for Training on GPU, optimized for performance and scale on AWS. These Docker images have been tested with the EC2, ECS and EKS service(s), and provide stable versions of NVIDIA CUDA, Intel MKL, and other components to provide an optimized user experience for running deep learning workloads on AWS. All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices. These new DLC are designed to be used on the EC2, ECS and EKS service.

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers") to get launch announcements and post your questions.

## Release Notes

- Introduced containers for PyTorch 2.7 for Training which support EC2, ECS and EKS. For details about this release, check out our GitHub [release tag.](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-ec2-2.7.1-tr-py312 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-ec2-2.7.1-tr-py312")
- Please refer to the official PyTorch 2.7.1 release notes [here](https://github.com/PyTorch/PyTorch/releases/tag/v2.7.1 "https://github.com/PyTorch/PyTorch/releases/tag/v2.7.1").
- Added Python 3.12 support
- Added PyTorch domain libraries:
  - torchtnt 0.2.4
  - torchdata 0.11.0
  - torchaudio 2.7.1
  - torchvision 0.22.1

- Added CUDA 12.8 support
- Added Ubuntu 22.04 support
- The GPU Docker Image includes the following libraries:
  - CUDA 12.8.0
  - cuDNN 9.7.1.26
  - NCCL 2.26.2
  - EFA installer 1.40.0 (with AWS OFI NCCL embedded)
  - Transformer Engine 2.3
  - Flash Attention 2.7.4.post1
  - GDRCopy 2.5

- Added fastai 2.8.2 support
- The Dockerfile for CPU can be found [here](https://github.com/aws/deep-learning-containers/blob/master/pytorch/training/docker/2.7/py3/Dockerfile.cpu "https://github.com/aws/deep-learning-containers/blob/master/pytorch/training/docker/2.7/py3/Dockerfile.cpu"), and the Dockerfile for GPU can be found [here](https://github.com/aws/deep-learning-containers/blob/master/pytorch/training/docker/2.7/py3/cu128/Dockerfile.gpu "https://github.com/aws/deep-learning-containers/blob/master/pytorch/training/docker/2.7/py3/cu128/Dockerfile.gpu").

**For latest updates, please refer to the [aws/deep-learning-containers GitHub repo.](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags")**

## Security Advisory

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python 3.12 Support

Python 3.12 is supported in the PyTorch Training containers.

## CPU Instance Type Support

The containers support x86_64 instance types.

## GPU Instance Type support

The containers support GPU instance types and contain the following software components for GPU support:

- CUDA 12.8
- cuDNN 9.7.1.26
- NCCL 2.26.2

## AWS Regions support

The containers are available in the following regions:

| Region                   | Code           |
| ------------------------ | -------------- |
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
| Asia Pacific (Thailand)  | ap-southeast-7 |
| Mexico (Central)         | mx-central-1   |
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
| China (Ningxia)          | cn-northwest-1 |

## Build and Test

- Built on: c5.18xlarge
- Tested on: p4d.24xlarge, p4de.24xlarge, p5.48xlarge, g4dn.4xlarge, g5.24xlarge, g5.12xlarge
- Tested with Resnet50, BERT along with ImageNet datasets on EC2, ECS AMI (Amazon Linux AMI 2.0.20250605), and EKS AMI (amazon-eks-gpu-node-1.32.3-20250610)
