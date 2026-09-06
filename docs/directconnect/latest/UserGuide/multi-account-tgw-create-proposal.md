

# Create a Transit Gateway and Direct Connect association proposal
<a name="multi-account-tgw-create-proposal"></a>

If you own the Transit Gateway, you must create the association proposal. The owner of the Direct Connect gateway must share the ID of the Direct Connect gateway and the ID of its AWS account. After you create the proposal, the owner of the Direct Connect gateway must accept it in order for you to gain access to the on-premises network over Direct Connect. You can create an association proposal using either the Direct Connect console or using the command line or API.

**To create an association proposal**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Transit Gateways** and then select the Transit Gateway.

1. Choose **View details**.

1. Choose **Direct Connect gateway associations** and then choose **Associate Direct Connect gateway**.

1. Under **Association account type**, for **Account owner**, choose **Another account**.

1. For **Direct Connect gateway owner**, enter the ID of the account that owns the Direct Connect gateway.

1. Under **Association settings**, do the following:

   1. For **Direct Connect gateway ID**, enter the ID of the Direct Connect gateway.

   1. For **Virtual interface owner**, enter the ID of the account that owns the virtual interface for the association.

   1. (Optional) To specify a list of prefixes to be allowed from the Transit Gateway, add the prefixes to **Allowed prefixes**, separating them using commas, or entering them on separate lines.

1. Choose **Associate Direct Connect gateway**.

**To create an association proposal using the command line or API**
+ [create-direct-connect-gateway-association-proposal](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.html) (AWS CLI)
+ [CreateDirectConnectGatewayAssociationProposal](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociationProposal.html) (Direct Connect API)