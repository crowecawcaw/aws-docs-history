# AWS Deep Learning Containers for PyTorch 2.7 ARM64 Training on EC2

[AWS Deep Learning Containers (DLCs)](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") for Amazon EC2 are now available for ARM64 platforms, including [AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") instance types, with support for PyTorch 2.7 and CUDA 12.8 on Ubuntu 22.04.

This release includes a container image for Training on GPU, optimized for performance and scale on AWS EC2. The image provides stable versions of NVIDIA CUDA, cuDNN, NCCL, and other components. All software components in this image are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices.

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers") to get launch announcements and post your questions.

## Release Notes

- Introduced containers for PyTorch 2.7 for Training on EC2. For details about this release, check out our GitHub [release tag](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-arm64-ec2-2.7.0-tr-gpu-py312 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-arm64-ec2-2.7.0-tr-gpu-py312").
- This image should be used with the [G5g instance type](https://aws.amazon.com/ec2/instance-types/g5g/ "https://aws.amazon.com/ec2/instance-types/g5g/"), which is powered by Graviton CPUs and NVIDIA T4G Tensor Core GPUs.
- Please refer to the official PyTorch 2.7.0 release notes [here](https://github.com/PyTorch/PyTorch/releases/tag/v2.7.0 "https://github.com/PyTorch/PyTorch/releases/tag/v2.7.0").
- This image includes the following libraries:
  - CUDA 12.8.0
  - cuDNN 9.8.0.87
  - NCCL 2.27.5
  - EFA installer 1.42.0 (with AWS OFI NCCL embedded)
  - Transformer Engine 2.0
  - Flash Attention 2.7.3
  - GDRCopy 2.5

- Please note that EFA, Transformer Engine, Flash Attention, and GDRCopy have not been tested because of lack of hardware support.
- The Dockerfile can be found [here](https://github.com/aws/deep-learning-containers/blob/master/PyTorch/Training/docker/2.7/py3/Dockerfile.arm64.gpu "https://github.com/aws/deep-learning-containers/blob/master/PyTorch/Training/docker/2.7/py3/Dockerfile.arm64.gpu").

For latest updates, please refer to the [aws/deep-learning-containers GitHub repo.](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags")

## Security Advisory

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python 3.12 Support

Python 3.12 is supported in the PyTorch ARM64 Training containers.

## GPU Instance Type support

The containers support the Graviton GPU instance type G5g and contain the following software components for GPU support:

- CUDA 12.8
- cuDNN 9.8.0.87+cuda12.8
- NCCL 2.27.5+cuda12.8

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

- Built on: c6g.12xlarge
- Tested on: c8g.4xlarge, t4g.2xlarge, r8g.2xlarge, m7g.4xlarge, g5g.16xlarge

## Known Issues

- There is no official [Triton](https://github.com/triton-lang/triton "https://github.com/triton-lang/triton") distribution for ARM64/aarch64 yet, so some torch.compile workloads will fail with:

```
torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
RuntimeError: Cannot find a working triton installation. More information on installing Triton can be found at https://github.com/openai/triton
```

- See [GitHub issue](https://github.com/pytorch/pytorch/issues/153960 "https://github.com/pytorch/pytorch/issues/153960"): Passing device_id to torch.distributed.init_process_group() results in NCCL randomly hanging during communications.
