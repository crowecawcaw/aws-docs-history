# Removing a cluster from an Amazon Aurora global database

You can remove Aurora DB clusters from your Aurora global database for several different reasons. For example,
you might want to remove an Aurora DB cluster from an Aurora global database if the primary cluster
becomes degraded or isolated. It then becomes a standalone
provisioned Aurora DB cluster that could be used to create a new Aurora global database. To learn more, see [Recovering an Amazon Aurora global database from an unplanned outage](aurora-global-database-disaster-recovery.md#aurora-global-database-failover "aurora-global-database-disaster-recovery.md#aurora-global-database-failover").

You also might want to remove Aurora DB clusters because you want to delete an Aurora global database that you no longer need. You can't
delete the Aurora global database until after you remove (detach) all associated Aurora DB clusters, leaving the primary for last.
For more information, see
[Deleting an Amazon Aurora global database](aurora-global-database-deleting.md "aurora-global-database-deleting.md").

When an Aurora DB cluster is detached from the Aurora global database, it's no longer synchronized with the primary. It becomes a
standalone provisioned Aurora DB cluster with full read/write capabilities.

You can remove Aurora DB clusters from your Aurora global database using the AWS Management Console, the AWS CLI, or the RDS API.

###### To remove an Aurora cluster from an Aurora global database

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose the cluster on the **Databases** page.
3. For **Actions**, choose **Remove from Global**.

![Screenshot showing selected Aurora DB cluster (secondary) and "Remove from global" Action.](images/aurora-global-db-detach-secondary-01.png)

You see a prompt to confirm that you want to detach the secondary from the Aurora global database.

![Screenshot showing confirmation prompt to remove a secondary cluster from an Aurora global database.](images/aurora-global-db-detach-secondary-02.png) 4. Choose **Remove and promote** to remove the cluster from the global database.
The Aurora DB cluster is no longer serving as a secondary in the Aurora global database, and is
no longer synchronized with the primary DB cluster. It is a
standalone Aurora DB cluster with full read/write capability.

![Screenshot showing confirmation prompt to remove a secondary cluster from an Aurora global database.](images/aurora-global-db-detach-secondary-03.png)
After you remove or delete all secondary clusters, then you can remove the primary cluster the same way.
You can't detach (remove) the primary Aurora DB cluster from an Aurora global database
until after you remove all secondary clusters.

The Aurora global database might remain in the **Databases** list, with zero
Regions and AZs. You can delete if you no longer want to use this Aurora global database.
For more information, see [Deleting an Amazon Aurora global database](aurora-global-database-deleting.md "aurora-global-database-deleting.md").

To remove an Aurora cluster from an Aurora global database, run the
[remove-from-global-cluster](../../../cli/latest/reference/rds/remove-from-global-cluster.md "../../../cli/latest/reference/rds/remove-from-global-cluster.md") CLI command with the
following parameters:

- `--global-cluster-identifier` – The name (identifier) of your Aurora global database.
- `--db-cluster-identifier` – The name of each Aurora DB cluster to remove from the Aurora global
  database. Remove all secondary Aurora DB clusters before removing the primary.

The following examples first remove a secondary cluster and then the primary cluster from an Aurora global database.

For Linux, macOS, or Unix:

```
aws rds --region `secondary_region` \
  remove-from-global-cluster \
    --db-cluster-identifier `secondary_cluster_ARN` \
    --global-cluster-identifier `global_database_id`

aws rds --region `primary_region` \
  remove-from-global-cluster \
    --db-cluster-identifier `primary_cluster_ARN` \
    --global-cluster-identifier `global_database_id`
```

Repeat the `remove-from-global-cluster --db-cluster-identifier `secondary_cluster_ARN`` command
for each secondary AWS Region in your Aurora global database.

For Windows:

```
aws rds --region `secondary_region` ^
  remove-from-global-cluster ^
    --db-cluster-identifier `secondary_cluster_ARN` ^
    --global-cluster-identifier `global_database_id`

aws rds --region `primary_region` ^
  remove-from-global-cluster ^
    --db-cluster-identifier `primary_cluster_ARN` ^
    --global-cluster-identifier `global_database_id`

```

Repeat the `remove-from-global-cluster --db-cluster-identifier `secondary_cluster_ARN``
command for each secondary AWS Region in your Aurora global database.

To remove an Aurora cluster from an Aurora global database with the RDS API, run the
[RemoveFromGlobalCluster](../APIReference/API_RemoveFromGlobalCluster.md "../APIReference/API_RemoveFromGlobalCluster.md") action.
