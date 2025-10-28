# Get set up to build custom images with Image Builder

Before you build images with EC2 Image Builder, verify that you've met the following
prerequisites to create an image pipeline. Unless specifically stated otherwise,
these prerequisites are required for all types of pipelines.

###### Prerequisites

- [Image Builder service-linked
  role](#prereq-slr "#prereq-slr")
- [Configuration requirements](#prereq-config "#prereq-config")
- [Container repository for
  container image pipelines](#start-prereq-container "#start-prereq-container")
- [Dedicated host for
  macOS images](#start-prereq-macos-host "#start-prereq-macos-host")
- [IAM prerequisites](#image-builder-IAM-prereq "#image-builder-IAM-prereq")
- [Systems Manager Agent prerequisites](#image-builder-SSM-prereq "#image-builder-SSM-prereq")
  After you've met the prerequisites, you can manage EC2 Image Builder from any of the
  following interfaces.

- [EC2 Image Builder console](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/")
- [Image Builder commands in the AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html")
- [EC2 Image Builder API Reference](../APIReference.md "../APIReference.md")
- [AWS SDKs and Tools](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")

## Image Builder service-linked

role

EC2 Image Builder uses a service-linked role to grant permissions to other AWS services
on your behalf. You don't need to manually create a service-linked role. When you
create your first Image Builder resource in the AWS Management Console, the AWS CLI, or the
AWS API, Image Builder creates the service-linked role for you. For more information about
the service-linked role that Image Builder creates in your account, see [Use IAM service-linked roles for
Image Builder](image-builder-service-linked-role.md "image-builder-service-linked-role.md").

## Configuration requirements

- Image Builder supports [AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-share-your-services.md "../../../vpc/latest/privatelink/privatelink-share-your-services.md").
  For more information about configuring VPC endpoints for Image Builder, see [Image Builder and AWS PrivateLink interface VPC endpoints](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
- The instances that Image Builder uses to build container images must have internet access
  to download the AWS CLI from Amazon S3, and to download a base image from the Docker Hub
  repository, if applicable. Image Builder uses the AWS CLI to get the Dockerfile from the container
  recipe, where it is stored as data.
- The instances that Image Builder uses to build images and run tests must have
  access to the Systems Manager service. Installation requirements depend on your operating system.

To see the installation requirements for your base image, choose the
tab that matches your base image operating system.

Linux
For Amazon EC2 Linux instances, Image Builder installs the Systems Manager Agent on the
build instance if it is not already present, and removes it before
creating the image.

Windows
Image Builder does not install the Systems Manager Agent on Amazon EC2 Windows Server build
instances. If your base image did not come preinstalled with the
Systems Manager Agent, you must launch an instance from your source image,
manually install Systems Manager on the instance, and create a new base
image from your instance.

To manually install the Systems Manager agent on your Amazon EC2 Windows Server instance,
see [Manually
install Systems Manager Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md "../../../systems-manager/latest/userguide/manually-install-ssm-agent-windows.md") in the
_AWS Systems Manager User Guide_.

## Container repository for

container image pipelines

For container image pipelines, the recipe defines the configuration for
the Docker images that are produced and stored in the target container
repository. You must create the target repository before you create the
container recipe for your Docker image.

Image Builder uses Amazon ECR as its target repository for container images. To create an Amazon ECR
repository, follow the steps described in
[Creating a
repository](../../../AmazonECR/latest/userguide/repository-create.md "../../../AmazonECR/latest/userguide/repository-create.md") in the _Amazon Elastic Container Registry User Guide_.

## Dedicated host for

macOS images

Amazon EC2 Mac instances require a Dedicated Host running on a metal instance type.
Before you create a custom macOS image, you must [Allocate a
Dedicated Host](../../../AWSEC2/latest/UserGuide/dedicated-hosts-allocating.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-allocating.md") to your account. For more information about Mac
instances and a list of instance types that natively support the macOS operating
system, see [Amazon EC2 Mac instances](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md")
in the _Amazon EC2 User Guide_.

When you've created a Dedicated Host, you can configure settings in the
infrastructure configuration resource for your image. The infrastructure configuration
includes placement properties where you can specify the host, host placement group,
or Availability Zone where the instances that launch from your image should go.

## IAM prerequisites

The IAM role that you associate with your instance profile must have permissions
to run the build and test components included in your image. The following IAM
role policies must be attached to the IAM role that is associated with the
instance profile:

- [EC2InstanceProfileForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-EC2InstanceProfileForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-EC2InstanceProfileForImageBuilder")
- [EC2InstanceProfileForImageBuilderECRContainerBuilds](security-iam-awsmanpol.md#sec-iam-manpol-EC2InstanceProfileForImageBuilderECRContainerBuilds "security-iam-awsmanpol.md#sec-iam-manpol-EC2InstanceProfileForImageBuilderECRContainerBuilds")
- AmazonSSMManagedInstanceCore

If you configure logging, the instance profile specified in your infrastructure
configuration must have `s3:PutObject` permissions for the target bucket
(`arn:aws:s3:::`BucketName`/*`). For
example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "UploadFileToS3Bucket",
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`bucket-name`/*"
 }
 ]
}`

```

###### Attach policy

The following steps guide you through the process of attaching the IAM
policies to an IAM role to grant the preceding permissions.

1. Sign in to the AWS Management Console and open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Policies**.
3. Filter the list of policies with **EC2InstanceProfileForImageBuilder**
4. Select the bullet next to the policy, and from the **Policy
   actions** dropdown list, select
   **Attach**.
5. Select the name of the IAM role to which to attach the policy.
6. Choose **Attach policy**.
7. Repeat steps 3-6 for the **EC2InstanceProfileForImageBuilderECRContainerBuilds**
   and **AmazonSSMManagedInstanceCore** policies.

###### Note

If you want to copy an image created with Image Builder to another account, you must
create the `EC2ImageBuilderDistributionCrossAccountRole` role in all
of the target accounts, and attach the [Ec2ImageBuilderCrossAccountDistributionAccess policy](security-iam-awsmanpol.md#sec-iam-manpol-Ec2ImageBuilderCrossAccountDistributionAccess "security-iam-awsmanpol.md#sec-iam-manpol-Ec2ImageBuilderCrossAccountDistributionAccess") managed policy to the role. For more information, see [Share Image Builder resources with AWS RAM](manage-shared-resources.md "manage-shared-resources.md").

## Systems Manager Agent prerequisites

EC2 Image Builder runs [AWS Systems Manager (Systems Manager)
Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") on the EC2 instances it launches to build and test your image.
Image Builder collects additional information about the instance used during the build phase
with [Systems Manager Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md").
This information includes the operating system (OS) name and version, as well as the
list of packages and their respective versions as reported by your operating system.

To opt out of collecting this information, select the method that matches
your preferred environment:

- **Image Builder console** – Deselect the
  **Enable enhanced metadata collection** check box.
- **AWS CLI** – Specify the
  `--no-enhanced-image-metadata-enabled` option
- **Image Builder API or SDKs** – Set the
  `enhancedImageMetadataEnabled` parameter to `false`.

Image Builder uses `RunCommand` to send actions to your build and test instance
as part of the image build and test workflow. You can't opt out of the use of
`RunCommand` to send actions to your build and test instance.
