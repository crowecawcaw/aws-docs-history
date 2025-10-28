# Creating a Multi-AZ DB cluster snapshot for Amazon RDS

When you create a Multi-AZ DB cluster snapshot, make sure to identify which Multi-AZ DB cluster you are going to back up, and then give your DB cluster snapshot a name so you can
restore from it later. You can also share a Multi-AZ DB cluster snapshot. For instructions,
see [Sharing a DB snapshot for Amazon RDS](USER_ShareSnapshot.md "USER_ShareSnapshot.md").

You can create a Multi-AZ DB cluster snapshot using the AWS Management Console, the AWS CLI, or the RDS API.

For very long-term backups, we recommend exporting snapshot data to Amazon S3. If the major
version of your DB engine is no longer supported, you can't restore to that version
from a snapshot. For more information, see [Exporting DB snapshot data to Amazon S3 for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md").

###### To create a DB cluster snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. In the list, choose the Multi-AZ DB cluster for which you want to take a snapshot.
4. For **Actions**, choose **Take snapshot**.

The **Take DB snapshot** window appears. 5. For **Snapshot name**, enter the name of the snapshot. 6. Choose **Take snapshot**.
The **Snapshots** page appears, with the new Multi-AZ DB cluster snapshot's status shown as `Creating`. After
its status is `Available`, you can see its creation time.

You can create a Multi-AZ DB cluster snapshot by using the AWS CLI [create-db-cluster-snapshot](../../../cli/latest/reference/rds/create-db-cluster-snapshot.md "../../../cli/latest/reference/rds/create-db-cluster-snapshot.md") command with the following options:

- `--db-cluster-identifier`
- `--db-cluster-snapshot-identifier`
  In this example, you create a Multi-AZ DB cluster snapshot called
  `mymultiazdbclustersnapshot` for a DB cluster called `mymultiazdbcluster`.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster-snapshot \
    --db-cluster-identifier `mymultiazdbcluster` \
    --db-cluster-snapshot-identifier `mymultiazdbclustersnapshot`
```

For Windows:

```
aws rds create-db-cluster-snapshot ^
    --db-cluster-identifier `mymultiazdbcluster` ^
    --db-cluster snapshot-identifier `mymultiazdbclustersnapshot`
```

You can create a Multi-AZ DB cluster snapshot by using the Amazon RDS API
[CreateDBClusterSnapshot](../APIReference/API_CreateDBClusterSnapshot.md "../APIReference/API_CreateDBClusterSnapshot.md") operation with the following
parameters:

- `DBClusterIdentifier`
- `DBClusterSnapshotIdentifier`

## Deleting a Multi-AZ DB cluster snapshot

You can delete Multi-AZ DB snapshots managed by Amazon RDS when you no longer need them. For
instructions, see [Deleting a DB snapshot for Amazon RDS](USER_DeleteSnapshot.md "USER_DeleteSnapshot.md").
