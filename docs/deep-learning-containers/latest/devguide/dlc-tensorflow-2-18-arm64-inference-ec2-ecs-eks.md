# AWS Deep Learning Containers for TensorFlow 2.18 ARM64 Inference on EC2, ECS and EKS

[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") (DLC) for Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Compute Cloud (EC2), and Amazon Elastic Container Service (ECS), are now available for ARM64 platforms, including the [Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") instance type with support for TensorFlow Serving 2.18. You can launch the new versions of the Deep Learning Containers on any of the EC2, ECS, EKS services. For a complete list of frameworks and versions supported by the AWS Deep Learning Containers, see the release notes below.

This release includes container images for inference on CPU optimized for performance and scale on AWS. These Docker images have been tested with each of the EC2, ECS, EKS services, and provide an optimized user experience for running deep learning workloads on AWS. All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices.

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). Refer to [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started "https://github.com/aws/aws-graviton-getting-started") for runtime configurations and performance tunings. You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers") to get launch announcements and post your questions.

## Release Notes

- Support for TensorFlow Serving 2.18 on EC2, ECS, and EKS services. For details about this release, checkout our GitHub [v1.0-tf-arm64-ec2-2.18.0-inf-cpu-py310](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-tf-arm64-ec2-2.18.0-inf-cpu-py310 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-tf-arm64-ec2-2.18.0-inf-cpu-py310")
- Starting with TensorFlow 2.18, we are changing the name of Graviton DLCs to ARM64 DLCs in order to generalize the usage. For example, the ECR repository name is now "tensorflow-inference-arm64" instead of "tensorflow-inference-graviton". Graviton DLCs and ARM64 DLCs are functionally equivalent.

For latest updates, please refer to the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags").

## Security Advisory

- AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python Support

Python 3.10 is supported in the containers for the installed deep learning frameworks.

## CPU Instance Type Support

The containers support Graviton CPU instance types.

## AWS Regions support

The containers are available in the following regions:

| Region                   | Code           |
| ------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
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
| China (Ningxia)          | cn-northwest-1 | ## Build and Test <br>• Built on: c6g.2xlarge <br>• DLC Images tested on: c8g.4xlarge, t4g.2xlarge, r8g.2xlarge, m7g.4xlarge |
