# Migrating previous generation nodes

Previous generation nodes are node types that are being phased out. If you have no
existing clusters using a previous generation node type, ElastiCache does not support the
creation of new clusters with that node type.

Due to the limited amount of previous generation node types, we cannot guarantee a
successful replacement when a node becomes unhealthy in your cluster(s). In such a
scenario, your cluster availability may be negatively impacted.

We recommend that you migrate your cluster(s) to a new node type for better
availability and performance. For a recommended node type to migrate to, see [Upgrade Paths](https://aws.amazon.com/ec2/previous-generation/ "https://aws.amazon.com/ec2/previous-generation/"). For a
full list of supported node types and previous generation node types in ElastiCache, see [Supported node types](CacheNodes.md "CacheNodes.md").

## Migrating nodes on a Valkey or Redis OSS cluster

The following procedure describes how to migrate your Valkey or Redis OSS cluster node type
using the ElastiCache Console. During this process, your Valkey or Redis OSS cluster will continue
to serve requests with minimal downtime. Depending on your cluster configuration you
may see the following downtimes. The following are estimates and may differ based on
your specific configurations:

- Cluster mode disabled (single node) may see approximately 60 seconds,
  primarily due to DNS propagation.
- Cluster mode disabled (with replica node) may see approximately 1 second
  for clusters running Valkey 7.2 and above or Redis OSS 5.0.6 and above. All lower versions can experience
  approximately 10 seconds.
- Cluster mode enabled may see approximately 1 second.

**To modify a Valkey or Redis OSS cluster node type using the
console:**

1. Sign in to the Console and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/home "https://console.aws.amazon.com/elasticache/home").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.
3. From the list of clusters, choose the cluster you want to migrate.
4. Choose **Actions** and then choose
   **Modify**.
5. Choose the new node type from the node type list.
6. If you want to perform the migration process right away, choose
   **Apply immediately**. If **Apply
   immediately** is not chosen, the migration process is performed
   during the cluster's next maintenance window.
7. Choose **Modify**. If you chose **Apply
   immediately** in the previous step, the cluster's status
   changes to **modifying**. When the status changes to
   **available**, the modification is complete and you can
   begin using the new cluster.

_To modify a Valkey or Redis OSS cluster node type using the AWS CLI:_

Use the [modify-replication-group](../../../cli/latest/reference/elasticache/modify-replication-group.md "../../../cli/latest/reference/elasticache/modify-replication-group.md") API as shown following:

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group /
	--replication-group-id `my-replication-group` /
	--cache-node-type `new-node-type` /
	--apply-immediately


```

For Windows:

```
aws elasticache modify-replication-group ^
	--replication-group-id `my-replication-group` ^
	--cache-node-type `new-node-type` ^
	--apply-immediately


```

In this scenario, the value of `new-node-type` is the
node type you are migrating to. By passing the `--apply-immediately`
parameter, the update will be applied immediately when the replication group
transitions from **modifying** to **available**
status. If **Apply immediately** is not chosen, the migration
process is performed during the cluster's next maintenance window.

###### Note

If you are unable to modify the cluster with an
`InvalidCacheClusterState` error, you need to remove a
restore-failed node first.

### Fixing or removing restore-failed-node(s)

The following procedure describes how to fix or remove restore-failed node(s) from your
Valkey or Redis OSS cluster.
To learn more on how ElastiCache node(s) enter a restore-failed state, see
[Viewing ElastiCache Node Status](Nodes.md "Nodes.md").
We recommend first removing any nodes in a restore-failed state, then
migrating the remaining previous generation nodes in the ElastiCache cluster to a newer
generation node type, and finally adding back the required number of nodes.

To remove restore-failed node (console):

1. Sign in to the Console and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/home "https://console.aws.amazon.com/elasticache/home").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.
3. From the list of clusters, choose the cluster you want to remove a
   node from.
4. From the list of shards, choose the shard you want to remove a node
   from. Skip this step if cluster mode is disabled for the cluster.
5. From the list of nodes, choose the node with a status of
   `restore-failed`.
6. Choose **Actions** and then choose **Delete
   node**.

Once you remove the restore-failed node(s) from your ElastiCache cluster, you can now migrate to a
newer generation type. For more information, see above on
[Migrating nodes on a Valkey or Redis OSS cluster](#CacheNodes.NodeMigration.Redis "#CacheNodes.NodeMigration.Redis").

To add back nodes to your ElastiCache cluster,
see [Adding nodes to an ElastiCache cluster](Clusters.md "Clusters.md").

## Migrating nodes on a Memcached

cluster

To migrate ElastiCache for Memcached to a different node type, you must create a new cluster, which
always starts out empty that your application can populate.

**To migrate your ElastiCache for Memcached cluster node type using the ElastiCache
Console:**

- Create a new cluster with the new node type. For more information, see
  [Creating a Memcached cluster (console)](Clusters.md#Clusters.Create.CON.Memcached "Clusters.md#Clusters.Create.CON.Memcached").
- In your application, update the endpoints to the new cluster's endpoints.
  For more information, see [Finding a Cluster's Endpoints (Console) (Memcached)](Endpoints.md#Endpoints.Find.Memcached "Endpoints.md#Endpoints.Find.Memcached")
- Delete the old cluster. For more information, see [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md")
