# Amazon SageMaker Model Monitor prebuilt container

SageMaker AI provides a built-in image called `sagemaker-model-monitor-analyzer` that
provides you with a range of model monitoring capabilities, including constraint suggestion,
statistics generation, constraint validation against a baseline, and emitting Amazon CloudWatch
metrics. This image is based on Spark version 3.3.0 and is built with [Deequ](https://github.com/awslabs/deequ "https://github.com/awslabs/deequ") version 2.0.2.

###### Note

You can not pull the built-in `sagemaker-model-monitor-analyzer` image
directly. You can use the `sagemaker-model-monitor-analyzer` image when you
submit a baseline processing or monitoring job using one of the AWS SDKs.

Use the SageMaker Python SDK (see `image_uris.retrieve` in the [SageMaker AI Python
SDK reference guide](https://sagemaker.readthedocs.io/en/stable/api/utility/image_uris.html "https://sagemaker.readthedocs.io/en/stable/api/utility/image_uris.html")) to generate the ECR image URI for you, or specify the ECR
image URI directly. The prebuilt image for SageMaker Model Monitor can be accessed as follows:

``<ACCOUNT_ID>`.dkr.ecr.`<REGION_NAME>`.amazonaws.com/sagemaker-model-monitor-analyzer`

For example:
`159807026194.dkr.ecr.us-west-2.amazonaws.com/sagemaker-model-monitor-analyzer`

If you are in an AWS region in China, the prebuilt images for SageMaker Model Monitor can be accessed
as follows:

``<ACCOUNT_ID>`.dkr.ecr.`<REGION_NAME>`.amazonaws.com.cn/sagemaker-model-monitor-analyzer`

For account IDs and AWS Region names, see
[Docker
Registry Paths and Example Code](../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md "../dg-ecr-paths/sagemaker-algo-docker-registry-paths.md").

To write your own analysis container, see the container contract described in [Custom
monitoring schedules](model-monitor-custom-monitoring-schedules.md "model-monitor-custom-monitoring-schedules.md").
