# Create a transit gateway and Direct Connect association

proposal

If you own the transit gateway, you must create the association proposal. The transit gateway must
be attached to a VPC or VPN in your AWS account. The owner of the Direct Connect
gateway must share the ID of the Direct Connect gateway and the ID of its AWS
account. After you create the proposal, the owner of the Direct Connect gateway
must accept it in order for you to gain access to the on-premises network over
Direct Connect. You can create an association proposal using either the Direct Connect console or using the command line or API.

###### To create an association proposal

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Transit gateways**
   and then select the transit gateway.
3. Choose **View details**.
4. Choose **Direct Connect gateway associations** and
   then choose **Associate Direct Connect
   gateway**.
5. Under **Association account type**, for **Account
   owner**, choose **Another account**.
6. For **Direct Connect gateway owner**, enter the ID of
   the account that owns the Direct Connect gateway.
7. Under **Association settings**, do the following:
   1. For **Direct Connect gateway ID**, enter the ID
      of the Direct Connect gateway.
   2. For **Virtual interface owner**, enter the ID of
      the account that owns the virtual interface for the
      association.
   3. (Optional) To specify a list of prefixes to be allowed from
      the transit gateway, add the prefixes to **Allowed
      prefixes**, separating them using commas, or
      entering them on separate lines.

8. Choose **Associate Direct Connect gateway**.

###### To create an association proposal using the command line or API

- [create-direct-connect-gateway-association-proposal](../../../cli/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.md "../../../cli/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.md") (AWS CLI)
- [CreateDirectConnectGatewayAssociationProposal](../APIReference/API_CreateDirectConnectGatewayAssociationProposal.md "../APIReference/API_CreateDirectConnectGatewayAssociationProposal.md") (Direct Connect API)
