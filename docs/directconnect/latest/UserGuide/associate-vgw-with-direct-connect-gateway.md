

# Associate or disassociate Direct Connect virtual private gateways
<a name="associate-vgw-with-direct-connect-gateway"></a>

You can associate or disassociate a virtual private gateway and Direct Connect gateway using either the Direct Connect console or using the command line or API. The account owner of the virtual private gateway performs these operations.

**To associate a virtual private gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways** and then choose the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations**, and then choose **Associate gateway**.

1. For **Gateways**, choose the virtual private gateways to associate, and then choose **Associate gateway**.

You can view all of the virtual private gateways that are associated with the Direct Connect gateway by choosing **Gateway associations**. 

**To disassociate a virtual private gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways** and then select the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations** and then select the virtual private gateway.

1. Choose **Disassociate**.

**To associate a virtual private gateway using the command line or API**
+ [create-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway-association.html) (AWS CLI)
+ [CreateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociation.html) (Direct Connect API)

**To view the virtual private gateways associated with a Direct Connect gateway using the command line or API**
+ [describe-direct-connect-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.html) (AWS CLI)
+ [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html) (Direct Connect API)

**To disassociate a virtual private gateway using the command line or API**
+ [delete-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociation.html) (Direct Connect API)