# Determining your ElastiCache cluster requirements

###### Preparation

Knowing the answers to the following questions helps make creating your ElastiCache cluster go
smoother:

- Which node instance type do you need?

For guidance on choosing an instance node type, see [Choosing your node size](CacheNodes.md "CacheNodes.md").

- Will you launch your cluster in a virtual private cloud (VPC) based on Amazon VPC?

###### Important

If you're going to launch your cluster in a VPC, make sure to create a subnet group
in the same VPC before you start creating a cluster.
For more information, see [Subnets and subnet groups](SubnetGroups.md "SubnetGroups.md").

ElastiCache is designed to be accessed from within AWS using Amazon EC2. However, if you launch in
a VPC based on Amazon VPC and your cluster is in an VPC, you can provide
access from outside AWS. For more information, see [Accessing ElastiCache resources from outside AWS](accessing-elasticache.md#access-from-outside-aws "accessing-elasticache.md#access-from-outside-aws").

- Do you need to customize any parameter values?

If you do, create a custom parameter group. For more information, see [Creating an ElastiCache parameter group](ParameterGroups.md "ParameterGroups.md").

If you're running Valkey or Redis OSS, consider setting `reserved-memory`
or `reserved-memory-percent`. For more information, see [Managing reserved memory for Valkey and Redis OSS](redis-memory-management.md "redis-memory-management.md").

- Do you need to create your own _VPC
  security group_?

For more information, see [Security in Your VPC](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md").

- How do you intend to implement fault tolerance?

For more information, see [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance").

###### Topics

- [ElastiCache memory and processor requirements](#cluster-create-determine-requirements-memory "#cluster-create-determine-requirements-memory")
- [Memcached cluster configuration](#memcached-cluster-configuration "#memcached-cluster-configuration")
- [Valkey and Redis OSS cluster configuration](#redis-cluster-configuration "#redis-cluster-configuration")
- [ElastiCache scaling requirements](#cluster-create-determine-requirements-scaling "#cluster-create-determine-requirements-scaling")
- [ElastiCache access requirements](#cluster-create-determine-requirements-access "#cluster-create-determine-requirements-access")
- [Region, Availability Zone and Local Zone requirements for ElastiCache](#cluster-create-determine-requirements-region "#cluster-create-determine-requirements-region")

## ElastiCache memory and processor requirements

The basic building block of Amazon ElastiCache is the node.
Nodes are configured singularly or in groupings to form clusters.
When determining the node type to use for your cluster, take the cluster’s node configuration and
the amount of data you have to store into consideration.

The Memcached engine is multi-threaded, so a node’s number of cores impacts the
compute power available to the cluster.

## Memcached cluster configuration

ElastiCache for Memcached clusters are comprised of from 1 to 60 nodes.
The data in a Memcached cluster is partitioned across the nodes in the cluster.
Your application connects with a Memcached cluster using a network address called an Endpoint.
Each node in a Memcached cluster has its own endpoint which your application uses to read from or write to the specific node.
In addition to the node endpoints, the Memcached cluster itself has an endpoint called the _configuration endpoint_.
Your application can use this endpoint to read from or write to the cluster, leaving the determination of which node to read from or write
to up to auto discovery.

![Image showing how a Memcached cluster is partitioned across the nodes in the cluster.](images/ElastiCache-Cluster-Memcached.png)

For more information, see [Managing clusters in ElastiCache](Clusters.md "Clusters.md").

## Valkey and Redis OSS cluster configuration

ElastiCache for Valkey and Redis OSS clusters are comprised of from 0 to 500 shards (also called node groups).
The data in a Valkey or Redis OSS cluster is partitioned across the shards in the cluster.
Your application connects with a Valkey or Redis OSS cluster using a network address called an Endpoint.
The nodes in a Valkey or Redis OSS shard fulfill one of two roles: one read/write primary and all other nodes read-only
secondaries (also called read replicas).
In addition to the node endpoints, the Valkey or Redis OSS cluster itself has an endpoint called the _configuration endpoint_.
Your application can use this endpoint to read from or write to the cluster, leaving the determination of which node to read from or write
to up to ElastiCache for Redis OSS.

![Image comparing a Valkey or Redis OSS cluster in disabled mode vs. enabled mode.](images/ElastiCacheClusters-Redis-ClustersRGs.png)

For more information, see [Managing clusters in ElastiCache](Clusters.md "Clusters.md").

## ElastiCache scaling requirements

All clusters can be scaled up by creating a new cluster with the new, larger node type.
When you scale up a Memcached cluster, the new cluster starts out empty.
When you scale
up a Valkey or Redis OSS cluster, you can seed it from a backup and avoid having the new cluster start out empty.

Amazon ElastiCache for Memcached clusters can be scaled out or in.
To scale a Memcached cluster out or in you merely add or remove nodes from the cluster.
If you have enabled Automatic Discovery and your application is connecting to the cluster’s
configuration endpoint, you do not need to make any changes in your application when you
add or remove nodes.

For more information, see [Scaling ElastiCache](Scaling.md "Scaling.md") in this guide.

## ElastiCache access requirements

By design, Amazon ElastiCache clusters are accessed from Amazon EC2 instances. Network access to an ElastiCache cluster is
limited to the account that created the cluster. Therefore, before you can access a
cluster from an Amazon EC2 instance, you must authorize the Amazon EC2 instance to access the cluster.
The steps to do this vary, depending upon whether you launched into EC2-VPC or
EC2-Classic.

If you launched your cluster into EC2-VPC you need to grant network ingress to the cluster.
If you launched your cluster into EC2-Classic you need to grant the Amazon Elastic Compute Cloud
security group associated with the instance access to your ElastiCache security group. For
detailed instructions, see [Step 3. Authorize access to the cluster](SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey "SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey") in this guide.

## Region, Availability Zone and Local Zone requirements for ElastiCache

Amazon ElastiCache supports all AWS regions. By locating your ElastiCache clusters in an AWS Region
close to your application you can reduce latency. If your cluster has multiple
nodes, locating your nodes in different Availability Zones or in Local Zones can reduce the impact
of failures on your cluster.

For more information, see the following:

- [Choosing regions and availability zones for ElastiCache](RegionsAndAZs.md "RegionsAndAZs.md")
- [Using local zones with ElastiCache](Local_zones.md "Local_zones.md")
- [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance")
