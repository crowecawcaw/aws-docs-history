

# Verify a Direct Connect gateway association to an AWS Cloud WAN core network
<a name="edit-cloudwan-with-direct-connect-gateway"></a>

You can verify the association of a Direct Connect gateway to a Cloud WAN core network using the Direct Connect console or the Direct Connect API or command line.

**To verify a Direct Connect gateway association to a Cloud WAN core network using the console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Direct Connect gateways** in the navigation pane.

1. Choose the Direct Connect gateway attachment that you want to view the association for.

1. Choose the **Gateway associations** tab. 
   + The **ID** column displays the core network ID that the Direct Connect gateway is associated with.
   + The **State** column displays **associated**.
   + The **Association type** column displays **Cloud WAN Core Network**.

**To verify a Direct Connect gateway association to a Cloud WAN core network using the command line or API**
+ [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html.html) (Direct Connect API)
+ [describe-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-association.html) (AWS CLI)