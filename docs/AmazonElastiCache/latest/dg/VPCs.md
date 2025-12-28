# Amazon VPCs and ElastiCache security

Because data security is important,
ElastiCache provides means for you to control who has access to your data.
How you control access to your data is dependent upon whether or not you launched
your clusters in an Amazon Virtual Private Cloud (Amazon VPC) or Amazon EC2-Classic.

###### Important

We have deprecated the use of Amazon EC2-Classic for launching ElastiCache clusters.
All current generation nodes are launched in Amazon Virtual Private Cloud only.

The Amazon Virtual Private Cloud (Amazon VPC) service defines a virtual network that closely
resembles a traditional data center. When you configure your Amazon VPC you can select its IP address range,
create subnets, and configure route tables, network gateways, and security settings.
You can also add a cluster to the virtual network, and
control access to the cluster by using Amazon VPC security groups.

This section explains how to manually configure an ElastiCache cluster in an Amazon VPC.
This information is intended for users who want a deeper understanding of how ElastiCache and
Amazon VPC work together.

###### Topics

- [Understanding ElastiCache and Amazon VPCs](VPCs.md "VPCs.md")
- [Access Patterns for Accessing an ElastiCache Cache in an Amazon VPC](elasticache-vpc-accessing.md "elasticache-vpc-accessing.md")
- [Creating a Virtual Private Cloud (VPC)](VPCs.md "VPCs.md")
- [Connecting to a cache running in an Amazon VPC](VPCs.md "VPCs.md")
