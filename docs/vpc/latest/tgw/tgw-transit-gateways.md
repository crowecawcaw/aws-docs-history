# Transit gateways in AWS Transit Gateway

A transit gateway enables you to attach VPCs and VPN connections and route traffic between
them. A transit gateway works across AWS accounts, and you can use AWS RAM to share your transit gateway
with other accounts. After you share a transit gateway with another AWS account, the account
owner can attach their VPCs to your transit gateway. A user from either account can delete the
attachment at any time.

You can enable multicast on a transit gateway, and then create a transit gateway multicast domain that
allows multicast traffic to be sent from your multicast source to multicast group
members over VPC attachments that you associate with the domain.

Each VPC or VPN attachment is associated with a single route table. That route table
decides the next hop for the traffic coming from that resource attachment. A route table
inside the transit gateway allows for both IPv4 or IPv6 CIDRs and targets. The targets are VPCs
and VPN connections. When you attach a VPC or create a VPN connection on a transit gateway, the
attachment is associated with the default route table of the transit gateway.

You can create additional route tables inside the transit gateway, and change the VPC or VPN
association to these route tables. This enables you to segment your network. For
example, you can associate development VPCs with one route table and production VPCs
with a different route table. This enables you to create isolated networks inside a
transit gateway similar to virtual routing and forwarding (VRFs) in traditional networks.

Transit gateways support dynamic and static routing between attached VPCs and VPN
connections. You can enable or disable route propagation for each attachment. Transit
gateway peering attachments support static routing only. You can point routes in transit
gateway route tables to the peering attachment for routing traffic between the peered
transit gateways.

You can optionally associate one or more IPv4 or IPv6 CIDR blocks with your transit
gateway. You specify an IP address from the CIDR block when you establish a
Transit Gateway Connect peer for a [Transit Gateway Connect attachment](tgw-connect.md "tgw-connect.md").
You can associate any public or private IP address range, except for addresses in
the `169.254.0.0/16` range, and ranges that
overlap with addresses for your VPC attachments and on-premises networks. For more
information about IPv4 and IPv6 CIDR blocks, see [IP addressing](../userguide/vpc-ip-addressing.md "../userguide/vpc-ip-addressing.md")
in the _Amazon VPC User Guide_.

###### Tasks

- [Create a transit gateway](create-tgw.md "create-tgw.md")
- [View a transit gateway](view-tgws.md "view-tgws.md")
- [Manage transit gateway tags](tgw-tagging.md "tgw-tagging.md")
- [Modify a transit gateway](tgw-modifying.md "tgw-modifying.md")
- [Accept a resource share](share-accept-tgw.md "share-accept-tgw.md")
- [Accept a shared attachment](acccept-tgw-attach.md "acccept-tgw-attach.md")
- [Delete a transit gateway](delete-tgw.md "delete-tgw.md")
