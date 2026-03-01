# Rebooting nodes

Some changes require that a Valkey, Memcached, or Redis OSS cluster reboot for the changes to be applied.
For example, for some parameters, changing the parameter value in a parameter group is only applied
after a reboot.

###### Topics

- [Rebooting Valkey or Redis OSS nodes (cluster mode disabled only)](#nodes.rebooting.redis "#nodes.rebooting.redis")
- [Rebooting a cluster for Memcached](#Clusters.Rebooting "#Clusters.Rebooting")

## Rebooting Valkey or Redis OSS nodes (cluster mode disabled only)

For Valkey or Redis OSS (cluster mode disabled) clusters, the parameters in parameter groups that are applied only after rebooting are:

- activerehashing
- databases

Valkey and Redis OSS nodes can only be updated through the ElastiCache console. You can only reboot a
single node at a time. To reboot multiple nodes, you must repeat the process for each
node.

###### Valkey or Redis OSS (Cluster Mode Enabled) parameter changes

If you make changes to the following parameters on a Valkey or Redis OSS (cluster mode enabled) cluster,
follow the ensuing steps.

- activerehashing
- databases

1. Create a manual backup of your cluster. See [Taking manual backups](backups-manual.md "backups-manual.md").
2. Delete the Valkey or Redis OSS (cluster mode enabled) cluster. See [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md").
3. Restore the cluster using the altered parameter group and backup to seed
   the new cluster. See [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").
   Changes to other parameters do not require this.

You can reboot a node using the ElastiCache console.

###### To reboot a node (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the list in the upper-right corner, choose the AWS Region that
   applies.
3. In the left navigation pane, choose **Valkey or Redis OSS**.

A list of clusters running Valkey or Redis OSS appears. 4. Choose the cluster under **Cluster Name**. 5. Under **Node name**, choose the radio button next to
the node you want to reboot. 6. Choose **Actions**, and then choose **Reboot
node**.
To reboot multiple nodes, repeat steps 2 through 5 for each node that you want
to reboot. You do not need to wait for one node to finish rebooting to reboot
another.

## Rebooting a cluster for Memcached

When you reboot a Memcached cluster, the cluster flushes all its data and restarts its engine.
During this process you cannot access the cluster.
Because the cluster flushed all its data,
when the cluster is available again, you are starting with an empty cluster.

You are able to reboot a cluster using the ElastiCache console, the AWS CLI, or the ElastiCache API.
Whether you use the ElastiCache console, the AWS CLI or the ElastiCache API, you can only initiate
rebooting a single cluster. To reboot multiple clusters you must iterate on the process
or operation.

You can reboot a cluster using the ElastiCache console.

###### To reboot a cluster (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the list in the upper-right corner, choose the AWS Region you are interested in.
3. In the navigation pane, choose the engine running on the cluster that you want to
   reboot.

A list of clusters running the chosen engine appears. 4. Choose the cluster to reboot by choosing on the box
to the left of the cluster's name.

The **Reboot** button becomes active.

If you choose more than one cluster, the **Reboot**
button isn't active. 5. Choose **Reboot**.

The reboot cluster confirmation screen appears. 6. To reboot the cluster, choose **Reboot**.
The status of the cluster changes to _rebooting cluster nodes_.

To not reboot the cluster, choose **Cancel**.
To reboot multiple clusters, repeat steps 2 through 5 for each cluster that you want to
reboot. You do not need to wait for one cluster to finish rebooting to reboot
another.

To reboot a specific node, select the node and then choose **Reboot**.

To reboot a cluster (AWS CLI), use the `reboot-cache-cluster` CLI operation.

To reboot specific nodes in the cluster,
use the `--cache-node-ids-to-reboot` to list the specific clusters to reboot.
The following command reboots the nodes 0001, 0002, and 0004 of _my-cluster_.

For Linux, macOS, or Unix:

```
aws elasticache reboot-cache-cluster \
    --cache-cluster-id `my-cluster` \
    --cache-node-ids-to-reboot `0001 0002 0004`
```

For Windows:

```
aws elasticache reboot-cache-cluster ^
    --cache-cluster-id `my-cluster` ^
    --cache-node-ids-to-reboot `0001 0002 0004`
```

To reboot all the nodes in the cluster, use the `--cache-node-ids-to-reboot` parameter
and list all the cluster's node ids.
For more information, see [reboot-cache-cluster](../../../cli/latest/reference/elasticache/reboot-cache-cluster.md "../../../cli/latest/reference/elasticache/reboot-cache-cluster.md").

To reboot a cluster using the ElastiCache API, use the `RebootCacheCluster` action.

To reboot specific nodes in the cluster,
use the `CacheNodeIdsToReboot` to list the specific clusters to reboot.
The following command reboots the nodes 0001, 0002, and 0004 of _my-cluster_.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=RebootCacheCluster
   &CacheClusterId=my-cluster
   &CacheNodeIdsToReboot.member.1=0001
   &CacheNodeIdsToReboot.member.2=0002
   &CacheNodeIdsToReboot.member.3=0004
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

To reboot all the nodes in the cluster, use the `CacheNodeIdsToReboot` parameter
and list all the cluster's node ids.
For more information, see [RebootCacheCluster](../APIReference/API_RebootCacheCluster.md "../APIReference/API_RebootCacheCluster.md").
