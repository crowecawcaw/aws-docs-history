# MemoryDB core components

Following, you can find an overview of the major components of a MemoryDB deployment.

###### Topics

- [Clusters](#whatis.clusters "#whatis.clusters")
- [Nodes](#whatis.components.nodes "#whatis.components.nodes")
- [Shards](#whatis.components.Shards "#whatis.components.Shards")
- [Parameter groups](#whatis.components.parametergroups "#whatis.components.parametergroups")
- [Subnet Groups](#whatis.components.subnetgroups "#whatis.components.subnetgroups")
- [Access Control Lists](#whatis.components.acls "#whatis.components.acls")
- [Users](#whatis.components.user "#whatis.components.user")

## Clusters

A cluster is a collection of one or more nodes serving a single dataset. A MemoryDB dataset is partitioned into shards, and each shard has a primary node and up to 5 optional replica nodes. A primary node serves read and write requests, while a replica only serves read requests. A primary node can failover to a replica node,
promoting that replica to the new primary node for that shard. MemoryDB runs Valkey or Redis OSS as its database engine, and when you create a cluster, you specify the engine version for your cluster. You can create and modify a cluster using the AWS CLI, the MemoryDB API, or the AWS Management Console.

Each MemoryDB cluster runs a Valkey or Redis OSS engine version. Each engine version has its own supported features. Additionally, each engine version has a set of parameters in a parameter group that control the behavior of the clusters that it manages.

The computation and memory capacity of a cluster is determined by its node type. You can select the node type that best meets your needs. If your needs change over time, you can change node types.
For information, see [Supported node types](nodes.md "nodes.md").

###### Note

For pricing information on MemoryDB node types, see [MemoryDB pricing](https://aws.amazon.com/memorydb/pricing/ "https://aws.amazon.com/memorydb/pricing/").

You run a cluster on a virtual private cloud (VPC) using the Amazon Virtual Private Cloud (Amazon VPC) service.
When you use a VPC, you have control over your virtual networking environment.
You can choose your own IP address range, create subnets, and configure routing and access control lists.
MemoryDB manages snapshots, software patching, automatic failure detection, and recovery. There's no additional cost to run your cluster in a VPC. For more information on using Amazon VPC with MemoryDB,
see [MemoryDB and Amazon VPC](vpcs.md "vpcs.md").

Many MemoryDB operations are targeted at clusters:

- Creating a cluster
- Modifying a cluster
- Taking snapshots of a cluster
- Deleting a cluster
- Viewing the elements in a cluster
- Adding or removing cost allocation tags to and from a cluster

For more detailed information, see the following related topics:

- [Managing clusters](clusters.md "clusters.md")
  and [Managing nodes](nodes.md "nodes.md")

Information about clusters, nodes, and related operations.

- [Resilience in MemoryDB](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")

Information about improving the fault tolerance of your clusters.

## Nodes

A _node_ is the smallest building block of a MemoryDB deployment and runs using an Amazon EC2 instance.
Each node runs the engine version that was chosen when you created your cluster. A node belongs to a shard which belongs to a cluster.

Each node runs an instance of the engine at the version chosen when
you created your cluster. If necessary, you can scale the nodes in a cluster up or down to a different
type. For more information, see [Scaling](scaling.md "scaling.md") .

Every node within a cluster is the same node type.

Multiple types of nodes are supported, each with varying amounts of memory.
For a list of supported node types, see [Supported node types](nodes.md "nodes.md").

For more information on nodes, see [Managing nodes](nodes.md "nodes.md").

## Shards

A shard is a grouping of one to 6
nodes, with one serving as the primary write node and the other 5 serving as read replicas. A MemoryDB cluster always has at least one shard.

MemoryDB clusters can have up to 500 shards, with your data partitioned across the shards. For example, you can choose to configure a 500 node cluster that ranges between
83 shards (one primary and 5 replicas per shard) and 500 shards (single primary and no replicas). Make sure there are enough available IP addresses to accommodate the increase.
Common pitfalls include the subnets in the subnet group have too small a CIDR range or the subnets are shared and heavily used by other clusters.

A _multiple node shard_ implements replication by having one
read/write primary node and 1–5 replica nodes. For more
information, see [Understanding MemoryDB replication](replication.md "replication.md").

For more information on shards, see [Working with shards](shards.md "shards.md").

## Parameter groups

Parameter groups are an easy way to manage runtime settings for the engine on your cluster. Parameters are used to control memory usage, item
sizes, and more. A MemoryDB parameter group is a named collection of engine-specific
parameters that you can apply to a cluster, and all of the nodes in that cluster are configured in exactly the same way.

For more detailed information on MemoryDB parameter groups, see [Configuring engine parameters using parameter groups](parametergroups.md "parametergroups.md").

## Subnet Groups

A _subnet group_ is a collection of subnets (typically private)
that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment.

When you create a cluster in an Amazon VPC, you can specify a subnet group or use the default one provided.
MemoryDB uses that subnet group to choose a subnet and IP addresses within that
subnet to associate with your nodes.

For more detailed information on MemoryDB subnet groups, see [Subnets and subnet groups](subnetgroups.md "subnetgroups.md").

## Access Control Lists

An Access control list is a collection of one or more users. Access strings follow the [ACL rules](https://valkey.io/topics/acl "https://valkey.io/topics/acl") to authorize

user access to Valkey or Redis OSS commands and data.

For more detailed information on MemoryDB Access Control Lists, see [Authenticating users with Access Control Lists (ACLs)](clusters.md "clusters.md").

## Users

A user has a user name and password, and is used to access data and issue commands on your MemoryDB cluster.
A user is a member of an Access Control List (ACL), which you can use to determine permissions for that user on MemoryDB clusters.
For more information, see [Authenticating users with Access Control Lists (ACLs)](clusters.md "clusters.md")
