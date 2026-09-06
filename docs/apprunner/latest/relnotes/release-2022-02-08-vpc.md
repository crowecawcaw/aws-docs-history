

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner supports custom Amazon VPC for outbound traffic on February 8, 2022
<a name="release-2022-02-08-vpc"></a>

Your AWS App Runner service can now communicate with other applications hosted in a private VPC from Amazon Virtual Private Cloud (Amazon VPC).

**Release date:** February 8, 2022

## Changes
<a name="release-2022-02-08-vpc.changes"></a>

You can now use AWS App Runner to route your service's outbound network traffic through a VPC from Amazon Virtual Private Cloud (Amazon VPC). This means that your service can communicate with other applications or AWS services that are hosted in a private VPC.

For example, you can connect your App Runner services to databases in Amazon Relational Database Service (Amazon RDS) or to Redis caches in Amazon ElastiCache. You can also connect your services to your own applications in Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), or Amazon Elastic Compute Cloud (Amazon EC2).

To associate a VPC with your service, you specify Amazon VPC subnets and security groups, and App Runner automatically provisions and manages the necessary connections to the VPC.

For more information, see [Enabling Amazon VPC access for your service](https://docs.aws.amazon.com/apprunner/latest/dg/network-vpc.html) in the *AWS App Runner Developer Guide*.