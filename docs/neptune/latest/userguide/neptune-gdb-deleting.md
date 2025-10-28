# Deleting a Neptune global database

You can't delete a global database and its associated clusters in a single step.
Instead, you have to delete its components one by one:

1. Detach all secondary DB clusters from the global database, as
   described in [Removing a cluster](neptune-gdb-detaching.md "neptune-gdb-detaching.md"). If you want to, you can now
   delete them individually.
2. Detach the primary DB cluster from the global database.
3. Delete all read-replica DB instances from the primary cluster.
4. Delete the primary (writer) DB instance from the primary cluster.
   If you do this on the console, it deletes the DB cluster as well.
5. Delete the global database itself. To do this using the AWS CLI, use the [delete-global-cluster](../../../cli/latest/reference/neptune/delete-global-cluster.md "../../../cli/latest/reference/neptune/delete-global-cluster.md")
   CLI command (which wraps the [DeleteGlobalCluster](api-global-dbs.md#DeleteGlobalCluster "api-global-dbs.md#DeleteGlobalCluster") API), as follows:

```
aws neptune delete-global-cluster \
  --region `(region of the DB cluster to delete)` \
  --global-cluster-identifier `(global database ID)`
```
