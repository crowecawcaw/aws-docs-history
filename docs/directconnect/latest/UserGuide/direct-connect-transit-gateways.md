# AWS Direct Connect gateways and transit gateway associations

You can use AWS Direct Connect gateway to connect your Direct Connect connection over a transit virtual
interface to the VPCs or VPNs that are attached to your transit gateway. You associate a Direct Connect
gateway with the transit gateway. Then, create a transit virtual interface for your AWS Direct Connect connection
to the Direct Connect gateway.

The following rules apply to transit gateway associations:

- You cannot attach a Direct Connect gateway to a transit gateway when the Direct Connect
  gateway is already associated with a virtual private gateway or is attached to a
  private virtual interface.
- There are limits for creating and using Direct Connect gateways. For more
  information, see [Direct Connect quotas](limits.md "limits.md").
- A Direct Connect gateway supports communication between attached transit virtual
  interfaces and associated transit gateways.
- If you connect to multiple transit gateways that are in different Regions, use unique
  ASNs for each transit gateway.
- Any point-to-point connectivity address using a `/30` range — for
  example, `192.168.0.0/30` — does not propagate to a transit gateway.

## Associating a transit gateway across accounts

You can associate an existing Direct Connect gateway or a new Direct Connect
gateway with a transit gateway that is owned by any AWS account. The owner of the transit gateway creates
an _association proposal_ and the owner of the Direct Connect
gateway must accept the association proposal.

An association proposal can contain prefixes that will be allowed from the transit gateway. The owner of the Direct Connect gateway can optionally override any
requested prefixes in the association proposal.

### Allowed prefixes

For a transit gateway association, you provision the allowed prefixes list on the Direct
Connect gateway. The list is used to route traffic from on-premises to AWS into
the transit gateway even if the VPCs attached to the transit gateway do not have assigned CIDRs.
Prefixes in the Direct Connect gateway allowed prefix list originate on the
Direct Connect gateway and are advertised to the on-premises network. For more
information on how allowed prefixes interact with transit gateway and virtual private
gateways, see [Allowed prefixes interactions](allowed-to-prefixes.md "allowed-to-prefixes.md").

###### Topics

- [Associate or disassociate a transit gateway with Direct Connect.](associate-tgw-with-direct-connect-gateway.md "associate-tgw-with-direct-connect-gateway.md")
- [Create a transit virtual
  interface to the Direct Connect gateway](create-transit-vif-for-gateway.md "create-transit-vif-for-gateway.md")
- [Create a transit gateway association
  proposal](multi-account-tgw-create-proposal.md "multi-account-tgw-create-proposal.md")
- [Accept or reject a transit gateway association proposal](multi-account-tgw-accept-reject-proposal.md "multi-account-tgw-accept-reject-proposal.md")
- [Update the allowed prefixes for a
  transit gateway association](multi-account-tgw-update-proposal-routes.md "multi-account-tgw-update-proposal-routes.md")
- [Delete a transit gateway association
  proposal](multi-account-tgw-delete-proposal.md "multi-account-tgw-delete-proposal.md")
