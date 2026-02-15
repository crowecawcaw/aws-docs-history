# Creating a DB cluster snapshot

Amazon RDS creates a storage volume snapshot of your DB cluster, backing up the entire DB
cluster and not just individual databases. When you create a DB cluster snapshot, you need
to identify which DB cluster you are going to back up, and then give your DB cluster snapshot
a name so you can restore from it later. The amount of time it takes to create a DB cluster
snapshot varies with the size of your databases. Because the snapshot includes the entire storage
volume, the size of files, such as temporary files, also affects the amount of time it takes
to create the snapshot.

###### Note

Your DB cluster must be in the `available` state to take a DB cluster snapshot.

Unlike automated backups, manual snapshots aren't subject to the backup retention
period. Snapshots don't expire.

For very long-term backups, we recommend exporting snapshot data to Amazon S3. If the major
version of your DB engine is no longer supported, you can't restore to that version
from a snapshot. For more information, see
[Exporting DB cluster snapshot data to Amazon S3](aurora-export-snapshot.md "aurora-export-snapshot.md").

You can create a DB cluster snapshot using the AWS Management Console, the AWS CLI, or the RDS API.

###### To create a DB cluster snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.

The **Manual snapshots** list appears. 3. Choose **Take snapshot**.

The **Take DB snapshot** window appears. 4. For **Snapshot type**, select **DB cluster**.

![Take DB snapshot.](images/take_db_cluster_snapshot.png) 5. Choose the **DB cluster** for which you want to take a snapshot. 6. Enter the **Snapshot name**. 7. Choose **Take snapshot**.

The **Manual snapshots** list appears, with the new DB cluster snapshot's status shown as
`Creating`. After its status is `Available`, you can see its creation time.
When you create a DB cluster snapshot using the AWS CLI, you need to identify which DB cluster you
are going to back up, and then give your DB cluster snapshot a name so you can restore from it
later. You can do this by using the AWS CLI [`create-db-cluster-snapshot`](../../../cli/latest/reference/rds/create-db-cluster-snapshot.md "../../../cli/latest/reference/rds/create-db-cluster-snapshot.md") command with the following parameters:

- `--db-cluster-identifier`
- `--db-cluster-snapshot-identifier`
  In this example, you create a DB cluster snapshot named `mydbclustersnapshot` for
  a DB cluster called `mydbcluster`.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-cluster-snapshot \
    --db-cluster-identifier `mydbcluster` \
    --db-cluster-snapshot-identifier `mydbclustersnapshot`
```

For Windows:

```
aws rds create-db-cluster-snapshot ^
    --db-cluster-identifier `mydbcluster` ^
    --db-cluster-snapshot-identifier `mydbclustersnapshot`
```

When you create a DB cluster snapshot using the Amazon RDS API, you need to identify which DB cluster
you are going to back up, and then give your DB cluster snapshot a name so you can restore from
it later. You can do this by using the Amazon RDS API [`CreateDBClusterSnapshot`](../APIReference/API_CreateDBClusterSnapshot.md "../APIReference/API_CreateDBClusterSnapshot.md") command with the following
parameters:

- DBClusterIdentifier
- DBClusterSnapshotIdentifier

## Determining whether the DB cluster snapshot is available

You can check that the DB cluster snapshot is available by looking under **Snapshots**
on the **Maintenance & backups** tab on the detail page for the
cluster in the AWS Management Console, by using the [`describe-db-cluster-snapshots`](../../../cli/latest/reference/rds/describe-db-cluster-snapshots.md "../../../cli/latest/reference/rds/describe-db-cluster-snapshots.md") CLI
command, or by using the [`DescribeDBClusterSnapshots`](../APIReference/API_DescribeDBClusterSnapshots.md "../APIReference/API_DescribeDBClusterSnapshots.md") API action.

You can also use the [`wait db-cluster-snapshot-available`](../../../cli/latest/reference/rds/wait/db-cluster-snapshot-available.md "../../../cli/latest/reference/rds/wait/db-cluster-snapshot-available.md") CLI command
to poll the API every 30 seconds until the snapshot is available.
