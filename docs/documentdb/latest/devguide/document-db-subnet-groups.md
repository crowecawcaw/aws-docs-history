# Managing Amazon DocumentDB subnet groups

A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can launch your AWS resources, such as Amazon DocumentDB clusters, into your Amazon VPC. You can specify an IP address range for the VPC, add subnets, associate security groups, and configure route tables.

A subnet is a range of IP addresses in your Amazon VPC. You can launch AWS resources into a specified subnet. Use a _public_ subnet for resources that must be connected to the internet. Use a _private_ subnet for resources that won't be connected to the internet. For more information about public and private subnets, see [VPC and Subnet Basics](../../../vpc/latest/userguide/VPC_Subnets.md#vpc-subnet-basics "../../../vpc/latest/userguide/VPC_Subnets.md#vpc-subnet-basics") in the _Amazon Virtual Private Cloud User Guide_.

A DB subnet group is a collection of subnets that you create in a VPC that you then designate for your clusters. A subnet group allows you to specify a particular VPC when creating clusters. If you use the `default` subnet group, it spans all subnets in the VPC.

Each DB subnet group should have subnets in at least two Availability Zones in a given Region. When creating a DB cluster in a VPC, you must select a DB subnet group. Amazon DocumentDB uses that DB subnet group and your preferred Availability Zone to select a subnet and an IP address within that subnet to associate with your cluster. If the primary instance fails, Amazon DocumentDB can promote a corresponding replica instance to be the new primary. It can then create a new replica instance using an IP address of the subnet in which the previous primary was located.

When Amazon DocumentDB creates an instance in a VPC, it assigns a network interface to your cluster by using an IP address selected from your DB subnet group. We strongly recommend that you use the DNS name because the underlying IP address can change during failover. For more information, see [Amazon DocumentDB endpoints](how-it-works.md#how-it-works.endpoints "how-it-works.md#how-it-works.endpoints").

For information about creating your own VPC and subnets, see [Working with VPCs and Subnets](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md") in the _Amazon Virtual Private Cloud User Guide_.

###### Topics

- [Creating an Amazon DocumentDB subnet group](document-db-subnet-group-create.md "document-db-subnet-group-create.md")
- [Describing an Amazon DocumentDB subnet group](document-db-subnet-group-describe.md "document-db-subnet-group-describe.md")
- [Modifying an Amazon DocumentDB subnet group](document-db-subnet-group-modify.md "document-db-subnet-group-modify.md")
- [Deleting an Amazon DocumentDB subnet group](document-db-subnet-group-delete.md "document-db-subnet-group-delete.md")
