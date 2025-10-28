# Getting started with AWS DataSync

Before you get started with AWS DataSync, you need to sign up for an AWS account if you
don't have one. We also recommend learning where DataSync can be used and how much it might
cost to transfer your data.

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Required IAM permissions for using

DataSync

DataSync can transfer your data to an Amazon S3 bucket, Amazon EFS file system, or a [number of other AWS storage services](working-with-locations.md "working-with-locations.md"). To
get your data where you want it to go, you need the right IAM permissions granted to
your identity. For example, the IAM role that you use with DataSync needs permission to
use the Amazon S3 operations required to transfer data to an S3 bucket.

You can grant these permissions with IAM policies provided by AWS or by creating
your own policies.

###### Contents

- [AWS managed policies](setting-up.md#permissions-requirements-managed "setting-up.md#permissions-requirements-managed")
- [Customer managed
  policies](setting-up.md#permissions-requirements-customer-managed "setting-up.md#permissions-requirements-customer-managed")

### AWS managed policies

AWS provides the following managed policies for common DataSync use cases:

- `AWSDataSyncReadOnlyAccess` – Provides read-only access
  to DataSync.
- `AWSDataSyncFullAccess` – Provides full access to DataSync
  and minimal access to its dependencies.

For more information, see [AWS managed policies for AWS DataSync](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

### Customer managed

policies

You can create custom IAM policies to use with DataSync. For more information, see
[IAM customer managed policies for
AWS DataSync](using-identity-based-policies.md "using-identity-based-policies.md").

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

On the [DataSync pricing](https://aws.amazon.com/datasync/pricing "https://aws.amazon.com/datasync/pricing") page,
create a custom estimate using the amount of data that you plan to transfer.

## Open-source components used by DataSync

To view the open-source components used by DataSync, download the following link:

- [datasync-open-source-components.zip](samples/datasync-open-source-components.md "samples/datasync-open-source-components.md")
