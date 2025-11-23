# Associate an Direct Connect virtual private gateway across accounts

You can associate a Direct Connect gateway with a virtual private gateway that is
owned by any AWS account. The Direct Connect gateway can be an existing gateway, or
you can create a new gateway. The owner of the virtual private gateway creates an
_association proposal_ and the owner of the Direct Connect
gateway must accept the association proposal.

An association proposal can contain prefixes that will be allowed from the virtual
private gateway. The owner of the Direct Connect gateway can optionally override any
requested prefixes in the association proposal.

## Allowed prefixes

When you associate a virtual private gateway with a Direct Connect gateway, you
specify a list of Amazon VPC prefixes to advertise to the Direct Connect gateway.
The prefix list acts as a filter that allows the same CIDRs, or smaller CIDRs to be
advertised to the Direct Connect gateway. You must set the **Allowed
prefixes** to a range that is the same or wider than the VPC CIDR
because we provision entire VPC CIDR on the virtual private gateway.

Consider the case where the VPC CIDR is 10.0.0.0/16. You can set the
**Allowed prefixes** to 10.0.0.0/16 (the VPC CIDR value),
or 10.0.0.0/15 ( a value that is wider than the VPC CIDR).

Any virtual interface inside network prefixes advertised over Direct Connect are
only propagated to transit gateways across Regions, not within the same
Region. For more information on how allowed prefixes interact
with virtual private gateways and transit gateways, see [Allowed prefixes interactions](allowed-to-prefixes.md "allowed-to-prefixes.md").
