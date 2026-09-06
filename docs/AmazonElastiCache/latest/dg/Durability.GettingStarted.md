

# Getting started with durability
<a name="Durability.GettingStarted"></a>

You can create a durable ElastiCache cluster using the AWS Management Console or the AWS CLI.

## Using the AWS Management Console
<a name="Durability.GettingStarted.Console"></a>

To get started, create a new ElastiCache cluster with durability by selecting Valkey 9.0 or later in your desired AWS Region. After enabling durability, you can choose either synchronous or asynchronous options depending on your application requirements by using the AWS Console.

For more information on creating a cluster, see [Creating a cluster for Valkey or Redis OSS](Clusters.Create.md).

## Using the CLI
<a name="Durability.GettingStarted.CLI"></a>

To create a new durable cluster with synchronous writes:

```
aws elasticache create-replication-group \
  --replication-group-id my-durable-cluster \
  --replication-group-description "ElastiCache durable cluster" \
  --engine valkey --engine-version 9.0 \
  --num-node-groups 2 --replicas-per-node-group 1 \
  --cache-node-type cache.r7g.large \
  --multi-az-enabled \
  --transit-encryption-enabled \
  --durability sync \
  --region us-east-1
```

To create a cluster with asynchronous writes, set `--durability async`:

```
aws elasticache create-replication-group \
  --replication-group-id my-durable-cluster \
  --replication-group-description "ElastiCache durable cluster" \
  --engine valkey --engine-version 9.0 \
  --num-node-groups 2 --replicas-per-node-group 1 \
  --cache-node-type cache.r7g.large \
  --multi-az-enabled \
  --transit-encryption-enabled \
  --durability async \
  --region us-east-1
```

To switch an existing cluster between synchronous and asynchronous writes, use `modify-replication-group`:

```
aws elasticache modify-replication-group \
  --replication-group-id my-durable-cluster \
  --durability async
```