# AWS Deep Learning Base Containers for EC2, ECS, EKS (with NVIDIA CUDA 12.8 and AWS EFA)

[AWS Deep Learning Containers (DLCs)](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") now support Base images that serve as a foundational layer to build the machine learning environment on EC2, ECS and EKS, with Ubuntu 24.04.

These Base DLCs package the essential deep learning components and dependencies without being tied to a specific framework implementation, providing users the flexibility to customize the DLCs with their preferred frameworks.

Pre-configured with the core components of CUDA, cuDNN, Python and EFA support, these images function seamlessly out-of-the-box, providing a stable, reliable starting point with inter-node connectivity, while maintaining compatibility across EC2, ECS and EKS services.

All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices.

A list of available containers can be found on [GitHub](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#base-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#base-containers"). Get started quickly with the AWS Deep Learning Containers using the getting-started section in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). To ensure you are using the latest DLC releases, we invite you to subscribe to our [DLC notification mechanism](dlc-release-notifications.md "dlc-release-notifications.md"). If you are looking for a DLC to use with SageMaker, please refer to [this documentation](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only").

## Release Notes

- Development Tools: Includes curl, build-essential, cmake, and git for common development needs
- Python Environment: Python 3.12 with AWS CLI, boto3, and requests pre-installed
- GPU Support: CUDA 12.8.1 with cuda-compat for backward compatibility
- Neural Network Libraries: cuDNN 9.8.0.87 for deep neural network operations
- Distributed Training: NCCL 2.26.2-1 for multi-GPU and multi-node communication
- Network Performance: EFA 1.40.0 for low-latency network communications

## Security Advisory

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python Support

Python 3.12 is supported.

## GPU Instance Type support

The containers support the Graviton GPU instance type G5g and contain the following software components for GPU support:

- CUDA 12.8
- cuDNN 9.8.0.87
- NCCL 2.26.2-1

## Example URL

```
763104351884.dkr.ecr.us-west-2.amazonaws.com/base:12.8.1-gpu-py312-cu128-ubuntu24.04-ec2
```

## AWS Regions support

The containers are available in the following regions:

| Region                   | Code           |
| ------------------------ | -------------- |
| US East (N. Virginia)    | us-east-1      |
| US East (Ohio)           | us-east-2      |
| US West (N. California)  | us-west-1      |
| US West (Oregon)         | us-west-2      |
| Asia Pacific (Hong Kong) | ap-east-1      |
| Asia Pacific (Mumbai)    | ap-south-1     |
| Asia Pacific (Hyderabad) | ap-south-2     |
| Asia Pacific (Tokyo)     | ap-northeast-1 |
| Asia Pacific (Seoul)     | ap-northeast-2 |
| Asia Pacific (Osaka)     | ap-northeast-3 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney)    | ap-southeast-2 |
| Asia Pacific (Jakarta)   | ap-southeast-3 |
| Asia Pacific (Melbourne) | ap-southeast-4 |
| Asia Pacific (Malaysia)  | ap-southeast-5 |
| Asia Pacific (Thailand)  | ap-southeast-7 |
| Canada (Central)         | ca-central-1   |
| Canada (Calgary)         | ca-west-1      |
| EU (Frankfurt)           | eu-central-1   |
| EU (Zurich)              | eu-central-2   |
| EU (Ireland)             | eu-west-1      |
| EU (London)              | eu-west-2      |
| EU (Paris)               | eu-west-3      |
| EU (Milan)               | eu-south-1     |
| EU (Spain)               | eu-south-2     |
| EU (Stockholm)           | eu-north-1     |
| Middle East (Bahrain)    | me-south-1     |
| Middle East (UAE)        | me-central-1   |
| Israel (Tel Aviv)        | il-central-1   |
| SA (Sau Paulo)           | sa-east-1      |
| AF South (Cape Town)     | af-south-1     |
| Mexico (Central)         | mx-central-1   |
| China (Beijing)          | cn-north-1     |
| China (Ningxia)          | cn-northwest-1 |

## Build and Test

- Built on: c5.18xlarge
- Tested on: p4d.24xlarge, p4de.24xlarge, p5.48xlarge
- Tested with: [openclip](https://github.com/mlfoundations/open_clip "https://github.com/mlfoundations/open_clip"), [nccl-tests](https://github.com/NVIDIA/nccl-tests "https://github.com/NVIDIA/nccl-tests")

## Known Issues

- No known issues so far
