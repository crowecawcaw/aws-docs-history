

# Changing durability on an existing cluster
<a name="Durability.ChangingDurability"></a>

You can switch an existing ElastiCache for Valkey cluster between the `sync`, `async`, and `disabled` durability modes without recreating it. ElastiCache applies the change to the live cluster while it continues to serve traffic. For information about tracking the change, see [Monitor the durability change](#Durability.ChangingDurability.Monitor).

You can change the durability mode by using the AWS Management Console, the AWS CLI, or an AWS SDK. The following sections describe the console and AWS CLI methods. In the AWS CLI, you use `ModifyReplicationGroup` with the `--durability` parameter. In the ElastiCache API, the corresponding request member is `Durability`.

Before you change durability on an existing cluster, make sure that your cluster meets the following requirements:
+ The cluster runs Valkey 9.0 or later.
+ Multi-AZ is enabled with at least one replica per shard.
+ The cluster has encryption in transit (TLS) enabled.
+ The cluster uses Cluster Mode Enabled (CME).
+ The cluster is not an ElastiCache Serverless cache.
+ The cluster is not part of a Global Datastore.

When a cluster uses the `sync` or `async` mode, ElastiCache automatically enables encryption at rest on the cluster. For more information, see [Configuring durability](Durability.Configuring.md).

For the complete list of durability requirements and limitations, see [Limitations](Durability.Limitations.md).

Change the durability mode as a standalone modification. ElastiCache rejects a `ModifyReplicationGroup` request that changes durability together with any other modification.

**Considerations**  
Changing the durability mode involves node replacement. For each shard, this causes a brief primary node change or an automatic failover. Clients can experience transient connection interruptions during this process. Clients might also need to refresh their view of the cluster topology. Configure your clients to reconnect and to retry write operations with exponential backoff. For guidance, see [Best practices: Valkey/Redis OSS clients and Amazon ElastiCache](https://aws.amazon.com/blogs/database/best-practices-valkey-redis-oss-clients-and-amazon-elasticache/).  
We recommend changing the durability mode during a planned operational window.

## Using the AWS Management Console
<a name="Durability.ChangingDurability.Console"></a>

You can change the durability mode for an existing cluster from the ElastiCache console. On the cluster's **Modify** page (**Update cluster**), change the durability setting and save your changes.

## Using the AWS CLI
<a name="Durability.ChangingDurability.CLI"></a>

To change the durability mode, set the `--durability` parameter to `sync`, `async`, or `disabled`. Use `sync` when your application cannot tolerate any data loss. Use `async` when your application prioritizes write performance. With `async`, you can lose up to 10 seconds of acknowledged writes during a failure. If your application cannot tolerate that loss, use `sync` instead.

### Set the sync or async mode
<a name="Durability.ChangingDurability.SyncAsync"></a>

The following AWS CLI command sets synchronous writes:

```
aws elasticache modify-replication-group \
  --replication-group-id my-valkey-cluster \
  --durability sync \
  --region us-east-1
```

To use asynchronous writes, set `--durability` to `async`.

When a cluster changes from `disabled` to `sync` or `async`, ElastiCache automatically enables encryption at rest, including snapshots and data in the Multi-AZ transactional log. If the cluster already uses a customer managed AWS KMS key, ElastiCache retains that key. If the cluster was not previously encrypted, you don't need to specify a KMS key in this request. Changing the durability mode to `disabled` later does not disable encryption at rest.

### Set the disabled mode
<a name="Durability.ChangingDurability.Disabled"></a>

If your workload no longer requires Multi-AZ transactional-log protection, you can set durability to `disabled`.

**Data-loss risk when you set the disabled mode**  
Setting durability to `disabled` removes the Multi-AZ transactional-log durability guarantee. It increases the risk of losing acknowledged writes during a failure. Make sure you understand this recovery and data-loss tradeoff before you proceed.

The following AWS CLI command sets the disabled mode:

```
aws elasticache modify-replication-group \
  --replication-group-id my-durable-cluster \
  --durability disabled \
  --region us-east-1
```

## Monitor the durability change
<a name="Durability.ChangingDurability.Monitor"></a>

The following AWS CLI command checks the status of a durability change:

```
aws elasticache describe-replication-groups \
  --replication-group-id my-durable-cluster \
  --query "ReplicationGroups[0].{Id:ReplicationGroupId,Status:Status,Durability:Durability,EffectiveDurability:EffectiveDurability}" \
  --region us-east-1
```

To block until the change finishes, use the `replication-group-available` waiter. The waiter polls until the cluster `Status` is `available`, which means the modification finished running.

```
aws elasticache wait replication-group-available \
  --replication-group-id my-durable-cluster \
  --region us-east-1
```

A status of `available` does not by itself confirm that the change succeeded, because a failed change can roll back. After the cluster is available, confirm that `EffectiveDurability` matches the durability mode you requested. If it does not match, the change might have rolled back; check the cluster's ElastiCache events for the reason. A requested `Durability` value of `default` can legitimately resolve to a different `EffectiveDurability` value.

For information about the CloudWatch metrics available for durable clusters, including `DurabilityLag` and `DurabilityBufferExceededErrorCount`, see [Monitoring](Durability.Monitoring.md).