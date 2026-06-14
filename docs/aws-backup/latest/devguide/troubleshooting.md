# Troubleshooting AWS Backup

When you use AWS Backup, you might encounter issues. The following sections can help you troubleshoot some
common issues that might occur.

For general questions about AWS Backup, see the [AWS Backup
FAQ](https://aws.amazon.com/backup/faqs/ "https://aws.amazon.com/backup/faqs/"). You can also search for answers and post questions in [AWS re:Post](https://repost.aws/ "https://repost.aws/").

###### Topics

- [Troubleshooting general issues](#troubleshooting-backup-general "#troubleshooting-backup-general")
- [Troubleshoot creating resources](#troubleshooting-create-backup "#troubleshooting-create-backup")
- [Troubleshooting deleting resources](#troubleshooting-delete-backup "#troubleshooting-delete-backup")
- [Troubleshooting restoring resources](#troubleshooting-restore-backup "#troubleshooting-restore-backup")
- [Troubleshooting formatting errors](#troubleshooting-formatting-errors "#troubleshooting-formatting-errors")
- [Common troubleshooting questions](#troubleshooting-common-questions "#troubleshooting-common-questions")
- [Additional important links](#troubleshooting-additional-links "#troubleshooting-additional-links")

## Troubleshooting general issues

When you back up and restore resources, you must have permission to use AWS Backup and
permission to access the resources that you want to protect. The easiest way to have the
proper permissions is to choose the **Default role** when you [assign resources to a backup plan](assigning-resources.md "assigning-resources.md"). For more information about access
control using AWS Identity and Access Management (IAM) with AWS Backup, see [Access control](access-control.md "access-control.md").

If you get an `AccessDenied` error when attempting to access a AWS Backup
resource, such as a backup vault, either the resource does not exist or you do not
have permissions to access the resource.

If you run into issues with backing up and restoring a particular resource type, it
can be helpful to review the backup and restore troubleshooting topic for that resource. For more
information, see the links under [How AWS Backup works with supported AWS services](working-with-supported-services.md "working-with-supported-services.md").

If AWS Backup fails to create or delete a resource, you can learn more about the issue by
using AWS CloudTrail to view error messages or logs. For more information about using CloudTrail
with AWS Backup, see [Logging AWS Backup API calls with CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

If you have a role with `tag:GetResources` permissions, but you also have
a service control policy (SCP) that blocks `tag:GetResources`, then AWS Backup
cannot successfully run a backup plan with tag-based selections. In these situations,
the CloudTrail event `ProcessBackupPlanSelection` shows a
`tag:GetResources` permissions error.

## Troubleshoot creating resources

The following information can help you troubleshoot problems with creating
backups.

- In general, **AWS database** services cannot start backups 1 hour before or during their maintenance window
  or automatic backup window. **Amazon FSx** cannot start backups 3 hours
  before or during the maintenance window or automatic backup window
  (Amazon Aurora is exempt from both the maintenance window restriction and the automatic backup window restriction).
  Snapshot backups scheduled during those times will fail. One exception: when you opt in to using
  AWS Backup for both snapshot and continuous backups for a supported service, you no longer need to
  worry about those windows because AWS Backup will schedule them for you. See [Point-in-Time
  Recovery](point-in-time-recovery.md "point-in-time-recovery.md") for a list of supported services and instructions on how to use AWS Backup to take
  continuous backups.
- Creating backups for **DynamoDB tables** will fail while tables are being created.
  Creating a DynamoDB table typically takes a couple of minutes.
- Backing up **Amazon EFS file systems** can take up to 7 days when the file systems are
  very large. Only one concurrent backup at a time can be queued for an Amazon EFS file
  system. If a subsequent backup is queued while a previous one is still in
  progress, the backup window can expire and no backup is created.
- **Amazon EBS** has a soft quota of 100,000 backups per AWS Region per account, and
  additional backups fail when this quota is reached. If you reach this quota, you
  can delete excess backups or request a quota increase. For more information
  about requesting a quota increase, see [AWS
  Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").
- When creating **Amazon Relational Database Service (RDS) backups**, consider the following:

  - If you do not use AWS Backup to manage both Amazon RDS snapshots and continuous
    backups with point-in-time recovery, your backups will fail if initiated
    if scheduled or made on-demand during the daily, user-configurable
    30-minute backup window. For more information about automated Amazon RDS
    backups, see [Working
    With Backups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md") in the _Amazon RDS User Guide_.
    You can avoid this limitation by using AWS Backup to manage both Amazon RDS
    snapshots and continuous backups with point-in-time recovery.
  - If you initiate a backup job from the Amazon RDS console, this can conflict
    with an Aurora clusters backup job, causing the error `Backup job
expired before completion.` If this occurs, configure a longer
    backup window in AWS Backup.
  - AWS Backup does not currently pass on the TDE option group when a copy job
    is created. If you intend to use this option group for copy job
    creation, you must use the Amazon RDS console or Amazon RDS API instead of AWS Backup
    tools. See [Copying an option group](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy") in the
    _Amazon Relational Database Service User Guide_ for more information.
  - **ERROR:** On-demand backups complete but scheduled
    backups fail with error "The source snapshot KMS key does not exist, is
    not enabled or you do not have permissions to access it."
    The on-demand job is completed because it uses the API call
    `CopyDBSnapshot`, which doesn't require KMS access.

  **REMEDY:** Add your IAM role to your KMS key.

- For resources that support [full
  AWS Backup management](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") with recovery points in the format
  `arn:aws:backup:`region`:`account-id`:recovery-point:*`
  and all continuous backups, ensure your IAM role has permission to perform
  `backup:TagResource` if your source resources contain tags or you
  want to add additional tags to your recovery points. Apply the
  `backup:TagResource` permission to `"Resource":
"arn:aws:backup:*:*:recovery-point:*"`.

## Troubleshooting deleting resources

Recovery points that are created by AWS Backup cannot be deleted in the console window of
the protected resource. You can delete them on the AWS Backup console by selecting them in
the vault where they are stored and then choosing **Delete**.

To delete a recovery point or a backup vault, you need the appropriate permissions.
For more information about access control using IAM with AWS Backup, see [Access control](access-control.md "access-control.md").

## Troubleshooting restoring resources

**Restoring using API**

To restore a backup programmatically, use the [StartRestoreJob](../APIReference/API_StartRestoreJob.md "../APIReference/API_StartRestoreJob.md") API operation.

To get the configuration metadata
that your backup was created with, you can call [GetRecoveryPointRestoreMetadata](../APIReference/API_GetRecoveryPointRestoreMetadata.md "../APIReference/API_GetRecoveryPointRestoreMetadata.md").

See [Restoring a backup](restoring-a-backup.md "restoring-a-backup.md") for more information.

**Restoring using the Console**

- [Restoring Amazon S3 data](restoring-s3.md "restoring-s3.md")
- [Restoring a virtual machine](restoring-vm.md "restoring-vm.md")
- [Restoring an Amazon FSx file system](restoring-fsx.md "restoring-fsx.md")
- [Restoring an Amazon EBS volume](restoring-ebs.md "restoring-ebs.md")
- [Restoring an Amazon EFS file system](restoring-efs.md "restoring-efs.md")
- [Restoring an Amazon DynamoDB table](restoring-dynamodb.md "restoring-dynamodb.md")
- [Restoring an Amazon RDS database](restoring-rds.md "restoring-rds.md")
- [Restoring an Aurora cluster](restoring-aur.md "restoring-aur.md")
- [Restoring an Amazon EC2 instance](restoring-ec2.md "restoring-ec2.md")
- [Restoring a Storage Gateway volume](restoring-storage-gateway.md "restoring-storage-gateway.md")
- [Restoring a Amazon DocumentDB cluster](restoring-docdb.md "restoring-docdb.md")
- [Restoring a Neptune cluster](restoring-nep.md "restoring-nep.md")

## Troubleshooting formatting errors

When a wildcard (\*) is included for the value in a parameter, the wildcard is processed
to include values other than whitespaces. Values in a key-value pair that contain white spaces
will not included as part of the wildcard.

## Common troubleshooting questions

The following resources can help you troubleshoot common issues with
AWS Backup.

- [Why
  does my AWS Backup job fail?](https://repost.aws/knowledge-center/backup-failed-job "https://repost.aws/knowledge-center/backup-failed-job")
- [How
  do I troubleshoot common errors for Amazon S3 backups that are failing in
  AWS Backup?](https://repost.aws/knowledge-center/backup-s3-backups-fail-errors "https://repost.aws/knowledge-center/backup-s3-backups-fail-errors")
- [How
  do I troubleshoot common errors for VMware backups that are failing in
  AWS Backup?](https://repost.aws/knowledge-center/backup-troubleshoot-vmware-backups "https://repost.aws/knowledge-center/backup-troubleshoot-vmware-backups")
- For additional VMware backup troubleshooting, see [Troubleshoot VM issues](vm-troubleshooting.md "vm-troubleshooting.md").
- [How
  do I troubleshoot the "You are not authorized to perform this operation" error when I
  try to restore my Amazon EC2 instance?](https://repost.aws/knowledge-center/aws-backup-encoded-authorization-failure "https://repost.aws/knowledge-center/aws-backup-encoded-authorization-failure")
- [How
  do I troubleshoot a backup policy that doesn't create jobs in my member accounts in
  an organization?](https://repost.aws/knowledge-center/backup-policy-no-jobs-created "https://repost.aws/knowledge-center/backup-policy-no-jobs-created")
- [How
  do I resolve the error "This image is managed by AWS Backup and cannot be deleted via
  Amazon EC2 APIs" when I try to delete an Amazon EC2 backup?](https://repost.aws/knowledge-center/backup-delete-ami-error "https://repost.aws/knowledge-center/backup-delete-ami-error")
- [How
  do I troubleshoot Amazon EC2 VSS failures in AWS Backup?](https://repost.aws/knowledge-center/backup-troubleshoot-vss-failures "https://repost.aws/knowledge-center/backup-troubleshoot-vss-failures")
- [How
  can I troubleshoot not receiving notifications from Amazon EventBridge for
  AWS Backup?](https://repost.aws/knowledge-center/backup-sns-notifications-not-received "https://repost.aws/knowledge-center/backup-sns-notifications-not-received")
- [How
  do I resolve "Insufficient privileges to perform this action" errors when performing
  an Amazon EFS restore using AWS Backup?](https://repost.aws/knowledge-center/backup-insufficient-privileges-efs "https://repost.aws/knowledge-center/backup-insufficient-privileges-efs")
- [How
  can I turn off automatic backups in Amazon EFS and remove the stored backup
  data?](https://repost.aws/knowledge-center/efs-disable-automatic-backups "https://repost.aws/knowledge-center/efs-disable-automatic-backups")
- [Why
  is my recovery point in the expired status in AWS Backup?](https://repost.aws/knowledge-center/backup-recovery-point-expired "https://repost.aws/knowledge-center/backup-recovery-point-expired")
- [How
  can I stop an Amazon RDS continuous backup in AWS Backup?](https://repost.aws/knowledge-center/backup-stop-rds-continuous-backup "https://repost.aws/knowledge-center/backup-stop-rds-continuous-backup")
- [How
  do I remove an AWS Backup Vault Lock?](https://repost.aws/knowledge-center/backup-delete-vault-lock "https://repost.aws/knowledge-center/backup-delete-vault-lock")
- [Why
  is my cross-account copy failing in AWS Backup?](https://repost.aws/knowledge-center/backup-troubleshoot-cross-account-copy "https://repost.aws/knowledge-center/backup-troubleshoot-cross-account-copy")
- [How
  can I resolve the "Given key ID not accessible" error when performing a cross-account
  copy in AWS Backup?](https://repost.aws/knowledge-center/backup-cross-account-copy-error "https://repost.aws/knowledge-center/backup-cross-account-copy-error")
- [How
  do I resolve the error "Access Denied trying to call AWS Backup service" when I try to
  create a cross-account copy in AWS Backup?](https://repost.aws/knowledge-center/backup-resolve-access-denied-error "https://repost.aws/knowledge-center/backup-resolve-access-denied-error")
- [Why
  do I get an Access Denied error when I try to create an AWS Backup
  vault?](https://repost.aws/knowledge-center/backup-vault-access-denied "https://repost.aws/knowledge-center/backup-vault-access-denied")
- [Why
  is my Aurora cluster endpoint stuck in the Creating status after the AWS Backup restore
  job completes?](https://repost.aws/knowledge-center/backup-aurora-cluster-endpoints-stuck "https://repost.aws/knowledge-center/backup-aurora-cluster-endpoints-stuck")
- [Why
  are my scheduled backup plans in AWS Backup not running?](https://repost.aws/knowledge-center/aws-backup-troubleshoot-scheduled-backup-plans "https://repost.aws/knowledge-center/aws-backup-troubleshoot-scheduled-backup-plans")

## Additional important links

The following resources provide additional guidance for working with
AWS Backup.

- [Troubleshoot
  a logically air-gapped vault issue](logicallyairgappedvault.md#lag-troubleshoot "logicallyairgappedvault.md#lag-troubleshoot")
- [Delegated
  administrator accounts](manage-cross-account.md#backup-delegatedadmin "manage-cross-account.md#backup-delegatedadmin") — Delegated administrator accounts are member
  accounts with enhanced features but cannot override service opt-in settings of other
  member accounts like a management account can.
- [Managing multiple
  accounts](manage-cross-account.md "manage-cross-account.md") — For backup plans that are managed by Organizations, the resource
  opt-in settings in the management account override the settings in a member account,
  even if one or more delegated administrator accounts are configured.
- [Backup plan
  options and configuration](plan-options-and-configuration.md "plan-options-and-configuration.md") — If you have a backup plan with multiple rules
  and the time frames of the two rules overlap, AWS Backup optimizes the backup and takes a
  backup for the rule with the longer retention time.
- [Metering and
  billing](metering-and-billing.md "metering-and-billing.md") — To avoid additional charges, we recommend that you configure your
  backup plan retention policy with a warm storage duration of at least one
  week.
- [AWS Backup pricing](https://aws.amazon.com/backup/pricing/ "https://aws.amazon.com/backup/pricing/")
- [AWS Backup SLA](https://aws.amazon.com/backup/sla/ "https://aws.amazon.com/backup/sla/")
- [AWS Backup
  quotas](aws-backup-limits.md "aws-backup-limits.md")
- [Continuous
  and point-in-time recovery considerations](point-in-time-recovery.md#point-in-time-recovery-supported-services "point-in-time-recovery.md#point-in-time-recovery-supported-services") — A resource can only have one
  continuous backup.
- [Prerequisites
  for Amazon S3 backups and considerations for Amazon S3 backups](s3-backups.md#s3-backup-prerequisites "s3-backups.md#s3-backup-prerequisites")
- [Best
  practices and cost considerations for Amazon S3 backups](s3-backups.md#bestpractices-costoptimization "s3-backups.md#bestpractices-costoptimization")
- [Feature
  availability, supported resources, and AWS Regions](backup-feature-availability.md "backup-feature-availability.md")
