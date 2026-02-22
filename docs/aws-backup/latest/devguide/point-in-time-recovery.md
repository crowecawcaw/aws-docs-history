# Continuous backups and point-in-time recovery

(PITR)

For some resources, AWS Backup supports continuous backups and point-in-time recovery (PITR) in
addition to snapshot backups.

With **continuous backups**, you can restore your AWS Backup-supported
resource by rewinding it back to a specific time that you choose, within 1 second of precision
(going back a maximum of 35 days). Continuous backup works by first creating a full backup of
your resource, and then constantly backing up your resource’s transaction logs. PITR works by
accessing your full backup and replaying the transaction log to the time that you tell AWS Backup
to recover.

Alternatively, **snapshot backups** can be taken as frequently as every
hour. Snapshot backups can be stored for up to a maximum of 100 years. Snapshots can be copied
for full or incremental backups.

Because continuous and snapshot backups offer different advantages, we recommend that you
protect your resources with both continuous and snapshot backup rules.

An on-demand backup begins to back up your resource immediately. You can choose an
on-demand backup if you wish to create a backup at a time other than the scheduled time
defined in a backup plan. An on-demand backup can be used, for example, to test backup and
functionality at any time.

You can't use [on-demand
backups](recov-point-create-on-demand-backup.md "recov-point-create-on-demand-backup.md") with PITR, because an on-demand backup preserves resources in the state they
are in when the backup is taken, while PITR uses continuous backups, which record changes over
a period of time.

You can opt in to continuous backups for supported resources when you create a backup plan
in AWS Backup using the AWS Backup console or the API. The continuous backup plan creates one continuous
recovery point and updates that recovery point whenever the job runs.

###### Contents

