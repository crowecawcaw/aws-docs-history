# Working with additional security groups for an Amazon EMR cluster

Whether you use the default managed security groups or specify custom managed security
groups, you can use additional security groups. Additional security groups give you the
flexibility to tailor access between different clusters and from external clients,
resources, and applications.

Consider the following scenario as an example. You have multiple clusters that you
need to communicate with each other, but you want to allow inbound SSH access to the
primary instance for only a particular subset of clusters. To do this, you can use the
same set of managed security groups for the clusters. You then create additional
security groups that allow inbound SSH access from trusted clients, and specify the
additional security groups for the primary instance to each cluster in the
subset.

You can apply up to 15 additional security groups for the primary instance, 15 for
core and task instances, and 15 for service access (in private subnets). If necessary,
you can specify the same additional security group for primary instances, core and task
instances, and service access. The maximum number of security groups and rules in your
account is subject to account limits. For more information, see [Security group
limits](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-security-groups "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-security-groups") in the _Amazon VPC User Guide_.
