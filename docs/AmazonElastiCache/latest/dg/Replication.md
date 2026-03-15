# High availability using replication groups

Single-node Amazon ElastiCache Valkey and Redis OSS clusters are in-memory entities with limited data protection
services (AOF). If your cluster fails for any reason, you lose all the cluster's data.
However, if you're running a Valkey or Redis OSS engine, you can group 2 to
6 nodes into a cluster with replicas where 1 to
5 read-only nodes contain replicate data of the group's single
read/write primary node. In this scenario, if one node fails for any reason, you do not lose
all your data since it is replicated in one or more other nodes. Due to replication latency,
some data may be lost if it is the primary read/write node that fails.

As seen in the following graphic, the replication structure is contained within a shard
(called _node group_ in the API/CLI) which is contained within a Valkey or Redis OSS cluster.
Valkey or Redis OSS (cluster mode disabled) clusters always have one shard. Valkey or Redis OSS (cluster mode enabled) clusters can have up to 500
shards with the cluster's data partitioned across the shards.
You can create a cluster with higher number of shards and lower number of replicas totaling up to 90 nodes per cluster.
This cluster configuration can range from 90 shards and 0 replicas to 15 shards and 5 replicas, which is the maximum number of replicas allowed.

The node or shard limit can be increased to a maximum of 500 per cluster with ElastiCache for Valkey, and with ElastiCache version 5.0.6 or higher for Redis OSS.
For example, you can choose to configure a 500 node cluster that ranges between
83 shards (one primary and 5 replicas per shard) and 500 shards (single primary and no replicas). Make sure there are enough available IP addresses to accommodate the increase.
Common pitfalls include the subnets in the subnet group have too small a CIDR range or the subnets are shared and heavily used by other clusters. For more information, see
[Creating a subnet group](SubnetGroups.md "SubnetGroups.md").

For versions below 5.0.6,
the limit is 250 per cluster.

To request a limit increase, see
[AWS Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
and choose the limit type **Nodes per cluster per instance type**.

![Image: Valkey or Redis OSS (cluster mode disabled) cluster has one shard and 0 to 5 replica nodes](images/ElastiCacheClusters-CSN-Redis-Replicas.png)
_Valkey or Redis OSS (cluster mode disabled) cluster has one shard and 0 to 5 replica nodes_

If the cluster with replicas has Multi-AZ enabled and the primary
node fails, the primary fails over to a read replica. Because the data is updated on the
replica nodes asynchronously, there may be some data loss due to latency in updating the
replica nodes. For more information, see [Mitigating Failures when Running Valkey or Redis OSS](disaster-recovery-resiliency.md#FaultTolerance.Redis "disaster-recovery-resiliency.md#FaultTolerance.Redis").

###### Topics

- [Understanding Valkey and Redis OSS replication](Replication.Redis.md "Replication.Redis.md")
- [Replication: Valkey and Redis OSS Cluster Mode Disabled vs. Enabled](Replication.md "Replication.md")
- [Minimizing downtime in ElastiCache by using Multi-AZ with Valkey and Redis OSS](AutoFailover.md "AutoFailover.md")
- [How synchronization and backup are implemented](Replication.Redis.md "Replication.Redis.md")
- [Creating a Valkey or Redis OSS replication group](Replication.md "Replication.md")
- [Viewing a replication group's details](Replication.md "Replication.md")
- [Finding replication group endpoints](Replication.md "Replication.md")
- [Modifying a replication group](Replication.md "Replication.md")
- [Deleting a replication group](Replication.md "Replication.md")
- [Changing the number of replicas](increase-decrease-replica-count.md "increase-decrease-replica-count.md")
- [Promoting a read replica to primary, for Valkey or Redis OSS (cluster mode disabled) replication groups](Replication.md "Replication.md")
