# Import verified Windows ISO disk images with Image Builder

A Windows operating system ISO file is a disk image file that contains the complete
installation package for a specific version of the Windows operating system. Microsoft
provides official Windows operating system ISO files for download, either directly from
their website or through authorized resellers. To avoid potential malware or
unauthorized versions, obtain the ISO files from a trusted and legitimate source.

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

###### Note

During the import process, the build instance downloads AWS drivers,
EC2Launch v2, and the Systems Manager Agent from Amazon S3, and
[Microsoft
Defender](https://go.microsoft.com/fwlink/?linkid=2144531 "https://go.microsoft.com/fwlink/?linkid=2144531") from the public internet. These components are pre-staged
onto the output AMI. The build instance also communicates with Amazon EC2,
Amazon CloudWatch Logs, and SSM APIs.

The build instance downloads AWS drivers from a Regional Amazon S3 bucket in the
same AWS Region where the import runs. Because this traffic stays within the
Region, the Amazon S3 Gateway endpoint is sufficient to download the drivers in any
Region.

However, Microsoft Defender requires public internet access to download regardless
of Region. If the build instance does not have internet access, the import
still succeeds but does not install Microsoft Defender on the output AMI.

For the list of the minimal required VPC endpoints and S3 URLs, see
[Minimal network requirements for private VPC](#iso-import-network-requirements "#iso-import-network-requirements").

To import an ISO disk image, you must meet the following prerequisites:

- The operating system of the disk image must be one that Image Builder supports. For
  a list of supported operating systems, see [Supported operating systems for ISO disk image import](#iso-import-supported-os "#iso-import-supported-os").
- To ensure that you can import your ISO image, download it from the Microsoft 365
  admin center.
- You must upload your ISO disk file to Amazon S3 in the same AWS account and
  AWS Region where the import runs before you can run the import process.
- The file extension is case-sensitive for the import process and must be
  `.ISO`. If your file extension is lowercase, run one of the following
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
- The import process uses two separate IAM roles:

**Execution role**

This role grants permission for Image Builder to call AWS services on
your behalf during the import process.

###### Important

We recommend that you don't pass the
[AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked
role as your execution role. Instead, create a custom IAM role and
attach the [EC2ImageBuilderExecutionPolicy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy "security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy") AWS managed
policy. This policy grants the same permissions that Image Builder needs to call
AWS services on your behalf. Using a custom role gives you full control
over the permissions that Image Builder uses. It also keeps your service control
policies (SCPs) and resource control policies (RCPs) in effect for
operations that Image Builder performs on your behalf.

**Instance profile role**

This role grants permission for the actions that the service
performs on the EC2 instance. You can specify an instance profile
role in your infrastructure configuration resource. Attach the following
managed policies to your instance profile role to ensure that you have
all of the permissions needed for the import process:

    + [EC2InstanceProfileForImageBuilder](../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilder.md "../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilder.md")
    + [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md")

For more information, see [Manage Image Builder infrastructure configuration](manage-infra-config.md "manage-infra-config.md").

## Optional import settings

You can optionally configure the following settings when you import an ISO
disk image. These settings control Secure Boot, UEFI data, and image index
selection for the imported image.

**Secure Boot**

Secure Boot is a UEFI security feature that ensures only trusted
software runs during the boot process. By default, Secure Boot is
enabled for ISO disk image imports. You can disable Secure Boot if
you need to use custom unsigned drivers for testing or legacy
application compatibility.

**Custom UEFI data**

You can provide a custom UEFI data blob as a Base64-encoded string
to use during the boot process instead of the default UEFI data that
Image Builder generates. You can specify custom UEFI data only when Secure
Boot is enabled (the default). The data can be at most 64 KB.

You can inspect and modify UEFI data by using the
[python-uefivars](https://github.com/awslabs/python-uefivars "https://github.com/awslabs/python-uefivars") tool on the GitHub website. For more information, see
[UEFI
variables for Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/uefi-variables.md "../../../AWSEC2/latest/UserGuide/uefi-variables.md").

**Image index**

A Windows ISO file can contain a `.wim` file with
multiple image indexes, where each index represents a different
Windows edition (for example, Home or Pro). By default, Image Builder uses
the first valid image index from the ISO file. You can specify a
one-based image index to select a specific edition from a
multi-edition ISO file.

## Import an ISO disk image into Image Builder

Before you start the import process, make sure that you have met all of the
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

Choose a tab to view the import steps for your preferred method:

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
   details. Then choose **Import image** when you are done.

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

7. You can optionally configure the following advanced settings
   for the import. For more information about these settings, see
   [Optional import settings](#iso-import-optional-settings "#iso-import-optional-settings").

   - **Secure Boot** – Secure Boot
     is enabled by default. To disable Secure Boot for the
     imported image, clear the **Secure Boot**
     check box.
   - **Custom UEFI data** – To
     provide a custom UEFI data blob, enter the Base64-encoded
     string. This option is available only when Secure Boot is
     enabled.
   - **Image index** – To select a
     specific Windows edition from a multi-edition ISO file,
     enter the one-based image index.

8. You can optionally add tags to your Image Builder image resource. Adding
   tags here does not add the tags to your AMI.
9. The **ISO infrastructure configuration** defines
   settings for the instance that Image Builder launches to host the import
   process. You can use an infrastructure configuration that Image Builder creates
   based on service defaults, or you can use an existing infrastructure
   configuration. For more information, see [Manage Image Builder infrastructure configuration](manage-infra-config.md "manage-infra-config.md").

To create a new infrastructure configuration, choose
**Create infrastructure configuration**. This opens
in a separate tab. After you finish creating the new resource, you
can return to the import configuration and choose **Use
existing infrastructure configuration**. 10. To start the import process, choose **Import image**.

After the import is complete, your image appears in the list of images
that you own. For more details, see [List images](image-details-list.md#list-images "image-details-list.md#list-images").

AWS CLI
The following example shows how to import an image from an ISO disk file and create an
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
  an image from a Microsoft ISO file. We recommend that you specify a custom
  role that has the [EC2ImageBuilderExecutionPolicy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy "security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy") AWS managed
  policy attached.
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
- registerImageOptions (object) –
  Configures Secure Boot and UEFI settings for the imported image.
  Contains the following fields:

  - secureBootEnabled (boolean) –
    Specifies whether Secure Boot is enabled for the output AMI.
    The default value is `true`. To disable Secure Boot
    for custom unsigned drivers, set this value to `false`.
  - uefiData (string) –
    A Base64-encoded representation of the non-volatile UEFI variable store.
    You can specify this parameter only when `secureBootEnabled`
    is `true` or unspecified.

- windowsConfiguration (object) –
  Windows-specific configuration settings for the ISO import.
  Contains the following fields:

  - imageIndex (integer) –
    The 1-based index that specifies which Windows edition to install
    from a multi-edition Windows ISO file. A Windows ISO can contain a
    `.wim` file with multiple image indexes, each representing
    a different edition.

```
aws imagebuilder import-disk-image \
    --name "`example-iso-disk-import`" \
    --semantic-version "`1.0.0`" \
    --description "`Import an ISO disk image`" \
    --execution-role "`ImageBuilderExecutionRole`" \
    --platform "Windows" \
    --os-version "Microsoft Windows 11" \
    --infrastructure-configuration-arn "arn:aws:imagebuilder:`us-east-1`:`111122223333`:infrastructure-configuration/`example-infrastructure-configuration-123456789abc`" \
    --uri "s3://`amzn-s3-demo-source-bucket`/`examplefile.ISO`" \
    --register-image-options '{"secureBootEnabled": `true`, "uefiData": "`custom-base64-encoded-uefi-data`"}' \
    --windows-configuration '{"imageIndex": `1`}'
```

After the import is complete, your image appears in the list of images
that you own. For more details, see [List images](image-details-list.md#list-images "image-details-list.md#list-images").

PowerShell
The following example shows how to import an image from an ISO disk file and create an
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
  an image from a Microsoft ISO file. We recommend that you specify a custom
  role that has the [EC2ImageBuilderExecutionPolicy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy "security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy") AWS managed
  policy attached.
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
- registerImageOptions (object) –
  Configures Secure Boot and UEFI settings for the imported image.
  Contains the following fields:

  - secureBootEnabled (boolean) –
    Specifies whether Secure Boot is enabled for the output AMI.
    The default value is `true`. To disable Secure Boot
    for custom unsigned drivers, set this value to `false`.
  - uefiData (string) –
    A Base64-encoded representation of the non-volatile UEFI variable store.
    You can specify this parameter only when `secureBootEnabled`
    is `true` or unspecified.

- windowsConfiguration (object) –
  Windows-specific configuration settings for the ISO import.
  Contains the following fields:

  - imageIndex (integer) –
    The 1-based index that specifies which Windows edition to install
    from a multi-edition Windows ISO file. A Windows ISO can contain a
    `.wim` file with multiple image indexes, each representing
    a different edition.

```
Import-EC2IBDiskImage `
    -Name "`example-iso-disk-import`" `
    -SemanticVersion "`1.0.0`" `
    -Description "`Import an ISO disk image`" `
    -ExecutionRole "`ImageBuilderExecutionRole`" `
    -Platform "Windows" `
    -OsVersion "Microsoft Windows 11" `
    -InfrastructureConfigurationArn "arn:aws:imagebuilder:`us-east-1`:`111122223333`:infrastructure-configuration/`example-infrastructure-configuration-123456789abc`" `
    -Uri "s3://`amzn-s3-demo-source-bucket`/examplefile.ISO" `
    -RegisterImageOptions_SecureBootEnabled `$true` `
    -RegisterImageOptions_UefiData "`custom-base64-encoded-uefi-data`" `
    -WindowsConfiguration_ImageIndex `1`
```

After the import is complete, your image appears in the list of images
that you own. For more details, see [List images](image-details-list.md#list-images "image-details-list.md#list-images").

## Launch an instance from the output AMI

You can now use the output AMI as a regular AMI and launch instances from it.
When you launch an instance from the output AMI, the Windows operating system
runs Sysprep Specialize to finalize the instance configuration.

###### Note

The network requirements described on this page apply to the import
build process only. After the import completes successfully, launching
instances from the output AMI follows standard Amazon EC2 networking
requirements. A successful import does not guarantee a successful instance
launch — your launch might still fail depending on your network
configuration.

## Minimal network requirements for private VPC

**Required VPC endpoints:**

| Endpoint                               | Type      | Purpose                                                                          |
| -------------------------------------- | --------- | -------------------------------------------------------------------------------- |
| `com.amazonaws.`{region}`.s3`          | Gateway   | Access Amazon S3 buckets (EC2Launch v2, SSM Agent, AWS drivers,<br>and your ISO) |
| `com.amazonaws.`{region}`.ec2`         | Interface | Create snapshots and describe volumes                                            |
| `com.amazonaws.`{region}`.logs`        | Interface | Write build logs to CloudWatch Logs                                              |
| `com.amazonaws.`{region}`.ssm`         | Interface | SSM API calls (SendCommand, DescribeInstanceInformation)                         |
| `com.amazonaws.`{region}`.ssmmessages` | Interface | SSM Agent data channel (receive commands, send output)                           |
| `com.amazonaws.`{region}`.ec2messages` | Interface | SSM Agent message polling                                                        |

**Amazon S3 endpoints accessed during import:**

- `https://ec2-windows-drivers-downloads-`{region}`.s3.dualstack.`{region}`.amazonaws.com/NVMe/Latest/AWSNVMe.zip`
- `https://ec2-windows-drivers-downloads-`{region}`.s3.dualstack.`{region}`.amazonaws.com/ENA/Latest/AwsEnaNetworkDriver.zip`
- `https://ec2-windows-drivers-downloads-`{region}`.s3.dualstack.`{region}`.amazonaws.com/AWSPCISerialDriver/Latest/AWSPCISerialDriver.zip`
- `https://ec2-windows-drivers-downloads-`{region}`.s3.dualstack.`{region}`.amazonaws.com/EC2WinUtil/Latest/EC2WinUtil.zip`
- `https://amazon-ec2launch-v2-`{region}`.s3.dualstack.`{region}`.amazonaws.com/windows/amd64/latest/AmazonEC2Launch.msi`
- `https://amazon-ssm-`{region}`.s3.`{region}`.amazonaws.com/latest/windows_amd64/AmazonSSMAgentSetup.exe`

###### Note

In `us-east-1`, the driver bucket name has no Region suffix. The build instance downloads the drivers from
`ec2-windows-drivers-downloads.s3.dualstack.us-east-1.amazonaws.com` instead. In both cases, the bucket is
in the same Region as the import, so the Amazon S3 Gateway endpoint is sufficient.

This represents the minimum configuration required for the import to
operate in a private subnet. Depending on your VPC settings and desired outcome,
you may need additional network configuration to allow traffic between the build
instance and the VPC endpoints.

## Next steps

You can use the output AMI like any other AMI – launch instances from it directly,
or use it as a base image in Image Builder to build and customize further. For more information,
see [Create custom images with Image Builder](create-images.md "create-images.md").

## Troubleshoot ISO disk image imports

If your ISO disk image import fails, you can use Amazon CloudWatch Logs to identify where the import went wrong. Image Builder streams build logs to CloudWatch Logs after the build completes. To find the logs for your import, use the following log group and stream, replacing `ImageName` with the name you gave your image:

**LogGroup:** `/aws/imagebuilder/`ImageName``

**LogStream:** ``ImageVersion`/`ImageBuildVersion``

For more information about Image Builder logs in CloudWatch Logs, see [Monitor Image Builder logs with Amazon CloudWatch Logs](monitor-cwlogs.md "monitor-cwlogs.md"). For additional troubleshooting guidance, see [Troubleshoot Image Builder issues](troubleshooting.md "troubleshooting.md").
