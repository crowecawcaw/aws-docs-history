

# Direct Connect gateways and Transit Gateway associations
<a name="direct-connect-transit-gateways"></a>

You can use Direct Connect gateway to connect your Direct Connect connection over a transit virtual interface to the VPCs or VPNs that are attached to your Transit Gateway. You associate a Direct Connect gateway with the Transit Gateway. Then, create a transit virtual interface for your Direct Connect connection to the Direct Connect gateway. 

The following rules apply to Transit Gateway associations:
+ You cannot attach a Direct Connect gateway to a Transit Gateway when the Direct Connect gateway is already associated with a virtual private gateway or is attached to a private virtual interface.
+ There are limits for creating and using Direct Connect gateways. For more information, see [Direct Connect quotas](limits.md).
+ A Direct Connect gateway supports communication between attached transit virtual interfaces and associated Transit Gateways.
+ If you connect to multiple Transit Gateways that are in different Regions, use unique ASNs for each Transit Gateway.
+ Any point-to-point connectivity address using a `/30` range — for example, `192.168.0.0/30` — does not propagate to a Transit Gateway.

## Associating a Transit Gateway across accounts
<a name="multi-account-associate-tgw"></a>

You can associate an existing Direct Connect gateway or a new Direct Connect gateway with a Transit Gateway that is owned by any AWS account. The owner of the Transit Gateway creates an *association proposal* and the owner of the Direct Connect gateway must accept the association proposal.

An association proposal can contain prefixes that will be allowed from the Transit Gateway. The owner of the Direct Connect gateway can optionally override any requested prefixes in the association proposal.

### Allowed prefixes
<a name="allowed-prefixes-transit-gateway"></a>

For a Transit Gateway association, you provision the allowed prefixes list on the Direct Connect gateway. The list is used to route traffic from on-premises to AWS into the Transit Gateway even if the VPCs attached to the Transit Gateway do not have assigned CIDRs. Prefixes in the Direct Connect gateway allowed prefix list originate on the Direct Connect gateway and are advertised to the on-premises network. For more information on how allowed prefixes interact with Transit Gateway and virtual private gateways, see [Allowed prefixes interactions](allowed-to-prefixes.md).

**Topics**
+ [Associating a Transit Gateway across accounts](#multi-account-associate-tgw)
+ [Associate or disassociate a Transit Gateway with Direct Connect.](associate-tgw-with-direct-connect-gateway.md)
+ [Create a transit virtual interface to the Direct Connect gateway](create-transit-vif-for-gateway.md)
+ [Create a Transit Gateway association proposal](multi-account-tgw-create-proposal.md)
+ [Accept or reject a Transit Gateway association proposal](multi-account-tgw-accept-reject-proposal.md)
+ [Update the allowed prefixes for a Transit Gateway association](multi-account-tgw-update-proposal-routes.md)
+ [Delete a Transit Gateway association proposal](multi-account-tgw-delete-proposal.md)