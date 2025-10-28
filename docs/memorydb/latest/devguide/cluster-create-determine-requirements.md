# Determining your requirements

###### Preparation

Knowing the answers to the following questions helps make creating your cluster go
smoother:

- Make sure to create a subnet group
  in the same VPC before you start creating a cluster. Alternatively, you can use the default subnet group provided.
  For more information, see [Subnets and subnet groups](subnetgroups.md "subnetgroups.md").

MemoryDB is designed to be accessed from within AWS using Amazon EC2. However, if you launch in
a VPC based on Amazon VPC, you can provide
access from outside AWS. For more information, see [Accessing MemoryDB resources from outside AWS](accessing-memorydb.md#access-from-outside-aws "accessing-memorydb.md#access-from-outside-aws").

- Do you need to customize any parameter values?

If you do, create a custom parameter group. For more information, see [Creating a parameter group](parametergroups.md "parametergroups.md").

- Do you need to create a VPC
  security group?

For more information, see [Security in Your VPC](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md").

- How do you intend to implement fault tolerance?

For more information, see [Mitigating Failures](faulttolerance.md "faulttolerance.md").

###### Topics

- [Memory and processor requirements](#cluster-create-determine-requirements-memory "#cluster-create-determine-requirements-memory")
- [MemoryDB cluster configuration](#cluster-configuration "#cluster-configuration")
- [Enhanced I/O Multiplexing](#cluster-create-determine-requirements-multiplexing "#cluster-create-determine-requirements-multiplexing")
- [Scaling requirements](#cluster-create-determine-requirements-scaling "#cluster-create-determine-requirements-scaling")
- [Access requirements](#cluster-create-determine-requirements-access "#cluster-create-determine-requirements-access")
- [Region and Availability Zones](#cluster-create-determine-requirements-region "#cluster-create-determine-requirements-region")

## Memory and processor requirements

The basic building block of MemoryDB is the node.
Nodes are configured in shards to form clusters.
When determining the node type to use for your cluster, take the cluster’s node configuration and
the amount of data you have to store into consideration.

## MemoryDB cluster configuration

MemoryDB clusters are comprised of from 1 to 500 shards.
The data in a MemoryDB cluster is partitioned across the shards in the cluster.
Your application connects with a MemoryDB cluster using a network address called an Endpoint.

In addition to the node endpoints, the MemoryDB cluster itself has an endpoint called the _cluster endpoint_.
Your application can use this endpoint to read from or write to the cluster, leaving the determination of which node to read from or write
to up to MemoryDB.

## Enhanced I/O Multiplexing

If you are running Valkey or Redis OSS version 7.0 or higher, you will get additional acceleration with enhanced I/O multiplexing, where each
dedicated network IO thread pipelines commands from multiple clients into the engine, taking advantage of the ability to
efficiently process commands in batches. For more information, see [Ultra-fast performance](https://aws.amazon.com/memorydb/features/#Ultra-fast_performance "https://aws.amazon.com/memorydb/features/#Ultra-fast_performance") and
[Supported node types](nodes.md "nodes.md").

## Scaling requirements

All clusters can be scaled up a larger node type.
When you scale
up a MemoryDB cluster, you can do it online so the cluster remains available or you can seed a new cluster from a snapshot and avoid having the new
cluster start out empty.

For more information, see [Scaling](scaling.md "scaling.md") in this guide.

## Access requirements

By design, MemoryDB clusters are accessed from Amazon EC2 instances. Network access to a MemoryDB cluster is
limited to the account that created the cluster. Therefore, before you can access a
cluster from an Amazon EC2 instance, you must authorize ingress to the cluster.
For
detailed instructions, see [Step 3: Authorize access to the cluster](getting-started.md#getting-started.authorizeaccess "getting-started.md#getting-started.authorizeaccess") in this guide.

## Region and Availability Zones

By locating your MemoryDB clusters in an AWS Region
close to your application you can reduce latency. If your cluster has multiple
nodes, locating your nodes in different Availability Zones can reduce the impact
of failures on your cluster.

For more information, see the following:

- [Choosing Regions and Availability Zones](regionsandazs.md "regionsandazs.md")
- [Mitigating Failures](faulttolerance.md "faulttolerance.md")
