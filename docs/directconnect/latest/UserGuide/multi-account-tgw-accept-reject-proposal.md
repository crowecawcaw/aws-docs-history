# Accept or reject a transit gateway and AWS Direct Connect association proposal

If you own the Direct Connect gateway, you must accept the association
proposal in order to create the association. You also have the option of
rejecting the association proposal. You can accept or reject the association proposal using either the AWS Direct Connect console or using the command line or API.

###### To accept an association proposal

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect
   gateways**.
3. Select the Direct Connect gateway with pending proposals and then
   choose **View details**.
4. On the **Pending proposals** tab, select the proposal
   and then choose **Accept proposal**.
5. ((Optional) To specify a list of prefixes to be allowed from the transit gateway,
   add the prefixes to **Allowed prefixes**, separating
   them using commas, or entering them on separate lines.
6. Choose **Accept proposal**.

###### To reject an association proposal

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect
   gateways**.
3. Select the Direct Connect gateway with pending proposals and then
   choose **View details**.
4. On the **Pending proposals** tab, select the transit
   gateway and then choose **Reject proposal**.
5. In the **Reject proposal** dialog box, enter Delete
   and then choose **Reject proposal**.

###### To view association proposals using the command line or API

- [describe-direct-connect-gateway-association-proposals](../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.md "../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.md") (AWS CLI)
- [DescribeDirectConnectGatewayAssociationProposals](../APIReference/API_DescribeDirectConnectGatewayAssociationProposals.md "../APIReference/API_DescribeDirectConnectGatewayAssociationProposals.md") (AWS Direct Connect API)

###### To accept an association proposal using the command line or API

- [accept-direct-connect-gateway-association-proposal](../../../cli/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.md "../../../cli/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.md") (AWS CLI)
- [AcceptDirectConnectGatewayAssociationProposal](../APIReference/API_AcceptDirectConnectGatewayAssociationProposal.md "../APIReference/API_AcceptDirectConnectGatewayAssociationProposal.md") (AWS Direct Connect API)

###### To reject an association proposal using the command line or API

- [delete-direct-connect-gateway-association-proposal](../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.md "../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.md") (AWS CLI)
- [DeleteDirectConnectGatewayAssociationProposal](../APIReference/API_DeleteDirectConnectGatewayAssociationProposal.md "../APIReference/API_DeleteDirectConnectGatewayAssociationProposal.md") (AWS Direct Connect API)
