# Amazon EC2 in AWS GovCloud (US)

Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizeable computing capacity—literally, servers in Amazon’s data centers—that you use to build and host your software systems.

## How Amazon Elastic Compute Cloud differs for AWS GovCloud (US)

The implementation of Amazon EC2 is different for AWS GovCloud (US) in the following ways:

###### General differences

- Use SSL (HTTPS) when you make calls to the service in AWS GovCloud (US) Regions. In other AWS Regions, you can use HTTP or HTTPS.
- Use SSL (HTTPS) when generating key pairs using [ec2-create-keypair](../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-CreateKeyPair.md "../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-CreateKeyPair.md") and [CreateKeyPair](../../../AWSEC2/latest/APIReference/API_CreateKeyPair.md "../../../AWSEC2/latest/APIReference/API_CreateKeyPair.md") commands.
- To import your own set of key pairs, follow the instructions in [Create a key pair using a third-party tool and import the public key to Amazon EC2](../../../AWSEC2/latest/UserGuide/create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws "../../../AWSEC2/latest/UserGuide/create-key-pairs.md#how-to-generate-your-own-key-and-import-it-to-aws").

###### Billing and purchasing differences

- Reserved Instance resale is not supported.
- Savings Plans can’t be purchased from AWS GovCloud (US) accounts, but can be purchased in any standard account and applied to usage in AWS GovCloud (US) Regions.
- Spot Instance data feed is not supported.
- When you use the launch instance wizard in the console to launch an instance using an AWS Marketplace AMI, we don’t automatically subscribe you to the AMI as we do in other AWS Regions. Instead, when you choose the AMI, choose **Subscribe with Marketplace** to open the AWS Marketplace to subscribe.
- The AWS Certificate Manager (ACM) for Nitro Enclaves AMI is not available from the AWS Marketplace. ACM for Nitro Enclaves must be installed from the Amazon Linux Extras repository.
- The Nitro Enclaves Developer AMI is not available from the AWS Marketplace.

###### Image differences

