# Associate or

disassociate AWS Direct Connect virtual private gateways

You can associate or disassociate a virtual private gateway and Direct Connect
gateway using either the AWS Direct Connect console or using the command line or API. The account owner of the virtual private gateway performs these
operations.

###### To associate a virtual private gateway

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect gateways** and
   then choose the Direct Connect gateway.
3. Choose **View details**.
4. Choose **Gateway associations**, and then choose
   **Associate gateway**.
5. For **Gateways**, choose the virtual private gateways to
   associate, and then choose **Associate gateway**.
   You can view all of the virtual private gateways that are associated with the
   Direct Connect gateway by choosing **Gateway associations**.

###### To disassociate a virtual private gateway

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect
   Gateways** and then select the Direct Connect gateway.
3. Choose **View details**.
4. Choose **Gateway associations** and then select the
   virtual private gateway.
5. Choose **Disassociate**.

###### To associate a virtual private gateway using the command line or API

- [create-direct-connect-gateway-association](../../../cli/latest/reference/directconnect/create-direct-connect-gateway-association.md "../../../cli/latest/reference/directconnect/create-direct-connect-gateway-association.md")
  (AWS CLI)
- [CreateDirectConnectGatewayAssociation](../APIReference/API_CreateDirectConnectGatewayAssociation.md "../APIReference/API_CreateDirectConnectGatewayAssociation.md")
  (AWS Direct Connect API)

###### To view the virtual private gateways associated with a Direct Connect gateway

using the command line or API

- [describe-direct-connect-gateway-associations](../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.md "../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.md")
  (AWS CLI)
- [DescribeDirectConnectGatewayAssociations](../APIReference/API_DescribeDirectConnectGatewayAssociations.md "../APIReference/API_DescribeDirectConnectGatewayAssociations.md")
  (AWS Direct Connect API)

###### To disassociate a virtual private gateway using the command line or

API

- [delete-direct-connect-gateway-association](../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association.md "../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association.md")
  (AWS CLI)
- [DeleteDirectConnectGatewayAssociation](../APIReference/API_DeleteDirectConnectGatewayAssociation.md "../APIReference/API_DeleteDirectConnectGatewayAssociation.md")
  (AWS Direct Connect API)
