# Share your VPC subnets with other accounts

VPC subnet sharing allows multiple AWS accounts to create their application resources, such as
Amazon EC2 instances, Amazon Relational Database Service (RDS) databases, Amazon Redshift clusters, and AWS Lambda functions, into
shared, centrally-managed virtual private clouds (VPCs). In this model, the account that
owns the VPC (owner) shares one or more subnets with other accounts (participants) that belong
to the same organization from AWS Organizations. After a subnet is shared, the participants can view,
create, modify, and delete their application resources in the subnets shared with them.
Participants cannot view, modify, or delete resources that belong to other participants or the
VPC owner.

You can share your VPC subnets to leverage the implicit routing within a VPC for
applications that require a high degree of interconnectivity and are within the same trust
boundaries. This reduces the number of VPCs that you create and manage, while using separate
accounts for billing and access control. You can simplify network topologies by interconnecting
shared Amazon VPC subnets using connectivity features, such as AWS PrivateLink, transit gateways,
and VPC peering. For more information about the benefits of VPC subnet sharing, see [VPC sharing: A new approach to multiple accounts and VPC management](https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/ "https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/").

There are quotas related to VPC subnet sharing. For more information, see [VPC subnet sharing](amazon-vpc-limits.md#vpc-share-limits "amazon-vpc-limits.md#vpc-share-limits").

###### Contents

- [Shared subnet prerequisites](vpc-share-prerequisites.md "vpc-share-prerequisites.md")
- [Working with shared subnets](vpc-sharing-share-subnet-working-with.md "vpc-sharing-share-subnet-working-with.md")
- [Billing and metering for owner and participants](vpc-share-billing.md "vpc-share-billing.md")
- [Responsibilities and permissions for owners and
  participants](vpc-share-limitations.md "vpc-share-limitations.md")
- [AWS resources and shared VPC subnets](vpc-sharing-service-behavior.md "vpc-sharing-service-behavior.md")
