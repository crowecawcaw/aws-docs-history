

# Delete a Transit Gateway and Direct Connect association proposal
<a name="multi-account-tgw-delete-proposal"></a>

The owner of the Transit Gateway can delete the Direct Connect gateway association proposal if it is still pending acceptance. After an association proposal is accepted, you can't delete it, but you can disassociate the transit gateway from the Direct Connect gateway. For more information, see [Create a Transit Gateway association proposal](multi-account-tgw-create-proposal.md).

You can delete a Transit Gateway and Direct Connect association proposal using either the Direct Connect console or using the command line or API.

**To delete an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Transit Gateways** and then select the Transit Gateway.

1. Choose **View details**.

1. Choose **Pending gateway associations**, select the association and then choose **Delete association**.

1. In the **Delete association proposal** dialog box, enter **Delete** and then choose **Delete**.

**To delete a pending association proposal using the command line or API**
+ [delete-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociationProposal.html) (Direct Connect API)