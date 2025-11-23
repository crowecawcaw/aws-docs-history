# Delete a transit gateway and Direct Connect association

proposal

The owner of the transit gateway can delete the Direct Connect gateway
association proposal if it is still pending acceptance. After an association
proposal is accepted, you can't delete it, but you can disassociate the transit
gateway from the Direct Connect gateway. For more information, see [Create a transit gateway association
proposal](multi-account-tgw-create-proposal.md "multi-account-tgw-create-proposal.md").

You can delete a transit gateway and Direct Connect association proposal using either the Direct Connect console or using the command line or API.

###### To delete an association proposal

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Transit gateways**
   and then select the transit gateway.
3. Choose **View details**.
4. Choose **Pending gateway associations**, select the
   association and then choose **Delete
   association**.
5. In the **Delete association proposal** dialog box,
   enter **Delete** and then choose
   **Delete**.

###### To delete a pending association proposal using the command line or API

- [delete-direct-connect-gateway-association-proposal](../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.md "../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.md") (AWS CLI)
- [DeleteDirectConnectGatewayAssociationProposal](../APIReference/API_DeleteDirectConnectGatewayAssociationProposal.md "../APIReference/API_DeleteDirectConnectGatewayAssociationProposal.md") (Direct Connect API)
