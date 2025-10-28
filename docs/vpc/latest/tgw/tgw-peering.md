# Transit gateway peering attachments in AWS Transit Gateway

You can peer both intra-Region and inter-Region transit gateways, and route traffic between them,
which includes IPv4 and IPv6 traffic. To do this, create a peering attachment on your transit gateway,
and specify a transit gateway. The peer transit gateway can either be in your account or can be from another
account. You can also request a peering attachment from your own account to a transit
gateway in another account.

After you create a peering attachment request, the owner of the peer transit gateway (also
referred to as the _accepter transit gateway_) must accept the request.
To route traffic between the transit gateways, add a static route to the transit gateway route table that points
to the transit gateway peering attachment.

We recommend using unique ASNs for each peered transit gateway to take advantage of future route
propagation capabilities.

Transit gateway peering does not support resolving public or private IPv4 DNS host names
to private IPv4 addresses across VPCs on either side of the transit gateway peering
attachment using the Amazon Route 53 Resolver in another Region. For more information
about the Route 53 Resolver, see [What is Route 53 Resolver?](../../../Route53/latest/DeveloperGuide/resolver.md "../../../Route53/latest/DeveloperGuide/resolver.md") in the
_Amazon Route 53 Developer Guide_.

Inter-Region gateway peering uses the same network infrastructure as VPC
peering. Therefore traffic is encrypted using AES-256 encryption at the virtual network
layer as it travels between Regions. Traffic is also encrypted using AES-256 encryption at
the physical layer when it traverses network links that are outside of the physical control
of AWS. As a result, traffic is double encrypted on network links outside the physical
control of AWS. Within the same Region, traffic is encrypted at the physical layer only
when it traverses network links that are outside of the physical control of AWS.

For information about which Regions support transit gateway peering attachments, see [AWS Transit Gateways FAQs](https://aws.amazon.com/transit-gateway/faqs/ "https://aws.amazon.com/transit-gateway/faqs/").

## Opt-in AWS Region considerations

You can peer transit gateways across opt-in Region boundaries. For information about these
Regions, and how to opt in, see [Managing AWS Regions](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md").
Take the following into consideration when you use transit gateway peering in these Regions:

- You can peer into an opt-in Region as long as the account that accepts the
  peering attachment has opted into that Region.
- Regardless of the Region opt-in status, AWS shares the following account data
  with the account that accepts the peering attachment:
  - AWS account ID
  - Transit gateway ID
  - Region code

- When you delete the transit gateway attachment, the above account data is
  deleted.
- We recommend that you delete the transit gateway peering attachment before you opt out
  of the Region. If you do not delete the peering attachment, traffic might
  continue to go over the attachment and you continue to incur charges. If you do
  not delete the attachment, you can opt back in, and then delete the
  attachment.
- In general, the transit gateway has a sender pays model. By using a transit gateway
  peering attachment across an opt in boundary, you might incur charges in a
  Region accepting the attachment, including those Regions you have not opted
  into. For more information, see [AWS Transit Gateway Pricing](https://aws.amazon.com/transit-gateway/pricing/ "https://aws.amazon.com/transit-gateway/pricing/").

###### Tasks

- [Create a peering attachment](tgw-peering-create.md "tgw-peering-create.md")
- [Accept or reject a peering request](tgw-peering-accept-reject.md "tgw-peering-accept-reject.md")
- [Add a route to a transit gateway route table](tgw-peering-add-route.md "tgw-peering-add-route.md")
- [Delete a peering attachment](tgw-peering-delete.md "tgw-peering-delete.md")
