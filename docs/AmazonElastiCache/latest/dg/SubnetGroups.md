# Subnets and subnet groups

A _subnet group_ is a collection of subnets (typically private)
that you can designate for your node-based clusters running in an Amazon Virtual Private Cloud (VPC) environment.

If you create a node-based cluster in an Amazon VPC, you must use a subnet group.
ElastiCache uses that subnet group to choose a subnet and IP addresses within that
subnet to associate with your nodes.

ElastiCache provides a default IPv4 subnet group or you can choose to create a new one. For IPv6, you need to create a subnet group with an IPv6 CIDR block. If you choose **dual stack**, you then must select a Discovery IP type, either IPv6 or IPv4.

ElastiCache Serverless does not use a subnet group resource, and instead takes a list of subnets directly during creation.

This section covers how to create and leverage subnets and subnet groups
to manage access to your ElastiCache resources.

For more information about subnet group usage in an Amazon VPC environment,
see [Accessing your ElastiCache cluster or replication group](accessing-elasticache.md "accessing-elasticache.md").

###### Topics

- [Creating a subnet group](SubnetGroups.md "SubnetGroups.md")
- [Assigning a subnet group to a cache](SubnetGroups.md "SubnetGroups.md")
- [Modifying a subnet group](SubnetGroups.md "SubnetGroups.md")
- [Deleting a subnet group](SubnetGroups.md "SubnetGroups.md")
