

# Upgrading engine versions including cross engine upgrades
<a name="VersionManagement.HowTo"></a>

**Valkey and Redis OSS**

With Valkey and Redis OSS, you initiate version upgrades to your cluster or replication group by modifying it using the ElastiCache console, the AWS CLI, or the ElastiCache API and specifying a newer engine version. 

You can also cross upgrade from Redis OSS to Valkey. For more information on cross upgrades, see [How to upgrade from Redis OSS to Valkey](#VersionManagement.HowTo.cross-engine-upgrade).

**Topics**
+ [How to modify clusters and replication groups](#modify-clusters-replication-groups)
+ [How to upgrade from Redis OSS to Valkey](#VersionManagement.HowTo.cross-engine-upgrade)
+ [Resolving blocked Valkey or Redis OSS engine upgrades](#resolving-blocked-engine-upgrades)

## How to modify clusters and replication groups
<a name="modify-clusters-replication-groups"></a>

**Valkey and Redis OSS**



| Caches | Replication groups | 
| --- | --- | 
| [Using the ElastiCache AWS Management Console](Clusters.Modify.md#Clusters.Modify.CON) | [Using the AWS Management Console](Replication.Modify.md#Replication.Modify.CON) | 
| [Using the AWS CLI with ElastiCache](Clusters.Modify.md#Clusters.Modify.CLI) | [Using the AWS CLI](Replication.Modify.md#Replication.Modify.CLI) | 
| [Using the ElastiCache API](Clusters.Modify.md#Clusters.Modify.API) | [Using the ElastiCache API](Replication.Modify.md#Replication.Modify.API) | 

**Memcached**

With Memcached, to start version upgrades to your cluster, you modify it and specify a newer engine version. You can do this by using the ElastiCache console, the AWS CLI, or the ElastiCache API:
+ To use the AWS Management Console, see – [Using the ElastiCache AWS Management Console](Clusters.Modify.md#Clusters.Modify.CON).
+ To use the AWS CLI, see [Using the AWS CLI with ElastiCache](Clusters.Modify.md#Clusters.Modify.CLI).
+ To use the ElastiCache API, see [Using the ElastiCache API](Clusters.Modify.md#Clusters.Modify.API).

## How to upgrade from Redis OSS to Valkey
<a name="VersionManagement.HowTo.cross-engine-upgrade"></a>

Valkey is designed as a drop-in replacement for Redis OSS 7. You can upgrade from Redis OSS to Valkey using the Console, API, or CLI, by specifying the new engine and major engine version. All aspects of your application, including the endpoint DNS name, will remain unchanged, except that for node-based clusters, the underlying node IP addresses will change during the upgrade. You will experience minimal downtime when upgrading from Redis OSS 5.0.6 or higher. The cluster is available for reads during the entire upgrade and is available for writes for most of the upgrade duration, except during the failover operation which lasts a few seconds. 

**Note**  
**AWS CLI version requirements for Redis OSS to Valkey upgrades:**  
For AWSCLI v1: Minimum required version 1.35.2 (Current version: 1.40.22)
For AWS CLI v2: Minimum required version 2.18.2 (Current version: 2.27.22)

**Note**  
When upgrading from earlier Redis OSS versions than 5.0.6, you may experience a failover time of 30 to 60 seconds during the DNS propagation.
To upgrade an existing Redis OSS (cluster mode disabled) single-node cluster to the Valkey engine, first follow these steps: [Creating a replication group using an existing cluster](Replication.CreatingReplGroup.ExistingCluster.md). Once the Redis OSS (cluster mode disabled) single-node cluster has been added to a replication group, you can cross-engine upgrade to Valkey.

### Upgrading a replication group from Redis OSS to Valkey
<a name="cross-engine-upgrades.replication-group"></a>

If you have an existing Redis OSS replication group that is using the default cache parameter group, you can upgrade to Valkey by specifying the new engine and engine version with modify-replication-group API.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
   --replication-group-id myReplGroup \
   --engine valkey \
   --engine-version 9.0
```

For Windows:

```
aws elasticache modify-replication-group ^
   --replication-group-id myReplGroup ^
   --engine valkey ^
   --engine-version 9.0
```

If you have a custom cache parameter group applied to the existing Redis OSS replication group you wish to upgrade, you will need to pass a custom Valkey cache parameter group in the request as well. The input Valkey custom parameter group must have the same Redis OSS static parameter values as the existing Redis OSS custom parameter group.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
   --replication-group-id myReplGroup \
   --engine valkey \
   --engine-version 9.0 \
   --cache-parameter-group-name myParamGroup
```

For Windows:

```
aws elasticache modify-replication-group ^
   --replication-group-id myReplGroup ^
   --engine valkey ^
   --engine-version 9.0 ^
   --cache-parameter-group-name myParamGroup
```

### Upgrading a Redis OSS serverless cache to Valkey with the CLI
<a name="cross-engine-upgrades.cli"></a>

For Linux, macOS, or Unix:

```
aws elasticache modify-serverless-cache \
   --serverless-cache-name myCluster \
   --engine valkey \
   --major-engine-version 9
```

For Windows:

```
aws elasticache modify-serverless-cache ^
   --serverless-cache-name myCluster ^
   --engine valkey ^
   --major-engine-version 9
```

### Upgrading Redis OSS to Valkey with the Console
<a name="cross-engine-upgrades.console"></a>

**Upgrading from Redis OSS 5 to Valkey**

1. Select the Redis OSS cache to upgrade.

1. An **Upgrade to Valkey** window should appear. Select the **Upgrade to Valkey** button.

1. Go to **Cache settings**, and then select **Engine version**. The most recent version of Valkey is recommended.

1. If this cache is serverless, then you will need to update the parameter group. Go to the **Parameter groups** area of **Cache settings**, select an appropriate parameter group such as *default.valkey8*.

1. Select **Upgrade**.

This cache will now be listed in the Valkey area of the console.

**Note**  
Upgrading directly from Redis OSS 4 or lower to Valkey may include a longer failover time of 30 to 60 seconds during the DNS propagation.

### How to downgrade from Valkey to Redis OSS
<a name="cross-engine-downgrades.console"></a>

 If for any reason you wish to rollback your upgraded cluster, Amazon ElastiCache supports rolling back a Valkey 7.2 cache to Redis OSS 7.1. You can perform a rollback using the same console, API, or CLI steps as an engine upgrade by specifying Redis OSS 7.1 as the target engine version. All aspects of your application, including the endpoint DNS name, will remain unchanged, except that for node-based clusters, the underlying node IP addresses will change during the rollback. You will experience minimal downtime while rolling back. The cluster is available for reads during the entire rollback and is available for writes for most of the rollback duration, except during the failover operation which lasts a few seconds. 

 Additionally, you can restore a snapshot created from your Valkey 7.2 cache as a Redis OSS 7.1 cache. When you restore from a snapshot, you can specify Redis OSS 7.1 as the target engine version. When using this option, a new cache will be created from the snapshot. Restoring from a snapshot has no effect on the Valkey cache that the snapshot was created from. 

 The following requirements and limitations apply when performing a rollback: 
+  ElastiCache only supports rolling back from Valkey 7.2 to Redis OSS 7.1. This is true even if you upgraded to Valkey 7.2 from an earlier version than Redis OSS 7.1. 
+  Any user group and user associated with the replication group or serverless cache being rolled back must be configured with engine type `REDIS`. 

## Resolving blocked Valkey or Redis OSS engine upgrades
<a name="resolving-blocked-engine-upgrades"></a>

As shown in the following table, your Valkey or Redis OSS engine upgrade operation is blocked if you have a pending scale up operation.




- **Scale up**
  - Immediate engine upgrade

- **Engine upgrade**
  - Immediate scale up

- **Scale up and engine upgrade**
  - Immediate scale up
  - Immediate engine upgrade



**To resolve a blocked Valkey or Redis OSS engine upgrade**
+ Do one of the following:
  + Schedule your Redis OSS or Valkey engine upgrade operation for the next maintenance window by clearing the **Apply immediately** check box. 

    With the CLI, use `--no-apply-immediately`. With the API, use `ApplyImmediately=false`.
  + Wait until your next maintenance window (or after) to perform your Redis OSS engine upgrade operation.
  + Add the Redis OSS scale up operation to this cluster modification with the **Apply Immediately** check box chosen. 

    With the CLI, use `--apply-immediately`. With the API, use `ApplyImmediately=true`. 

    This approach effectively cancels the engine upgrade during the next maintenance window by performing it immediately.