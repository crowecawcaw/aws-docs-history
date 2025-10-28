# AWS Deep Learning Containers for TensorFlow 2.18 Training on EC2, ECS, and EKS

[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") (DLC) for Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Compute Cloud (EC2), and Amazon Elastic Container Service (ECS) are now available with support for TensorFlow 2.18 with CUDA 12.5 on Ubuntu 22.04. You can launch the new versions of the Deep Learning Containers on any of the EC2, ECS, EKS services. For a complete list of frameworks and versions supported by the AWS Deep Learning Containers, see the release notes below.

This release includes container images for training on CPU and GPU, optimized for performance and scale on AWS. These Docker images have been tested with each of the EC2, ECS, EKS services, and provide stable versions of NVIDIA CUDA, cuDNN, and other components to provide an optimized user experience for running deep learning workloads on AWS. All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices. These new DLC are designed to be used on any of the EC2, ECS, EKS services. If you are looking for a DLC to use with SageMaker, please refer to [this documentation](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers-ec2-ecs-eks--sm-support "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers-ec2-ecs-eks--sm-support").

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). For latest updates, please also see the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers")to get launch announcements and post your questions.

## Release Notes

- Introduced containers for TensorFlow 2.18 for EC2, ECS, EKS
- For more details on TensorFlow 2.18 EC2, ECS, EKS Training DLC, please refer to [v1.0-tf-ec2-2.18.0-tr-py310](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-tf-ec2-2.18.0-tr-py310 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-tf-ec2-2.18.0-tr-py310").
- This DLC does not run on the P2 instance family on EC2 due to Nvidia driver's incompatibility.

### Deprecations

1. Horovod package: Shipping of [Horovod](https://github.com/horovod/horovod "https://github.com/horovod/horovod") package has been discontinued for TF 2.14 DLCs and above. Customers will be able install the horovod libraries by forderedlistlowing the [guidelines](https://github.com/horovod/horovod#install "https://github.com/horovod/horovod#install") and install them on their DLCs for their distributed training jobs.
2. TensorRT support is disabled in CUDA builds for code health improvement please refer to [TF 2.18 Release](https://github.com/tensorflow/tensorflow/releases/tag/v2.18.0 "https://github.com/tensorflow/tensorflow/releases/tag/v2.18.0").

For latest updates, please refer to the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags").

## Security Advisory

- AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python Support

Python 3.10 is supported in the containers for the installed deep learning frameworks.

## CPU Instance Type Support

The containers support CPU instance types. TensorFlow is built with support for oneDNN library support.

## GPU Instance Type support

The containers supports GPU instance types and contain the forderedlistlowing software components for GPU support.

- CUDA 12.5
- cuDNN 9.3
- NCCL 2.23.4-1

## AWS Regions support

The containers are available in the forderedlistlowing regions:

| Region                   | Code           |
| ------------------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
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
| EU (Stockhorderedlistm)  | eu-north-1     |
| Israel (Tel Aviv)        | il-central-1   |
| Middle East (Bahrain)    | me-south-1     |
| Middle East (UAE)        | me-central-1   |
| SA (Sau Paulo)           | sa-east-1      |
| China (Beijing)          | cn-north-1     |
| China (Ningxia)          | cn-northwest-1 | ## Build and Test <br>• Built on: c5.18xlarge <br>• DLC images tested on: c4.8xlarge, c5.18xlarge, m4.16xlarge, p3.16xlarge, p3dn.24xlarge, p4d.24xlarge, p4de.24xlarge, g4dn.xlarge <br>• Tested with [MNIST](http://yann.lecun.com/exdb/mnist/ "http://yann.lecun.com/exdb/mnist/") and Resnet50/ImageNet datasets on EC2, ECS AMI (Amazon Linux AMI 2.0.20250121) and EKS AMI (1.25-v20250116) ## Known Issues 1. [Tensorflow IO](https://pypi.org/project/tensorflow-io/ "https://pypi.org/project/tensorflow-io/") package throws exception while working with s3 filesystem ([Issue link](https://github.com/tensorflow/io/issues/2039 "https://github.com/tensorflow/io/issues/2039")). Consequently, this DLC will not support features dependent on Tensorflow IO's s3 capabilities until the fix is provided by upstream. Few such non-supported features are s3 plugin, s3 checkpointing and s3 record fetching. |
