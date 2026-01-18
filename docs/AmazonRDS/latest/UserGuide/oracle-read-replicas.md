# Working with RDS for Oracle replica backups

You can create and restore backups of an RDS for Oracle replica. Both automatic backups and manual snapshots are supported. For more information,
see [Backing up, restoring, and exporting data](CHAP_CommonTasks.md "CHAP_CommonTasks.md"). The following sections describe the key
differences between managing backups of a primary and an RDS for Oracle replica.

## Turning on RDS for Oracle replica backups

An Oracle replica doesn't have automated backups turned on by default. You turn on automated backups by setting the backup retention
period to a positive nonzero value.

###### To enable automated backups immediately

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose
   the DB instance or Multi-AZ DB cluster that you want to modify.
3. Choose **Modify**.
4. For **Backup retention period**, choose a positive nonzero
   value, for example three days.
5. Choose **Continue**.
6. Choose **Apply immediately**.
7. Choose **Modify DB instance** or **Modify
   cluster** to save your changes and enable automated
   backups.
   To enable automated backups, use the AWS CLI [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") or [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") command.

Include the following parameters:

- `--db-instance-identifier` (or `--db-cluster-identifier`
  for a Multi-AZ DB cluster)
- `--backup-retention-period`
- `--apply-immediately` or `--no-apply-immediately`
  In the following example, we enable automated backups by setting the backup retention period to three days. The changes are applied
  immediately.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my_db_instance`  \
    --backup-retention-period `3` \
    `--apply-immediately`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my_db_instance`  ^
    --backup-retention-period `3` ^
    `--apply-immediately`
```

To enable automated backups, use the RDS API [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") or [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") operation with the following required
parameters:

- `DBInstanceIdentifier` or `DBClusterIdentifier`
- `BackupRetentionPeriod`

## Restoring an RDS for Oracle replica backup

You can restore an Oracle replica backup just as you can restore a backup of the primary instance. For more information, see the
following:

- [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md")
- [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md")

The main consideration when you restore a replica backup is determining the point in time to which you are restoring. The
_database time_ refers to the latest applied transaction time of the data in the backup. When you restore a
replica backup, you restore to the database time, not the time when the backup completed. The difference is significant because an
RDS for Oracle replica can lag behind the primary by minutes or hours. Thus, the database time of a replica backup, and thus the point in time
to which you restore it, might be much earlier than the backup creation time.

To find the difference between database time and creation time, use the `describe-db-snapshots` command. Compare the
`SnapshotDatabaseTime`, which is the database time of the replica backup, and the `OriginalSnapshotCreateTime`
field, which is the latest applied transaction on the primary database. The following example shows the difference between the two
times:

```
aws rds describe-db-snapshots \
    --db-instance-identifier my-oracle-replica
    --db-snapshot-identifier my-replica-snapshot

{
    "DBSnapshots": [
        {
            "DBSnapshotIdentifier": "my-replica-snapshot",
            "DBInstanceIdentifier": "my-oracle-replica",
            "SnapshotDatabaseTime": "2022-07-26T**17:49:44Z**",
            ...
            "OriginalSnapshotCreateTime": "2021-07-26T**19:49:44Z**"
        }
    ]
}
```
