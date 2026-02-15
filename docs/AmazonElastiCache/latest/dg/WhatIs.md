# ElastiCache components and features

Following, you can find an overview of the major components of an
Amazon ElastiCache deployment.

###### Topics

- [ElastiCache nodes](#WhatIs.Components.Nodes "#WhatIs.Components.Nodes")
- [ElastiCache shards](#WhatIs.Components.Shards "#WhatIs.Components.Shards")
- [ElastiCache clusters](#WhatIs.Components.Clusters "#WhatIs.Components.Clusters")
- [ElastiCache replication](#WhatIs.Components.ReplicationGroups "#WhatIs.Components.ReplicationGroups")
- [ElastiCache endpoints](#WhatIs.Components.Endpoints "#WhatIs.Components.Endpoints")
- [ElastiCache parameter groups](#WhatIs.Components.ParameterGroups "#WhatIs.Components.ParameterGroups")
- [ElastiCache security](#WhatIs.Components.Security "#WhatIs.Components.Security")
- [ElastiCache subnet groups](#WhatIs.Components.SubnetGroups "#WhatIs.Components.SubnetGroups")
- [ElastiCache backups](#WhatIs.Components.Snapshots "#WhatIs.Components.Snapshots")
- [ElastiCache events](#WhatIs.Components.Events "#WhatIs.Components.Events")

## ElastiCache nodes

A _node_ is the smallest building block of an ElastiCache deployment.
A node can exist in isolation from or in some relationship to other nodes.

A node is a fixed-size chunk of secure, network-attached RAM.
Each node runs an instance of the engine and version that was chosen when
you created your cluster. If necessary, you can scale the nodes in a cluster up or down to a different instance
type. For more information, see [Scaling ElastiCache](Scaling.md "Scaling.md").

Every node within a cluster is the same instance type and runs the same cache engine.
Each cache node has its own Domain Name Service (DNS) name and port.
Multiple types of cache nodes are supported, each with varying amounts of associated memory.
For a list of supported node instance types, see [Supported node types](CacheNodes.md "CacheNodes.md").

You can purchase nodes on a pay-as-you-go basis, where you only pay for your use of a node.
Or you can purchase reserved nodes at a much-reduced hourly rate. If your usage rate
is high, purchasing reserved nodes can save you money. Suppose that your cluster is
almost always in use, and you occasionally add nodes to handle use spikes. In this
case, you can purchase a number of reserved nodes to run most of the time. You can
then purchase pay-as-you-go nodes for the times you occasionally need to add nodes.
For more information on reserved nodes, see [Reserved nodes](CacheNodes.md "CacheNodes.md").

For more information on nodes, see [Managing nodes in ElastiCache](CacheNodes.md "CacheNodes.md").

## ElastiCache shards

A Valkey or Redis OSS _shard_ (called a _node group_
in the API and CLI) is a grouping of one to six related
nodes. A Valkey or Redis OSS cluster with cluster mode enabled always has at least one shard.

Sharding is a method of database partitioning that separates large databases into smaller, faster,
and more easily managed parts called data shards. This can increase database efficiency by
distributing operations across multiple separate sections. Using shards can offer many benefits including
improved performance, scalability, and cost efficiency.

Valkey and Redis OSS clusters with cluster mode enabled can have up to 500 shards, with your data partitioned across the shards.
The node or shard limit can be increased to a maximum of 500 per cluster if the Valkey or Redis OSS engine version is 5.0.6 or higher.
For example, you can choose to configure a 500 node cluster that ranges between
83 shards (one primary and 5 replicas per shard) and 500 shards (single primary and no replicas). Make sure there are enough available IP addresses to accommodate the increase.
Common pitfalls include the subnets in the subnet group have too small a CIDR range or the subnets are shared and heavily used by other clusters. For more information, see
[Creating a subnet group](SubnetGroups.md "SubnetGroups.md"). For versions below 5.0.6,
the limit is 250 per cluster.

To request a limit increase, see
[AWS Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
and choose the limit type **Nodes per cluster per instance type**.

A _multiple node shard_ implements replication by having one
read/write primary node and 1–5 replica nodes. For more
information, see [High availability using replication groups](Replication.md "Replication.md").

For more information on shards, see [Working with shards in ElastiCache](Shards.md "Shards.md").

## ElastiCache clusters

A _cluster_ is a logical grouping of one or more [nodes](CacheNodes.md "CacheNodes.md").
Data is partitioned across the nodes in a Memcached cluster, and across the shards in a Valkey or Redis OSS cluster that has cluster mode enabled.

Many ElastiCache operations are targeted at clusters:

- Creating a cluster
- Modifying a cluster
- Taking snapshots of a cluster (all versions of Redis)
- Deleting a cluster
- Viewing the elements in a cluster
- Adding or removing cost allocation tags to and from a cluster

For more detailed information, see the following related topics:

- [Managing clusters in ElastiCache](Clusters.md "Clusters.md")
  and [Managing nodes in ElastiCache](CacheNodes.md "CacheNodes.md")

Information about clusters, nodes, and related operations.

- [AWS service limits: Amazon ElastiCache](../../../general/latest/gr/aws_service_limits.md#limits_elasticache "../../../general/latest/gr/aws_service_limits.md#limits_elasticache")

Information about ElastiCache limits, such as the maximum number of nodes or clusters. To
exceed certain of these limits, you can make a request using the [Amazon ElastiCache cache node request form](https://aws.amazon.com/contact-us/elasticache-node-limit-request/ "https://aws.amazon.com/contact-us/elasticache-node-limit-request/").

- [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance")

Information about improving the fault tolerance of your clusters and Valkey or Redis OSS replication groups.

### Typical cluster configurations

Following are typical cluster configurations.

#### Valkey or Redis OSS clusters

Valkey or Redis OSS clusters with cluster mode disabled always
contain just one shard (in the API and CLI, one node group). A Valkey or Redis OSS shard
contains one to six nodes. If there is more than
one node in a shard, the shard supports replication. In this case, one node
is the read/write primary node and the others are read-only replica
nodes.

For improved fault tolerance, we recommend having at least two nodes in a Valkey or Redis OSS cluster and enabling
Multi-AZ.
For more information, see [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance").

As demand upon your Valkey or Redis OSS cluster changes, you can scale up or down. To do this,
move your cluster to a different node instance type. If your application
is read intensive, we recommend adding read-only replicas to the
cluster. By doing this, you can spread the reads across a more appropriate
number of nodes.

You can also use data-tiering. More frequently accessed data is stored in memory and less frequently accessed data is stored on disk. The advantage of using data tiering is that it decreases memory needs. For
more information, see [Data tiering in ElastiCache](data-tiering.md "data-tiering.md").

ElastiCache supports changing a Valkey or Redis OSS cluster's node type to a larger node type dynamically.
For information on scaling up or down, see [Scaling for Valkey or Redis OSS (Cluster Mode Disabled) clusters](scaling-redis-classic.md#Scaling.RedisStandalone "scaling-redis-classic.md#Scaling.RedisStandalone")
or [Scaling replica nodes for Valkey or Redis OSS (Cluster Mode Disabled)](Scaling.md "Scaling.md").

#### Typical cluster configurations for Memcached

Memcached supports up to 300 nodes per customer for each AWS Region with
each cluster having 1–60 nodes. You partition
your data across the nodes in a Memcached cluster.

When you run the Memcached engine, clusters can be made up of 1–60 nodes.
You partition your database across the nodes.
Your application reads and writes to each node's endpoint. For more information, see

[Auto Discovery](AutoDiscovery.md "AutoDiscovery.md").

For improved fault tolerance, locate your Memcached nodes in various Availability Zones
(AZs) within the cluster's AWS Region. That way, a failure in one AZ has minimal
impact upon your entire cluster and application. For more information, see [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance").

As demand upon your Memcached cluster changes, you can scale out or in by adding or
removing nodes, which repartitions your data across the new number of nodes.
When you partition your data, we recommend using consistent hashing. For more
information about consistent hashing, see [Configuring your ElastiCache client for efficient load balancing (Memcached)](BestPractices.md "BestPractices.md").

## ElastiCache replication

For Valkey and Redis OSS, replication is implemented by grouping from two to six nodes in a
shard (in the API and CLI, called a node group). One of these nodes is the
read/write primary node. All the other nodes are read-only replica nodes.
Replications are only available for ElastiCache for Valkey and Redis OSS, and not for ElastiCache for Memcached.

Each replica node maintains a copy of the data from the primary node.
Replica nodes use asynchronous replication mechanisms to keep synchronized with the primary node.
Applications can read from any node in the cluster but can write only to primary nodes.
Read replicas enhance scalability by spreading reads across multiple endpoints.
Read replicas also improve fault tolerance by maintaining multiple copies of the data.
Locating read replicas in multiple Availability Zones further improves fault tolerance.
For more information on fault tolerance, see [Mitigating Failures](disaster-recovery-resiliency.md#FaultTolerance "disaster-recovery-resiliency.md#FaultTolerance").

Valkey or Redis OSS clusters support one shard (in the API and CLI, called a _node
group_).

Replication from the API and CLI perspective uses different terminology to maintain
compatibility with previous versions, but the results are the same. The following
table shows the API and CLI terms for implementing replication.

**Comparing Replication: Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled)--> Valkey or Redis OSS cluster with cluster mode enabled vs. Valkey or Redis OSS cluster with cluster mode disabled**

In the following table, you can find a comparison of the features of Valkey or Redis OSS (cluster mode disabled) and Valkey or Redis OSS (cluster mode enabled) replication groups.

|                                                                                                   | Valkey or Redis OSS cluster with cluster mode disabled | Valkey or Redis OSS cluster with cluster mode enabled |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- |
| Shards (node groups)                                                                              | 1                                                      | 1–500                                                 |
| Replicas for each shard (node group)                                                              | 0–5                                                    | 0–5                                                   |
| Data partitioning                                                                                 | No                                                     | Yes                                                   |
| Add/Delete replicas                                                                               | Yes                                                    | Yes                                                   |
| Add/Delete node groups                                                                            | No                                                     | Yes                                                   |
| Supports scale up                                                                                 | Yes                                                    | Yes                                                   |
| Supports engine upgrades                                                                          | Yes                                                    | Yes                                                   |
| Promote replica to primary                                                                        | Yes                                                    | Automatic                                             |
| Multi-AZ                                                                                          | Optional                                               | Required                                              |
| Backup/Restore                                                                                    | Yes                                                    | Yes                                                   |
| **Notes:**                                                                                        |
| If any primary has no replicas and the primary fails, you lose all that primary's data.           |
| You can use backup and restore to migrate to Valkey or Redis OSS (cluster mode enabled).          |
| You can use backup and restore to resize your Valkey or Redis OSS (cluster mode enabled) cluster. |

All of the shards (in the API and CLI, node groups) and nodes must reside in the same AWS
Region. However, you can provision the individual nodes in multiple Availability
Zones within that AWS Region.

Read replicas guard against potential data loss because your data is replicated over two or
more nodes—the primary and one or more read replicas. For greater reliability
and faster recovery, we recommend that you create one or more read replicas in
different Availability Zones.

You can also leverage Global datastores. By using the Global Datastore for Redis OSS feature, you can work with fully managed, fast, reliable, and secure
replication across AWS Regions. Using this feature, you can create cross-Region read replica clusters for ElastiCache to enable low-latency reads
and disaster recovery across AWS Regions. For more information,
see [Replication across AWS Regions using global datastores](Redis-Global-Datastore.md "Redis-Global-Datastore.md").

###### Replication: Limits and exclusions

- Multi-AZ is not supported on node types T1.

## ElastiCache endpoints

An _endpoint_ is the unique address your application uses
to connect to an ElastiCache node or cluster.

### Single node endpoints for Valkey or Redis OSS with cluster mode disabled

The endpoint for a single node Valkey or Redis OSS cluster is used to connect to the cluster
for both reads and writes.

### Multi-node endpoints for Valkey or Redis OSS with cluster mode disabled

A multiple node Valkey or Redis OSS cluster with cluster mode disabled has two types of endpoints.
The primary endpoint always connects to the primary node in the cluster,
even if the specific node in the primary role changes.
Use the primary endpoint for all writes to the cluster.

Use the Reader Endpoint to evenly split incoming connections to the endpoint between all read replicas. Use the individual Node Endpoints for read operations (In the API/CLI these are referred to as Read Endpoints).

### Valkey or Redis OSS (Cluster Mode Enabled) endpoints

A Valkey or Redis OSS cluster with cluster mode enabled has a single configuration endpoint. By connecting to the
configuration endpoint, your application is able to discover the primary and
read endpoints for each shard in the cluster.

For more information, see [Finding connection endpoints in ElastiCache](Endpoints.md "Endpoints.md").

### ElastiCache for Memcached endpoints

Each node in a Memcached cluster has its own endpoint.
The cluster also has an endpoint called the _configuration endpoint_.
If you enable Auto Discovery and connect to the configuration endpoint,
your application automatically _knows_ each node endpoint,
even after adding or removing nodes from the cluster.
For more information, see

[Auto Discovery](AutoDiscovery.md "AutoDiscovery.md").

For more information, see [Finding connection endpoints in ElastiCache](Endpoints.md "Endpoints.md").

## ElastiCache parameter groups

Cache parameter groups are an easy way to manage runtime settings for supported engine
software. Parameters are used to control memory usage, eviction policies, item
sizes, and more. An ElastiCache parameter group is a named collection of engine-specific
parameters that you can apply to a cluster. By doing this, you make sure that all of
the nodes in that cluster are configured in exactly the same way.

For a list of supported parameters, their default values, and which ones can be modified,
see DescribeEngineDefaultParameters
(CLI: describe-engine-default-parameters).

For more detailed information on ElastiCache parameter groups, see [Configuring engine parameters using ElastiCache parameter
groups](ParameterGroups.md "ParameterGroups.md").

## ElastiCache security

For enhanced security, ElastiCache node access is restricted to applications running on the
Amazon EC2 instances that you allow. You can control the Amazon EC2 instances that can access
your cluster using security groups.

By default, all new ElastiCache clusters are launched in an Amazon Virtual Private Cloud (Amazon VPC) environment. You
can use _subnet groups_ to grant cluster access from Amazon EC2
instances running on specific subnets.

In addition to restricting node access, ElastiCache supports TLS and in-place encryption for
nodes running specified versions of ElastiCache. For more information, see the
following:

- [Data security in Amazon ElastiCache](encryption.md "encryption.md")
- [Authenticating with the Valkey and Redis OSS AUTH command](auth.md "auth.md")

## ElastiCache subnet groups

A _subnet group_ is a collection of subnets (typically
private) that you can designate for your clusters running in an Amazon VPC
environment.

If you create a cluster in an Amazon VPC, then you must specify a cache subnet group.
ElastiCache uses that cache subnet group to choose a subnet and IP addresses within that subnet to
associate with your cache nodes.

For more information about cache subnet group usage in an Amazon VPC environment, see the
following:

- [Amazon VPCs and ElastiCache security](VPCs.md "VPCs.md")
- [Step 3. Authorize access to the cluster](SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey "SubnetGroups.designing-cluster-pre.md#GettingStarted.AuthorizeAccess.valkey")
- [Subnets and subnet groups](SubnetGroups.md "SubnetGroups.md")

## ElastiCache backups

A _backup_ is a point-in-time copy of a Valkey or Redis OSS cluster or serverless cache, or
a Memcached serverless cache.
Backups can be used to restore an existing cluster or to seed a new cluster. Backups
consist of all the data in a cluster plus some metadata.

Depending upon the version of Valkey or Redis OSS running on your cluster, the backup process requires
differing amounts of reserved memory to succeed. For more information, see the
following:

- [Snapshot and restore](backups.md "backups.md")
- [How synchronization and backup are implemented](Replication.Redis.md "Replication.Redis.md")
- [Performance impact of backups of node-based clusters](backups.md#backups-performance "backups.md#backups-performance")
- [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.md "BestPractices.md")

## ElastiCache events

When important events happen on a cluster, ElastiCache sends notification to a specific
Amazon SNS topic. These events can include such things as failure or success in adding a
node, a security group modification, and others. By monitoring for key events, you
can know the current state of your clusters and in many cases take corrective
action.

For more information on ElastiCache events, see [Amazon SNS monitoring of ElastiCache events](ECEvents.md "ECEvents.md").
