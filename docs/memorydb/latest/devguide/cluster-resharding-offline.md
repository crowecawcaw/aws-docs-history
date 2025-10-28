# Offline resharding for MemoryDB

The main advantage you get from offline shard reconfiguration is that you can do more than
merely add or remove shards from your cluster. When you reshard offline,
in addition to changing the number of shards in your cluster, you can do
the following:

- Change the node type of your cluster.
- Upgrade to a newer engine version.

###### Note

Offline resharding is not supported on clusters with data tiering enabled. For more information, see [Data tiering](data-tiering.md "data-tiering.md")..

The main disadvantage of offline shard reconfiguration is that your cluster is offline
beginning with the restore portion of the process and continuing until you update
the endpoints in your application. The length of time that your cluster is offline
varies with the amount of data in your cluster.

###### To reconfigure your shards MemoryDB cluster offline

1. Create a manual snapshot of your existing MemoryDB cluster.
   For more information, see [Making manual snapshots](snapshots-manual.md "snapshots-manual.md").
2. Create a new cluster by restoring from the snapshot.
   For more information, see [Restoring from a snapshot](snapshots-restoring.md "snapshots-restoring.md").
3. Update the endpoints in your application to the new
   cluster's endpoints.
   For more information, see [Finding connection endpoints](endpoints.md "endpoints.md").
