# Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters

As demand on your clusters changes, you might decide to improve performance or reduce costs
by changing the number of shards in your Valkey or Redis OSS (cluster mode enabled) cluster. We recommend using
online horizontal scaling to do so, because it allows your cluster to continue serving
requests during the scaling process.

Conditions under which you might decide to rescale your cluster include the
following:

- **Memory pressure:**

If the nodes in your cluster are under memory pressure, you might decide to scale out so
that you have more resources to better store data and serve requests.

You can determine whether your nodes are under memory pressure by monitoring the
following metrics: _FreeableMemory_, _SwapUsage_,
and _BytesUsedForCache_.

- **CPU or network bottleneck:**

If latency/throughput issues are plaguing your cluster, you might need to scale out to
resolve the issues.

You can monitor your latency and throughput levels by monitoring the following metrics:
_CPUUtilization_, _NetworkBytesIn_,
_NetworkBytesOut_, _CurrConnections_,
and _NewConnections_.

- **Your cluster is over-scaled:**

Current demand on your cluster is such that scaling in doesn't hurt performance and
reduces your costs.

You can monitor your cluster's use to determine whether or not you can safely
scale in using the following metrics:
_FreeableMemory_, _SwapUsage_,
_BytesUsedForCache_,
_CPUUtilization_, _NetworkBytesIn_,
_NetworkBytesOut_, _CurrConnections_,
and _NewConnections_.

###### Performance Impact of Scaling

When you scale using the offline process, your cluster is offline for a significant portion
of the process and thus unable to serve requests.
When you scale using the online method, because scaling is a compute-intensive operation, there
is some degradation in performance, nevertheless, your cluster continues to serve requests throughout
the scaling operation. How much degradation you experience depends upon your normal CPU utilization
and your data.

There are two ways to scale your Valkey or Redis OSS (cluster mode enabled) cluster; horizontal and vertical scaling.

- Horizontal scaling allows you to change the number of node groups (shards) in the replication group by adding or removing node groups (shards).
  The online resharding process allows scaling in/out while the cluster continues serving incoming requests.

Configure the slots in your new cluster differently than they were
in the old cluster. Offline method only.

- Vertical Scaling - Change the node type to resize the cluster. The online vertical scaling allows scaling up/down while the cluster continues serving incoming requests.
  If you are reducing the size and memory capacity of the cluster, by either scaling in or scaling down, ensure that the new configuration has sufficient memory for your data and Valkey or Redis OSS overhead.

For more information, see [Choosing your node size](CacheNodes.md "CacheNodes.md").

###### Contents

