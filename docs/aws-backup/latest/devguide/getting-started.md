# Getting started with AWS Backup

This tutorial shows you the generic steps for using AWS Backup features and functionality. As
with any part of this technical documentation, you should follow along with the AWS Management
Console in the other window.

## Prerequisites

Before you begin, ensure that you have the following:

- An AWS account. For more information, see [Create an AWS
  account](../../../accounts/latest/reference/manage-acct-creating.md "../../../accounts/latest/reference/manage-acct-creating.md").
- At least one resource supported by AWS Backup. See the list of [supported AWS
  resources and third-party applications](whatisbackup.md#supported-resources "whatisbackup.md#supported-resources").

When new AWS services become available, enable AWS Backup to use those services.

- If you intend to include multiple resource types, such as Amazon EBS volumes and Amazon S3
  buckets, in the same backup plan, confirm those resources are in the same AWS Region.

###### To configure the AWS services to use with AWS Backup

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Settings**.
3. On the **Service opt-in** page, choose **Configure
   resources**.
4. On the **Configure resources** page, use the toggle switches to
   enable or disable the services that are used with AWS Backup. Choose
   **Confirm** when your services are configured. Make sure that the AWS
   service you're opting in is available in your AWS Region.

See for
additional information. The AWS Backup console allows a user to assign a resource type to a backup
plan; this will be included even if the opt-in is not enabled for that particular
service.

To complete this tutorial, you can use your AWS account root user to sign in to the
AWS Management Console. However, AWS Identity and Access Management (IAM) recommends that you not use the AWS account root user.
Instead, create an administrator in your account and use those credentials to manage resources
in your account.

The AWS Backup console provides different options to back up your resources. You can create a
backup on-demand, schedule and configure how you want the resource backed up, or configure
resources to back up automatically when the resource is created.

## Service Opt-in

The AWS Backup console has two ways to include resource types in a backup plan: explicitly
assign the resource type in a backup plan or include all resources. See the points below to
understand how these selections work with service opt ins.

- If resource assignments are only based on tags, then service opt-in settings are
  applied.
- If a resource type is explicitly assigned to a backup plan, it will be included in the
  backup even if the opt-in is not enabled for that particular service. This does not apply
  to Aurora, Neptune, and Amazon DocumentDB. For these services to be included, the opt-in must be
  enabled.
- If both resource type and tags are specified in a resource assignment, the specified
  resource types are filtered first, then tags further filter those resources.

Service opt-in settings are ignored for most resource types. However Aurora,
Neptune, and Amazon DocumentDB require service opt-in.

- For Amazon FSx for NetApp ONTAP, when using tag-based resource selection, apply tags to individual
  volumes instead of the whole file system.

Opt-in choices apply to the specific account and AWS Region. When an account uses AWS Backup
(creates a backup vault or backup plan) in a Region, the account automatically is opted into
all resource types supported by AWS Backup in the Region at that time. Supported services added to
that Region at a later date will not be automatically included in a backup plan. You can
choose to opt into those resource types once they become supported.

As AWS Backup supports more and more AWS services and third-party applications, you might
need to revisit this step to opt in to those newly-supported resources.

AWS Backup does not govern or manage backups taken in AWS environments other than
AWS Backup.

###### Note

For more information on how service opt-ins work for management and delegated administrator accounts, see [Managing AWS Backup resources across multiple AWS accounts](manage-cross-account.md "manage-cross-account.md").

###### To opt in to use AWS Backup to protect all supported resource types

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, choose **Settings**.
3. Under **Service opt-in**, choose **Configure
   resources**.
4. Opt in to all AWS Backup-supported **Resources** by moving all the toggles
   to the right.
5. Choose **Confirm**.
