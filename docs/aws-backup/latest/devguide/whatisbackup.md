# What is AWS Backup?

AWS Backup is a fully-managed service that makes it easy to centralize and automate data
protection across AWS services, in the cloud, and on premises. Using this service, you can
configure backup policies and monitor activity for your AWS resources in one place. It allows
you to automate and consolidate backup tasks that were previously performed service-by-service,
and removes the need to create custom scripts and manual processes. With a few clicks in the
AWS Backup console, you can automate your data protection policies and schedules.

AWS Backup does not govern backups you take in your AWS environment outside of AWS Backup.
Therefore, if you want a centralized, end-to-end solution for business and regulatory compliance
requirements, start using AWS Backup today.

## Feature overview

AWS Backup provides many features and capabilities, including the following.

### Centralized backup management

AWS Backup provides a centralized backup console, a set of backup APIs, and the AWS Command Line Interface
(AWS CLI) to manage backups across the AWS services that your applications use. With AWS Backup,
you can centrally manage backup policies that meet your backup requirements. You can then
apply them to your AWS resources across AWS services, enabling you to back up your
application data in a consistent and compliant manner. The AWS Backup centralized backup console
offers a consolidated view of your backups and backup activity logs, making it easier to
audit your backups and ensure compliance.

### Policy-based backup

With AWS Backup, you can create backup policies known as _backup plans_.
Use these backup plans to define your backup requirements and then apply them to the AWS
resources that you want to protect across the AWS services that you use. You can create
separate backup plans that each meet specific business and regulatory compliance
requirements. This helps ensure that each AWS resource is backed up according to your
requirements. Backup plans make it easy to enforce your backup strategy across your
organization and across your applications in a scalable manner.

For all the configuration options for backup plans, see [Backup plan options and
configuration](plan-options-and-configuration.md "plan-options-and-configuration.md").

### Tag-based backup policies

You can use AWS Backup to apply backup plans to your AWS resources in a wide variety of
ways, including tagging them. Tagging makes it easier to implement your backup strategy
across all your applications and to ensure that all your AWS resources are backed up and
protected. AWS tags are a great way to organize and classify your AWS resources.
Integration with AWS tags enables you to quickly apply a backup plan to a group of AWS
resources, so that they are backed up in a consistent and compliant manner.

For all the ways you can assign your resources to backup plans, see [Select AWS services to backup](assigning-resources.md "assigning-resources.md").

### Lifecycle management policies

AWS Backup enables you to meet compliance requirements while minimizing backup storage costs
by storing backups in a low-cost cold storage tier. You can configure lifecycle policies
that automatically transition backups from warm storage to cold storage according to a
schedule that you define.

