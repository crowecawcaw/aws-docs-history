# AWS Direct Connect virtual private gateway associations

You can associate a virtual private gateway with a Direct Connect gateway to enable
connectivity between your AWS Direct Connect connection and VPCs across different accounts and
Regions. Each VPC requires a virtual private gateway that you associate with the Direct
Connect gateway. Once these associations are established, you create private virtual
interfaces on your Direct Connect connection to the Direct Connect gateway, allowing
multiple VPCs to share the same Direct Connect connection through their respective virtual
private gateway associations..

The following rules apply to virtual private gateway associations:

- Do not enable route propagation until after you've associated a virtual
  gateway with a Direct Connect gateway. If you enable route propagation before
  associating the gateways, routes might be propagated incorrectly.
- There are limits for creating and using Direct Connect gateways. For more
  information, see [Direct Connect quotas](limits.md "limits.md").
- You cannot attach a Direct Connect gateway to a virtual private gateway when the
  Direct Connect gateway is already associated with a transit gateway.
- The VPCs to which you connect through a Direct Connect gateway cannot have
  overlapping CIDR blocks. If you add an IPv4 CIDR block to a VPC that's
  associated with a Direct Connect gateway, ensure that the CIDR block does not
  overlap with an existing CIDR block for any other associated VPC. For more
  information, see [Adding
  IPv4 CIDR Blocks to a VPC](../../../vpc/latest/userguide/VPC_Subnets.md#vpc-resize "../../../vpc/latest/userguide/VPC_Subnets.md#vpc-resize") in the
  _Amazon VPC User Guide_.
- You cannot create a public virtual interface to a Direct Connect
  gateway.
- A Direct Connect gateway supports communication between attached private virtual
  interfaces and associated virtual private gateways only, and may enable a
  virtual private gateway to another private gateway. The following traffic flows
  are not supported:
  - Direct communication between the VPCs that are associated with a
    single Direct Connect gateway. This includes traffic from one VPC to
    another by using a hairpin through an on-premises network through a
    single Direct Connect gateway.
  - Direct communication between the virtual interfaces that are attached
    to a single Direct Connect gateway.
  - Direct communication between the virtual interfaces that are attached
    to a single Direct Connect gateway and a VPN connection on a virtual
    private gateway that's associated with the same Direct Connect
    gateway.

- You cannot associate a virtual private gateway with more than one Direct
  Connect gateway and you cannot attach a private virtual interface to more than
  one Direct Connect gateway.
- A virtual private gateway that you associate with a Direct Connect gateway
  must be attached to a VPC.
- A virtual private gateway association proposal expires 7 days after it is
  created.
- An accepted virtual private gateway proposal, or a deleted virtual private
  gateway proposal remains visible for 3 days.
- A virtual private gateway can be associated with a Direct Connect gateway and
  also attached to a virtual interface.
- Detaching a virtual private gateway from a VPC also disassociates the virtual
  private gateway from a Direct Connect gateway.
- If you are planning to use the virtual private gateway for a Direct Connect
  gateway and a dynamic VPN connection, set the ASN on the virtual private gateway to
  the value that you require for the VPN connection. Otherwise, the ASN on the virtual
  private gateway can be set to any permitted value. The Direct Connect gateway
  advertises all connected VPCs over the ASN assigned to it.
  To connect your AWS Direct Connect connection to a VPC in the same Region only, you can create a
  Direct Connect gateway. Or, you can create a private virtual interface and attach it to the
  virtual private gateway for the VPC. For more information, see [Create a private virtual interface](create-private-vif.md "create-private-vif.md") and [VPN CloudHub](../../../vpc/latest/userguide/VPN_CloudHub.md "../../../vpc/latest/userguide/VPN_CloudHub.md").

To use your AWS Direct Connect connection with a VPC in another account, you can create a hosted
private virtual interface for that account. When the owner of the other account accepts
the hosted virtual interface, they can choose to attach it either to a virtual private
gateway or to a Direct Connect gateway in their account. For more information, see [Virtual interfaces and hosted virtual interfaces](WorkingWithVirtualInterfaces.md "WorkingWithVirtualInterfaces.md").

###### Topics

- [Create a virtual private gateway](create-virtual-private-gateway.md "create-virtual-private-gateway.md")
- [Associate or disassociate virtual private gateways](associate-vgw-with-direct-connect-gateway.md "associate-vgw-with-direct-connect-gateway.md")
- [Create a private virtual
  interface to the Direct Connect gateway](create-private-vif-for-gateway.md "create-private-vif-for-gateway.md")
- [Associate a virtual private gateway across accounts](multi-account-associate-vgw.md "multi-account-associate-vgw.md")
