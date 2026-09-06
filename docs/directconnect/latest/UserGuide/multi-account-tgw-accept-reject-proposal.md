

# Accept or reject a Transit Gateway and Direct Connect association proposal
<a name="multi-account-tgw-accept-reject-proposal"></a>

If you own the Direct Connect gateway, you must accept the association proposal in order to create the association. You also have the option of rejecting the association proposal. You can accept or reject the association proposal using either the Direct Connect console or using the command line or API.

**To accept an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways**.

1. Select the Direct Connect gateway with pending proposals and then choose **View details**.

1. On the **Pending proposals** tab, select the proposal and then choose **Accept proposal**.

1. ((Optional) To specify a list of prefixes to be allowed from the Transit Gateway, add the prefixes to **Allowed prefixes**, separating them using commas, or entering them on separate lines.

1. Choose **Accept proposal**.

**To reject an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways**.

1. Select the Direct Connect gateway with pending proposals and then choose **View details**.

1. On the **Pending proposals** tab, select the transit gateway and then choose **Reject proposal**.

1. In the **Reject proposal** dialog box, enter Delete and then choose **Reject proposal**.

**To view association proposals using the command line or API**
+ [describe-direct-connect-gateway-association-proposals](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.htm) (AWS CLI)
+ [DescribeDirectConnectGatewayAssociationProposals](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociationProposals.html) (Direct Connect API)

**To accept an association proposal using the command line or API**
+ [accept-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [AcceptDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AcceptDirectConnectGatewayAssociationProposal.html) (Direct Connect API)

**To reject an association proposal using the command line or API**
+ [delete-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociationProposal.html) (Direct Connect API)