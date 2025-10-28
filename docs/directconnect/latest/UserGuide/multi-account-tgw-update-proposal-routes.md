# Update the allowed prefixes for a transit

gateway and AWS Direct Connect association

You can update the prefixes that are allowed from the transit gateway over the Direct Connect gateway
using either the AWS Direct Connect console or using the command line or API. To update the allowed
prefixes for a transit gateway and Direct Connect association using the AWS Direct Connect console,

- If you're the owner of the transit gateway. you'll need to create a new association
  proposal for that Direct Connect gateway, specifying the prefixes to allow. For the steps to create a new association proposal, see [Create a transit gateway association
  proposal](multi-account-tgw-create-proposal.md "multi-account-tgw-create-proposal.md").
- If you're the owner of the Direct Connect gateway you can update the allowed prefixes
  when you accept the association proposal, or if you update the allowed prefixes for
  an existing association. For the steps to update the allowed prefixes when you accept the association, see [Accept or reject a transit gateway association proposal](multi-account-tgw-accept-reject-proposal.md "multi-account-tgw-accept-reject-proposal.md").

###### To update the allowed prefixes for an existing association using the command

line or API

- [update-direct-connect-gateway-association](../../../cli/latest/reference/directconnect/update-direct-connect-gateway-association.md "../../../cli/latest/reference/directconnect/update-direct-connect-gateway-association.md") (AWS CLI)
- [UpdateDirectConnectGatewayAssociation](../APIReference/API_UpdateDirectConnectGatewayAssociation.md "../APIReference/API_UpdateDirectConnectGatewayAssociation.md") (AWS Direct Connect API)
