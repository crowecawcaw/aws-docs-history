# Create an AWS Direct Connect gateway

You can create a Direct Connect gateway in any supported Region using either the AWS Direct Connect
console or using the command line or API.

###### To create a Direct Connect gateway

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect
   Gateways**.
3. Choose **Create Direct Connect gateway**.
4. Specify the following information, and choose **Create Direct
   Connect gateway**.
   - **Name**: Enter a name to help you identify the
     Direct Connect gateway.
   - **Amazon side ASN**: Specify the ASN for the
     Amazon side of the BGP session. The ASN must be in the 64,512 to
     65,534 range or 4,200,000,000 to 4,294,967,294 range.

   ###### Note

   If you want to create a Direct Connect gateway to use with an AWS Cloud WAN core
   network. The ASN must not be in the same range as the ASN of the core
   network.

###### To create a Direct Connect gateway using the command line or API

- [create-direct-connect-gateway](../../../cli/latest/reference/directconnect/create-direct-connect-gateway.md "../../../cli/latest/reference/directconnect/create-direct-connect-gateway.md") (AWS CLI)
- [CreateDirectConnectGateway](../APIReference/API_CreateDirectConnectGateway.md "../APIReference/API_CreateDirectConnectGateway.md") (AWS Direct Connect API)
