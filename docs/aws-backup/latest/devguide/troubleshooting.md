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

## Troubleshoot creating resources

The following information can help you troubleshoot problems with creating
backups.

- In general, **AWS database** services cannot start backups 1 hour before or during their maintenance window
  or automatic backup window. **Amazon FSx** cannot start backups 4 hours
  before or during the maintenance window or automatic backup window
  (Amazon Aurora is exempt from this maintenance window restriction).
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

## Troubleshooting deleting resources

Recovery points that are created by AWS Backup cannot be deleted in the console window of
the protected resource. You can delete them on the AWS Backup console by selecting them in
the vault where they are stored and then choosing **Delete**.

To delete a recovery point or a backup vault, you need the appropriate permissions.
For more information about access control using IAM with AWS Backup, see [Access control](access-control.md "access-control.md").

## Troubleshooting restoring resources

**Restoring using API**

To restore a backup programmatically, use the [StartRestoreJob](API_StartRestoreJob.md "API_StartRestoreJob.md") API operation.

To get the configuration metadata
that your backup was created with, you can call [GetRecoveryPointRestoreMetadata](API_GetRecoveryPointRestoreMetadata.md "API_GetRecoveryPointRestoreMetadata.md").

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
