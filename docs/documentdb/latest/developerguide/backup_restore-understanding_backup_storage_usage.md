# Understanding backup storage usage

Amazon DocumentDB backup storage consists of continuous backups within the
backup retention period and manual snapshots outside the retention
period. To control your backup storage usage, you can reduce the backup
retention interval, remove old manual snapshots when they are no longer
needed, or both. For general information about Amazon DocumentDB backups, see [Backing up and restoring in Amazon DocumentDB](backup_restore.md "backup_restore.md").
For pricing information about Amazon DocumentDB backup storage, see [Amazon DocumentDB Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/").

To control your costs, you can monitor the amount of storage
consumed by continuous backups and manual snapshots that persist beyond
the retention period. Then you can reduce the backup retention interval
and remove manual snapshots when they are no longer needed.

You can use the Amazon CloudWatch metrics `TotalBackupStorageBilled`,
`SnapshotStorageUsed`, and
`BackupRetentionPeriodStorageUsed` to review and monitor the
amount of storage used by your Amazon DocumentDB backups, as follows:

- `BackupRetentionPeriodStorageUsed` represents the
  amount of backup storage used for storing continuous backups at
  the current time. This metric value depends on the size of the
  cluster volume and the number of changes you make during the
  retention period. However, for billing purposes the metric does
  not exceed the cumulative cluster volume size during the
  retention period. For example, if your cluster size is 100 GiB
  and your retention period is two days, the maximum value for
  `BackRetentionPeriodStorageUsed` is 200 GiB
  (100 GiB + 100 GiB).
- `SnapshotStorageUsed` represents the amount of
  backup storage used for storing manual snapshots beyond the
  backup retention period. Manual snapshots taken within the
  retention period do not count against your backup storage.
  Similarly, automatic snapshots do not count against your backup
  storage. The size of each snapshot is the size of the cluster
  volume at the time you take the snapshot. The
  `SnapshotStorageUsed` value depends on the number of
  snapshots you keep and the size of each snapshot. For example,
  suppose that you have one snapshot outside the retention period
  and cluster volume size was 100 GiB when that snapshot was taken.
  The amount of `SnapshotStorageUsed` is 100 GiB.
- `TotalBackupStorageBilled` represents the sum of
  `BackupRetentionPeriodStorageUsed` and
  `SnapshotStorageUsed`, minus an amount of free backup
  storage equal to the size of cluster volume for one day. For
  example, if your cluster size is 100 GiB, you have one retention
  day, and you have one snapshot outside the retention period, the
  `TotalBackupStorageBilled` is
  100 GiB (100 GiB + 100 GiB - 100 GiB).
- These metrics are computed independently for each Amazon DocumentDB
  cluster.
  You can monitor your Amazon DocumentDB clusters and build reports using CloudWatch
  metrics through the [CloudWatch console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
  For more information about how to use CloudWatch metrics, see [Monitoring Amazon DocumentDB](monitoring_docdb.md "monitoring_docdb.md").