- AMI copy and snapshot copy do not support migrating AMIs and snapshots from another AWS Region into AWS GovCloud (US) Regions. For information about how to migrate your AMIs from another AWS Region into AWS GovCloud (US) Regions, see [How VM Import/Export Differs for AWS GovCloud (US)](#govcloud-vmie-diffs "#govcloud-vmie-diffs").
- When using the [Amazon EC2 AMI tools](../../../AWSEC2/latest/CommandLineReference/set-up-ami-tools.md "../../../AWSEC2/latest/CommandLineReference/set-up-ami-tools.md"), AWS GovCloud (US) Regions uses a non-default public key certificate to encrypt AMI manifests. The [ec2-bundle-image](../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-bundle-image.md "../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-bundle-image.md"), [ec2-bundle-vol](../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-bundle-vol.md "../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-bundle-vol.md"), [ec2-migrate-bundle](../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-migrate-bundle.md "../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-migrate-bundle.md"), and [ec2-migrate-manifest](../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-migrate-manifest.md "../../../AWSEC2/latest/CommandLineReference/CLTRG-ami-migrate-manifest.md") commands require the `--ec2cert $EC2_AMITOOL_HOME/etc/ec2/amitools/cert-ec2-gov.pem` option in AWS GovCloud (US) Regions.
- The `lastLaunchedTime` AMI attribute is not supported.

###### Instance differences

- The get-console-screenshot CLI command is not supported.
- Get instance screenshot is not supported.
- On-Demand Instance hibernation is not supported.
- Amazon EC2 instance topology is not supported.
- [EC2 Instance Connect](../../../AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.md "../../../AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.md") will not work if your Linux instance has SELinux enabled in enforcing mode. The process for enabling or disabling SELinux varies across Linux distributions. For information about how to check the status of SELinux on your instance, or to enable or disable SELinux, see the relevant operating system guide for your instance.
- EC2 CPU Optimization is currently API-only.
- [Attestation documents](../../../enclaves/latest/user/set-up-attestation.md "../../../enclaves/latest/user/set-up-attestation.md") used by Nitro Enclaves are signed by the AWS Nitro Attestation Public Key Infrastructure (PKI). You can verify that the attestation documents are signed by the Nitro Attestation PKI. For more information, see [Verifying the root of trust](../../../enclaves/latest/user/verify-root.md "../../../enclaves/latest/user/verify-root.md") in the _AWS Nitro Enclaves User Guide_.
  - The root certificate for the Nitro Attestation PKI is unique for each [partition](../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/partitions.md"). The root certificate for the `aws-us-gov` partition is as follows:

  ```
  -----BEGIN CERTIFICATE-----
  MIICIDCCAaWgAwIBAgIQP+wUYfyWFFRko9PR00zhZzAKBggqhkjOPQQDAzBQMQsw
  CQYDVQQGEwJVUzEPMA0GA1UECgwGQW1hem9uMQwwCgYDVQQLDANBV1MxIjAgBgNV
  BAMMGWF3cy11cy1nb3Yubml0cm8tZW5jbGF2ZXMwIBcNMjAwOTEwMTIwMzQ2WhgP
  MjA1MDA5MTAxMzAzNDZaMFAxCzAJBgNVBAYTAlVTMQ8wDQYDVQQKDAZBbWF6b24x
  DDAKBgNVBAsMA0FXUzEiMCAGA1UEAwwZYXdzLXVzLWdvdi5uaXRyby1lbmNsYXZl
  czB2MBAGByqGSM49AgEGBSuBBAAiA2IABCzkRJcZVx7Sg2yXXkl0Nqj9o1ECZNAh
  0L8/90ATZXAaS1rxA1ti1F3wE86PGsh2UiQIYXiMu81l5kO7775gPuLsgYcGMO/J
  0t08BHI8s3+JmjxTlA+/UyAqEmj7fD5CbKNCMEAwDwYDVR0TAQH/BAUwAwEB/zAd
  BgNVHQ4EFgQUUKIzFk2FAlhihuQexsqOxZ5ZjF0wDgYDVR0PAQH/BAQDAgGGMAoG
  CCqGSM49BAMDA2kAMGYCMQD9bO9epcf5kMSdsHcyNJXs4bo07wvTIOwnxN41t5eE
  SDyXtUei++RebAbI9Viap2gCMQC7PVZ6Kpg0+N9k+DDpksoJv7gx6YwCqKsmTfU/
  WigyQlpyJUrWapqk0afDA4lef14=
  -----END CERTIFICATE-----
  ```

  - The Nitro Attestation PKI root certificate for the `aws-us-gov` partition has a subject as follows:

  `CN=aws-us-gov.nitro-enclaves, C=US, O=Amazon, OU=AWS`

###### Networking differences

- When you launch an instance using the [ec2-run-instances](../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-RunInstances.md "../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-RunInstances.md") CLI command or [RunInstances](../../../AWSEC2/latest/APIReference/API_RunInstances.md "../../../AWSEC2/latest/APIReference/API_RunInstances.md") API operation, you must specify the `subnet` parameter.
- By default, enhanced networking is not enabled on Windows Server 2012 R2 AMIs. For more information, see [Optimize network performance on EC2 Windows instances](../../../AWSEC2/latest/UserGuide/enhanced-networking-os.md "../../../AWSEC2/latest/UserGuide/enhanced-networking-os.md").

## How VM Import/Export Differs for AWS GovCloud (US)

VM Import/Export is different for AWS GovCloud (US) in the following ways:

- When using VM Import:
  - If your account is set up as default VPC, then your default VPC will be the target for your import.
  - If your account is not set up as default VPC, then you will need to specify an Availability Zone and subnet. To specify a subnet to use when you create the import task, use the `--subnet –0—` option and `–z –1—` option (specifying the Availability Zone corresponding to the subnet ID) with the [ec2-import-instance](../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-ImportInstance.md "../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-ImportInstance.md") command.

- When using VM Export:
  - The Amazon EC2 instance must have been previously imported using VM Import.
  - The Amazon S3 bucket for the destination image must exist and must have WRITE and READ_ACP permissions granted to the AWS GovCloud (US) account with canonical ID: af913ca13efe7a94b88392711f6cfc8aa07c9d1454d4f190a624b126733a5602.
  - To export an instance, you can use the [ec2-create-instance-export-task](../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-CreateInstanceExportTask.md "../../../AWSEC2/latest/CommandLineReference/ApiReference-cmd-CreateInstanceExportTask.md") command. For more information, see [Exporting an instance as a VM using VM Import/Export](../../../vm-import/latest/userguide/vmexport.md "../../../vm-import/latest/userguide/vmexport.md").

## Determining if your account has a default VPC

Your account might have a default VPC. If your account doesn’t have a default VPC, you must create a VPC before you can launch EC2 instances. For more information, see [Virtual private clouds for your EC2 instances](../../../AWSEC2/latest/UserGuide/using-vpc.md "../../../AWSEC2/latest/UserGuide/using-vpc.md") in the _Amazon EC2 User Guide_.

If you don’t want a default VPC for your AWS GovCloud (US) account, you can delete the default VPC and default subnets.
The default VPC and subnets will not be recreated.
However, you still need to create a VPC before launching instances.

If you deleted your default VPC, you can create a new one. For more information, see [Create a default VPC](../../../vpc/latest/userguide/work-with-default-vpc.md#create-default-vpc "../../../vpc/latest/userguide/work-with-default-vpc.md#create-default-vpc") in the _Amazon VPC User Guide_.

If your account doesn’t have a default VPC but you want a default VPC, you can submit a request by completing the [AWS GovCloud (US) – Contact Us](https://aws.amazon.com/govcloud-us/contact/ "https://aws.amazon.com/govcloud-us/contact/") form.
In the form, include your AWS GovCloud (US-West) account ID and indicate that you want to enable your account for a default VPC.

## Documentation for Amazon EC2

The following documentation is based on the public AWS documentation. As you read this documentation, you should consider how Amazon EC2 differs for AWS GovCloud (US) Regions, as described in this topic. Also, some features and new functionality described in this documentation might not be available in the current release of AWS GovCloud (US) Regions. There are other differences, such as links, endpoints, and screenshots.

[Amazon Elastic Compute Cloud documentation](../../../ec2.md "../../../ec2.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon EC2 metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your instances.
- Do not enter export-controlled data in the following fields:
  - Instance names
  - AMI descriptions
  - Resource tags

- Key pairs created using HTTP.
- When using VM Import, you may not enter any export-controlled data as part of CLI arguments, paths, or OS disk images. Any data that is export-controlled should be encrypted and placed in partitions other than root and boot.
- If importing export-controlled images, do not use pre-signed URLs for the CLI argument `–0—`.
