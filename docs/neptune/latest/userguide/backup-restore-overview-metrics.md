# CloudWatch metrics that are useful for managing Neptune backup storage

You can use the Amazon CloudWatch metrics `TotalBackupStorageBilled`,
`SnapshotStorageUsed`, and `BackupRetentionPeriodStorageUsed` to review and
monitor the amount of storage used by your Neptune backups, as follows:

- `BackupRetentionPeriodStorageUsed` represents the amount of backup storage used,
  in bytes, for storing continuous backups at the current time. This value depends on the size of the
  cluster volume and the amount of changes you make during the retention period. However, for
  billing purposes it doesn't exceed the cumulative cluster volume size during the retention
  period. For example, if your cluster's `VolumeBytesUsed` size is 107,374,182,400 bytes
  (100 GiB), and your retention period is two days, the maximum value for `BackupRetentionPeriodStorageUsed`
  is 214,748,364,800 bytes (100 GiB + 100 GiB).
- `SnapshotStorageUsed` represents the amount of backup storage used, in bytes,
  for storing manual snapshots beyond the backup retention period. Manual snapshots don't count
  against your snapshot backup storage while their creation timestamp is within the retention period.
  All automatic snapshots also don't count against your snapshot backup storage. The size of each
  snapshot is the size of the cluster volume at the time you take the snapshot. The `SnapshotStorageUsed`
  value depends on the number of snapshots you keep and the size of each snapshot. For example, suppose
  you have one manual snapshot outside the retention period, and the cluster's `VolumeBytesUsed`
  size was 100 GiB when that snapshot was taken. The amount of SnapshotStorageUsed is 107,374,182,400 bytes
  (100 GiB).
- `TotalBackupStorageBilled` represents the sum, in bytes, of
  `BackupRetentionPeriodStorageUsed` and `SnapshotStorageUsed`, minus
  an amount of free backup storage, which equals the size of the cluster volume
  for one day. The free backup storage is equal to the latest volume size. For
  example if your cluster's `VolumeBytesUsed` size is 100 GiB, your
  retention period is two days, and you have one manual snapshot outside the
  retention period, the `TotalBackupStorageBilled` is
  214,748,364,800 bytes (200 GiB + 100 GiB - 100 GiB).
  You can monitor a Neptune cluster and build reports using CloudWatch metrics through the
  [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/ ").
  For more information about how to use CloudWatch metrics, see [Monitoring Neptune](monitoring.md "monitoring.md") and the table of metrics in [Neptune CloudWatch metrics](cw-metrics.md#cw-metrics-available "cw-metrics.md#cw-metrics-available").
