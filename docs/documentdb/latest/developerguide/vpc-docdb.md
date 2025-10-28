# Amazon VPC and Amazon DocumentDB

Amazon Virtual Private Cloud (Amazon VPC) makes it possible for you to launch AWS resources, such as Amazon DocumentDB instances, into a virtual private cloud (VPC).

When you use a VPC, you have control over your virtual networking environment.
You can choose your own IP address range, create subnets, and configure routing and access control lists.
There is no additional cost to run your cluster in a VPC.

Accounts have a default VPC. All new clusters are created in the default VPC unless you specify otherwise.

###### Topics

- [DocumentDB clusters in a VPC](vpc-clusters.md "vpc-clusters.md")
- [Accessing an Amazon DocumentDB cluster in a VPC](access-cluster-vpc.md "access-cluster-vpc.md")
- [Create an IPv4-only VPC for use with a DocumentDB cluster](docdb-vpc-create-ipv4.md "docdb-vpc-create-ipv4.md")
- [Create a dual-stack VPC for use with a DocumentDB cluster](docdb-vpc-create-dual-stack.md "docdb-vpc-create-dual-stack.md")
  Following, you can find a discussion about VPC functionality relevant to Amazon DocumentDB clusters.
  For more information about Amazon VPC, see the [Amazon VPC User Guide](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").
