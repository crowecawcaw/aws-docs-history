# Restoring from a snapshot to a Multi-AZ DB cluster

You can restore a snapshot to a Multi-AZ DB cluster using the AWS Management Console, the AWS CLI, or the RDS API. You
can restore each of these types of snapshots to a Multi-AZ DB cluster:

- A snapshot of a Single-AZ deployment
- A snapshot of a Multi-AZ DB cluster deployment with a single DB instance
- A snapshot of a Multi-AZ DB cluster
  For information about Multi-AZ deployments, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").

###### Tip

You can migrate a Single-AZ deployment or a Multi-AZ DB cluster deployment to a
Multi-AZ DB cluster deployment by restoring a snapshot.

For information about restoring Multi-AZ DB cluster with an RDS Extended Support version, see [Restoring a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md").

###### To restore a snapshot to a Multi-AZ DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the snapshot that you want to restore from.
4. For **Actions**, choose **Restore
   snapshot**.
5. On the **Restore snapshot** page, in
   **Availability and durability**, choose
   **Multi-AZ DB cluster**.

![Multi-AZ DB cluster choice](images/multi-az-db-cluster-create.png) 6. For **DB cluster identifier**, enter the name for your
restored Multi-AZ DB cluster. 7. For the remaining sections, specify your DB cluster settings. For
information about each setting, see [Settings for creating Multi-AZ DB clusters](create-multi-az-db-cluster.md#create-multi-az-db-cluster-settings "create-multi-az-db-cluster.md#create-multi-az-db-cluster-settings"). 8. Choose **Restore DB instance**.
To restore a snapshot to a Multi-AZ DB cluster, use the AWS CLI command [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md").

In the following example, you restore from a previously created snapshot named
`mysnapshot`. You restore to a new Multi-AZ DB cluster named
`mynewmultiazdbcluster`. You also specify the DB instance class used
by the DB instances in the Multi-AZ DB cluster. Specify either `mysql` or
`postgres` for the DB engine.

For the `--snapshot-identifier` option, you can use either the name or
the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can
use only the ARN to specify a DB snapshot.

For the `--db-cluster-instance-class` option, specify the DB instance
class for the new Multi-AZ DB cluster. Multi-AZ DB clusters only support specific DB instance classes, such as
the db.m6gd and db.r6gd DB instance classes. For more information about DB instance
classes, see [DB instance classes](Concepts.md "Concepts.md").

You can also specify other options.

###### Example

For Linux, macOS, or Unix:

```
aws rds restore-db-cluster-from-snapshot \
    --db-cluster-identifier `mynewmultiazdbcluster` \
    --snapshot-identifier `mysnapshot` \
    --engine `mysql|postgres` \
    --db-cluster-instance-class `db.r6gd.xlarge`
```

For Windows:

```
aws rds restore-db-cluster-from-snapshot ^
    --db-cluster-identifier `mynewmultiazdbcluster` ^
    --snapshot-identifier `mysnapshot` ^
    --engine `mysql|postgres` ^
    --db-cluster-instance-class `db.r6gd.xlarge`
```

After you restore the DB cluster, you can add the Multi-AZ DB cluster to the security group
associated with the DB cluster or DB instance that you used to create the snapshot,
if applicable. Completing this action provides the same functions of the previous DB
cluster or DB instance.

To restore a snapshot to a Multi-AZ DB cluster, call the RDS API operation [RestoreDBClusterFromSnapshot](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md") with the following parameters:

- `DBClusterIdentifier`
- `SnapshotIdentifier`
- `Engine`
  You can also specify other optional parameters.

After you restore the DB cluster, you can add the Multi-AZ DB cluster to the security group
associated with the DB cluster or DB instance that you used to create the snapshot,
if applicable. Completing this action provides the same functions of the previous DB
cluster or DB instance.
