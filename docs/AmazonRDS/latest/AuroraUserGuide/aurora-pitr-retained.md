# Restoring a DB cluster to a specified time from a retained automated backup

You can restore a DB cluster from a retained automated backup after you delete the source DB cluster, if the backup is within
the retention period of the source cluster. The process is similar to restoring a DB cluster from an automated backup.

###### Note

You can't restore an Aurora Serverless v1 DB cluster using this procedure, because automated backups for Aurora Serverless v1
clusters aren't retained.

###### To restore a DB cluster to a specified time

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Automated backups**.
3. Choose the **Retained** tab.

![Retained automated backups](images/db-cluster-retained-automated-backups.png) 4. Choose the DB cluster that you want to restore. 5. For **Actions**, choose **Restore to point in time**.

The **Restore to point in time** window appears. 6. Choose **Latest restorable time** to restore to the latest possible time, or choose
**Custom** to choose a time.

If you chose **Custom**, enter the date and time to which you want to restore the cluster.

###### Note

Times are shown in your local time zone, which is indicated by an offset from Coordinated Universal Time
(UTC). For example, UTC-5 is Eastern Standard Time/Central Daylight Time. 7. For **DB cluster identifier**, enter the name of the target restored DB cluster. The name
must be unique. 8. Choose other options as needed, such as DB instance class.

For information about each setting, see [Settings for Aurora DB clusters](Aurora.md#Aurora.CreateInstance.Settings "Aurora.md#Aurora.CreateInstance.Settings"). 9. Choose **Restore to point in time**.
To restore a DB cluster to a specified time, use the AWS CLI command [restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md") to
create a new DB cluster.

You can specify other settings. For information about each setting, see [Settings for Aurora DB clusters](Aurora.md#Aurora.CreateInstance.Settings "Aurora.md#Aurora.CreateInstance.Settings").

Resource tagging is supported for this operation. When you use the `--tags` option, the source DB cluster tags
are ignored and the provided ones are used. Otherwise, the latest tags from the source cluster are used.

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-to-point-in-time \
    --source-db-cluster-resource-id `cluster-123ABCEXAMPLE` \
    --db-cluster-identifier `mytargetdbcluster` \
    --restore-to-time `2017-10-14T23:45:00.000Z`
```

For Windows:

```
aws rds restore-db-cluster-to-point-in-time ^
    --source-db-cluster-resource-id `cluster-123ABCEXAMPLE` ^
    --db-cluster-identifier `mytargetdbcluster` ^
    --restore-to-time `2017-10-14T23:45:00.000Z`
```

###### Important

If you use the console to restore a DB cluster to a specified time, then Amazon RDS
automatically creates the primary instance (writer) for your DB cluster. If you
use the AWS CLI to restore a DB cluster to a specified time, you must explicitly
create the primary instance for your DB cluster. The primary instance is the
first instance that is created in a DB cluster.

To create the primary instance for your DB cluster, call the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
AWS CLI command. Include the name of the DB cluster as the
`--db-cluster-identifier` option value.

To restore a DB cluster to a specified time, call the Amazon RDS API
[`RestoreDBClusterToPointInTime`](../APIReference/API_RestoreDBClusterToPointInTime.md "../APIReference/API_RestoreDBClusterToPointInTime.md") operation with the following parameters:

- `SourceDbClusterResourceId`
- `DBClusterIdentifier`
- `RestoreToTime`

###### Important

If you use the console to restore a DB cluster to a specified time, then Amazon RDS
automatically creates the primary instance (writer) for your DB cluster. If you
use the RDS API to restore a DB cluster to a specified time, make sure to
explicitly create the primary instance for your DB cluster. The primary instance
is the first instance that is created in a DB cluster.

To create the primary instance for your DB cluster, call the RDS API operation
[CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md"). Include the name of the DB cluster as the
`DBClusterIdentifier` parameter value.
