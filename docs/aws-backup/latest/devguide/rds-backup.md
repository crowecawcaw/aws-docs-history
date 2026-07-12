# Amazon Relational Database Service backups

## Amazon RDS and AWS Backup

When you consider the options to back up your Amazon RDS instances and clusters, it's
important to clarify which kind of backup you want to create and use. Several AWS
resources, including Amazon RDS, offer their own native backup solutions.

Amazon RDS gives the option of making [automated
backups](../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md") and [manual backups](../../../AmazonRDS/latest/UserGuide/USER_ManagingManualBackups.md "../../../AmazonRDS/latest/UserGuide/USER_ManagingManualBackups.md").
Recovery points created by AWS Backup are classified differently depending on the backup type:

- **Periodic snapshots** created by AWS Backup are considered manual backups in Amazon RDS. These are snapshot-based backups taken according to your backup plan schedule.
- **Continuous backups** created by AWS Backup are considered automated backups in Amazon RDS. These enable point-in-time restore (PITR) by maintaining transaction logs alongside automated snapshots.

This distinction is important because manual and automated backups have different retention behaviors and lifecycle management in Amazon RDS.

When you use AWS Backup to [create a backup](creating-a-backup-plan.md#create-backup-plan-console "creating-a-backup-plan.md#create-backup-plan-console") (recovery point) of an Amazon RDS instance, AWS Backup
checks if you have previously used Amazon RDS to create an automated backup. If an automated
backup exists, AWS Backup creates a incremental snapshot copy (`copy-db-snapshot`
operation). If no backup exists, AWS Backup creates a snapshot of the instance you
indicate, instead of a copy (`create-db-snapshot` operation).

The first snapshot made by AWS Backup, created by either operation, will result in 1 full
snapshot. All subsequent _copies_ of this will be incremental backups,
as long as the full backup exists.

When using cross account or cross Region copies, incremental snapshot copy jobs process faster than full snapshot copy jobs. Keeping a previous snapshot copy until the new copy job is complete may reduce the copy job duration. If you choose to copy snapshots from RDS database instances, it is important to note that deleting previous copies first will cause full snapshot copies to be made (instead of incremental). For more information on optimizing copying, see [Incremental snapshot copying](../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md#USER_CopySnapshot.Incremental "../../../AmazonRDS/latest/UserGuide/USER_CopySnapshot.md#USER_CopySnapshot.Incremental") in the _Amazon RDS User Guide_.

###### Important

When a AWS Backup backup plan is scheduled to create multiple daily snapshots of an Amazon RDS
instance, and when one of those scheduled [AWS Backup Start Backup window](creating-a-backup-plan.md#plan-options-and-configuration "creating-a-backup-plan.md#plan-options-and-configuration") coincides with the [Amazon RDS Backup window](../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupWindow "../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupWindow"), the data lineage of the backups can branch off into
non-identical backups, creating unplanned and conflicting backups. To prevent this, ensure
your AWS Backup backup plan or Amazon RDS window do not coincide in their times.

### Considerations

AWS Backup supports creating on-demand backups of RDS Custom for SQL Server instances.
However, restoring RDS Custom for SQL Server through AWS Backup is not natively supported.
To restore, use the `restore-db-instance-from-db-snapshot` operation in Amazon RDS
with the AWS Backup-created snapshot. For more information, see [Restore an Amazon RDS Custom for SQL Server instance using a backup from
AWS Backup](https://aws.amazon.com/blogs/database/restore-an-amazon-rds-custom-for-sql-server-instance-using-a-backup-from-aws-backup/ "https://aws.amazon.com/blogs/database/restore-an-amazon-rds-custom-for-sql-server-instance-using-a-backup-from-aws-backup/").

RDS Custom for Oracle is not currently supported by AWS Backup.

AWS Backup does not support backup and restore of RDS on Outposts or in Local Zones,
including Dedicated Local Zones. AWS Backup requires RDS instances to have
`BackupTarget` set to `region` (the default).

## Understanding backup overlap and costs

AWS Backup periodic snapshots are classified as manual backups in Amazon RDS. While they
share the same incremental snapshot chain as automated backups, they count toward your
total backup storage alongside automated backups. Amazon RDS provides a free backup storage
allocation equal to your provisioned DB instance storage — this covers both automated
backups and manual snapshots combined. Storage beyond that allocation is billed. If you
run both scheduled AWS Backup snapshots and Amazon RDS automated backups, both contribute to this
total, and you should factor this into your cost planning.

When you use AWS Backup to back up an Amazon RDS DB instance, an automated snapshot might
appear with an unexpected timestamp; it matches the AWS Backup snapshot creation time rather
than the Amazon RDS automated backup window. If Amazon RDS does not find a recent automated backup
within the past day, it consolidates the backup. Amazon RDS attaches automated backup metadata
to the manual snapshot that AWS Backup created. This ensures the DB instance maintains a
regular automated backup. This most commonly occurs when an AWS Backup operation runs long
enough to overlap with the Amazon RDS automated backup window.

When a backup is consolidated, both the manual and automated snapshot entries
reference the same underlying snapshot data. You are charged only once for that single
underlying snapshot and your data remains fully protected. Also, backup retention and
point-in-time restore functionality are unaffected regardless of whether entries are
consolidated.

## Amazon RDS continuous backups and point in time restore

Continuous backups involve using AWS Backup to create a full backup of your Amazon RDS resource,
then capturing all changes through a transaction log. You can achieve a greater
granularity by rewinding to the point in time you desire to restore to instead of choosing
a previous snapshot taken at fixed time intervals.

See [continuous backups and PITR supported services](point-in-time-recovery.md#point-in-time-recovery-supported-services "point-in-time-recovery.md#point-in-time-recovery-supported-services") and [managing continuous backup settings](point-in-time-recovery.md#point-in-time-recovery-managing "point-in-time-recovery.md#point-in-time-recovery-managing") for more information.

###### Important

Enabling continuous backups for Amazon RDS using AWS Backup when they were previously
disabled (or disabling continuous backups when they were previously enabled) takes the
Amazon RDS instance offline to make the changes. Plan this change during a maintenance window
to minimize impact. If automated backups were enabled from Amazon RDS and that backup was
simply moved to AWS Backup, then no downtime is required.

## Amazon RDS Multi-Availability Zone backups

AWS Backup backs up and supports Amazon RDS for MySQL and for PostgreSQL Multi-AZ
(Availability Zone) deployment options with one primary and two readable standby
database instances.

For a list of Regions where Multi-Availability Zone backups are available, see the
Amazon RDS Multi-AZ column in [Supported services by AWS Region](backup-feature-availability.md#supported-services-by-region "backup-feature-availability.md#supported-services-by-region").

The Multi-AZ deployment option optimizes write transactions and is ideal when your
workloads require additional read capacity, lower write transaction latency,
more resilience from network jitter (which impacts the consistency of write
transaction latency), and high availability and durability.

To create a Multi-AZ cluster, you can choose either MySQL or PostgreSQL as
the engine type.

In the AWS Backup console, there are three deployment options:

- **Multi-AZ DB cluster:** Creates a DB cluster
  with a primary DB instances and two readable standby DB instances, which
  each DB instance in a different Availability Zone. Provides high availability,
  data redundancy, and increases capacity to server-ready workloads.
- **Multi-AZ DB instance:** Creates a primary
  DB instance and a standby DB instance in a different Availability Zone.
  This provides high availability and data redundancy, but the standby DB
  instance doesn’t support connections for read workloads.
- **Single DB instance:** Creates a single DB
  instance with no standby DB instances.

**Backup behavior with instances and clusters**

- [Point-in-Time Recovery](point-in-time-recovery.md "point-in-time-recovery.md") (PITR) can support instances,
  but not clusters.
- Copying a Multi-AZ DB cluster snapshot is not supported.
- The Amazon Resource Name (ARN) for an RDS recovery point depends on whether
  an instance or cluster is used:

An RDS instance ARN: `arn:aws:rds:`region`:
 `account`:db:`name``

An RDS Multi-Availability Cluster:
`arn:aws:rds:`region`:`account`:cluster:`name``

For more information, consult
[Multi-AZ DB cluster deployments](../../../AmazonRDS/latest/UserGuide/Concepts.MultiAZ.md "../../../AmazonRDS/latest/UserGuide/Concepts.MultiAZ.md") in the _Amazon RDS User Guide_.

For more information on
[Creating a Multi-AZ DB cluster snapshot](../../../AmazonRDS/latest/UserGuide/USER_CreateMultiAZDBClusterSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CreateMultiAZDBClusterSnapshot.md"), see the Amazon RDS User Guide.

## Amazon Aurora Global Databases

AWS recommends maintaining backups in every Region where your global database
is deployed.
