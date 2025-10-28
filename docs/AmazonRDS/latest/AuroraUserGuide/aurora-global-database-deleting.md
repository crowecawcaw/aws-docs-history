# Deleting an Amazon Aurora global database

Because an Aurora global database typically holds business-critical data, you can't delete the global database and its
associated clusters in a single step. To delete an Aurora global database, do the following:

- Remove all secondary DB clusters from the Aurora global database. Each cluster becomes a standalone Aurora DB cluster.
  To learn how, see [Removing a cluster from an Amazon Aurora global database](aurora-global-database-detaching.md "aurora-global-database-detaching.md").
- From each standalone Aurora DB cluster, delete all Aurora Replicas.
- Remove the primary DB cluster from the Aurora global database. This becomes a standalone Aurora DB cluster.
- From the Aurora primary DB cluster, first delete all Aurora Replicas, then delete the writer DB instance.

Deleting the writer instance from the newly standalone Aurora DB cluster also typically removes the Aurora DB cluster
and the Aurora global database.

For more general information, see [Deleting a DB instance from an Aurora DB cluster](USER_DeleteCluster.md#USER_DeleteInstance "USER_DeleteCluster.md#USER_DeleteInstance").

To delete an Aurora global database, you can use the AWS Management Console, the AWS CLI, or the RDS API.

###### To delete an Aurora global database

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases** and find the Aurora global database you want to delete in the listing.
3. Confirm that all clusters are removed from the Aurora global database. The Aurora global
   database should show 0 Regions and AZs and a size of 0 clusters.

If the Aurora global database contains any Aurora DB clusters, you can't delete it. If necessary, detach the primary and secondary Aurora
DB clusters from the Aurora global database. For more information, see [Removing a cluster from an Amazon Aurora global database](aurora-global-database-detaching.md "aurora-global-database-detaching.md"). 4. Choose your Aurora global database in the list, and then choose **Delete** from the **Actions** menu.

![An Aurora global database based on Aurora MySQL 5.6.10a remains in the AWS Management Console until you delete it, even if it doesn't have any associated Aurora DB clusters.](images/aurora-global-db-ams5610a-delete-empty-cluster.png)
To delete an Aurora global database, run the
[delete-global-cluster](../../../cli/latest/reference/rds/delete-global-cluster.md "../../../cli/latest/reference/rds/delete-global-cluster.md") CLI command with
the name of the AWS Region and the Aurora global database identifier, as shown in the following example.

For Linux, macOS, or Unix:

```
aws rds --region `primary_region` delete-global-cluster \
   --global-cluster-identifier `global_database_id`
```

For Windows:

```
aws rds --region `primary_region` delete-global-cluster ^
   --global-cluster-identifier `global_database_id`
```

To delete a cluster that is part of an Aurora global database, run
the [DeleteGlobalCluster](../APIReference/API_DeleteGlobalCluster.md "../APIReference/API_DeleteGlobalCluster.md") API operation.
