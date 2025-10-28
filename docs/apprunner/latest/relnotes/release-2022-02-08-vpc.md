# Release: App Runner supports custom Amazon VPC for outbound traffic on February 8, 2022

Your AWS App Runner service can now communicate with other applications hosted in a private VPC from Amazon Virtual Private Cloud (Amazon VPC).

**Release date:** February 8, 2022

## Changes

You can now use AWS App Runner to route your service's outbound network traffic through a VPC from Amazon Virtual Private Cloud (Amazon VPC). This means that your service can
communicate with other applications or AWS services that are hosted in a private VPC.

For example, you can connect your App Runner services to databases in Amazon Relational Database Service (Amazon RDS) or to Redis caches in Amazon ElastiCache. You can also connect your services
to your own applications in Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), or Amazon Elastic Compute Cloud (Amazon EC2).

To associate a VPC with your service, you specify Amazon VPC subnets and security groups, and App Runner automatically provisions and manages the necessary
connections to the VPC.

For more information, see [Enabling Amazon VPC access for your service](../dg/network-vpc.md "../dg/network-vpc.md") in the
_AWS App Runner Developer Guide_.
