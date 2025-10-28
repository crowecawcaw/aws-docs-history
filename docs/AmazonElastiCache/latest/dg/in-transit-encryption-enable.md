# Enabling in-transit encryption

All serverless caches have in-transit encryption enabled. On a node-based cluster, you can enable in-transit encryption using the AWS Management Console, the AWS CLI, or the ElastiCache
API.

## Enabling in-transit

encryption using the AWS Management Console

When designing your own cluster, 'Dev/Test' and 'Production' configurations
with the 'Easy create' method have in-transit encryption enabled. When choosing
configuration yourself, make the following selections:

- Choose engine version 3.2.6, 4.0.10 or later.
- Click the checkbox next to **Enable** for the **Encryption
  in transit** option.
  For the step-by-step process, see the following:

- [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs "SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs")
- [Creating a Valkey or Redis OSS (cluster mode enabled) cluster (Console)](Clusters.md#Clusters.Create.CON.RedisCluster "Clusters.md#Clusters.Create.CON.RedisCluster")

Enabling encryption in transit, is a two-step process, you must first set the transit encryption mode to `preferred`. This mode allows your Valkey or Redis OSS clients to connect using both encrypted and
unencrypted connections. After you migrate all your Valkey or Redis OSS clients to use encrypted connections, you can then modify your cluster configuration to set the transit encryption mode to `required`.
Setting the transit encryption mode to `required` will drop all unencrypted connections and will allow encrypted connections only.

###### Set your **Transit encryption mode** to

**Preferred**

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. Choose **Valkey caches** or **Redis OSS caches** from the ElastiCache
   **Resources** listed on the navigation pane,
   present on the left hand.
3. Choose the cache you want to
   update.
4. Choose the **Actions** dropdown, then choose
   **Modify**.
5. Choose **Enable** under **Encryption in
   transit** in the **Security**
   section.
6. Choose **Preferred** as the **Transit
   encryption mode**.
7. Choose **Preview changes** and save your
   changes.
   After you migrate all your Valkey or Redis OSS clients to use encrypted
   connections:

###### Set your **Transit encryption mode** to

**Required**

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. Choose **Valkey caches** or **Redis OSS caches** from the ElastiCache
   **Resources** listed on the navigation pane,
   present on the left hand.
3. Choose the cache you want to
   update.
4. Choose the **Actions** dropdown, then choose
   **Modify**.
5. Choose **Required** as the **Transit
   encryption mode**, in the **Security**
   section.
6. Choose **Preview changes** and save your
   changes.

## Enabling in-transit

encryption using the AWS CLI

To enable in-transit encryption when creating a Valkey or Redis OSS replication group using the
AWS CLI, use the parameter `transit-encryption-enabled`.

Use the AWS CLI operation `create-replication-group` and the
following parameters to create a Valkey or Redis OSS replication group with replicas that
has in-transit encryption enabled:

###### Key parameters:

- `--engine`—Must be `valkey` or
  `redis`.
- `--engine-version`—If the engine is Redis OSS, this must be 3.2.6,
  4.0.10 or later.
- `--transit-encryption-enabled`—Required.
  If you enable in-transit encryption, you must also provide a value
  for the `--cache-subnet-group` parameter.
- `--num-cache-clusters`—Must be at
  least 1. The maximum value for this parameter is
  six.
  For more information, see the following:

- [Creating a Valkey or Redis OSS (Cluster Mode Disabled) replication group from scratch (AWS CLI)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Classic.CLI "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Classic.CLI")
- [create-replication-group](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md")

Use the AWS CLI operation `create-replication-group` and the
following parameters to create a Valkey or Redis OSS (cluster mode enabled) replication group that has
in-transit encryption enabled:

###### Key parameters:

- `--engine`—Must be `valkey` or
  `redis`.
- `--engine-version`—If the engine is Redis OSS, this must be 3.2.6,
  4.0.10 or later.
- `--transit-encryption-enabled`—Required.
  If you enable in-transit encryption you must also provide a value
  for the `--cache-subnet-group` parameter.
- Use one of the following parameter sets to specify the
  configuration of the replication group's node groups:

      + `--num-node-groups`—Specifies
       the number of shards (node groups) in this replication
       group. The maximum value of this parameter is
       500.


      `--replicas-per-node-group`—Specifies
       the number of replica nodes in each node group. The value
       specified here is applied to all shards in this replication
       group. The maximum value of this parameter is
       5.
      + `--node-group-configuration`—Specifies
       the configuration of each shard independently.

  For more information, see the following:

- [Creating a Valkey or Redis OSS (Cluster Mode Enabled) replication group from scratch (AWS CLI)](Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CLI "Replication.CreatingReplGroup.NoExistingCluster.md#Replication.CreatingReplGroup.NoExistingCluster.Cluster.CLI")
- [create-replication-group](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md")

Enabling encryption in transit, is a two-step process, you must first set the transit encryption mode to `preferred`. This mode allows your Valkey or Redis OSS clients to connect using both encrypted and
unencrypted connections. After you migrate all your Valkey or Redis OSS clients to use encrypted connections, you can then modify your cluster configuration to set the transit encryption mode to `required`.
Setting the transit encryption mode to `required` will drop all unencrypted connections and will allow encrypted connections only.

Use the AWS CLI operation `modify-replication-group` and the
following parameters to update a Valkey or Redis OSS (cluster mode enabled) replication group that has
in-transit encryption disabled.

###### To enable in-transit encryption

1. Set transit-encryption-mode to `preferred`, using the
   following parameters
   - `--transit-encryption-enabled`—Required.
   - `--transit-encryption-mode`—Must
     be set to `preferred`.

2. Set transit-encryption-mode to `required`, using the
   following parameters:
   - `--transit-encryption-enabled`—Required.
   - `--transit-encryption-mode`—Must
     be set to `required`.
