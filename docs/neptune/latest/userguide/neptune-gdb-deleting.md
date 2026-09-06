

# Deleting a Neptune global database
<a name="neptune-gdb-deleting"></a>

You can't delete a global database and its associated clusters in a single step. Instead, you have to delete its components one by one:

1. Detach all secondary DB clusters from the global database, as described in [Removing a cluster](neptune-gdb-detaching.md). If you want to, you can now delete them individually.

1. Detach the primary DB cluster from the global database.

1. Delete all read-replica DB instances from the primary cluster.

1. Delete the primary (writer) DB instance from the primary cluster. If you do this on the console, it deletes the DB cluster as well.

1. Delete the global database itself. To do this using the AWS CLI, use the [delete-global-cluster](https://docs.aws.amazon.com/cli/latest/reference/neptune/delete-global-cluster.html) CLI command (which wraps the [DeleteGlobalCluster](api-global-dbs.md#DeleteGlobalCluster) API), as follows:

   ```
   aws neptune delete-global-cluster \
     --region {{(region of the DB cluster to delete)}} \
     --global-cluster-identifier {{(global database ID)}}
   ```