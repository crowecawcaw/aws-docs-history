# Modifying a replication group

###### Important Constraints

- Currently, ElastiCache supports limited modifications of a Valkey or Redis OSS (cluster mode enabled) replication group,
  for example changing the engine version, using the API operation `ModifyReplicationGroup`
  (CLI: `modify-replication-group`). You can modify the number of shards (node groups) in
  a Valkey or Redis OSS (cluster mode enabled) cluster with the API operation [`ModifyReplicationGroupShardConfiguration`](../APIReference/API_ModifyReplicationGroupShardConfiguration.md "../APIReference/API_ModifyReplicationGroupShardConfiguration.md")
  (CLI: [`modify-replication-group-shard-configuration`](../../../cli/latest/reference/elasticache/modify-replication-group-shard-configuration.md "../../../cli/latest/reference/elasticache/modify-replication-group-shard-configuration.md")).
  For more information, see [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md "scaling-redis-cluster-mode-enabled.md").

Other modifications to a Valkey or Redis OSS (cluster mode enabled) cluster require that you create a cluster
with the new cluster incorporating the changes.

- You can upgrade Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled) clusters and replication groups
  to newer engine versions. However, you can't downgrade to earlier engine versions except by deleting
  the existing cluster or replication group and creating it again. For more information, see [Version Management for ElastiCache](VersionManagement.md "VersionManagement.md").
- You can upgrade an existing ElastiCache for Valkey or Redis OSS cluster that uses cluster mode disabled to use cluster mode enabled, using the console, [ModifyReplicationGroup](../APIReference/API_ModifyReplicationGroup.md "../APIReference/API_ModifyReplicationGroup.md") API or the
  [modify-replication-group](../../../cli/latest/reference/elasticache/modify-replication-group.md "../../../cli/latest/reference/elasticache/modify-replication-group.md") CLI command, as shown in the example below. Or you can follow the
  steps at [Modifying cluster mode](modify-cluster-mode.md "modify-cluster-mode.md").
  You can modify a Valkey or Redis OSS (cluster mode disabled) cluster's settings using the ElastiCache console, the AWS CLI, or the ElastiCache API.
  Currently, ElastiCache supports a limited number of modifications on a Valkey or Redis OSS (cluster mode enabled) replication group. Other
  modifications require you create a backup of the current replication group then using that backup to seed a new
  Valkey or Redis OSS (cluster mode enabled) replication group.

###### Topics

- [Using the AWS Management Console](#Replication.Modify.CON "#Replication.Modify.CON")
- [Using the AWS CLI](#Replication.Modify.CLI "#Replication.Modify.CLI")
- [Using the ElastiCache API](#Replication.Modify.API "#Replication.Modify.API")

## Using the AWS Management Console

To modify a Valkey or Redis OSS (cluster mode disabled) cluster,
see [Modifying an ElastiCache cluster](Clusters.md "Clusters.md").

## Using the AWS CLI

The following are AWS CLI examples of the `modify-replication-group` command. You can use the same command to make other modifications to a replication group.

**Enable Multi-AZ on an existing Valkey or Redis OSS replication group:**

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
   --replication-group-id `myReplGroup` \
   --multi-az-enabled = true
```

For Windows:

```
aws elasticache modify-replication-group ^
   --replication-group-id `myReplGroup` ^
   --multi-az-enabled
```

**Modify cluster mode from disabled to enabled:**

To modify cluster mode from _disabled_ to _enabled_, you must first set the cluster mode to _compatible_. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode
configuration and set the cluster mode to _enabled_.

For Linux, macOS, or Unix:

Set to cluster mode to _compatible_.

```
aws elasticache modify-replication-group \
   --replication-group-id `myReplGroup` \
   --cache-parameter-group-name `myParameterGroupName` \
   --cluster-mode compatible
```

Set to cluster mode to _enabled_.

```
aws elasticache modify-replication-group \
   --replication-group-id `myReplGroup` \
   --cluster-mode enabled
```

For Windows:

Set to cluster mode to _compatible_.

```
aws elasticache modify-replication-group ^
   --replication-group-id `myReplGroup` ^
   --cache-parameter-group-name `myParameterGroupName` ^
   --cluster-mode compatible
```

Set to cluster mode to _enabled_.

```
aws elasticache modify-replication-group ^
   --replication-group-id `myReplGroup` ^
   --cluster-mode enabled
```

For more information on the AWS CLI `modify-replication-group` command,
see modify-replication-group or Modifying cluster mode in the _ElastiCache for Redis OSS User Guide_.

## Using the ElastiCache API

The following ElastiCache API operation enables Multi-AZ on an existing Valkey or Redis OSS replication group.
You can use the same operation to make other modifications to a replication group.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=ModifyReplicationGroup
   &AutomaticFailoverEnabled=true
   &Mutli-AZEnabled=true
   &ReplicationGroupId=myReplGroup
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20141201T220302Z
   &Version=2014-12-01
   &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
   &X-Amz-Date=20141201T220302Z
   &X-Amz-SignedHeaders=Host
   &X-Amz-Expires=20141201T220302Z
   &X-Amz-Credential=<credential>
   &X-Amz-Signature=<signature>
```

For more information on the ElastiCache API `ModifyReplicationGroup` operation,
see ModifyReplicationGroup.
