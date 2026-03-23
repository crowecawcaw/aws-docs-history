# Managing clusters

Most MemoryDB operations are performed at the cluster level.
You can set up a cluster with a specific number of nodes and
a parameter group that controls the properties for each node.
All nodes within a cluster are designed to be of the same node type
and have the same parameter and security group settings.

Every cluster must have a cluster identifier.
The cluster identifier is a customer-supplied name for the cluster.
This identifier specifies a particular cluster when interacting with the MemoryDB API and
AWS CLI commands.
The cluster identifier must be unique for that customer in an AWS Region.

MemoryDB clusters are designed to be accessed using an Amazon EC2 instance. You can only launch your
MemoryDB cluster in a virtual private cloud (VPC) based on the Amazon VPC service, but you can access it from
outside AWS. For more information, see [Accessing MemoryDB resources from outside AWS](accessing-memorydb.md#access-from-outside-aws "accessing-memorydb.md#access-from-outside-aws").