- [Offline resharding for Valkey or Redis OSS (cluster mode enabled)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-offline "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-offline")
- [Online resharding for Valkey or Redis OSS (cluster mode enabled)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online")
  - [Adding shards with online resharding](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-add "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-add")
  - [Removing shards with online resharding](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove")
    - [Removing shards (Console)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove-console "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove-console")
    - [Removing shards (AWS CLI)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove-cli "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove-cli")
    - [Removing shards (ElastiCache API)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove-api "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-remove-api")

  - [Online shard rebalancing](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance")
    - [Online Shard Rebalancing (Console)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance-console "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance-console")
    - [Online shard rebalancing (AWS CLI)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance-cli "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance-cli")
    - [Online shard rebalancing (ElastiCache API)](scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance-api "scaling-redis-cluster-mode-enabled.md#redis-cluster-resharding-online-rebalance-api")

- [Online vertical scaling by modifying node type](redis-cluster-vertical-scaling.md "redis-cluster-vertical-scaling.md")
  - [Online scaling up](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-up "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-up")
    - [Scaling up Valkey or Redis OSS clusters (Console)](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-console "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-console")
    - [Scaling up Valkey or Redis OSS clusters (AWS CLI)](redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleUp.CLI "redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleUp.CLI")
    - [Scaling up Valkey or Redis OSS clusters (ElastiCache API)](redis-cluster-vertical-scaling.md#VeticalScaling.RedisReplGrps.ScaleUp.API "redis-cluster-vertical-scaling.md#VeticalScaling.RedisReplGrps.ScaleUp.API")

  - [Online scaling down](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-down "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-scaling-down")
    - [Scaling down Valkey or Redis OSS clusters (Console)](redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-down-console "redis-cluster-vertical-scaling.md#redis-cluster-vertical-scaling-down-console")
    - [Scaling down Valkey or Redis OSS clusters (AWS CLI)](redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleDown.CLI "redis-cluster-vertical-scaling.md#Scaling.RedisStandalone.ScaleDown.CLI")
    - [Scaling down Valkey or Redis OSS clusters (ElastiCache API)](redis-cluster-vertical-scaling.md#Scaling.Vertical.ScaleDown.API "redis-cluster-vertical-scaling.md#Scaling.Vertical.ScaleDown.API")

## Offline resharding for Valkey or Redis OSS (cluster mode enabled)

The main advantage you get from offline shard reconfiguration is that you can do more than
merely add or remove shards from your replication group. When you reshard and rebalance offline,
in addition to changing the number of shards in your replication group, you can do
the following:

###### Note

Offline resharding is not supported on Valkey or Redis OSS clusters with data tiering enabled. For more information, see [Data tiering in ElastiCache](data-tiering.md "data-tiering.md").

- Change the node type of your replication group.
- Specify the Availability Zone for each node in the replication group.
- Upgrade to a newer engine version.
- Specify the number of replica nodes in each shard independently.
- Specify the keyspace for each shard.

The main disadvantage of offline shard reconfiguration is that your cluster is offline
beginning with the restore portion of the process and continuing until you update
the endpoints in your application. The length of time that your cluster is offline
varies with the amount of data in your cluster.

###### To reconfigure your shards Valkey or Redis OSS (cluster mode enabled) cluster offline

1. Create a manual backup of your existing Valkey or Redis OSS cluster.
   For more information, see [Taking manual backups](backups-manual.md "backups-manual.md").
2. Create a new cluster by restoring from the backup.
   For more information, see [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").
3. Update the endpoints in your application to the new
   cluster's endpoints.
   For more information, see [Finding connection endpoints in ElastiCache](Endpoints.md "Endpoints.md").

## Online resharding for Valkey or Redis OSS (cluster mode enabled)

By using online resharding and shard rebalancing with ElastiCache Valkey 7.2 or newer, or Redis OSS version 3.2.10 or newer, you can scale
your Valkey or Redis OSS (cluster mode enabled) cluster dynamically with no downtime. This approach means that your cluster
can continue to serve requests even while scaling or rebalancing is in process.

You can do the following:

- **Scale out** –
  Increase read and write capacity by adding shards (node groups)
  to your Valkey or Redis OSS (cluster mode enabled) cluster (replication group).

If you add one or more shards to your replication group, the number of nodes in each new
shard is the same as the number of nodes in the smallest of the existing
shards.

- **Scale in** –
  Reduce read and write capacity,
  and thereby costs, by removing shards from your Valkey or Redis OSS (cluster mode enabled) cluster.
- **Rebalance** – Move the keyspaces among the shards in your
  Valkey or Redis OSS (cluster mode enabled) cluster so they are as equally distributed among the shards as possible.

You can't do the following:

- **Configure shards independently:**

You can't specify the keyspace for shards independently. To do this, you must use
the offline process.

Currently, the following limitations apply to ElastiCache online resharding and
rebalancing:

- These processes require Valkey 7.2 and newer or Redis OSS 3.2.10 or newer. For information on
  upgrading your engine version, see [Version Management for ElastiCache](VersionManagement.md "VersionManagement.md").
- There are limitations with slots or keyspaces and large items:

If any of the keys in a shard contain a large item, that key isn't migrated to a
new shard when scaling out or rebalancing. This functionality can result in
unbalanced shards.

If any of the keys in a shard contain a large item (items greater than 256 MB after
serialization), that shard isn't deleted when scaling in. This
functionality can result in some shards not being deleted.

- When scaling out, the number of nodes in any new shards equals the number of nodes in the
  smallest existing shard.
- When scaling out, any tags that are common to all existing shards are copied to the new shards.
- When scaling out a Global Data Store cluster, ElastiCache will not automatically replicate Functions from one of the existing nodes to the new node(s). We recommend loading your Functions in the new shard(s) after scaling out your cluster so that every shards have the same functions.

###### Note

In ElastiCache for Valkey 7.2 and above, and ElastiCache for Redis OSS version 7 and above: When scaling out your cluster, ElastiCache will automatically replicate the Functions loaded in one of the existing nodes (selected at random) to the new node(s).
If your application uses [Functions](https://valkey.io/topics/functions-intro/ "https://valkey.io/topics/functions-intro/"), we recommend loading all of your functions to all the shards before scaling out so that your cluster does not end up with different function definitions on different shards.

For more information, see [Online cluster resizing](best-practices-online-resharding.md "best-practices-online-resharding.md").

You can horizontally scale or rebalance your Valkey or Redis OSS (cluster mode enabled) clusters using the AWS Management Console, the
AWS CLI, and the ElastiCache API.

### Adding shards with online resharding

You can add shards to your Valkey or Redis OSS (cluster mode enabled) cluster using the AWS Management Console, AWS CLI, or ElastiCache
API. When you add shards to a Valkey or Redis OSS (cluster mode enabled) cluster, any tags on the existing
shards are copied over to the new shards.

###### Topics

You can use the AWS Management Console to add one or more shards to your Valkey or Redis OSS (cluster mode enabled)
cluster. The following procedure describes the process.

###### To add shards to your Valkey or Redis OSS (cluster mode enabled) cluster

1. Open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.
3. Locate and choose the name, not the box to the left of the cluster's name, of the Valkey or Redis OSS (cluster mode enabled)
   cluster that you want to add shards to.

###### Tip

Valkey or Redis OSS (cluster mode enabled) show **Clustered Valkey** or **Clustered Redis OSS** in the **Mode** column 4. Choose **Add shard**.

    1. For **Number of shards to be added**, choose the number of shards
     you want added to this cluster.
    2. For **Availability zone(s)**, choose either **No
     preference** or **Specify availability
     zones**.
    3. If you chose **Specify availability zones**,
     for each node in each shard, select the node's Availability Zone
     from the list of Availability Zones.
    4. Choose **Add**.

The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
cluster by adding shards using the AWS CLI.

Use the following parameters with `modify-replication-group-shard-configuration`.

###### Parameters

- `--apply-immediately` –
  Required. Specifies the shard reconfiguration operation is
  to be started immediately.
- `--replication-group-id` –
  Required. Specifies which replication group (cluster)
  the shard reconfiguration operation is to be performed on.
- `--node-group-count` – Required. Specifies the number of shards (node
  groups) to exist when the operation is completed. When adding
  shards, the value of `--node-group-count` must be greater
  than the current number of shards.

Optionally, you can specify the Availability Zone for each node in the replication
group using `--resharding-configuration`.

- `--resharding-configuration` –
  Optional. A list of preferred Availability Zones for each node in each shard
  in the replication group.
  Use this parameter only if the value of `--node-group-count`
  is greater than the current number of shards.
  If this parameter is omitted when adding shards, Amazon ElastiCache selects
  the Availability Zones for the new nodes.
  The following example reconfigures the keyspaces over four shards in a Valkey or Redis OSS (cluster mode enabled)
  cluster named `my-cluster`. The example also specifies the Availability
  Zone for each node in each shard. The operation begins immediately.

###### Example- Adding Shards

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group-shard-configuration \
    --replication-group-id `my-cluster` \
    --node-group-count `4` \
    --resharding-configuration \
        "PreferredAvailabilityZones=`us-east-2a`,`us-east-2c`" \
        "PreferredAvailabilityZones=`us-east-2b`,`us-east-2a`" \
        "PreferredAvailabilityZones=`us-east-2c`,`us-east-2d`" \
        "PreferredAvailabilityZones=`us-east-2d`,`us-east-2c`" \
    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group-shard-configuration ^
    --replication-group-id `my-cluster` ^
    --node-group-count `4` ^
    --resharding-configuration ^
        "PreferredAvailabilityZones=`us-east-2a`,`us-east-2c`" ^
        "PreferredAvailabilityZones=`us-east-2b`,`us-east-2a`" ^
        "PreferredAvailabilityZones=`us-east-2c`,`us-east-2d`" ^
        "PreferredAvailabilityZones=`us-east-2d`,`us-east-2c`" ^
    --apply-immediately
```

For more information, see [modify-replication-group-shard-configuration](../../../cli/latest/reference/elasticache/modify-replication-group-shard-configuration.md "../../../cli/latest/reference/elasticache/modify-replication-group-shard-configuration.md") in the AWS CLI documentation.

You can use the ElastiCache API to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled) cluster
online by using the `ModifyReplicationGroupShardConfiguration` operation.

Use the following parameters with `ModifyReplicationGroupShardConfiguration`.

###### Parameters

- `ApplyImmediately=true` –
  Required. Specifies the shard reconfiguration operation is
  to be started immediately.
- `ReplicationGroupId` –
  Required. Specifies which replication group (cluster)
  the shard reconfiguration operation is to be performed on.
- `NodeGroupCount` – Required. Specifies the number of shards (node
  groups) to exist when the operation is completed. When adding
  shards, the value of `NodeGroupCount` must be greater
  than the current number of shards.

Optionally, you can specify the Availability Zone for each node in the replication
group using `ReshardingConfiguration`.

- `ReshardingConfiguration` –
  Optional. A list of preferred Availability Zones for each node in each shard
  in the replication group.
  Use this parameter only if the value of `NodeGroupCount`
  is greater than the current number of shards.
  If this parameter is omitted when adding shards, Amazon ElastiCache selects
  the Availability Zones for the new nodes.
  The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
  cluster by adding shards using the ElastiCache API.

###### Example- Adding Shards

The following example adds node groups to the Valkey or Redis OSS (cluster mode enabled) cluster
`my-cluster`, so there are a total of four node groups
when the operation completes. The example also specifies the
Availability Zone for each node in each shard. The operation begins
immediately.

```
https://elasticache.us-east-2.amazonaws.com/
    ?Action=ModifyReplicationGroupShardConfiguration
    &ApplyImmediately=true
    &NodeGroupCount=`4`
    &ReplicationGroupId=`my-cluster`
    &ReshardingConfiguration.ReshardingConfiguration.1.PreferredAvailabilityZones.AvailabilityZone.1=`us-east-2a`
    &ReshardingConfiguration.ReshardingConfiguration.1.PreferredAvailabilityZones.AvailabilityZone.2=`us-east-2c`
    &ReshardingConfiguration.ReshardingConfiguration.2.PreferredAvailabilityZones.AvailabilityZone.1=`us-east-2b`
    &ReshardingConfiguration.ReshardingConfiguration.2.PreferredAvailabilityZones.AvailabilityZone.2=`us-east-2a`
    &ReshardingConfiguration.ReshardingConfiguration.3.PreferredAvailabilityZones.AvailabilityZone.1=`us-east-2c`
    &ReshardingConfiguration.ReshardingConfiguration.3.PreferredAvailabilityZones.AvailabilityZone.2=`us-east-2d`
    &ReshardingConfiguration.ReshardingConfiguration.4.PreferredAvailabilityZones.AvailabilityZone.1=`us-east-2d`
    &ReshardingConfiguration.ReshardingConfiguration.4.PreferredAvailabilityZones.AvailabilityZone.2=`us-east-2c`
    &Version=2015-02-02
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20171002T192317Z
    &X-Amz-Credential=<credential>
```

For more information, see [ModifyReplicationGroupShardConfiguration](../APIReference/API_ModifyReplicationGroupShardConfiguration.md "../APIReference/API_ModifyReplicationGroupShardConfiguration.md") in the ElastiCache API Reference.

### Removing shards with online resharding

You can remove shards from your Valkey or Redis OSS (cluster mode enabled) cluster using the AWS Management Console, AWS CLI, or
ElastiCache API.

###### Topics

- [Removing shards (Console)](#redis-cluster-resharding-online-remove-console "#redis-cluster-resharding-online-remove-console")
- [Removing shards (AWS CLI)](#redis-cluster-resharding-online-remove-cli "#redis-cluster-resharding-online-remove-cli")
- [Removing shards (ElastiCache API)](#redis-cluster-resharding-online-remove-api "#redis-cluster-resharding-online-remove-api")

#### Removing shards (Console)

The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
cluster by removing shards using the AWS Management Console.

Before removing node groups (shards) from your replication group, ElastiCache makes sure that
all your data will fit in the remaining shards. If the data will fit, the specified
shards are deleted from the replication group as requested. If the data
won't fit in the remaining node groups, the process is terminated and the replication group is left with the same node group configuration as before the request was made.

You can use the AWS Management Console to remove one or more shards from your Valkey or Redis OSS (cluster mode enabled) cluster.
You cannot remove all the shards in a replication group. Instead, you must
delete the replication group. For more information, see [Deleting a replication group](Replication.md "Replication.md"). The following procedure
describes the process for deleting one or more shards.

###### To remove shards from your Valkey or Redis OSS (cluster mode enabled) cluster

1. Open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.
3. Locate and choose the name, not the box to the left of the cluster's name, of the
   Valkey or Redis OSS (cluster mode enabled) cluster you want to remove shards from.

###### Tip

Valkey or Redis OSS (cluster mode enabled) clusters have a value of 1 or greater in the
**Shards** column. 4. From the list of shards, choose the box to the left of the name of each shard
that you want to delete. 5. Choose **Delete shard**.

#### Removing shards (AWS CLI)

The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
cluster by removing shards using the AWS CLI.

###### Important

Before removing node groups (shards) from your replication group, ElastiCache makes sure that
all your data will fit in the remaining shards. If the data will fit, the
specified shards (`--node-groups-to-remove`) are deleted from
the replication group as requested and their keyspaces mapped into the
remaining shards. If the data will not fit in the remaining node
groups, the process is terminated and the replication group is left with the same node group configuration as before the request was made.

You can use the AWS CLI to remove one or more shards from your Valkey or Redis OSS (cluster mode enabled) cluster. You
cannot remove all the shards in a replication group. Instead, you must
delete the replication group. For more information, see [Deleting a replication group](Replication.md "Replication.md").

Use the following parameters with `modify-replication-group-shard-configuration`.

###### Parameters

- `--apply-immediately` –
  Required. Specifies the shard reconfiguration operation is
  to be started immediately.
- `--replication-group-id` –
  Required. Specifies which replication group (cluster)
  the shard reconfiguration operation is to be performed on.
- `--node-group-count` – Required. Specifies the number of shards (node
  groups) to exist when the operation is completed. When removing
  shards, the value of `--node-group-count` must be less
  than the current number of shards.
- `--node-groups-to-remove` –
  Required when `--node-group-count` is less than the current number
  of node groups (shards).
  A list of shard (node group) IDs to remove from the replication group.

The following procedure describes the process for deleting one or more shards.

###### Example- Removing Shards

The following example removes two node groups from the Valkey or Redis OSS (cluster mode enabled) cluster
`my-cluster`, so there are a total of two node groups
when the operation completes. The keyspaces from the removed shards are
distributed evenly over the remaining shards.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group-shard-configuration \
    --replication-group-id `my-cluster` \
    --node-group-count `2` \
    --node-groups-to-remove "`0002`" "`0003`" \
    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group-shard-configuration ^
    --replication-group-id `my-cluster` ^
    --node-group-count `2` ^
    --node-groups-to-remove "`0002`" "`0003`" ^
    --apply-immediately
```

#### Removing shards (ElastiCache API)

You can use the ElastiCache API to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled) cluster
online by using the `ModifyReplicationGroupShardConfiguration` operation.

The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
cluster by removing shards using the ElastiCache API.

###### Important

Before removing node groups (shards) from your replication group, ElastiCache makes sure that
all your data will fit in the remaining shards. If the data will fit, the
specified shards (`NodeGroupsToRemove`) are deleted from the
replication group as requested and their keyspaces mapped into the
remaining shards. If the data will not fit in the remaining node
groups, the process is terminated and the replication group is left with the same node group configuration as before the request was made.

You can use the ElastiCache API to remove one or more shards from your Valkey or Redis OSS (cluster mode enabled) cluster.
You cannot remove all the shards in a replication group. Instead, you must
delete the replication group. For more information, see [Deleting a replication group](Replication.md "Replication.md").

Use the following parameters with `ModifyReplicationGroupShardConfiguration`.

###### Parameters

- `ApplyImmediately=true` –
  Required. Specifies the shard reconfiguration operation is
  to be started immediately.
- `ReplicationGroupId` –
  Required. Specifies which replication group (cluster)
  the shard reconfiguration operation is to be performed on.
- `NodeGroupCount` – Required. Specifies the number of shards (node
  groups) to exist when the operation is completed. When removing
  shards, the value of `NodeGroupCount` must be less than
  the current number of shards.
- `NodeGroupsToRemove` –
  Required when `--node-group-count` is less than the current number
  of node groups (shards). A list of shard (node group) IDs to remove from the replication group.

The following procedure describes the process for deleting one or more shards.

###### Example- Removing Shards

The following example removes two node groups from the Valkey or Redis OSS (cluster mode enabled) cluster
`my-cluster`, so there are a total of two node groups
when the operation completes. The keyspaces from the removed shards are
distributed evenly over the remaining shards.

```
https://elasticache.us-east-2.amazonaws.com/
    ?Action=ModifyReplicationGroupShardConfiguration
    &ApplyImmediately=true
    &NodeGroupCount=`2`
    &ReplicationGroupId=`my-cluster`
    &NodeGroupsToRemove.member.1=`0002`
    &NodeGroupsToRemove.member.2=`0003`
    &Version=2015-02-02
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20171002T192317Z
    &X-Amz-Credential=<credential>
```

### Online shard rebalancing

You can rebalance shards in your Valkey or Redis OSS (cluster mode enabled) cluster using the AWS Management Console, AWS CLI, or
ElastiCache API.

###### Topics

- [Online Shard Rebalancing (Console)](#redis-cluster-resharding-online-rebalance-console "#redis-cluster-resharding-online-rebalance-console")
- [Online shard rebalancing (AWS CLI)](#redis-cluster-resharding-online-rebalance-cli "#redis-cluster-resharding-online-rebalance-cli")
- [Online shard rebalancing (ElastiCache API)](#redis-cluster-resharding-online-rebalance-api "#redis-cluster-resharding-online-rebalance-api")

#### Online Shard Rebalancing (Console)

The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
cluster by rebalancing shards using the AWS Management Console.

###### To rebalance the keyspaces among the shards on your Valkey or Redis OSS (cluster mode enabled) cluster

1. Open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Valkey clusters** or **Redis OSS clusters**.
3. Choose the name, not the box to the left of the name, of the Valkey or Redis OSS (cluster mode enabled) cluster
   that you want to rebalance.

###### Tip

Valkey or Redis OSS (cluster mode enabled) clusters have a value of 1 or greater in the
**Shards** column. 4. Choose **Rebalance**. 5. When prompted, choose **Rebalance**. You might see a message similar
to this one: `Slots in the replication group are
 uniformly distributed. Nothing to do. (Service:
 AmazonElastiCache; Status Code: 400; Error Code:
 InvalidReplicationGroupState; Request ID:
 2246cebd-9721-11e7-8d5b-e1b0f086c8cf)`. If you do,
choose **Cancel**.

#### Online shard rebalancing (AWS CLI)

Use the following parameters with `modify-replication-group-shard-configuration`.

###### Parameters

- `-apply-immediately` –
  Required. Specifies the shard reconfiguration operation is
  to be started immediately.
- `--replication-group-id` –
  Required. Specifies which replication group (cluster)
  the shard reconfiguration operation is to be performed on.
- `--node-group-count` –
  Required. To rebalance the keyspaces across all shards in the cluster,
  this value must be the same as the current number of shards.

The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
cluster by rebalancing shards using the AWS CLI.

###### Example- Rebalancing the Shards in a Cluster

The following example rebalances the slots in the Valkey or Redis OSS (cluster mode enabled) cluster `my-cluster`
so that the slots are distributed as equally as possible.
The value of `--node-group-count` (`4`) is the number of
shards currently in the cluster.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group-shard-configuration \
    --replication-group-id `my-cluster` \
    --node-group-count `4` \
    --apply-immediately
```

For Windows:

```
aws elasticache modify-replication-group-shard-configuration ^
    --replication-group-id `my-cluster` ^
    --node-group-count `4` ^
    --apply-immediately
```

#### Online shard rebalancing (ElastiCache API)

You can use the ElastiCache API to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled) cluster
online by using the `ModifyReplicationGroupShardConfiguration` operation.

Use the following parameters with `ModifyReplicationGroupShardConfiguration`.

###### Parameters

- `ApplyImmediately=true` –
  Required. Specifies the shard reconfiguration operation is
  to be started immediately.
- `ReplicationGroupId` –
  Required. Specifies which replication group (cluster)
  the shard reconfiguration operation is to be performed on.
- `NodeGroupCount` –
  Required. To rebalance the keyspaces across all shards in the cluster,
  this value must be the same as the current number of shards.

The following process describes how to reconfigure the shards in your Valkey or Redis OSS (cluster mode enabled)
cluster by rebalancing the shards using the ElastiCache API.

###### Example- Rebalancing a Cluster

The following example rebalances the slots in the Valkey or Redis OSS (cluster mode enabled) cluster `my-cluster`
so that the slots are distributed as equally as possible.
The value of `NodeGroupCount` (`4`) is the number of
shards currently in the cluster.

```
https://elasticache.us-east-2.amazonaws.com/
    ?Action=ModifyReplicationGroupShardConfiguration
    &ApplyImmediately=true
    &NodeGroupCount=`4`
    &ReplicationGroupId=`my-cluster`
    &Version=2015-02-02
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20171002T192317Z
    &X-Amz-Credential=<credential>
```
