# AWS Deep Learning Containers for PyTorch 2.5 Inference on SageMaker

[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/")(DLC) for Amazon SageMaker are now available with support for PyTorch 2.5 and support for CUDA 12.4 on Ubuntu 22.04. You can launch the new versions of the Deep Learning Containers on the SageMaker service. For a complete list of frameworks and versions supported by the AWS Deep Learning Containers, see the release notes below.

This release includes container images for inference on CPU and GPU, optimized for performance and scale on AWS. These Docker images have been tested with SageMaker services, and provide stable versions of NVIDIA CUDA, cuDNN, and other components to provide an optimized user experience for running deep learning workloads on AWS. All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices. These new DLC are designed to be used on SageMaker Inference services.

A list of available containers can be found in[our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). For latest updates, please also see the[aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our[developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our[discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers")to get launch announcements and post your questions.

## Release Notes

- Introduced containers for PyTorch 2.5.1 for inference supporting SageMaker services. For details about this release, check out our GitHub[release tag](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-sagemaker-2.5.1-inf-py311 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-sagemaker-2.5.1-inf-py311").
- PyTorch 2.5 features a new CuDNN backend for SDPA, enabling speedups by default for users of SDPA on H100s or newer GPUs. As well, regional compilation of torch.compile offers a way to reduce the cold start up time for torch.compile by allowing users to compile a repeated nn.Module (e.g. a transformer layer in LLM) without recompilations. Finally, TorchInductor CPP backend offers solid performance speedup with numerous enhancements like FP16 support, CPP wrapper, AOT-Inductor mode, and max-autotune mode.
- Includes the fix for wheels from PyPI being unusable out-of-the-box on RPM-based Linux distributions, as addressed in PyTorch 2.5.1.
- Please refer to the official PyTorch 2.5.0 release notes[here](https://github.com/pytorch/pytorch/releases/tag/v2.5.0 "https://github.com/pytorch/pytorch/releases/tag/v2.5.0")and PyTorch 2.5.1 release notes[here](https://github.com/pytorch/pytorch/releases/tag/v2.5.1 "https://github.com/pytorch/pytorch/releases/tag/v2.5.1")for the full description of updates.
- The Dockerfile for CPU can be found[here](https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.5/py3/Dockerfile.cpu "https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.5/py3/Dockerfile.cpu"), and the Dockerfile for GPU can be found[here](https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.5/py3/cu124/Dockerfile.gpu "https://github.com/aws/deep-learning-containers/blob/master/pytorch/inference/docker/2.5/py3/cu124/Dockerfile.gpu").

## Security Advisory

- AWS recommends that customers monitor critical security updates in the[AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python 3.11 Support

Python 3.11 is supported in the PyTorch Inference containers.

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
| ------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
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
| China (Ningxia)          | cn-northwest-1 | ## Build and Test <br>• Built on: c5.18xlarge <br>• Tested on: c5.18xlarge, g3.16xlarge, m5.16xlarge, t3.2xlarge, p3.16xlarge, p3dn.24xlarge, p4d.24xlarge, g4dn.xlarge <br>• Tested with[MNIST](http://yann.lecun.com/exdb/mnist/ "http://yann.lecun.com/exdb/mnist/")and Resnet50/ImageNet datasets on EC2, ECS AMI (Amazon Linux AMI2.0.20221102), and EKS AMI (amazon-eks-gpu-node-1.25.16-20240307) |