- [Point-in-time recovery
  considerations](#point-in-time-recovery-considerations "#point-in-time-recovery-considerations")
- [Supported services for
  continuous backup and PITR](#point-in-time-recovery-supported-services "#point-in-time-recovery-supported-services")
- [Finding a continuous backup](point-in-time-recovery-finding.md "point-in-time-recovery-finding.md")
- [Restoring a continuous backup](point-in-time-recovery-restoring.md "point-in-time-recovery-restoring.md")
- [Stopping or deleting continuous
  backups](point-in-time-recovery-stopping.md "point-in-time-recovery-stopping.md")
- [Copying continuous backups](point-in-time-recovery-copying.md "point-in-time-recovery-copying.md")
- [Changing your retention
  period](point-in-time-recovery-retention-period.md "point-in-time-recovery-retention-period.md")
- [Removing the only continuous backup
  rule from a backup plan](point-in-time-recovery-removing_rule.md "point-in-time-recovery-removing_rule.md")

## Point-in-time recovery

considerations

Be aware of the following considerations for point-in-time recovery:

- **Automatic fallback to snapshots** — If AWS Backup
  is unable to perform a continuous backup, it tries to perform a _snapshot_ backup instead.
- **No support for on-demand continuous backups** — AWS Backup doesn't support on-demand continuous backup because on-demand
  backup records a point in time, whereas continuous backup records changes over a period
  of time.
- **No support for transition to cold storage** —
  Continuous backups don't support transition to cold storage because transition to cold
  requires a minimum transition period of 90 days, whereas continuous backups have a
  maximum retention period of 35 days.
- **Restoring recent activity** — Amazon RDS activity
  allows restores up until the most recent 5 minutes of activity; Amazon S3 allows restores up
  until the most recent 15 minutes of activity.

###### Important

A single resource can only have one continuous backup. Expand below for additional
details and best practices.

Each resource (such as an Amazon S3 bucket or an Amazon RDS database) can only have one
continuous backup (recovery point); additional continuous backups are redundant. When
multiple backup policies, plans, or rules instruct AWS Backup to create multiple continuous
backups for the same resource, the following process applies:

- If multiple rules specify that more than one continuous backup should be in a
  single vault, AWS Backup follows the rule with the longest retention period (lifecycle)
  and ignores additional rules.
- If multiple rules specify that more than one continuous backup should be in more
  than one vault, AWS Backup creates one continuous backup according to the first rule
  processed. Each subsequent rule specifying a continuous backup for a resource that
  already has a continuous backup will result in a snapshot (periodic) backup
  instead.
  When duplicate continuous backup plans occur, the snapshot backups created after the
  continuous recovery point can show a status of `Completed with issues`. The
  detailed information of this recovery point will show an error similar to
  `“Enabling continuous backup failed, because of the following error: PITR already
 configured in backup plan: [ARN]”`. This error indicates that there is already
  at least one continuous backup configured (for a different recovery point than the one
  containing the error). That first continuous backup (recovery point) is able to be used
  for point in time restore (PITR) as long as it is has a status of
  `COMPLETED`.

To prevent the creation of unintended snapshots with issues (and error message),
review your organization backup strategy. If necessary, adjust backup plans and policies
that create multiple continuous backups of the same resource.

After you have made adjustments that result in only one continuous backup for a
resource, the snapshot backups will be retained according to the specified lifecycle of
the plan that created them, then they will transition to `EXPIRED` and be
deleted. The continuous backup and its point-in-time recovery ability will be maintained
according to the rule that created it.

## Supported services for

continuous backup and PITR

AWS Backup supports continuous backups and point-in-time recovery for the following services
and applications:

### Amazon S3

To turn on PITR for S3 backups, continuous backups need to part of the backup
plan.

While this original backup of the source bucket can have PITR active, cross-Region or
cross-account destination copies will not have PITR, and restoring from these copies will
restore to the time they were created (the copies will be snapshot copies) instead of
restoring to a specified point in time.

AWS Backup for S3 relies on receiving S3 events through Amazon EventBridge. If this setting is
disabled in S3 bucket notification settings, continuous backups will stop for those
buckets with the setting turned off. For more information, see [Using EventBridge](../../../AmazonS3/latest/userguide/EventBridge.md "../../../AmazonS3/latest/userguide/EventBridge.md").

### RDS

**Backup schedules:** When an AWS Backup plan creates both Amazon RDS snapshots
and continuous backups, AWS Backup will intelligently schedule your backup windows to
coordinate with the Amazon RDS maintenance window to prevent conflicts. To further prevent
conflicts, manual configuration of the Amazon RDS automated backup window is unavailable. RDS
takes snapshots once per day, even if a backup plan has a frequency for snapshot
backups other than once per day.

**Settings:** After you apply an AWS Backup continuous backup rule to an
Amazon RDS instance, you can't create or modify continuous backup settings in Amazon RDS. You must
make modifications through the AWS Backup console or the AWS Backup CLI. When you turn on automated
backups for the first time, an outage occurs if you change the backup retention period of
the DB instance from 0 to a nonzero value. Plan this change during a maintenance window to
minimize impact. For more information about enabling automated backups, see [Enabling automated backups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md") in the _Amazon RDS User
Guide_.

**Transition control of continuous backup for an Amazon RDS instance back to
Amazon RDS:**

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup plans**.
3. Delete all the Amazon RDS backup plans with continuous backup protecting that
   resource.
4. Choose **Backup vaults**. Delete the continuous backup
   recovery point from your backup vault. Or, wait for their retention period to
   elapse, causing AWS Backup to automatically delete the recovery point.

After you complete these steps, AWS Backup will transition continuous backup control
of your resource back to Amazon RDS.

AWS CLI
Call the `DisassociateRecoveryPoint` API operation.

To learn more, see [DisassociateRecoveryPoint](API_DisassociateRecoveryPoint.md "API_DisassociateRecoveryPoint.md").

###### IAM permissions required for Amazon RDS continuous backups

- To use AWS Backup to configure continuous backups for your Amazon RDS database, verify that
  the API permission `rds:ModifyDBInstance` exists in the IAM role defined by
  your backup plan configuration. To restore Amazon RDS continuous backups, you must add the
  permission `rds:RestoreDBInstanceToPointInTime` to the IAM role that you
  submitted for the restore job. You can use the `AWS Backup default service role`
  to perform backups and restores.
- To describe the range of times available for point-in-time recovery, AWS Backup calls
  `rds:DescribeDBInstanceAutomatedBackups`. In the AWS Backup console, you must
  have the `rds:DescribeDBInstanceAutomatedBackups` API permission in your
  AWS Identity and Access Management (IAM) managed policy. You can use the `AWSBackupFullAccess` or
  `AWSBackupOperatorAccess` managed policies. Both policies have all
  required permissions. For more information, see [Managed
  Policies](access-control.md#managed-policies "access-control.md#managed-policies").

**Retention periods:** When you change your PITR retention period,
AWS Backup calls [`ModifyDBInstance`](../../../AmazonRDS/latest/APIReference/API_ModifyDBInstance.md "../../../AmazonRDS/latest/APIReference/API_ModifyDBInstance.md") and [applies that change](point-in-time-recovery-retention-period.md "point-in-time-recovery-retention-period.md"), starting
with the next backup that occurs as defined by the frequency rule set in the backup
plan.

**Copies of Amazon RDS continuous backups:**

- **Creating copies of Amazon RDS continuous backups**
  — You can't create copies of Amazon RDS continuous backups because AWS Backup for Amazon RDS
  does not allow copying transaction logs. Instead, AWS Backup creates a snapshot and copies
  it with the frequency specified in the backup plan.

**Restores:** You can perform a point-in-time restore using either
AWS Backup or Amazon RDS. For AWS Backup console instructions, see [Restoring an Amazon RDS Database](restoring-rds.md "restoring-rds.md").
For Amazon RDS instructions, see [Restoring a DB Instance to a specified
time](../../../AmazonRDS/latest/UserGuide/USER_PIT.md "../../../AmazonRDS/latest/UserGuide/USER_PIT.md") in the _Amazon RDS User Guide_.

###### Tip

A multi AZ (availability zone) database instance set to `Always On`
should not have a backup retention set to zero. If errors occur, use AWS CLI command
`disassociate-recovery-point` instead of
`delete-recovery-point`, then change the retention setting to 1 in your Amazon RDS
settings.

For general information about working with Amazon RDS, see the [Amazon RDS User Guide](../../../AmazonRDS/latest/UserGuide/Welcome.md "../../../AmazonRDS/latest/UserGuide/Welcome.md").

#### CLI examples for RDS and Aurora PITR restore

The following examples demonstrate how to restore RDS and Aurora databases to a point in time using the AWS Backup CLI with metadata parameters.

###### Example: Restore RDS database to a point in time with metadata

```
aws backup start-restore-job \
    --recovery-point-arn arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45 \
    --metadata '{"DBInstanceIdentifier":"restored-db-instance","Engine":"mysql","UseLatestRestorableTime":"false","RestoreTime":"2024-01-15T10:30:00Z"}' \
    --iam-role-arn arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole \
    --resource-type RDS \
    --copy-source-tags-to-restored-resource
```

###### Example: Restore Aurora cluster to a point in time

```
aws backup start-restore-job \
    --recovery-point-arn arn:aws:backup:us-east-1:123456789012:recovery-point:2FC4C6F8-0FC1-546B-B91C-209C599C1D56 \
    --metadata '{"DBClusterIdentifier":"restored-aurora-cluster","Engine":"aurora-mysql","UseLatestRestorableTime":"true"}' \
    --iam-role-arn arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole \
    --resource-type Aurora \
    --copy-source-tags-to-restored-resource
```

###### Metadata parameters for RDS PITR restore

The following metadata parameters are supported for RDS and Aurora PITR restores:

- **DBInstanceIdentifier** (RDS) or **DBClusterIdentifier** (Aurora) - Required. The name for the restored database.
- **Engine** - Required. The database engine (e.g., mysql, postgres, aurora-mysql, aurora-postgresql).
- **UseLatestRestorableTime** - Optional. Set to "true" to restore to the latest restorable time, or "false" to specify a RestoreTime.
- **RestoreTime** - Optional. The date and time to restore to (ISO 8601 format). Required if UseLatestRestorableTime is "false".

###### Copy tags to restored resource

Use the `--copy-source-tags-to-restored-resource` flag to copy tags from the source database to the restored database. This ensures tag-based access controls and cost allocation tags are preserved.

For complete details on RDS PITR restore parameters, see:

- [RestoreDBInstanceToPointInTime](../../../AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.md "../../../AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.md") in the Amazon RDS API Reference
- [RestoreDBClusterToPointInTime](../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.md "../../../AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.md") in the Amazon RDS API Reference

### Aurora

To enable continuous backup of your Aurora resources, see the steps in the first
section of this page.

The procedure to restore an Aurora cluster to a point in time is a [variation of
the steps to restore a snapshot of an aurora cluster](restoring-aur.md "restoring-aur.md").

When you conduct a point in time restore, the console displays a **restore
time** section. See _Restoring a continuous backup_ further
down on this page in [Working with Continuous backups](point-in-time-recovery.md#point-in-time-recovery-working-with "point-in-time-recovery.md#point-in-time-recovery-working-with").

### SAP HANA on Amazon EC2 instances

You can make [continuous backups](point-in-time-recovery.md "point-in-time-recovery.md")
, which can be used with point-in-time restore (PITR) (note that on-demand backups
preserve resources in the state in which they are taken; whereas PITR uses continuous
backups which record changes over a period of time).

With continuous backups, you can restore your SAP HANA database on an EC2 instance by
rewinding it back to a specific time that you choose, within 1 second of precision (going
back a maximum of 35 days). Continuous backup works by first creating a full backup of
your resource, and then constantly backing up your resource’s transaction logs. PITR
restore works by accessing your full backup and replaying the transaction log to the time
that you tell AWS Backup to recover.

You can opt in to continuous backups when you create a backup plan in AWS Backup using the
AWS Backup console or the API.

###### To enable continuous backups using the console

1. Sign in to the AWS Management Console, and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Backup plans**, and then choose
   **Create Backup plan**.
3. Under **Backup rules**, choose **Add Backup
   rule**.
4. In the **Backup rule configuration** section, select
   **Enable continuous backups for supported resources**.

After you disable [PITR (point-in-time
restore)](point-in-time-recovery.md "point-in-time-recovery.md") for SAP HANA database backups, logs will continue to be sent to AWS Backup
until the recovery point expires (status equals `EXPIRED)`. You can change to
an alternative log backup location in SAP HANA to stop the transmission of logs to
AWS Backup.

A continuous recovery point with a status of `STOPPED` indicates that a
continuous recovery point has been interrupted; that is, the logs transmitted from SAP
HANA to AWS Backup that show the incremental changes to a database have a gap. The recovery
points that occur within this timeframe gap have a status of `STOPPED.`.

For issues you may encounter during restore jobs of continuous backups (recovery
points), see the [SAP
HANA Restore troubleshooting](saphana-restore.md#saphanarestoretroubleshooting "saphana-restore.md#saphanarestoretroubleshooting") section of this guide.
