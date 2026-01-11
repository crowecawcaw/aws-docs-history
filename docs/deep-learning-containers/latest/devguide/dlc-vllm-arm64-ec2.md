# AWS Deep Learning Containers for vLLM ARM64 with EFA Support on EC2, ECS, and EKS

[AWS Deep Learning Containers (DLCs)](https://aws.amazon.com/machine-learning/containers/ "https://aws.amazon.com/machine-learning/containers/") now support vLLM images that are optimized for large language model serving. The vLLM DLC provides a production-ready environment for deploying and serving LLMs with built-in support for EFA (Elastic Fabric Adapter). With vLLM's advanced features and optimizations pre-configured, this specialized container offer an ideal starting point for high-performance, scalable and efficient LLM serving for various use cases, from single-node to multi-node deployments.

All software components in this container are scanned for security vulnerabilities and updated or patched in accordance with AWS Security best practices. A list of all available AWS DLCs can be found in our [github repo](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#dlc-available-image-user-guide "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#dlc-available-image-user-guide"). Get started quickly with AWS DLCs using the getting-started section in our [developer guide](../../../dlami/latest/devguide/deep-learning-containers.md "../../../dlami/latest/devguide/deep-learning-containers.md"). To ensure you're using the latest DLC releases, we invite you to subscribe to our [DLC notification mechanism](dlc-release-notifications.md "dlc-release-notifications.md"). If you are looking for a DLC to use with SageMaker, please refer to [this documentation](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers-ec2-ecs-eks--sm-support "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#general-framework-containers-ec2-ecs-eks--sm-support"). For guide on how to use vLLM, checkout [vLLM documentation](https://docs.vllm.ai/en/latest/ "https://docs.vllm.ai/en/latest/").

## Changelog

To learn about latest changes in vLLM DLC, checkout the [changelog](https://github.com/aws/deep-learning-containers/blob/master/vllm/CHANGELOG.md "https://github.com/aws/deep-learning-containers/blob/master/vllm/CHANGELOG.md").

A list of available containers can be found on [GitHub](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#vllm-containers "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#vllm-containers").

## Security Advisory

AWS recommends that customers monitor critical security updates in the [AWS Security Bulletin](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/").

## Python 3.12 Support

Python 3.12 is supported.

## Instance Type Support

The containers support ARM64 instance types.

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

- Built on: c6g.12xlarge
- Tested on: g5g.16xlarge
- Tested with deepseek-ai/DeepSeek-R1-Distill-Qwen-32B model, single-node and multi-node serving configurations

## Known Issues

No known issues so far
