

# Working with RDS for Db2 replica backups
<a name="db2-read-replicas.backups"></a>

You can create and restore backups of an RDS for Db2 replica just like a primary database. However, there are important differences in how replica backups work, particularly regarding restore timing and backup retention settings.

RDS for Db2 supports both automatic backups and manual snapshots for replicas. RDS for Db2 doesn't support point-in-time restore. For information about RDS backups, see [Backing up, restoring, and exporting data](CHAP_CommonTasks.BackupRestore.md). 

## Key differences for replica backups
<a name="db2-read-replicas-backups-overview"></a>

Replica backups differ from primary database backups in several important ways:
+ Automatic backups aren't enabled by default for replicas.
+ Restore operations use database time rather than backup creation time.
+ Replica lag can affect the actual data restored. For information about monitoring replica lag, see [Monitoring Db2 replication lag](db2-troubleshooting-replicas.md#db2-troubleshooting-replicas-lag).

## Enabling automatic backups for RDS for Db2 replicas
<a name="db2-read-replicas.backups.turning-on"></a>

Unlike primary databases, RDS for Db2 replicas don't have automated backups enabled by default. You must manually configure the backup retention period to enable automatic backups. Enable automated backups by setting the backup retention period to a positive nonzero value.

### Console
<a name="db2-read-replicas.backups.turning-on-console"></a>

**To enable automatic backups immediately**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to modify.

1. Choose **Modify**.

1. For **Backup retention period**, choose a positive nonzero value, for example three days.

1. Choose **Continue**.

1. Choose **Apply immediately**.

1. Choose **Modify DB instance** to save your changes and enable automated backups.

### AWS CLI
<a name="db2-read-replicas.backups.turning-on-cli"></a>

To enable automated backups, use the AWS CLI [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command.

Include the following parameters:
+ `--db-instance-identifier`
+ `--backup-retention-period`
+ `--apply-immediately` or `--no-apply-immediately`

The following example enables automated backups by setting the backup retention period to three days. The changes are applied immediately.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds modify-db-instance \
    --db-instance-identifier {{my_db_instance }} \
    --backup-retention-period 3 \
    --apply-immediately
```
For Windows:  

```
aws rds modify-db-instance ^
    --db-instance-identifier {{my_db_instance }} ^
    --backup-retention-period 3 ^
    --apply-immediately
```

### RDS API
<a name="db2-read-replicas.backups.turning-on-api"></a>

To enable automated backups, use the RDS API [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation with the following required parameters:
+ `DBInstanceIdentifier`
+ `BackupRetentionPeriod`

## Restoring an RDS for Db2 replica backup
<a name="db2-read-replicas.backups.restoring"></a>

You can restore an RDS for Db2 replica backup the same way that you can restore a backup of the primary database. For more information, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md).

The most important consideration when restoring replica backups is understanding the difference between database time and backup creation time, especially when replica lag is present.

You can monitor replication lag and ensure that your backups contain the expected data. For information about the ReplicaLag metric, see [Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md).

### Understanding timing differences
<a name="db2-read-replicas-backups-restoring-timing"></a>

When you restore a replica backup, you must determine the point in time to which you are restoring. The database time refers to the latest applied transaction time of the data in the backup. When you restore a replica backup, you restore to the database time, not the time when the backup completed. The difference is significant because a replica can lag behind the primary database by minutes or hours. Thus, the database time of a replica backup might be much earlier than the snapshot creation time.

To find the difference between database time and creation time, run the AWS CLI [describe-db-snapshots](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-snapshots.html) command or call the RDS API [DescribeDBSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBSnapshots.html) operation. Compare the `SnapshotDatabaseTime` value and the `OriginalSnapshotCreateTime` value. The `SnapshotDatabaseTime` value is the earliest database time among all the databases of the replica backup. The `OriginalSnapshotCreateTime` value is the latest applied transaction on the primary database. Note that replication lags could be different for multiple databases, and the database time could be in between these two times. 

The following AWS CLI example shows the difference between the two times:

For Linux, macOS, or Unix:

```
aws rds describe-db-snapshots \
    --db-instance-identifier {{my_db2_replica}} \
    --db-snapshot-identifier {{my_replica_snapshot}}
```

For Windows:

```
aws rds describe-db-snapshots ^
    --db-instance-identifier {{my_db2_replica}} ^
    --db-snapshot-identifier {{my_replica_snapshot}}
```

This command produces output similar to the following example. 

```
{
    "DBSnapshots": [
        {
            "DBSnapshotIdentifier": "{{my_replica_snapshot}}",
            "DBInstanceIdentifier": "{{my_db2_replica}}", 
            "SnapshotDatabaseTime": "2022-07-26T17:49:44Z",
            ...
            "OriginalSnapshotCreateTime": "2021-07-26T19:49:44Z"
        }
    ]
}
```