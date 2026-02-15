# Restoring a Multi-AZ DB cluster to a specified time

You can restore a Multi-AZ DB cluster to a specific point in time, creating a new Multi-AZ DB cluster.

RDS uploads transaction logs for Multi-AZ DB clusters to Amazon S3 continuously. You can restore to any point
in time within your backup retention period. To see the earliest restorable time for a Multi-AZ DB cluster,
use the AWS CLI [describe-db-clusters](../../../cli/latest/reference/rds/describe-db-clusters.md "../../../cli/latest/reference/rds/describe-db-clusters.md")
command. Look at the value returned in the `EarliestRestorableTime` field for the DB cluster.
To see the latest restorable time for a Multi-AZ DB cluster, look at the value returned in the
`LatestRestorableTime` field for the DB cluster.

When you restore a Multi-AZ DB cluster to a point in time, you can choose the default VPC security group
for your Multi-AZ DB cluster, or you can apply a custom VPC security group to your Multi-AZ DB cluster.

Restored Multi-AZ DB clusters are automatically associated with the default DB cluster parameter group.
However, you can apply a custom DB cluster parameter group by specifying it during a
restore.

If the source DB cluster has resource tags, RDS adds the latest tags to the restored
DB cluster.

###### Note

We recommend that you restore to the same or similar Multi-AZ DB cluster size as the source
DB cluster. We also recommend that you restore with the same or similar IOPS value if
you're using Provisioned IOPS storage. You might get an error if, for example, you
choose a DB cluster size with an incompatible IOPS value.

If the source Multi-AZ DB cluster uses General Purpose SSD (gp3) storage and has less than 400 GiB
of allocated storage, you can't modify the provisioned IOPS for the restored DB cluster.

For information about restoring a Multi-AZ DB cluster with an RDS Extended Support version, see [Restoring a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md").

You can restore a Multi-AZ DB cluster to a point in time using the AWS Management Console, the AWS CLI, or the RDS API.

###### To restore a Multi-AZ DB cluster to a specified time

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the Multi-AZ DB cluster that you want to restore.
4. For **Actions**, choose **Restore to point in time**.

The **Restore to point in time** window appears. 5. Choose **Latest restorable time** to restore to the latest possible time, or choose
**Custom** to choose a time.

If you chose **Custom**, enter the date and time to which you want to restore the Multi-AZ DB cluster.

###### Note

Times are shown in your local time zone, which is indicated by an offset from Coordinated Universal Time
(UTC). For example, UTC-5 is Eastern Standard Time/Central Daylight Time. 6. For **DB cluster identifier**, enter the name for your
restored Multi-AZ DB cluster. 7. In **Availability and durability**, choose **Multi-AZ DB cluster**.

![Multi-AZ DB cluster choice](images/multi-az-db-cluster-create.png) 8. In **DB instance class**, choose a DB instance class.

Currently, Multi-AZ DB clusters only support db.m6gd and db.r6gd DB instance classes.
For more information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md"). 9. For the remaining sections, specify your DB cluster settings. For information about each setting, see
[Settings for creating Multi-AZ DB clusters](create-multi-az-db-cluster.md#create-multi-az-db-cluster-settings "create-multi-az-db-cluster.md#create-multi-az-db-cluster-settings"). 10. Choose **Restore to point in time**.
To restore a Multi-AZ DB cluster to a specified time, use the AWS CLI command
[restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md") to create a new Multi-AZ DB cluster.

Currently, Multi-AZ DB clusters only support db.m6gd and db.r6gd DB instance classes.
For more information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

###### Example

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-to-point-in-time \
    --source-db-cluster-identifier `mysourcemultiazdbcluster` \
    --db-cluster-identifier `mytargetmultiazdbcluster` \
    --restore-to-time `2021-08-14T23:45:00.000Z` \
    --db-cluster-instance-class `db.r6gd.xlarge`
```

For Windows:

```
aws rds restore-db-cluster-to-point-in-time ^
    --source-db-cluster-identifier `mysourcemultiazdbcluster` ^
    --db-cluster-identifier `mytargetmultiazdbcluster` ^
    --restore-to-time `2021-08-14T23:45:00.000Z` ^
    --db-cluster-instance-class `db.r6gd.xlarge`
```

To restore a DB cluster to a specified time, call the Amazon RDS API
[RestoreDBClusterToPointInTime](../APIReference/API_RestoreDBClusterToPointInTime.md "../APIReference/API_RestoreDBClusterToPointInTime.md") operation with the following parameters:

- `SourceDBClusterIdentifier`
- `DBClusterIdentifier`
- `RestoreToTime`
