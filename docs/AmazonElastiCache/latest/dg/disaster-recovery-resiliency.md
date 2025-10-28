# Resilience in Amazon ElastiCache

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon ElastiCache offers several features to help support your data resiliency and backup needs.

###### Topics

- [Mitigating Failures](#FaultTolerance "#FaultTolerance")

## Mitigating Failures

When planning your Amazon ElastiCache implementation,
you should plan so that failures have a minimal impact upon your application and data.
The topics in this section cover approaches you can take to protect your application and data from failures.

###### Topics

- [Mitigating Failures when Running Memcached](#FaultTolerance.Memcached "#FaultTolerance.Memcached")
- [Mitigating Failures when Running Valkey or Redis OSS](#FaultTolerance.Redis "#FaultTolerance.Redis")
- [Recommendations](#FaultTolerance.Recommendations "#FaultTolerance.Recommendations")

### Mitigating Failures when Running Memcached

When running the Memcached engine,
you have the following options for minimizing the impact of a failure.
There are two types of failures to address in your failure mitigation plans:
node failure and Availability Zone failure.

#### Mitigating Node Failures

Serverless caches automatically mitigate node failures with a replicated Multi-AZ architecture so that node failures are transparent to your application.
To mitigate the impact of a node failure in a node-based cluster, spread your cached data over more nodes.
Because node-based clusters do not support replication, a node failure will always result in
some data loss from your cluster.

When you create your Memcached cluster you can create it with 1 to 60 nodes,
or more by special request.
Partitioning your data across a greater number of nodes means you'll lose less data if
a node fails.
For example, if you partition your data across 10 nodes,
any single node stores approximately 10% of your cached data.
In this case, a node failure loses approximately 10% of your cache which needs to be replaced
when a replacement node is created and provisioned.
If the same data were cached in 3 larger nodes,
the failure of a node would lose approximately 33% of your cached data.

For information on specifying the number of nodes in a Memcached cluster, see [Creating a Memcached cluster (console)](Clusters.md#Clusters.Create.CON.Memcached "Clusters.md#Clusters.Create.CON.Memcached").

#### Mitigating Availability Zone Failures

Serverless caches automatically mitigate availability zone failures with a replicated Multi-AZ architecture so that AZ failures are transparent to your application.

To mitigate the impact of an Availability Zone failure in a node-based cluster, locate your nodes in as many
Availability Zones as possible. In the unlikely event of an AZ failure, you will
lose the data cached in that AZ, not the data cached in the other AZs.

###### Why so many nodes?

_If my region has only 3 Availability Zones,
why do I need more than 3 nodes since if an AZ fails I lose approximately one-third of my data?_

This is an excellent question.
Remember that we’re attempting to mitigate two distinct types of failures,
node and Availability Zone.
You’re right, if your data is spread across Availability Zones and one of the zones fails,
you will lose only the data cached in that AZ,
irrespective of the number of nodes you have.
However, if a node fails, having more nodes will reduce the proportion of data lost.

There is no "magic formula" for determining how many nodes to have in your cluster.
You must weight the impact of data loss vs. the likelihood of a failure vs. cost, and come to your own
conclusion.

For information on specifying the number of nodes in a Memcached cluster, see [Creating a Memcached cluster (console)](Clusters.md#Clusters.Create.CON.Memcached "Clusters.md#Clusters.Create.CON.Memcached").

For more information on regions and Availability Zones, see
[Choosing regions and availability zones for ElastiCache](RegionsAndAZs.md "RegionsAndAZs.md").

### Mitigating Failures when Running Valkey or Redis OSS

When running a Valkey or Redis OSS engine, you have the following options for minimizing the impact of a node or
Availability Zone failure.

#### Mitigating Node Failures

Serverless caches automatically mitigate node failures with a Multi-AZ architecture so that node failures are transparent to your application.
Node-based clusters must be configured appropriately to mitigate the failure of an individual node.

To mitigate the impact of Valkey or Redis OSS node failures on node-based clusters, you have the following options:

###### Topics

- [Mitigating Failures: Valkey or Redis OSS Replication Groups](#FaultTolerance.Redis.Cluster.Replication "#FaultTolerance.Redis.Cluster.Replication")

##### Mitigating Failures: Valkey or Redis OSS Replication Groups

A Valkey or Redis OSS replication group is comprised of a single primary node
which your application can both read from and write to,
and from 1 to 5 read-only replica nodes.
Whenever data is written to the primary node it is also asynchronously updated on the read replica nodes.

###### When a read replica fails

1. ElastiCache detects the failed read replica.
2. ElastiCache takes the failed node off line.
3. ElastiCache launches and provisions a replacement node in the same AZ.
4. The new node synchronizes with the primary node.

During this time your application can continue reading and writing using the other nodes.

###### Valkey or Redis OSS Multi-AZ

You can enable Multi-AZ on your Valkey or Redis OSS replication groups.
Whether you enable Multi-AZ or not, a failed primary will be detected and replaced automatically.
How this takes place varies whether or not Multi-AZ is or is not enabled.

###### When Multi-AZ is enabled

1. ElastiCache detects the primary node failure.
2. ElastiCache promotes the read replica node with the least replication lag to primary node.
3. The other replicas sync with the new primary node.
4. ElastiCache spins up a read replica in the failed primary's AZ.
5. The new node syncs with the newly promoted primary.

Failing over to a replica node is generally faster than creating and provisioning a new primary node.
This means your application can resume writing to your primary node sooner than if Multi-AZ were not enabled.

For more information, see [Minimizing downtime in ElastiCache by using Multi-AZ with Valkey and Redis OSS](AutoFailover.md "AutoFailover.md").

###### When Multi-AZ is disabled

1. ElastiCache detects primary failure.
2. ElastiCache takes the primary offline.
3. ElastiCache creates and provisions a new primary node to replace the failed primary.
4. ElastiCache syncs the new primary with one of the existing replicas.
5. When the sync is finished, the new node functions as the cluster's primary node.

During steps 1 through 4 of this process, your application can't write to the primary
node. However, your application can continue reading from your replica
nodes.

For added protection,
we recommend that you launch the nodes in your replication group in different Availability Zones (AZs).
If you do this, an AZ failure will only impact the nodes in that AZ and not the others.

For more information, see [High availability using replication groups](Replication.md "Replication.md").

#### Mitigating Availability Zone Failures

Serverless caches automatically mitigate availability zone failures with a replicated Multi-AZ architecture so that AZ failures are transparent to your application.

To mitigate the impact of an Availability Zone failure in a node-based cluster,
locate your nodes for each shard in as many Availability Zones as possible.

No matter how many nodes you have in a shard,
if they are all located in the same Availability Zone,
a catastrophic failure of that AZ results in your losing all your shard's data.
However, if you locate your nodes in multiple AZs,
a failure of any AZ results in your losing only the nodes in that AZ.

Any time you lose a node you can experience a performance degradation since read
operations are now shared by fewer nodes. This performance degradation will
continue until the nodes are replaced.

For information on specifying the Availability Zones for Valkey or Redis OSS nodes, see [Creating a Valkey (cluster mode disabled) cluster (Console)](SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs "SubnetGroups.designing-cluster-pre.md#Clusters.Create.CON.valkey-gs").

For more information on regions and Availability Zones, see [Choosing regions and availability zones for ElastiCache](RegionsAndAZs.md "RegionsAndAZs.md").

### Recommendations

We recommend creating serverless caches over node-based clusters, as you automatically obtain
better fault tolerance without additional configuration. When creating a node-based cluster, however, there are two types of failures you need to plan for:
individual node failures and broad Availability Zone failures.
The best failure mitigation plan will address both kinds of failures.

#### Minimizing the Impact of Node Failures

To minimize the impact of a node failure when using Valkey or Redis OSS,
we recommend that your implementation use multiple nodes in each shard and distribute the nodes across
multiple Availability Zones. This is done automatically for serverless caches.

For node-based clusters on Valkey or Redis OSS, we recommend that you enable Multi-AZ on your replication group
so that ElastiCache will automatically fail over to a replica if the primary node fails.

When running Memcached and partitioning your data across nodes,
the more nodes you use the smaller the data loss if any one node fails.

#### Minimizing the Impact of Availability Zone Failures

To minimize the impact of an Availability Zone failure,
we recommend launching your nodes in as many different Availability Zones as are available.
Spreading your nodes evenly across AZs will minimize the impact in the unlikely event
of an AZ failure. This is done automatically for serverless caches.

#### Other precautions

If you're running Valkey or Redis OSS, then in addition to the above,
we recommend that you schedule regular backups of your cluster.
Backups (snapshots) create a .rdb file you can use to restore your cache
in case of failure or corruption. For more information, see [Snapshot and restore](backups.md "backups.md").
