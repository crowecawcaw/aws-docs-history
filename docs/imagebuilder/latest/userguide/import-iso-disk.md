# Import verified Windows ISO disk images with Image Builder

A Windows operating system ISO file is a disk image file that contains the complete
installation package for a specific version of the Windows operating system. Microsoft
provides official Windows operating system ISO files for download, either directly from
their website or through authorized resellers. It's important to ensure that you obtain
the ISO files from a trusted and legitimate source to avoid potential malware or
unauthorized versions.

EC2 Image Builder uses the `build-image-from-iso` import workflow to import the ISO disk
file and create a secondary volume from it. After configuration is complete, Image Builder takes
a snapshot of the volume it created from the import and uses it to create an Amazon Machine
Image (AMI).

## Supported operating systems for ISO disk image import

Image Builder supports the following Windows operating system ISO disk images:

- Windows 11 Enterprise version 25H2 (x64)
- Windows 11 Enterprise version 24H2 (x64)
- Windows 11 Enterprise version 23H2 (x64)

Image Builder does not support the following Windows operating system ISO disk images:

- Long-Term Servicing Channel (LTSC) images
- ISO disk images created from the Windows Media Creation Tool
- Evaluation images

## Prerequisites to import an ISO disk image

To import an ISO disk image, you must first meet the following prerequisites:

