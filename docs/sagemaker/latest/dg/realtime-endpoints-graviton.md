#

Migrate inference workload from x86 to AWS Graviton

[AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") is a series of ARM-based processors
designed by AWS. They are more energy efficient than x86-based processors and offer a compelling
price-performance ratio. Amazon SageMaker AI offers Graviton-based instances so that you can take advantage of these
advanced processors for your inference needs.

You can migrate your existing inference workloads from x86-based instances to Graviton-based instances, by using
either ARM compatible container images or multi-architecture container images. This guide assumes that you are
either using [AWS
Deep Learning container images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md"), or your own ARM compatible container images. For more information on
building your own images, check [Building your image](https://github.com/aws/deep-learning-containers#building-your-image "https://github.com/aws/deep-learning-containers#building-your-image").

At a high level, migrating inference workload from x86-based instances to Graviton-based instances is a four-step
process:

1. Push container images to Amazon Elastic Container Registry (Amazon ECR), an AWS managed container registry.
2. Create a SageMaker AI Model.
3. Create an endpoint configuration.
4. Create an endpoint.

The following sections of this guide provide more details regarding the above steps. Replace the
`user placeholder text` in the code examples with your own information.

###### Topics

- [Push container images to Amazon ECR](#realtime-endpoints-graviton-ecr "#realtime-endpoints-graviton-ecr")
- [Create a SageMaker AI Model](#realtime-endpoints-graviton-model "#realtime-endpoints-graviton-model")
- [Create an endpoint configuration](#realtime-endpoints-graviton-epc "#realtime-endpoints-graviton-epc")
- [Create an endpoint](#realtime-endpoints-graviton-ep "#realtime-endpoints-graviton-ep")

## Push container images to Amazon ECR

You can push your container images to Amazon ECR with the AWS CLI. When using an ARM compatible image, verify that
it supports ARM architecture:

```
docker inspect `deep-learning-container-uri`

```

The response `"Architecture": "arm64"` indicates that the image supports ARM architecture. You
can push it to Amazon ECR with the `docker push` command. For more information, check [Pushing a Docker
image](../../../AmazonECR/latest/userguide/docker-push-ecr-image.md "../../../AmazonECR/latest/userguide/docker-push-ecr-image.md").

Multi-architecture container images are fundamentally a set of container images supporting different
architectures or operating systems, that you can refer to by a common manifest name. If you are using
multi-architecture container images, then in addition to pushing the images to Amazon ECR, you will also have to
push a manifest list to Amazon ECR. A manifest list allows for the nested inclusion of other image manifests,
where each included image is specified by architecture, operating system and other platform attributes. The
following example creates a manifest list, and pushes it to Amazon ECR.

1. Create a manifest list.

```
docker manifest create `aws-account-id`.dkr.ecr.`aws-region`.amazonaws.com/`my-repository` \
  `aws-account-id`.dkr.ecr.`aws-account-id`.amazonaws.com/`my-repository:amd64` \
	`aws-account-id`.dkr.ecr.`aws-account-id`.amazonaws.com/`my-repository:arm64` \

```

2. Annotate the manifest list, so that it correctly identifies which image is for which architecture.

```
docker manifest annotate --arch arm64 `aws-account-id`.dkr.ecr.`aws-region`.amazonaws.com/`my-repository` \
  `aws-account-id`.dkr.ecr.`aws-region`.amazonaws.com/`my-repository:arm64`

```

3. Push the manifest.

```
docker manifest push `aws-account-id`.dkr.ecr.`aws-region`.amazonaws.com/`my-repository`

```

For more information on creating and pushing manifest lists to Amazon ECR, check [Introducing
multi-architecture container images for Amazon ECR](https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr/ "https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr/"), and [Pushing a multi-architecture
image](../../../AmazonECR/latest/userguide/docker-push-multi-architecture-image.md "../../../AmazonECR/latest/userguide/docker-push-multi-architecture-image.md").

## Create a SageMaker AI Model

Create a SageMaker AI Model by calling the [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md") API.

```
import boto3
from sagemaker import get_execution_role


aws_region = "`aws-region`"
sagemaker_client = boto3.client("sagemaker", region_name=aws_region)

role = get_execution_role()

sagemaker_client.create_model(
    ModelName = "`model-name`",
    PrimaryContainer = {
        "Image": "`deep-learning-container-uri`",
        "ModelDataUrl": "`model-s3-location`",
        "Environment": {
            "SAGEMAKER_PROGRAM": "`inference.py`",
            "SAGEMAKER_SUBMIT_DIRECTORY": "`inference-script-s3-location`",
            "SAGEMAKER_CONTAINER_LOG_LEVEL": "20",
            "SAGEMAKER_REGION": aws_region,
        }
    },
    ExecutionRoleArn = role
)

```

## Create an endpoint configuration

Create an endpoint configuration by calling the [`CreateEndpointConfig`](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md")
API. For a list of Graviton-based instances, check [Compute optimized instances](../../../AWSEC2/latest/UserGuide/compute-optimized-instances.md "../../../AWSEC2/latest/UserGuide/compute-optimized-instances.md").

```
sagemaker_client.create_endpoint_config(
    EndpointConfigName = "`endpoint-config-name`",
    ProductionVariants = [
        {
            "VariantName": "`variant-name`",
            "ModelName": "`model-name`",
            "InitialInstanceCount": `1`,
            "InstanceType": "`ml.c7g.xlarge`", # Graviton-based instance
       }
    ]
)

```

## Create an endpoint

Create an endpoint by calling the [`CreateEndpoint`](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md") API.

```
sagemaker_client.create_endpoint(
    EndpointName = "`endpoint-name`",
    EndpointConfigName = "`endpoint-config-name`"
)

```
