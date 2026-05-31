# Backing up and restoring in Amazon DocumentDB

Amazon DocumentDB (with MongoDB compatibility) continuously backs up your data to Amazon Simple Storage Service (Amazon S3) for
1–35 days so that you can quickly restore to any
point within the backup retention period. Amazon DocumentDB also takes automatic
snapshots of your data as part of this continuous backup process.

###### Note

These are service-managed Amazon S3 buckets and you will not have access to the backup files.
If you want to control your own backups, follow the instructions on [Dumping, Restoring, Importing, and Exporting Data](backup_restore-dump_restore_import_export_data.md "backup_restore-dump_restore_import_export_data.md").

You can also retain backup data beyond the backup retention period by
creating a manual snapshot of your cluster's data. The backup process does
not impact your cluster's performance.

This section discusses the use cases for the backup capabilities in
Amazon DocumentDB and shows you how to manage backups for your Amazon DocumentDB clusters.

###### Topics

- [Back up and restore: concepts](backup_restore-nouns_verbs.md "backup_restore-nouns_verbs.md")
- [Understanding backup storage usage](backup_restore-understanding_backup_storage_usage.md "backup_restore-understanding_backup_storage_usage.md")
- [Dumping, restoring, importing, and exporting data](backup_restore-dump_restore_import_export_data.md "backup_restore-dump_restore_import_export_data.md")
- [Cluster snapshot considerations](backup_restore-cluster_snapshot_considerations.md "backup_restore-cluster_snapshot_considerations.md")
- [Comparing automatic and manual snapshots](backup_restore-compare_automatic_manual_snapshots.md "backup_restore-compare_automatic_manual_snapshots.md")
- [Creating a manual cluster snapshot](backup_restore-create_manual_cluster_snapshot.md "backup_restore-create_manual_cluster_snapshot.md")
- [Copying a cluster snapshot](backup_restore-copy_cluster_snapshot.md "backup_restore-copy_cluster_snapshot.md")
- [Sharing a cluster snapshot](backup_restore-share_cluster_snapshots.md "backup_restore-share_cluster_snapshots.md")
- [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md "backup_restore-restore_from_snapshot.md")
- [Restoring to a point in time](backup_restore-point_in_time_recovery.md "backup_restore-point_in_time_recovery.md")
- [Deleting a cluster snapshot](backup_restore-delete_cluster_snapshot.md "backup_restore-delete_cluster_snapshot.md")
