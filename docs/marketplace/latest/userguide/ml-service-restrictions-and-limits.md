# Service restrictions and quotas for machine

learning products in AWS Marketplace

This section describes restrictions and quotas on your machine learning (ML) products in
AWS Marketplace.

###### Topics

- [Network isolation](#ml-network-isolation "#ml-network-isolation")
- [Image size](#ml-image-size "#ml-image-size")
- [Storage size](#ml-storage-size "#ml-storage-size")
- [Instance size](#ml-instance-size "#ml-instance-size")
- [Payload size for inference](#ml-payload-size-for-inference "#ml-payload-size-for-inference")
- [Processing time for inference](#ml-processing-time-for-inference "#ml-processing-time-for-inference")
- [Service quotas](#ml-service-quotas "#ml-service-quotas")
- [Asynchronous inference](#asynchronous-inference "#asynchronous-inference")
- [Serverless inference](#severless-inference "#severless-inference")
- [Managed spot training](#ml-managed-spot-training "#ml-managed-spot-training")
- [Docker images and AWS accounts](#ml-docker-images-and-aws-accounts "#ml-docker-images-and-aws-accounts")
- [Publishing model packages from built-in algorithms or AWS Marketplace](#ml-publishing-model-packages-from-built-in-algorithms-or-aws-marketplace "#ml-publishing-model-packages-from-built-in-algorithms-or-aws-marketplace")
- [Supported AWS Regions for
  publishing](#ml-supported-aws-regions-for-publishing "#ml-supported-aws-regions-for-publishing")

## Network isolation

For security purposes, when a buyer subscribes to your containerized product, the Docker
containers are run in an isolated environment without network access. When you create your
containers, don't rely on making outgoing calls over the internet because they will fail.
Calls to AWS services will also fail.

## Image size

Your Docker image size is governed by the Amazon Elastic Container Registry (Amazon ECR) [service quotas](../../../AmazonECR/latest/userguide/service_limits.md "../../../AmazonECR/latest/userguide/service_limits.md"). The Docker
image size affects the startup time during training jobs, batch-transform jobs, and endpoint
creation. For better performance, maintain an optimal Docker image size.

## Storage size

When you create an endpoint, Amazon SageMaker AI attaches an Amazon Elastic Block Store (Amazon EBS) storage volume to each
ML compute instance that hosts the endpoint. (An endpoint is also known as _real-time
inference_ or _Amazon SageMaker AI hosting service_.) The size of the
storage volume depends on the instance type. For more information, see [Host Instance
Storage Volumes](../../../sagemaker/latest/dg/host-instance-storage.md "../../../sagemaker/latest/dg/host-instance-storage.md") in the _Amazon SageMaker AI Developer
Guide_. 

For batch transform, see [Storage in Batch Transform](../../../sagemaker/latest/dg/batch-transform-storage.md "../../../sagemaker/latest/dg/batch-transform-storage.md") in the _Amazon SageMaker AI Developer Guide_.

## Instance size

SageMaker AI provides a selection of instance types that are optimized to fit different ML use
cases. Instance types are comprised of varying combinations of CPU, GPU, memory, and
networking capacity. Instance types give you the flexibility to choose the appropriate mix of
resources for building, training, and deploying your ML models. For more information, see
[Amazon SageMaker AI ML Instance
Types](https://aws.amazon.com/sagemaker/pricing/instance-types/ "https://aws.amazon.com/sagemaker/pricing/instance-types/").

## Payload size for inference

For an endpoint, limit the maximum size of the input data per invocation to 25 MB. This
value can't be adjusted.

For batch transform, the maximum size of the input data per invocation is 100 MB. This
value can't be adjusted.

## Processing time for inference

For an endpoint, the maximum processing time per invocation is 60 seconds for
regular responses and 8 min for streaming responses. This value can't be adjusted.

For batch transform, the maximum processing time per invocation is 60 minutes. This value
can't be adjusted.

## Service quotas

For more information about quotas related to training and inference, see [Amazon SageMaker AI
Service Quotas](../../../general/latest/gr/sagemaker.md#limits_sagemaker "../../../general/latest/gr/sagemaker.md#limits_sagemaker").

## Asynchronous inference

Model packages and algorithms published in AWS Marketplace can't be deployed to endpoints configured
for [Amazon SageMaker AI
Asynchronous Inference](../../../sagemaker/latest/dg/async-inference.md "../../../sagemaker/latest/dg/async-inference.md"). Endpoints configured for asynchronous inference requires
models to have network connectivity. All AWS Marketplace models operate in network isolation. For more
information, see [No network access](ml-security-and-intellectual-property.md#ml-no-network-access "ml-security-and-intellectual-property.md#ml-no-network-access").

## Serverless inference

Model packages and algorithms published in AWS Marketplace can't be deployed to endpoints configured
for [Amazon SageMaker AI
Serverless Inference](../../../sagemaker/latest/dg/serverless-endpoints.md "../../../sagemaker/latest/dg/serverless-endpoints.md"). Endpoints configured for serverless inference require models
to have network connectivity. All AWS Marketplace models operate in network isolation. For more
information, see [No network access](ml-security-and-intellectual-property.md#ml-no-network-access "ml-security-and-intellectual-property.md#ml-no-network-access").

## Managed spot training

For all algorithms from AWS Marketplace, the value of `MaxWaitTimeInSeconds` is set to
3,600 seconds (60 minutes), even if the checkpoint for [managed spot training](../../../sagemaker/latest/dg/model-managed-spot-training.md "../../../sagemaker/latest/dg/model-managed-spot-training.md") is
implemented. This value can't be adjusted.

## Docker images and AWS accounts

For publishing, images must be stored in Amazon ECR repositories owned by the AWS account of
the seller. It isn't possible to publish images that are stored in a repository owned by
another AWS account.

##

Publishing model packages from built-in algorithms or AWS Marketplace

Model packages created from training jobs using an [Amazon SageMaker AI built-in algorithm](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") or an algorithm
from an AWS Marketplace subscription can't be published.

You can still use the model artifacts from the training job, but your own inference image
is required for publishing model packages.

## Supported AWS Regions for

publishing

AWS Marketplace supports publishing model package and algorithm resources from AWS Regions where
the following are both true:

- A Region that [Amazon SageMaker AI
  supports](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/")
- An [available
  Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") that is opted-in by default (for example, [describe-regions](../../../general/latest/gr/rande-manage.md#ec2-describe-regions "../../../general/latest/gr/rande-manage.md#ec2-describe-regions")
  returns `"OptInStatus": "opt-in-not-required"`)

All assets required for publishing a model package or algorithm product must be stored in
the same Region that you choose to publish from. This includes the following:

- Model package and algorithm resources that are created in Amazon SageMaker AI
- Inference and training images that are uploaded to Amazon ECR repositories
- Model artifacts (if any) that are stored in Amazon Simple Storage Service and dynamically loaded
  during model deployment for model package resources
- Test data for inference and training validation that are stored in Amazon S3

You can develop and train your product in any Region that is supported by SageMaker AI. But,
before you can publish, you must copy all assets to and re-create resources in a Region that
AWS Marketplace supports publishing from.
