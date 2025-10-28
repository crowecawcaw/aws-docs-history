# Modifying cluster mode

Valkey and Redis OSS are a distributed in-memory databases that supports sharding and replication.
ElastiCache Valkey and Redis OSS clusters are the distributed implementation that allows data to be partitioned across multiple nodes. An ElastiCache for Redis OSS cluster
has two modes of operation, Cluster mode enabled (CME) and cluster mode disabled (CMD).
In CME, a Valkey and Redis OSS engine works as a distributed database with multiple shards and nodes, while in CMD, Valkey and Redis OSS work as a single node.

Before migrating from CMD to CME, the following conditions must be met:

###### Important

Cluster mode configuration can only be changed from cluster mode disabled to cluster mode enabled. Reverting this configuration is not possible.

- The cluster may only have keys in database 0 only.
- Applications must use a Valkey or Redis OSS client that is capable of using Cluster protocol and use a configuration endpoint.
- Auto-failover must be enabled on the cluster with a minimum of 1 replica.
- The minimum engine version required for migration is Valkey 7.2 and above, or Redis OSS 7.0 and above.
  To migrate from CMD to CME, the cluster mode configuration must be changed from cluster mode disabled to cluster mode enabled. This is a two-step procedure that ensures cluster availability during the migration process.

###### Note

You need to provide a parameter group with cluster-enabled configuration, that is, the cluster-enabled parameter is set as `yes`.
If you are using a default parameter group, ElastiCache for Redis OSS will automatically pick the corresponding default parameter group with a cluster-enabled configuration.
The cluster-enabled parameter value is set to `no` for a CMD cluster. As the cluster moves to the compatible mode, the cluster-enabled parameter value is updated to `yes` as part of the modification action.

For more information, see [Configuring engine parameters using ElastiCache parameter
groups](ParameterGroups.md "ParameterGroups.md")

1. **Prepare** – Create a test CME cluster and make sure your stack is ready to work with it. ElastiCache for Redis OSS has no way to verify your readiness.
   For more information, see [Creating a cluster for Valkey or Redis OSS](Clusters.md "Clusters.md").
2. **Modify existing CMD Cluster Configuration to cluster mode compatible** – In this mode, there will be a single shard deployed, and ElastiCache for Redis OSS will work as a single node but also as a single shard cluster.
   Compatible mode means the client application can use either protocol to communicate with the cluster. In this mode, applications must be reconfigured to start using Valkey or Redis OSS Cluster protocol and configuration endpoint.
   To change the Valkey or Redis OSS cluster mode to cluster mode compatible, follow the steps below:

###### Note

In compatible mode, other modification operations such as scaling and engine version are not allowed for the cluster.
Additionally, parameters (excluding `cacheParameterGroupName`) cannot be modified when defining cluster-mode parameter within the [ModifyReplicationGroup](../APIReference/API_ModifyReplicationGroup.md "../APIReference/API_ModifyReplicationGroup.md") request.

    1. Using the AWS Management Console, see [Modifying a replication group](Replication.md "Replication.md") and set the cluster mode to **Compatible**
    2. Using the API, see [ModifyReplicationGroup](../APIReference/API_ModifyReplicationGroup.md "../APIReference/API_ModifyReplicationGroup.md") and
     update the `ClusterMode` parameter to `compatible`.
    3. Using the AWS CLI, see [modify-replication-group](../../../cli/latest/reference/elasticache/modify-replication-group.md "../../../cli/latest/reference/elasticache/modify-replication-group.md") and
     update the `cluster-mode` parameter to `compatible`.After changing the Valkey or Redis OSS cluster mode to cluster mode compatible, the [DescribeReplicationGroups](../APIReference/API_DescribeReplicationGroups.md "../APIReference/API_DescribeReplicationGroups.md") API will return the ElastiCache for Redis OSS cluster configuration endpoint. The cluster configuration endpoint is a single endpoint that can be used by applications to connect to the cluster.

For more information, see [Finding connection endpoints in ElastiCache](Endpoints.md "Endpoints.md"). 3. **Modify Cluster Configuration to cluster mode enabled** – Once the cluster mode is set to cluster mode compatible, the second step is to modify the cluster configuration to cluster mode enabled. In this mode, a single shard is running, and customers can now scale their clusters or modify other cluster configurations.

To change the cluster mode to enabled, follow the steps below:

Before you begin, make sure your Valkey or Redis OSS clients have migrated to using cluster protocol and that the cluster's configuration endpoint is not in use.

    1. Using the AWS Management Console, see [Modifying a replication group](Replication.md "Replication.md") and set the cluster mode to **Enabled**.
    2. Using the API, see [ModifyReplicationGroup](../APIReference/API_ModifyReplicationGroup.md "../APIReference/API_ModifyReplicationGroup.md") and
     update the `ClusterMode` parameter to `enabled`.
    3. Using the AWS CLI, see [modify-replication-group](../../../cli/latest/reference/elasticache/modify-replication-group.md "../../../cli/latest/reference/elasticache/modify-replication-group.md") and
     update the `cluster-mode` parameter to `enabled`.After changing the cluster mode to enabled, the endpoints will be configured as per the Valkey or Redis OSS cluster specification. The [DescribeReplicationGroups](../APIReference/API_DescribeReplicationGroups.md "../APIReference/API_DescribeReplicationGroups.md") API will

return the cluster mode parameter as `enabled` and the cluster endpoints that are now available to be used by applications to connect to the cluster.

Note that the cluster endpoints will change once the cluster mode is changed to enabled. Make sure to update your applications with the new endpoints.
You can also choose to revert back to cluster mode disabled (CMD) from cluster mode compatible and preserve the original configurations.

###### Modify Cluster Configuration to cluster mode disabled from cluster mode compatible

1. Using the AWS Management Console, see [Modifying a replication group](Replication.md "Replication.md") and set the cluster mode to **Disabled**
2. Using the API, see [ModifyReplicationGroup](../APIReference/API_ModifyReplicationGroup.md "../APIReference/API_ModifyReplicationGroup.md") and
   update the `ClusterMode` parameter to `disabled`.
3. Using the AWS CLI, see [modify-replication-group](../../../cli/latest/reference/elasticache/modify-replication-group.md "../../../cli/latest/reference/elasticache/modify-replication-group.md") and
   update the `cluster-mode` parameter to `disabled`.
   After changing the cluster mode to disabled, the [DescribeReplicationGroups](../APIReference/API_DescribeReplicationGroups.md "../APIReference/API_DescribeReplicationGroups.md") API will
   return the cluster mode parameter as `disabled`.
