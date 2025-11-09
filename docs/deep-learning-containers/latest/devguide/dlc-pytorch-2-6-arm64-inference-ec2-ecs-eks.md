# AWS Deep Learning Containers for PyTorch 2.6 ARM64 Inference on EC2, ECS, and EKS

[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") (DLC) for Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Compute Cloud (EC2), and Amazon Elastic Container Service (ECS) are now available for ARM64 platforms, including [AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") instance types, with support for PyTorch 2.6.

This release includes container images for inference on CPU and GPU, optimized for performance and scale on AWS. The CPU image has been tested with each of the EC2, ECS, and EKS services, while the GPU image only supports EC2 (see the table below). The GPU image provides stable versions of NVIDIA CUDA, cuDNN, NCCL, and other components. All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices.

|           | EC2       | ECS           | EKS           |
| --------- | --------- | ------------- | ------------- |
| CPU image | Supported | Supported     | Supported     |
| GPU image | Supported | Not Supported | Not Supported |

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers") to get launch announcements and post your questions.

## Release Notes

- Introduced containers for PyTorch 2.6.0 for inference supporting EC2, ECS, and EKS on ARM64 instances. For details about this release, check out our GitHub [release tag](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-arm64-ec2-2.6.0-inf-py312 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-arm64-ec2-2.6.0-inf-py312").
- Starting with PyTorch 2.6, we are removing Conda from the DLCs and installing all Python packages from PyPI.
- TorchServe version: 0.12.0
- The GPU image should be used with the [G5g instance type](https://aws.amazon.com/ec2/instance-types/g5g/ "https://aws.amazon.com/ec2/instance-types/g5g/"), which is powered by Graviton CPUs and NVIDIA T4G Tensor Core GPUs.
- Please refer to the official PyTorch 2.6.0 release notes [here](https://github.com/pytorch/pytorch/releases/tag/v2.6.0 "https://github.com/pytorch/pytorch/releases/tag/v2.6.0") for the full description of framework updates.

## Performance Improvements

These DLCs continue to deliver the best performance on Graviton CPU for BERT and RoBERTa sentiment analysis and fill mask models, making Graviton3 the most cost effective CPU platform on the AWS cloud for these models. For more information, please refer to the [Graviton PyTorch User Guide.](https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md "https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md")

## Security Advisory

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python 3.12 Support

Python 3.12 is supported in the PyTorch ARM64 Inference containers.

## CPU Instance Type Support

The CPU container supports Graviton CPU instance types supported under each of the above mentioned services.

## GPU Instance Type support

The GPU container supports the Graviton GPU instance type G5g and contains the following software components for GPU support:

- CUDA 12.4.1
- cuDNN 9.1.0.70+cuda12.4
- NCCL 2.21.5+cuda12.4

## Release Notes

- Introduced containers for PyTorch 2.4 for inference supporting EC2, ECS, and EKS on Graviton instances. For details about this release, check out our GitHub release tags: [for CPU](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-graviton-ec2-2.4.0-inf-cpu-py311 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-graviton-ec2-2.4.0-inf-cpu-py311") and [for GPU](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-graviton-ec2-2.4.0-inf-gpu-py311 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-graviton-ec2-2.4.0-inf-gpu-py311").
- TorchServe version: 0.11.1
- 11/01/24: Updated TorchServe to 0.12.0 (release tags: [for CPU](https://github.com/aws/deep-learning-containers/releases/tag/v1.5-pt-graviton-ec2-2.4.0-inf-cpu-py311 "https://github.com/aws/deep-learning-containers/releases/tag/v1.5-pt-graviton-ec2-2.4.0-inf-cpu-py311") and [for GPU](https://github.com/aws/deep-learning-containers/releases/tag/v1.4-pt-graviton-ec2-2.4.0-inf-gpu-py311 "https://github.com/aws/deep-learning-containers/releases/tag/v1.4-pt-graviton-ec2-2.4.0-inf-gpu-py311"))
- The GPU image is the first ever DLC supporting Graviton (ARM64) + GPU platforms. It should be used with the [G5g instance type](https://aws.amazon.com/ec2/instance-types/g5g/ "https://aws.amazon.com/ec2/instance-types/g5g/"), which is powered by Graviton CPUs and NVIDIA T4G Tensor Core GPUs.
- Please refer to the official PyTorch 2.4 release notes [here](https://github.com/pytorch/pytorch/releases/tag/v2.4.0 "https://github.com/pytorch/pytorch/releases/tag/v2.4.0") for framework updates.

### Performance Improvements

These DLCs continue to deliver the best performance on Graviton CPU for BERT and RoBERTa sentiment analysis and fill mask models, making Graviton3 the most cost effective CPU platform on the AWS cloud for these models. For more information, please refer to the [Graviton PyTorch User Guide.](https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md "https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md")

### Security Advisory

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

### Python 3.11 Support

Python 3.11 is supported in the PyTorch Graviton Inference containers.

### CPU Instance Type Support

The containers support Graviton CPU instance types supported under each of the above mentioned services.

### GPU Instance Type support

The containers support the Graviton GPU instance type G5g and contain the following software components for GPU support:

- CUDA 12.4.0
- cuDNN 9.1.0.70+cuda12.4
- NCCL 2.20.5+cuda12.4

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

- Built on: c6g.2xlarge
- Tested on: c8g.4xlarge, t4g.2xlarge, r8g.2xlarge, m7g.4xlarge, g5g.4xlarge

## Known Issues

- There is no official [Triton](https://github.com/triton-lang/triton "https://github.com/triton-lang/triton") distribution for ARM64/aarch64 yet, so some torch.compile workloads will fail with:

```
torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
RuntimeError: Cannot find a working triton installation. More information on installing Triton can be found at https://github.com/openai/triton
```

For latest updates, please refer to the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags").
