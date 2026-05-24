# Getting started with AWS DataSync

Before you get started with AWS DataSync, you need to sign up for an AWS account if you
don't have one. We also recommend learning where DataSync can be used and how much it might
cost to transfer your data.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Required IAM permissions for using DataSync

DataSync can transfer your data to or from an Amazon S3 bucket, Amazon EFS file system, or Amazon FSx file system.
To get your data where you want it to go, you need the right IAM permissions granted to
your identity. For example, the IAM role that you use with DataSync needs permission to
use the Amazon S3 operations required to transfer data to an S3 bucket.

You can grant these permissions with IAM policies provided by AWS or by creating
your own policies.

###### Contents

- [AWS managed policies](setting-up.md#permissions-requirements-managed "setting-up.md#permissions-requirements-managed")
- [Customer managed policies](setting-up.md#permissions-requirements-customer-managed "setting-up.md#permissions-requirements-customer-managed")

### AWS managed policies

AWS provides the following managed policies for common DataSync use cases:

- `AWSDataSyncReadOnlyAccess` – Provides read-only access
  to DataSync.
- `AWSDataSyncFullAccess` – Provides full access to DataSync
  and minimal access to its dependencies.

For more information, see [AWS managed policies for AWS DataSync](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

### Customer managed policies

You can create custom IAM policies to use with DataSync. For more information, see
[IAM customer managed policies for AWS DataSync](using-identity-based-policies.md "using-identity-based-policies.md").

## Where can I use DataSync?

For a list of AWS Regions and endpoints that DataSync supports, see [AWS DataSync endpoints and
quotas](../../../general/latest/gr/datasync.md "../../../general/latest/gr/datasync.md") in the _AWS General Reference_.

## How can I use DataSync?

There are several ways to use DataSync:

- [DataSync console](https://console.aws.amazon.com/datasync/home "https://console.aws.amazon.com/datasync/home"), which is
  part of the AWS Management Console.
- [DataSync API](API_Reference.md "API_Reference.md") or the [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync") to programmatically configure and manage DataSync.
- [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/AWS_DataSync.md "../../../AWSCloudFormation/latest/UserGuide/AWS_DataSync.md")
  or [Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/datasync_agent "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/datasync_agent") to provision your DataSync resources.
- [AWS SDKs](https://aws.amazon.com/developer/ "https://aws.amazon.com/developer/") to build
  applications that use DataSync.

## How much will DataSync cost?

To create a custom estimate using the amount of data that you plan to transfer, see [DataSync pricing](https://aws.amazon.com/datasync/pricing "https://aws.amazon.com/datasync/pricing").

## Open-source components used by DataSync

To view the open-source components used by DataSync, download the following link:

- [datasync-open-source-components.zip](samples/datasync-open-source-components.zip.md "samples/datasync-open-source-components.zip.md")
