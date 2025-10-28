# Amazon Relational Database Service backups

## Amazon RDS and AWS Backup

When you consider the options to back up your Amazon RDS instances and clusters, it's
important to clarify which kind of backup you want to create and use. Several AWS
resources, including Amazon RDS, offer their own native backup solutions.

Amazon RDS gives the option of making [automated
backups](../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md "../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md") and [manual backups](../../../AmazonRDS/latest/UserGuide/USER_ManagingManualBackups.md "../../../AmazonRDS/latest/UserGuide/USER_ManagingManualBackups.md").
In Amazon RDS terminology, all recovery points created by AWS Backup, including those in a backup
plan, are considered manual backups.

When you use AWS Backup to [create a backup](creating-a-backup-plan.md#create-backup-plan-console "creating-a-backup-plan.md#create-backup-plan-console") (recovery point) of an Amazon RDS instance, AWS Backup
checks if you have previously used Amazon RDS to create an automated backup. If an automated
backup exists, AWS Backup creates a incremental snapshot copy (`copy-db-snapshot`
operation). If no backup exists, AWS Backup creates a snapshot of the instance you
indicate, instead of a copy (`create-db-snapshot` operation).

The first snapshot made by AWS Backup, created by either operation, will result in 1 full
snapshot. All subsequent _copies_ of this will be incremental backups,
as long as the full backup exists.

###### Important

When a AWS Backup backup plan is scheduled to create multiple daily snapshots of an Amazon RDS
instance, and when one of those scheduled [AWS Backup Start Backup window](creating-a-backup-plan.md#plan-options-and-configuration "creating-a-backup-plan.md#plan-options-and-configuration") coincides with the [Amazon RDS Backup window](../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupWindow "../../../AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupWindow"), the data lineage of the backups can branch off into
non-identical backups, creating unplanned and conflicting backups. To prevent this, ensure
your AWS Backup backup plan or Amazon RDS window do not coincide in their times.

### Considerations

RDS Custom for SQL Server and RDS Custom for Oracle are not currently supported by AWS Backup.

AWS Backup does not support backup and restore of RDS on Outposts.

## Amazon RDS continuous backups and point in time

restore

Continuous backups involve using AWS Backup to create a full backup of your Amazon RDS resource,
then capturing all changes through a transaction log. You can achieve a greater
granularity by rewinding to the point in time you desire to restore to instead of choosing
a previous snapshot taken at fixed time intervals.

See [continuous backups and PITR supported services](point-in-time-recovery.md#point-in-time-recovery-supported-services "point-in-time-recovery.md#point-in-time-recovery-supported-services") and [managing continuous backup settings](point-in-time-recovery.md#point-in-time-recovery-managing "point-in-time-recovery.md#point-in-time-recovery-managing") for more information.

## Amazon RDS Multi-Availability Zone backups

AWS Backup backs up and supports Amazon RDS for MySQL and for PostgreSQL Multi-AZ
(Availability Zone) deployment options with one primary and two readable standby
database instances.

Multi-Availability Zone backups are available in the following regions:
Asia Pacific (Sydney) Region, Asia Pacific (Tokyo) Region, Europe (Ireland) Region, US East (Ohio) Region,
US West (Oregon) Region, Europe (Stockholm) Region, Asia Pacific (Singapore) Region, US East (N. Virginia) Region,
and Europe (Frankfurt) Region.

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
[Multi-AZ DB cluster deployments](../../../AmazonRDS/latest/UserGuide/Concepts.md "../../../AmazonRDS/latest/UserGuide/Concepts.md") in the _Amazon RDS User Guide_.

For more information on
[Creating a Multi-AZ DB cluster snapshot](../../../AmazonRDS/latest/UserGuide/USER_CreateMultiAZDBClusterSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CreateMultiAZDBClusterSnapshot.md"), see the Amazon RDS User Guide.
