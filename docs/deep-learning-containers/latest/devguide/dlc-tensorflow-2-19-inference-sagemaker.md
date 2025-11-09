# AWS Deep Learning Containers for TensorFlow 2.19 Inference on SageMaker

[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") (DLC) for Amazon SageMaker are now available with support for TensorFlow 2.19 Inference and support for CUDA 12.2 on Ubuntu 22.04. You can launch the new versions of the Deep Learning Containers on the SageMaker service. For a complete list of frameworks and versions supported by the AWS Deep Learning Containers, see the release notes below.

This release includes container images for inference on CPU and GPU, optimized for performance and scale on AWS. These Docker images have been tested with SageMaker services, and provide stable versions of NVIDIA CUDA, cuDNN, and other components to provide an optimized user experience for running deep learning workloads on AWS. All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices. These new DLC are designed to be used on SageMaker inference services.

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). For latest updates, please also see the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers")to get launch announcements and post your questions.

## Release Notes

- Introduced containers of TensorFlow 2.19 for inference on SageMaker.
- For more details on TensorFlow 2.19 Inference DLCs, please refer to [v1.1-tf-sagemaker-2.19.0-inf-py312](https://github.com/aws/deep-learning-containers/releases/tag/v1.1-tf-sagemaker-2.19.0-inf-py312 "https://github.com/aws/deep-learning-containers/releases/tag/v1.1-tf-sagemaker-2.19.0-inf-py312").

For latest updates, please refer to the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags").

## Security Advisory

- AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python Support

Python 3.12 is supported in the TensorFlow Inference containers.

## CPU Instance Type Support

The containers support CPU instance types.

## GPU Instance Type support

The containers support GPU instance types and contain the following software components for GPU support:

- CUDA 12.2
- cuDNN 8.9.4.25-1+cuda12.2
- NCCL 2.18.3-1+cuda12.2

## AWS Regions support

The containers are available in the following regions:

| Region                    | Code           |
| ------------------------- | -------------- |
| US East (Ohio)            | us-east-2      |
| US East (N. Virginia)     | us-east-1      |
| US West (N. California)   | us-west-1      |
| US West (Oregon)          | us-west-2      |
| Africa (Cape Town)        | af-south-1     |
| Asia Pacific (Hong Kong)  | ap-east-1      |
| Asia Pacific (Hyderabad)  | ap-south-2     |
| Asia Pacific (Jakarta)    | ap-southeast-3 |
| Asia Pacific (Malaysia)   | ap-southeast-5 |
| Asia Pacific (Melbourne)  | ap-southeast-4 |
| Asia Pacific (Mumbai)     | ap-south-1     |
| Asia Pacific (Osaka)      | ap-northeast-3 |
| Asia Pacific (Seoul)      | ap-northeast-2 |
| Asia Pacific (Singapore)  | ap-southeast-1 |
| Asia Pacific (Sydney)     | ap-southeast-2 |
| Asia Pacific (Taipei)     | ap-east-2      |
| Asia Pacific (Thailand)   | ap-southeast-7 |
| Asia Pacific (Tokyo)      | ap-northeast-1 |
| Canada (Central)          | ca-central-1   |
| Canada (Calgary)          | ca-west-1      |
| Europe (Frankfurt)        | eu-central-1   |
| Europe (Ireland)          | eu-west-1      |
| Europe (London)           | eu-west-2      |
| Europe (Milan)            | eu-south-1     |
| Europe (Paris)            | eu-west-3      |
| Europe (Spain)            | eu-south-2     |
| Europe (Stockholm)        | eu-north-1     |
| Europe (Zurich)           | eu-central-2   |
| Israel (Tel Aviv)         | il-central-1   |
| Mexico (Central)          | mx-central-1   |
| Middle East (Bahrain)     | me-south-1     |
| Middle East (UAE)         | me-central-1   |
| South America (Sau Paulo) | sa-east-1      |

## Build and Test

- Built on: c5.18xlarge
- Tested on: t3.2xlarge, m5.16xlarge, c5.18xlarge, g5.24xlarge, g5.12xlarge, p4d.24xlarge, p5.48xlarge, g4dn.4xlarge, g4dn.8xlarge, ml.p4de.24xlarge, p4de.24xlarge