For a list of resources which can be transitioned to cold storage, see
[Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").
For steps to turn on cold storage in your backup plan, see
[Lifecycle and storage tiers](plan-options-and-configuration.md#backup-lifecycle "plan-options-and-configuration.md#backup-lifecycle").

### Cross-Region backup

Using AWS Backup, you can copy backups to multiple different AWS Regions on demand or
automatically as part of a scheduled backup plan. Cross-Region backup is particularly
valuable if you have business continuity or compliance requirements to store backups a
minimum distance away from your production data. For more information, see [Creating
backup copies across AWS Regions](cross-region-backup.md "cross-region-backup.md").

### Cross-account management and cross-account backup

You can use AWS Backup to manage your backups across all AWS accounts inside your [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") structure. With cross-account
management, you can automatically use backup policies to apply backup plans across the
AWS accounts within your organization. This makes compliance and data protection efficient
at scale and reduces operational overhead. It also helps eliminate manually duplicating
backup plans across individual accounts. For more information, see [Managing
AWS Backup resources across multiple AWS accounts](manage-cross-account.md "manage-cross-account.md").

You can also copy backups to multiple different AWS accounts inside your AWS Organizations
management structure. This way, you can "fan in" backups to a single repository account,
then "fan out" backups for greater resilience. [Creating backup copies
across AWS accounts](create-cross-account-backup.md "create-cross-account-backup.md").

Before you can use the cross-account management and cross-account backup features, you
must have an existing organization structure configured in AWS Organizations. An
_organizational unit_ (OU) is a group of accounts that can be managed
as a single entity. AWS Organizations is a list of accounts that can be grouped into organizational
units and managed as a single entity.

### Auditing and reporting with AWS Backup Audit Manager

AWS Backup Audit Manager helps you simplify data governance and compliance management of your
backups across AWS. AWS Backup Audit Manager provides built-in, customizable controls that you
can align with your organizational requirements. You can also use these controls to
automatically track your backup activities and resources.

AWS Backup Audit Manager can help you locate specific activities and resources that are not
yet compliant with the controls that you defined. It also generates daily reports that you
can use to demonstrate evidence of compliance with your controls over time.

To include your backup compliance alongside your overall compliance posture, you can
automatically import AWS Backup Audit Manager findings into AWS Audit Manager.

### Incremental backups

AWS Backup efficiently stores your periodic backups incrementally. The first backup of an
AWS resource backs up a full copy of your data. For each successive incremental backup,
only the changes to your AWS resources are backed up. Incremental backups enable you to
benefit from the data protection of frequent backups while minimizing storage costs.

For a list of which resources support incremental backups, see [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").

For more information on behaviors in vaults, see [Incremental backups](creating-a-backup.md#incremental-backup-works "creating-a-backup.md#incremental-backup-works").

### Full AWS Backup management

Some resource types support full AWS Backup management. The benefits of full AWS Backup management
include:

- **Independent encryption**. AWS Backup automatically
  encrypts your backups with the KMS key of your AWS Backup vault, instead of using the same
  encryption key as your source resource. This increases your layers of defense. See [Encryption for backups in AWS Backup](encryption.md "encryption.md") for more information.
- **`awsbackup` Amazon Resource Names
  (ARNs)**. Backup ARNs begin with `arn:aws:backup` instead of
  `arn:aws:`source-resource``. This allows you to
  create access policies that apply specifically to backups and not the source resources.
  See [Access control](access-control.md "access-control.md") for more
  information.
- **Centralized backup billing and Cost Explorer cost allocation
  tags.**. Charges for AWS Backup (including storage, data transfers, restores, and
  early deletion) appear under "Backup" in your Amazon Web Services bill, instead of appearing under
  each supported resource. You can also use Cost Explorer cost allocation tags to track and
  optimize your backup costs. See [Metering, costs, and billing for AWS Backup](metering-and-billing.md "metering-and-billing.md") for more information.

To see which resource types are eligible for full AWS Backup management, see [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").

### Backup activity monitoring

AWS Backup provides a dashboard that makes it simple to audit backup and restore activity
across AWS services. With just a few clicks on the AWS Backup console, you can view the status
of recent backup jobs. You can also restore jobs across AWS services to ensure that your
AWS resources are properly protected.

AWS Backup integrates with Amazon CloudWatch and Amazon EventBridge. CloudWatch allows you to track metrics and create
alarms. EventBridge allows you to view and monitor AWS Backup events. For more information, see [Monitoring AWS Backup
events using EventBridge](eventbridge.md "eventbridge.md") and [Monitoring AWS Backup metrics with
CloudWatch](cloudwatch.md "cloudwatch.md").

AWS Backup integrates with AWS CloudTrail. CloudTrail gives you a consolidated view of backup activity
logs that make it quick and easy to audit how your resources are backed up. AWS Backup also
integrates with Amazon Simple Notification Service (Amazon SNS), providing you with backup activity notifications, such as
when a backup succeeds or a restore has been initiated. For more information, see [Logging AWS Backup API calls with CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md") and [Amazon SNS and AWS Backup events](backup-notifications.md#backup-notifications-section "backup-notifications.md#backup-notifications-section").

### Secure your data in backup vaults

The content of each AWS Backup backup is immutable, meaning that no one can alter that
content. AWS Backup further secures your backups in backup vaults, which separates them safely
from their source instances. For example, your vault will retain your Amazon EC2 and Amazon EBS
backups according to the lifecycle policy you choose, even if you delete the source Amazon EC2
instance and Amazon EBS volumes.

Backup vaults offer encryption and resource-based access policies that let you define
who has access to your backups. You can define access policies for a backup vault that
define who has access to the backups within that vault and what actions they can take. This
provides a simple and secure way to control access to your backups across AWS services. To
review AWS and customer managed policies for AWS Backup, see [Managed policies for
AWS Backup](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You can use AWS Backup Vault Lock to prevent anyone (including you) from deleting backups or
altering their retention period. AWS Backup Vault Lock helps you enforce a
_write-once-read-many_ (WORM) model and add another layer of defense to
your defense in depth. To get started, see [AWS Backup Vault Lock](vault-lock.md "vault-lock.md").

## Getting started

To learn more about AWS Backup, we recommend that you start with [Getting started with AWS Backup](getting-started.md "getting-started.md").

## Supported AWS resources and applications

The following are AWS resources and third-party applications that you can back up and
restore using AWS Backup. For more information, see [AWS Backup feature availability](backup-feature-availability.md "backup-feature-availability.md").

| Service                                                                                                                                                              | Supported resource types                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [Amazon Elastic Compute Cloud (Amazon EC2)](../../../AWSEC2/latest/UserGuide.md "../../../AWSEC2/latest/UserGuide.md")                                               | Amazon EC2 instances backed by Amazon EBS volumes                                                   |
| [Amazon Simple Storage Service (Amazon S3)](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")                                           | Amazon S3 data                                                                                      |
| [Amazon Elastic Block Store (Amazon EBS)](../../../ebs/latest/userguide/what-is-ebs.md "../../../ebs/latest/userguide/what-is-ebs.md")                               | Amazon EBS volumes                                                                                  |
| [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/GettingStartedDynamoDB.md "../../../amazondynamodb/latest/developerguide/GettingStartedDynamoDB.md") | Amazon DynamoDB tables                                                                              |
| [Amazon Relational Database Service (Amazon RDS)](../../../AmazonRDS/latest/UserGuide.md "../../../AmazonRDS/latest/UserGuide.md")                                   | Amazon RDS database instances (including all database engines);<br>Multi-Availability Zone clusters |
| [Amazon Aurora DSQL](../../../aurora-dsql/latest/userguide/what-is-aurora-dsql.md "../../../aurora-dsql/latest/userguide/what-is-aurora-dsql.md")                    | Single-Region clusters and multi-Region clusters                                                    |
| [Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide.md "../../../AmazonRDS/latest/AuroraUserGuide.md")                                                         | Aurora clusters                                                                                     |
| [Amazon Elastic File System (Amazon EFS)](../../../efs/latest/ug.md "../../../efs/latest/ug.md")                                                                     | Amazon EFS file systems                                                                             |
| [FSx for Lustre](../../../fsx/latest/LustreGuide.md "../../../fsx/latest/LustreGuide.md")                                                                            | FSx for Lustre file systems                                                                         |
| [FSx for Windows File Server](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md")                                             | FSx for Windows File Server file systems                                                            |
| [Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")                             | FSx for ONTAP file systems                                                                          |
| [Amazon FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/what-is-fsx.md "../../../fsx/latest/OpenZFSGuide/what-is-fsx.md")                                          | FSx for OpenZFS file systems                                                                        |
| [AWS Storage Gateway (Volume Gateway)](../../../storagegateway/latest/vgw/WhatIsStorageGateway.md "../../../storagegateway/latest/vgw/WhatIsStorageGateway.md")      | AWS Storage Gateway volumes                                                                         |
| [Amazon DocumentDB](../../../documentdb/latest/developerguide.md "../../../documentdb/latest/developerguide.md")                                                     | Amazon DocumentDB instance-based clusters                                                           |
| [Amazon Neptune](../../../neptune/latest/userguide.md "../../../neptune/latest/userguide.md")                                                                        | Amazon Neptune clusters                                                                             |
| [Amazon Redshift](../../../redshift/latest/dg/welcome.md "../../../redshift/latest/dg/welcome.md")                                                                   | Amazon Redshift clusters                                                                            |
| [Amazon Timestream](../../../timestream/latest/developerguide/what-is-timestream.md "../../../timestream/latest/developerguide/what-is-timestream.md")               | Amazon Timestream tables                                                                            |
| [VMware Cloud™ on AWS](https://aws.amazon.com/vmware/ "https://aws.amazon.com/vmware/")                                                                             | VMware Cloud™ virtual machines on AWS                                                              |
| [VMware Cloud™ on AWS Outposts](https://aws.amazon.com/vmware/aws-services/ "https://aws.amazon.com/vmware/aws-services/")                                          | VMware Cloud™ virtual machines on AWS Outposts                                                     |
| [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/stacks.md "../../../AWSCloudFormation/latest/UserGuide/stacks.md")                                  | AWS CloudFormation stacks                                                                           |
| [SAP HANA databases](backup-saphana.md "backup-saphana.md")                                                                                                          | SAP HANA databases on Amazon EC2 instances                                                          |

## Pricing

With AWS Backup, you pay for backup storage, data restored, restore testing, cross-Region data transfer, and
AWS Backup Audit Manager. For more information, see [AWS Backup Pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/").
