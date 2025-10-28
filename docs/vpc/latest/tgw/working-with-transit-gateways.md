# Work with AWS Transit Gateway

You can work with transit gateways using the Amazon VPC console or the AWS CLI.

###### Topics

- [Shared transit gateways](#transit-gateway-share "#transit-gateway-share")
- [Transit gateways](tgw-transit-gateways.md "tgw-transit-gateways.md")
- [VPC attachments](tgw-vpc-attachments.md "tgw-vpc-attachments.md")
- [Network function attachments](tgw-nf-fw.md "tgw-nf-fw.md")
- [VPN attachments](tgw-vpn-attachments.md "tgw-vpn-attachments.md")
- [Transit gateway attachments to a Direct Connect gateway](tgw-dcg-attachments.md "tgw-dcg-attachments.md")
- [Peering attachments](tgw-peering.md "tgw-peering.md")
- [Connect attachments and Connect peers](tgw-connect.md "tgw-connect.md")
- [Transit gateway route tables](tgw-route-tables.md "tgw-route-tables.md")
- [Transit gateway policy tables](tgw-policy-tables.md "tgw-policy-tables.md")
- [Multicast on transit gateways](tgw-multicast-overview.md "tgw-multicast-overview.md")

## Shared transit gateways

You can use AWS Resource Access Manager (RAM) to share a transit gateway for VPC attachments across
accounts or across your organization in AWS Organizations. RAM must be enabled and resources shared with
an organization. For more information, see [Enable
resource sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.

### Considerations

Take the following into account when you want to share a transit gateway.

- An AWS Site-to-Site VPN attachment must be created in the same AWS account that owns the
  transit gateway.
- An attachment to a Direct Connect gateway uses a transit gateway association and can be
  in the same AWS account as the Direct Connect gateway, or a different one from the Direct
  Connect gateway.

By default, users do not have permission to create or modify AWS RAM resources. To allow users
to create or modify resources and perform tasks, you must create IAM policies that grant
permission to use specific resources and API actions. You then attach those policies to the IAM
users or groups that require those permissions.

Only the resource owner can perform the following operations:

- Create a resource share.
- Update a resource share.
- View a resource share.
- View the resources that are shared by your account, across all resource shares.
- View the principals with whom you are sharing your resources, across all resource
  shares. Viewing the principals with whom you are sharing enables you to determine who has
  access to your shared resources.
- Delete a resource share.
- Run all transit gateway, transit gateway attachment, and transit gateway route tables APIs.

You can perform the following operations on resources that are shared with you:

- Accept, or reject a resource share invitation.
- View a resource share.
- View the shared resources that you can access.
- View a list of all the principals that are sharing resources with you. You can see which
  resources and resource shares they have shared with you.
- Can run the `DescribeTransitGateways` API.
- Run the APIs that create and describe attachments, for example
  `CreateTransitGatewayVpcAttachment` and
  `DescribeTransitGatewayVpcAttachments`, in their VPCs.
- Leave a resource share.

When a transit gateway is shared with you, you cannot create, modify, or delete its transit gateway route
tables, or its transit gateway route table propagations and associations.

When you create a transit gateway, the transit gateway, is created in the Availability Zone that is mapped to
your account and is independent from other accounts. When the transit gateway and the attachment entities
are in different accounts, use the Availability Zone ID to uniquely and consistently identify
the Availability Zone. For example, use1-az1 is an AZ ID for the us-east-1 Region and maps to
the same location in every AWS account.

### Unshare a transit gateway

When the share owner unshares the transit gateway, the following rules apply:

- The transit gateway attachment remains functional.
- The shared account can not describe the transit gateway.
- The transit gateway owner, and the share owner can delete the transit gateway attachment.

When a transit gateway is unshared with another AWS account, or if the AWS account that the
transit gateway is shared with is removed from the organization, the transit gateway itself won't be
impacted.

### Shared subnets

A VPC owner can attach a transit gateway to a shared VPC subnet. Participants cannot. The traffic from
participant’s resources can use the attachments depending on the routes set up on the shared VPC subnet by the VPC owner.

For more information, see [Share your VPC with other accounts](../userguide/vpc-sharing.md "../userguide/vpc-sharing.md") in the _Amazon VPC User Guide_.
