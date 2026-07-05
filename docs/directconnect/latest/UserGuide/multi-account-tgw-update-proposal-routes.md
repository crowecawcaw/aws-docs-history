# Update the allowed prefixes for a transit gateway and Direct Connect association

You can update the prefixes that are allowed from the Transit Gateway over the Direct Connect gateway
using either the Direct Connect console or using the command line or API. To update the allowed
prefixes for a Transit Gateway and Direct Connect association using the Direct Connect console,

- If you're the owner of the Transit Gateway. you'll need to create a new association
  proposal for that Direct Connect gateway, specifying the prefixes to allow. For the steps to create a new association proposal, see [Create a Transit Gateway association
  proposal](multi-account-tgw-create-proposal.md "multi-account-tgw-create-proposal.md").
- If you're the owner of the Direct Connect gateway you can update the allowed prefixes
  when you accept the association proposal, or if you update the allowed prefixes for
  an existing association. For the steps to update the allowed prefixes when you accept the association, see [Accept or reject a Transit Gateway association proposal](multi-account-tgw-accept-reject-proposal.md "multi-account-tgw-accept-reject-proposal.md").

###### To update the allowed prefixes for an existing association using the command line or API

- [update-direct-connect-gateway-association](../../../cli/latest/reference/directconnect/update-direct-connect-gateway-association.md "../../../cli/latest/reference/directconnect/update-direct-connect-gateway-association.md") (AWS CLI)
- [UpdateDirectConnectGatewayAssociation](../APIReference/API_UpdateDirectConnectGatewayAssociation.md "../APIReference/API_UpdateDirectConnectGatewayAssociation.md") (Direct Connect API)
