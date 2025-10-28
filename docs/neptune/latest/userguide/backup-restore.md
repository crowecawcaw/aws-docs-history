# Backing up and restoring an Amazon Neptune DB cluster

This section shows how you can back up and restore Amazon Neptune DB clusters.

###### Topics

- [Neptune Backups](#backup-restore-overview-backups "#backup-restore-overview-backups")
- [Fault tolerance for a Neptune DB cluster](backup-restore-overview-fault-tolerance.md "backup-restore-overview-fault-tolerance.md")
- [CloudWatch metrics that are useful for managing Neptune backup storage](backup-restore-overview-metrics.md "backup-restore-overview-metrics.md")
- [Restoring data from a Neptune backup](backup-restore-overview-restore.md "backup-restore-overview-restore.md")
- [Backup window in Neptune](backup-restore-overview-backup-window.md "backup-restore-overview-backup-window.md")
- [Creating a DB Cluster Snapshot in Neptune](backup-restore-create-snapshot.md "backup-restore-create-snapshot.md")
- [Restoring from a DB Cluster Snapshot](backup-restore-restore-snapshot.md "backup-restore-restore-snapshot.md")
- [Copying a DB Cluster Snapshot](backup-restore-copy-snapshot.md "backup-restore-copy-snapshot.md")
- [Sharing a DB Cluster Snapshot](backup-restore-share-snapshot.md "backup-restore-share-snapshot.md")
- [Deleting a Neptune Snapshot](backup-restore-delete-snapshot.md "backup-restore-delete-snapshot.md")

## Neptune Backups

Neptune backs up your cluster volume automatically and retains restore data for the
length of the _backup retention period_. Neptune backups are continuous
and incremental so you can quickly restore to any point within the backup retention period. No
performance impact or interruption of database service occurs as backup data is being written.
You can specify a backup retention period, from 1 to 35 days, when you create or modify a DB
cluster.

To control your backup storage usage, you can reduce the backup retention interval,
remove old manual snapshots when they are no longer needed, or both. To help manage your
costs, you can monitor the amount of storage consumed by continuous backups and manual
snapshots that persist beyond the retention period. You can reduce the backup retention
interval and remove manual snapshots when they are no longer needed.

If you want to retain a backup beyond the backup retention period, you can also take a
snapshot of the data in your cluster volume. Storing snapshots incurs the standard storage
charges for Neptune. For more information about Neptune storage pricing, see [Amazon Neptune Pricing](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").

Neptune retains incremental restore data for the entire backup retention period. So
you only need to create a snapshot for data that you want to retain beyond the backup
retention period. You can create a new DB cluster from the snapshot.

###### Important

If you delete a DB cluster, all its automated backups are deleted
at the same time and cannot be recovered. This means that unless you choose to create
a final DB snapshot manually, you can't restore the DB instance to its final state at
a later time. Manual snapshots are not deleted when the cluster is deleted.

###### Note

- For Amazon Neptune DB clusters, the default backup retention period is one day
  regardless of how the DB cluster is created.
- You cannot disable automated backups on Neptune. The backup retention period for
  Neptune is managed by the DB cluster.
