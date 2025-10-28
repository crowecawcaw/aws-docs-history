# AWS Deep Learning Containers for TensorFlow 2.19 ARM64 Inference on SageMaker

[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") (DLCs) for Amazon SageMaker, are now available for ARM64 platforms, including the [Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") instance types with support for TensorFlow Serving 2.19. You can launch the new versions of the Deep Learning Containers on SageMaker.

This release includes a container image for inference on CPU optimized for performance and scale on AWS. This Docker image was tested on [Amazon SageMaker](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/"). It provides an optimized user experience for running deep learning workloads on SageMaker. All software components in this image are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices.

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). Get started quickly with the AWS Deep Learning Containers using the getting-started guides and beginner to advanced level tutorials in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers") to get launch announcements and post your questions.

## Release Notes

- Support for TensorFlow Serving 2.19 on Amazon SageMaker. For details about this release, checkout our GitHub [v1.0-tf-arm64-sagemaker-2.19.0-inf-cpu-py312](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-tf-arm64-sagemaker-2.19.0-inf-cpu-py312 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-tf-arm64-sagemaker-2.19.0-inf-cpu-py312")

For latest updates, please refer to the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags").

## Security Advisory

- AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python Support

Python 3.12 is supported in the containers for the installed deep learning frameworks.

## CPU Instance Type Support

The container supports Graviton CPU instance types.

## AWS Regions support

The containers are available in the following regions:

| Region                    | Code           |
| ------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
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
| South America (Sau Paulo) | sa-east-1      | ## Build and Test <br>• Built on: c6g.2xlarge <br>• DLC Images tested on: c8g.4xlarge, t4g.2xlarge, r8g.2xlarge, m7g.4xlarge |
