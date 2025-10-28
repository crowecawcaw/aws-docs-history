# AWS Deep Learning Containers for vLLM with EFA Support

[AWS Deep Learning Containers (DLCs)](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") now support vLLM images that are optimized for large language model serving.

The vLLM DLC provides a production-ready environment for deploying and serving LLMs with built-in support for EFA (Elastic Fabric Adapter). With vLLM's advanced features and optimizations pre-configured, this specialized container offer an ideal starting point for high-performance, scalable and efficient LLM serving for various use cases, from single-node to multi-node deployments. For guide on how to use vLLM, checkout [vLLM documentation](https://docs.vllm.ai "https://docs.vllm.ai").

Get started quickly with the AWS Deep Learning Containers using the getting-started section in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md").

If you are looking for a DLC to use with SageMaker, please refer to [this documentation](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only").

To ensure you are using the latest DLC releases, we invite you to subscribe to our [DLC notification mechanism](dlc-release-notifications.md "dlc-release-notifications.md").

## Changelog

To learn about latest changes in vLLM DLC, checkout the [changelog](https://github.com/aws/deep-learning-containers/blob/master/vllm/CHANGELOG.md "https://github.com/aws/deep-learning-containers/blob/master/vllm/CHANGELOG.md").

A list of available containers can be found on [GitHub](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#ec2-vllm-containers-ec2-ecs-and-eks-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#ec2-vllm-containers-ec2-ecs-and-eks-support-only").

## Security Advisory

All software components in these images are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices.

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

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
