# AWS for Fluent Bit image

repositories for Amazon ECS

AWS provides a Fluent Bit image with plugins for both CloudWatch Logs and
Firehose. We recommend using Fluent Bit as your log router because it has a
lower resource utilization rate than Fluentd. For more information, see
[CloudWatch Logs for
Fluent Bit](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit "https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit") and [Amazon Kinesis
Firehose for Fluent Bit](https://github.com/aws/amazon-kinesis-firehose-for-fluent-bit "https://github.com/aws/amazon-kinesis-firehose-for-fluent-bit").

The **AWS for Fluent Bit** image is available on Amazon ECR on both the
Amazon ECR Public Gallery and in an Amazon ECR repository for high
availability.

## Amazon ECR Public Gallery

The AWS for Fluent Bit image is available on the Amazon ECR Public
Gallery. This is the recommended location to download the AWS for Fluent
Bit image because it's a public repository and available to be used from
all AWS Regions. For more information, see [aws-for-fluent-bit](https://gallery.ecr.aws/aws-observability/aws-for-fluent-bit "https://gallery.ecr.aws/aws-observability/aws-for-fluent-bit") on the Amazon ECR Public Gallery.

### Linux

The AWS for Fluent Bit image in the Amazon ECR Public Gallery
supports the Amazon Linux operating system with the `ARM64` or
`x86-64` architecture.

You can pull the AWS for Fluent Bit image from the Amazon ECR
Public Gallery by specifying the repository URL with the desired image tag. The
available image tags can be found on the **Image tags** tab on
the Amazon ECR Public Gallery.

The following shows the syntax to use for the Docker CLI.

```
`docker pull public.ecr.aws/aws-observability/aws-for-fluent-bit:`tag``
```

For example, you can pull the latest stable AWS for Fluent
Bit image using this Docker CLI command.

```
`docker pull public.ecr.aws/aws-observability/aws-for-fluent-bit:stable`
```

###### Note

Unauthenticated pulls are allowed, but have a lower rate limit than
authenticated pulls. To authenticate using your AWS account before
pulling, use the following command.

```
`aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws`
```

#### AWS for Fluent

Bit 3.0.0

In addition to the existing AWS for Fluent
Bit versions `2.x`, AWS for Fluent Bit supports a new major
version `3.0.0`. The new major version includes upgrading images from Amazon Linux 2
to Amazon Linux 2023 and Fluent Bit version `1.9.10` to
`4.1.1`. For more information, see the [AWS for Fluent Bit repository](https://github.com/aws/aws-for-fluent-bit/blob/mainline/VERSIONS.md "https://github.com/aws/aws-for-fluent-bit/blob/mainline/VERSIONS.md") on
GitHub.

The following examples demonstrate updated tags for AWS for
Fluent Bit
`3.0.0` images:

You can use architecture-specific tags for the AWS for Fluent
Bit image. For example, you can pull an `ARM64` architecture image
using a docker command that follows this syntax.

```
`docker pull public.ecr.aws/aws-observability/aws-for-fluent-bit:arm64-3.0.0`
```

You can use multi-architecture tags for the AWS for Fluent
Bit image. For example, you can pull an image with the latest
debug version and init process using a docker command that follows this
syntax.

```
`docker pull public.ecr.aws/aws-observability/aws-for-fluent-bit:init-debug-3.0.0`
```

### Windows

The AWS for Fluent Bit image in the Amazon ECR Public Gallery
supports the `AMD64` architecture with the following operating
systems:

- Windows Server 2022 Full
- Windows Server 2022 Core
- Windows Server 2019 Full
- Windows Server 2019 Core

Windows containers that are on AWS Fargate don't support FireLens.

You can pull the AWS for Fluent Bit image from the Amazon ECR
Public Gallery by specifying the repository URL with the desired image tag. The
available image tags can be found on the **Image tags** tab on
the Amazon ECR Public Gallery.

The following shows the syntax to use for the Docker CLI.

```
`docker pull public.ecr.aws/aws-observability/aws-for-fluent-bit:`tag``
```

For example, you can pull the newest stable AWS for Fluent
Bit image using this Docker CLI command.

```
`docker pull public.ecr.aws/aws-observability/aws-for-fluent-bit:windowsservercore-stable`
```

###### Note

Unauthenticated pulls are allowed, but have a lower rate limit than
authenticated pulls. To authenticate using your AWS account before
pulling, use the following command.

```
`aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws`
```

## Amazon ECR

The AWS for Fluent Bit image is available on Amazon ECR for high availability. The following commands can be used to retreive image URIs and establish image availability in a given AWS Region.

### Linux

The latest stable AWS for Fluent Bit image URI can be retrieved using
the following command.

```
`aws ssm get-parameters \
 --names /aws/service/aws-for-fluent-bit/stable \
 --region `us-east-1``
```

All versions of the AWS for Fluent Bit image can be listed using the
following command to query the Systems Manager Parameter Store parameter.

```
`aws ssm get-parameters-by-path \
 --path /aws/service/aws-for-fluent-bit \
 --region `us-east-1``
```

The newest stable AWS for Fluent Bit image can be referenced in an AWS CloudFormation
template by referencing the Systems Manager parameter store name. The
following is an example:

```
Parameters:
  FireLensImage:
    Description: Fluent Bit image for the FireLens Container
    Type: AWS::SSM::Parameter::Value<String>
    Default: /aws/service/aws-for-fluent-bit/stable
```

###### Note

If the command fails or there is no output, the image isn't available in the AWS Region in which the command is called.

### Windows

The latest stable AWS for Fluent Bit image URI can be retrieved using
the following command.

```
`aws ssm get-parameters \
 --names /aws/service/aws-for-fluent-bit/windowsservercore-stable \
 --region `us-east-1``
```

All versions of the AWS for Fluent Bit image can be listed using the
following command to query the Systems Manager Parameter Store parameter.

```
`aws ssm get-parameters-by-path \
 --path /aws/service/aws-for-fluent-bit/windowsservercore \
 --region `us-east-1``
```

The latest stable AWS for Fluent Bit image can be referenced in an AWS CloudFormation
template by referencing the Systems Manager parameter store name. The
following is an example:

```
Parameters:
  FireLensImage:
    Description: Fluent Bit image for the FireLens Container
    Type: AWS::SSM::Parameter::Value<String>
    Default: /aws/service/aws-for-fluent-bit/windowsservercore-stable
```
