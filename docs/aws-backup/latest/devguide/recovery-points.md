# Backup creation, maintenance, and restore

A backup, or _recovery point_, represents the content of a resource, such
as an Amazon Elastic Block Store (Amazon EBS) volume or Amazon DynamoDB table, at a specified time. Recovery point is a term
that refers generally to the different backups in AWS services, such as Amazon EBS snapshots and
DynamoDB backups. The terms _recovery point_ and _backup_ are
used interchangeably.

AWS Backup saves recovery points in backup vaults, which you can organize according to your
business needs. For example, you can save a set of resources that contain financial information
for fiscal year 2020. When you need to recover a resource, you can use either the AWS Backup console
or the AWS Command Line Interface (AWS CLI) to find and recover the resource you need.

Each recovery point has a unique ID. The unique ID is at the end of the recovery point's
Amazon Resource Name (ARN). For examples of recovery point ARNs and unique IDs, see the table in
[Resources and operations](access-control.md#access-control-resources "access-control.md#access-control-resources").

###### Important

To avoid additional charges, configure your retention policy with a warm storage duration
of **at least one week**. For more information, see [Metering, costs, and billing for AWS Backup](metering-and-billing.md "metering-and-billing.md").

The following sections provide an overview of the basic backup management tasks in
AWS Backup.

###### Topics

- [Creating an on-demand backup using AWS Backup](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md")
- [Continuous backups and point-in-time recovery (PITR)](point-in-time-recovery.md "point-in-time-recovery.md")
- [Backup creation by resource type](creating-a-backup.md "creating-a-backup.md")
- [Backup and tag copy](recov-point-create-a-copy.md "recov-point-create-a-copy.md")
- [Backup deletion](deleting-backups.md "deleting-backups.md")
- [Backup and tag edits](editing-a-backup.md "editing-a-backup.md")
- [Backup search](backup-search.md "backup-search.md")
- [Backup tiering](backup-tiering.md "backup-tiering.md")
- [Restore a backup by resource type](restoring-a-backup.md "restoring-a-backup.md")
- [Restore testing](restore-testing.md "restore-testing.md")
- [Stop a backup job](stopping-a-backup-job.md "stopping-a-backup-job.md")
- [View existing backups](listing-backups.md "listing-backups.md")
