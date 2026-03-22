# Deleting a Multi-AZ DB cluster for Amazon RDS

You can delete a DB Multi-AZ DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.

The time required to delete a Multi-AZ DB cluster can vary depending on the following factors:

- Thee backup retention period (that is, how many backups to delete).
- How much data is deleted.
- Whether a final snapshot is taken.
  Deletion protection must be disabled on the Multi-AZ DB cluster before you can delete it. For more
  information, see [Prerequisites for deleting a DB instance](USER_DeleteInstance.md#USER_DeleteInstance.DeletionProtection "USER_DeleteInstance.md#USER_DeleteInstance.DeletionProtection"). You can disable deletion
  protection by modifying the Multi-AZ DB cluster. For more information, see [Modifying a Multi-AZ DB cluster for Amazon RDS](modify-multi-az-db-cluster.md "modify-multi-az-db-cluster.md").

###### To delete a Multi-AZ DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the Multi-AZ DB cluster that you want to delete.
3. For **Actions**, choose **Delete**.
4. Choose **Create final snapshot?** to create a final DB snapshot for the
   Multi-AZ DB cluster.

If you create a final snapshot, enter a name for **Final
snapshot name**. 5. Choose **Retain automated backups** to retain automated backups. 6. Enter `delete me` in the box. 7. Choose **Delete**.
To delete a Multi-AZ DB cluster by using the AWS CLI, call the [delete-db-cluster](../../../cli/latest/reference/rds/delete-db-cluster.md "../../../cli/latest/reference/rds/delete-db-cluster.md") command with the following options:

- `--db-cluster-identifier`
- `--final-db-snapshot-identifier` or `--skip-final-snapshot`

###### Example With a final snapshot

For Linux, macOS, or Unix:

```
aws rds delete-db-cluster \
    --db-cluster-identifier `mymultiazdbcluster` \
    --final-db-snapshot-identifier `mymultiazdbclusterfinalsnapshot`
```

For Windows:

```
aws rds delete-db-cluster ^
    --db-cluster-identifier `mymultiazdbcluster` ^
    --final-db-snapshot-identifier `mymultiazdbclusterfinalsnapshot`
```

###### Example With no final snapshot

For Linux, macOS, or Unix:

```
aws rds delete-db-cluster \
    --db-cluster-identifier `mymultiazdbcluster` \
    --skip-final-snapshot
```

For Windows:

```
aws rds delete-db-cluster ^
    --db-cluster-identifier `mymultiazdbcluster` ^
    --skip-final-snapshot
```

To delete a Multi-AZ DB cluster by using the Amazon RDS API, call the [DeleteDBCluster](../APIReference/API_DeleteDBCluster.md "../APIReference/API_DeleteDBCluster.md") operation with the following parameters:

- `DBClusterIdentifier`
- `FinalDBSnapshotIdentifier` or `SkipFinalSnapshot`
