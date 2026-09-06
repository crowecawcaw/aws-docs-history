

# Getting started with AWS DataSync
<a name="setting-up"></a>

Before you get started with AWS DataSync, you need to sign up for an AWS account if you don't have one. We also recommend learning where DataSync can be used and how much it might cost to transfer your data.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Required IAM permissions for using DataSync
<a name="permissions-requirements"></a>

DataSync can transfer your data to or from an Amazon S3 bucket, Amazon EFS file system, or Amazon FSx file system. To get your data where you want it to go, you need the right IAM permissions granted to your identity. For example, the IAM role that you use with DataSync needs permission to use the Amazon S3 operations required to transfer data to an S3 bucket.

You can grant these permissions with IAM policies provided by AWS or by creating your own policies.

**Contents**
+ [AWS managed policies](#permissions-requirements-managed)
+ [Customer managed policies](#permissions-requirements-customer-managed)

### AWS managed policies
<a name="permissions-requirements-managed"></a>

AWS provides the following managed policies for common DataSync use cases:
+ `AWSDataSyncReadOnlyAccess` – Provides read-only access to DataSync.
+ `AWSDataSyncFullAccess` – Provides full access to DataSync and minimal access to its dependencies.

For more information, see [AWS managed policies for AWS DataSync](security-iam-awsmanpol.md).

### Customer managed policies
<a name="permissions-requirements-customer-managed"></a>

You can create custom IAM policies to use with DataSync. For more information, see [IAM customer managed policies for AWS DataSync](using-identity-based-policies.md).

## Where can I use DataSync?
<a name="datasync-regions"></a>

For a list of AWS Regions and endpoints that DataSync supports, see [AWS DataSync endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/datasync.html) in the *AWS General Reference*.

## How can I use DataSync?
<a name="datasync-access"></a>

There are several ways to use DataSync:
+ [DataSync console](https://console.aws.amazon.com/datasync/home), which is part of the AWS Management Console.
+ [DataSync API](https://docs.aws.amazon.com/datasync/latest/apireference/Welcome.html) or the [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync) to programmatically configure and manage DataSync.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataSync.html) or [Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/datasync_agent) to provision your DataSync resources.
+ [AWS SDKs](https://aws.amazon.com/developer/) to build applications that use DataSync.

## How much will DataSync cost?
<a name="datasync-pricing"></a>

To create a custom estimate using the amount of data that you plan to transfer, see [DataSync pricing](https://aws.amazon.com/datasync/pricing). 

## Open-source components used by DataSync
<a name="datasync-os-attributions"></a>

To view the open-source components used by DataSync, download the following link:
+ [datasync-open-source-components.zip](samples/datasync-open-source-components.zip)