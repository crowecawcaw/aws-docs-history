# Backup creation by resource type

With AWS Backup, you can create backups automatically using backup plans or manually by
initiating an on-demand backup.

## Creating automatic backups

When backups are created automatically by backup plans, they are configured with the
lifecycle settings that are defined in the backup plan. They are organized in the backup
vault that is specified in the backup plan. They are also assigned the tags that are listed
in the backup plan. For more information about backup plans, see [Backup plans](about-backup-plans.md "about-backup-plans.md").

## Creating on-demand backups

When you create an on-demand backup, you can configure these settings for the backup
that is being created. When a backup is created either automatically or manually, a backup
_job_ is initiated. For how to create an on-demand backup, see [Creating an on-demand backup using AWS Backup](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md").

Note: An on-demand backup creates a backup job; the backup job will transition
in state of `Running` within an hour (or when specified). You can choose
an on-demand backup if you wish to create a backup at a time other than the scheduled time
defined in a backup plan. An on-demand backup can be used, for example, to test backup and
functionality at any time.

[On-demand backups](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md") cannot be used with
[point-in-time restore (PITR)](point-in-time-recovery.md "point-in-time-recovery.md") since an on-demand backup preserves resources
in the state they are in when the backup is taken, whereas PITR uses
[continuous backups](point-in-time-recovery.md#point-in-time-recovery-working-with "point-in-time-recovery.md#point-in-time-recovery-working-with") which record changes over a period of time.

## Backup job statuses

Each backup job has a unique ID. For example,
`D48D8717-0C9D-72DF-1F56-14E703BF2345`.

You can view the status of a backup job on the **Jobs** page of the
AWS Backup console. Backup job statuses include `CREATED`, `PENDING`,
`RUNNING`, `ABORTING`, `ABORTED`, `COMPLETED`,
`FAILED`, `EXPIRED`, and `PARTIAL`.

## Incremental backups

Many resources support incremental backup with AWS Backup. A full list is available in the
incremental backup section of the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource") table.

Although each backup after the first (full) one is incremental (meaning it only captures
changes from the previous backup), all backups made with AWS Backup retain the necessary
reference data to allow a full restore. This is true even if the original (full) backup has
reached the end of its lifecycle and been deleted.

For example, if your day 1 (full) backup was deleted due to a 3-day lifecycle policy,
you would still be able to perform a full restore with the backups from days 2 and 3. AWS Backup
maintains the necessary reference data from day 1 to do so.

**Incremental backups and Regions**

Backups of resources which are fully managed by AWS Backup can only be incremental
if the vault in which the backup is created also contains an earlier backup (incremental or full); other
resource types (not fully managed by AWS Backup) can have incremental backups
as long as a vault within the same _Region_ has an earlier backup.

## Access to source resources

AWS Backup needs access to your source resources to back them up. For example:

- To back up an Amazon EC2 instance, the instance can be in the `running` or
  `stopped` state, but not the `terminated` state. This is because
  a `running` or `stopped` instance can communicate with AWS Backup, but
  a `terminated` instance cannot.
- To back up a virtual machine, its hypervisor must have the Backup gateway status
  `ONLINE`. For more information, see [Understanding hypervisor status](working-with-hypervisors.md#understand-hypervisor-status "working-with-hypervisors.md#understand-hypervisor-status").
- To back up an Amazon RDS database, Amazon Aurora, or Amazon DocumentDB cluster, those resources must
  have the status `AVAILABLE`.
- To back up an Amazon Elastic File System (Amazon EFS), it must have the status
  `AVAILABLE`.
- To back up an Amazon FSx file system, it must have the status `AVAILABLE`. If
  the status is `UPDATING`, the backup request is queued until the file system
  becomes `AVAILABLE`.

FSx for ONTAP doesn’t support backing up certain volume types, including DP (data-protection)
volumes, LS (load-sharing) volumes, full volumes, or volumes on file
systems that are full. For more information, please see
[FSx for ONTAP
Working with backups](../../../fsx/latest/ONTAPGuide/using-backups.md "../../../fsx/latest/ONTAPGuide/using-backups.md").

AWS Backup retains previously-created backups consistent with your lifecycle policy,
regardless of the health of your source resource.

###### Topics

- [AWS CloudFormation stack backups](applicationstackbackups.md "applicationstackbackups.md")
- [Amazon Aurora DSQL backups](backup-aurora.md "backup-aurora.md")
- [Advanced DynamoDB backup](advanced-ddb-backup.md "advanced-ddb-backup.md")
- [Amazon EBS and AWS Backup](multi-volume-crash-consistent.md "multi-volume-crash-consistent.md")
- [Amazon Relational Database Service backups](rds-backup.md "rds-backup.md")
- [Amazon Redshift backups](redshift-backups.md "redshift-backups.md")
- [Amazon Redshift Serverless backups](redshift-serverless-backups.md "redshift-serverless-backups.md")
- [SAP HANA backup on Amazon EC2](backup-saphana.md "backup-saphana.md")
- [Amazon S3 backups](s3-backups.md "s3-backups.md")
- [Amazon Timestream backups](timestream-backup.md "timestream-backup.md")
- [Virtual machine backups](vm-backups.md "vm-backups.md")
- [Create Windows VSS backups](windows-backups.md "windows-backups.md")