- The operating system of the disk image must be one that Image Builder supports. For
  a list of supported operating systems, see [Supported operating systems for ISO disk image import](#iso-import-supported-os "#iso-import-supported-os").
- To ensure that you can import your ISO image, download it from the Microsoft 365
  admin center.
- Before you can run the import process, you must upload your ISO disk
  file to Amazon S3 in the same AWS account and AWS Region where the import runs.
- The file extension is case sensitive for the import process, and must be
  `.ISO`. If your file extension is lowercase, you can run one of the following
  commands to rename it:

Command

```
aws s3 cp s3://`amzn-s3-demo-bucket`/`Win11_24H2_English`.iso s3://`amzn-s3-demo-bucket`/`Win11_24H2_English`.ISO
```

PowerShell

```
Copy-S3Object -BucketName `amzn-s3-demo-bucket` -Key `Win11_24H2_English`.iso -DestinationKey `Win11_24H2_English`.ISO
```

- Microsoft licensing is not automatically included with the import. You must bring
  your own license (BYOL). For more information about licensing for Microsoft software,
  see [Licensing](https://aws.amazon.com/windows/faq/#licensing-q "https://aws.amazon.com/windows/faq/#licensing-q") on the
  _Amazon Web Services and Microsoft Frequently Asked Questions_
  page.
- The import process uses two separate IAM roles, as follows:

**Execution role**

This role grants permission for Image Builder to call AWS services on
your behalf. You can specify the
[AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked
role, which includes the permissions needed for the execution role, or
you can create your own role.

**Instance profile role**

This role grants permission for the actions that the service
performs on the EC2 instance. You can specify an instance profile
role in your infrastructure configuration resource. Attach the following
managed policies to your instance profile role to ensure that you have
all of the permissions needed for the import process.

    + [EC2InstanceProfileForImageBuilder](../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilder.md "../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilder.md")
    + [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md")

For more information, see [Manage Image Builder infrastructure configuration](manage-infra-config.md "manage-infra-config.md").

## Import an ISO disk image into Image Builder

Before you start the import process, make sure that you've met all of the
[Prerequisites](#iso-import-prereq "#iso-import-prereq").

The import process installs the following software and drivers on your
image:

- EC2Launch v2
- AWS Systems Manager agent
- AWS NVMe driver
- AWS ENA network driver
- AWS PCI Serial Driver
- EC2 Windows Utility Driver
- Microsoft Defender Update Kit

The import process makes the following configuration updates on your
image:

- Configures the system to use the Amazon Time server.

Console
To import an ISO disk image with the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Images** from the
   navigation pane.
3. To open the import dialog, choose **Import image**.
4. Enter the following **General** information:
   - Specify a unique **Name** for your image.
   - Specify a **Version** for the base image. Use the
     following format: `*major*.*minor*.*patch*`.

5. Choose the import type: **ISO import**.
6. Enter the following **ISO import configuration**
   details. Then choose **Import image** when you're done.
   - **S3 URI** – Enter the location
     where your ISO disk file is stored. To browse for the file,
     choose **Browse S3**.
   - **IAM role** – To associate an IAM role
     with your import configuration, select the role from the
     **IAM role** dropdown list, or choose
     **Create new role** to create a new one. If you
     create a new role, the IAM Roles console page opens in a
     separate tab.

   You can specify the [AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked
   role, or you can specify your own custom role for service access.

7. You can optionally add tags to your Image Builder image resource. This does
   not add the tags to your AMI.
8. The **ISO infrastructure configuration** defines
   settings for the instance that Image Builder launches to host the import
   process. You can use an infrastructure configuration that Image Builder creates,
   based on service defaults, or you can use an existing infrastructure
   configuration. For more information, see [Manage Image Builder infrastructure configuration](manage-infra-config.md "manage-infra-config.md").

To create a new infrastructure configuration , choose
**Create infrastructure configuration**. This opens
in a separate tab. When you're done creating the new resource, you
can return to the import configuration, and choose **Use
existing infrastructure configuration**. 9. To start the import process, choose **Import image**.

After the import is complete, your image appears in the list of images
that you own. For more details, see [List images](image-details-list.md#list-images "image-details-list.md#list-images").

AWS CLI
This example shows how to import an image from an ISO disk file and create an
AMI from it with the AWS CLI.

Here is a summary of the parameters that we specify in this example:

- name (string, required) –
  The name for the Image Builder image resource to create as output from the import.
- semanticVersion (string, required) –
  The semantic version for the output image that specifies the version
  in the following format, with numeric values in each position to indicate
  a specific version: <major>.<minor>.<patch>. For example,
  `1.0.0`. To learn more about semantic versioning for Image Builder resources, see
  [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").
- description (string) –
  The description of the image recipe.
- executionRole (string)
  – The name or Amazon Resource Name (ARN) for the IAM role that
  grants Image Builder access to perform workflow actions to import
  an image from a Microsoft ISO file. You can specify the [AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked
  role, or you can specify your own custom role for service access.
- platform (string, required) –
  The operating system platform for the ISO disk image. Valid values include
  `Windows`.
- osVersion (string, required) –
  The operating system version for the ISO disk image. Valid values include
  `Microsoft Windows 11`.
- infrastructureConfigurationArn
  (string, required) – The Amazon Resource Name (ARN) of the
  infrastructure configuration resource that's used for launching the
  EC2 instance on which the ISO image is built.
- uri (string, required) – The
  URI of the ISO disk file that's stored in Amazon S3.

```
aws imagebuilder import-disk-image \
    --name "`example-iso-disk-import`" \
    --semantic-version "`1.0.0`" \
    --description "`Import an ISO disk image`" \
    --execution-role "`AWSServiceRoleForImageBuilder`" \
    --platform "Windows" \
    --os-version "Microsoft Windows 11" \
    --infrastructure-configuration-arn "arn:aws:imagebuilder:`us-east-1`:`111122223333`:infrastructure-configuration/`example-infrastructure-configuration-123456789abc`",
    --uri: "s3://`amzn-s3-demo-source-bucket`/`examplefile.iso`"
```

After the import is complete, your image appears in the list of images
that you own. For more details, see [List images](image-details-list.md#list-images "image-details-list.md#list-images").

PowerShell
This example shows how to import an image from an ISO disk file and create an
AMI from it with PowerShell.

Here is a summary of the parameters that we specify in this example:

- name (string, required) –
  The name for the Image Builder image resource to create as output from the import.
- semanticVersion (string, required) –
  The semantic version for the output image that specifies the version
  in the following format, with numeric values in each position to indicate
  a specific version: <major>.<minor>.<patch>. For example,
  `1.0.0`. To learn more about semantic versioning for Image Builder resources, see
  [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").
- description (string) –
  The description of the image recipe.
- executionRole (string)
  – The name or Amazon Resource Name (ARN) for the IAM role that
  grants Image Builder access to perform workflow actions to import
  an image from a Microsoft ISO file. You can specify the [AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked
  role, or you can specify your own custom role for service access.
- platform (string, required) –
  The operating system platform for the ISO disk image. Valid values include
  `Windows`.
- osVersion (string, required) –
  The operating system version for the ISO disk image. Valid values include
  `Microsoft Windows 11`.
- infrastructureConfigurationArn
  (string, required) – The Amazon Resource Name (ARN) of the
  infrastructure configuration resource that's used for launching the
  EC2 instance on which the ISO image is built.
- uri (string, required) – The
  URI of the ISO disk file that's stored in Amazon S3.

```
Import-EC2IBDiskImage `
    -Name "`example-iso-disk-import`" `
    -SemanticVersion "`1.0.0`" `
    -Description "`Import an ISO disk image`" `
    -ExecutionRole "`AWSServiceRoleForImageBuilder`" `
    -Platform "Windows" `
    -OsVersion "Microsoft Windows 11" `
    -InfrastructureConfigurationArn "arn:aws:imagebuilder:`us-east-1`:`111122223333`:infrastructure-configuration/`example-infrastructure-configuration-123456789abc`" `
    -Uri "s3://`amzn-s3-demo-source-bucket`/examplefile.ISO"
```

After the import is complete, your image appears in the list of images
that you own. For more details, see [List images](image-details-list.md#list-images "image-details-list.md#list-images").

## Launch an instance from the output AMI

When you launch an instance from an AMI that the import process creates, the Windows operating system
runs Sysprep Specialize, which automatically downloads and installs EC2Launch v2 and the Systems Manager Agent
from public S3 endpoints. These endpoints require public internet access. If you launch an
instance from a private subnet, the Sysprep Specialize process is unable to access the S3 endpoints,
and the launch fails.
