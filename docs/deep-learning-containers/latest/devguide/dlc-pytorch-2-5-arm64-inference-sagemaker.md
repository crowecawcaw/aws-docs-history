# AWS Deep Learning Containers for PyTorch 2.5 ARM64 Inference on Sagemaker

AWS Deep Learning Containers (DLCs) for Amazon SageMaker are now available for ARM64 platforms, including [AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") instance types with support for PyTorch 2.5. You can launch the new versions of the DLC on SageMaker.

This release includes a container image for inference on CPU, optimized for performance and scale on AWS. This Docker image was tested on SageMaker. It provides an optimized user experience for running deep learning workloads on SageMaker. All software components in this image are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices.

A list of available containers can be found in [our documentation](../../../dlami/latest/devguide/deep-learning-containers-images.md "../../../dlami/latest/devguide/deep-learning-containers-images.md"). Please refer to the [SageMaker Graviton blog](https://aws.amazon.com/blogs/machine-learning/run-machine-learning-inference-workloads-on-aws-graviton-based-instances-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/run-machine-learning-inference-workloads-on-aws-graviton-based-instances-with-amazon-sagemaker/") and DLC [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md") to migrate the Deep Learning workloads to Graviton instances. You can also subscribe to our [discussion forum](https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers "https://repost.aws/tags/TAtQOYCNQXQAypuIl0ZxRowA/aws-deep-learning-containers") to get launch announcements and post your questions.

## Release Notes

- Introduced container for PyTorch 2.5.1 for inference supporting SageMaker services on ARM64 instances. For details about this release, check out our GitHub [release tag](https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-arm64-sagemaker-2.5.1-inf-cpu-py311 "https://github.com/aws/deep-learning-containers/releases/tag/v1.0-pt-arm64-sagemaker-2.5.1-inf-cpu-py311").
- Starting with PyTorch 2.5, we are changing the name of Graviton DLCs to ARM64 DLCs in order to generalize the usage. For example, the ECR repository name is now "pytorch-inference-arm64" instead of "pytorch-inference-graviton". Graviton DLCs and ARM64 DLCs are functionally equivalent.
- TorchServe version: 0.12.0
- Includes the fix for wheels from PyPI being unusable out-of-the-box on RPM-based Linux distributions, as addressed in PyTorch 2.5.1.
- Please refer to the official PyTorch 2.5.0 release notes [here](https://github.com/pytorch/pytorch/releases/tag/v2.5.0 "https://github.com/pytorch/pytorch/releases/tag/v2.5.0") and PyTorch 2.5.1 release notes [here](https://github.com/pytorch/pytorch/releases/tag/v2.5.1 "https://github.com/pytorch/pytorch/releases/tag/v2.5.1") for the full description of updates.

## Performance Improvements

These DLCs continue to deliver the best performance on Graviton for BERT and RoBERTa sentiment analysis and fill mask models, making Graviton3 the most cost effective CPU platform on the AWS cloud for these models. For more information, please refer to the [Graviton PyTorch User Guide.](https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md "https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md")

## Security Advisory

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python 3.11 Support

Python 3.11 is supported in the PyTorch ARM64 Inference containers.

## CPU Instance Type Support

The containers support Graviton CPU instance types supported under SageMaker.

## AWS Regions support

The containers are available in the following regions:

| Region                   | Code           |
| ------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
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
| China (Ningxia)          | cn-northwest-1 | ## Build and Test <br>• Built on: c6g.2xlarge <br>• Tested on: c8g.4xlarge, t4g.2xlarge, r8g.2xlarge, m7g.4xlarge, g5g.4xlarge <br>• Tested with [MNIST](http://yann.lecun.com/exdb/mnist/ "http://yann.lecun.com/exdb/mnist/") and Resnet50/DenseNet datasets on EC2, ECS AMI (Amazon Linux AMI 2.0.20220822 arm64) and EKS AMI (1.25.6-20230304 arm64) ## Known Issues <br>• None For latest updates, please refer to the [aws/deep-learning-containers GitHub repo](https://github.com/aws/deep-learning-containers/tags "https://github.com/aws/deep-learning-containers/tags"). |
