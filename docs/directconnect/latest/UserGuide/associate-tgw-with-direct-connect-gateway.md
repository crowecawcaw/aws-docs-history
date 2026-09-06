

# Associate or disassociate Direct Connect with a Transit Gateway
<a name="associate-tgw-with-direct-connect-gateway"></a>

Associate or disassociate a Transit Gateway using either the Direct Connect console or using the command line or API.

**To associate a Transit Gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways** and then select the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations** and then choose **Associate gateway**.

1. For **Gateways**, choose the Transit Gateway to associate.

1. In **Allowed prefixes**, enter the prefixes (separated by a comma, or on a new line) which the Direct Connect gateway advertises to the on-premises data center. For more information on allowed prefixes, see [Allowed prefixes interactions](allowed-to-prefixes.md).

1. Choose **Associate gateway**

You can view all of the gateways that are associated with the Direct Connect gateway by choosing **Gateway associations**. 

**To disassociate a Transit Gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways** and then select the Direct Connect gateway.

1. Choose **View details**.

1. Choose **Gateway associations** and then select the Transit Gateway.

1. Choose **Disassociate**.

**To update allowed prefixes for a Transit Gateway**

You can add or remove allowed prefixes to the Transit Gateway.

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect gateways** and then choose the Direct Connect gateway you want to add or remove allowed prefixes for.

1. Choose the **Gateway associations** tab.

1. Choose the gateway you want to modify allowed prefixes for, and then choose **Edit**.

1. In **Allowed prefixes**, enter the prefixes which the Direct Connect gateway advertises to the on-premises data center. For multiple prefixes, separate each prefix by a comma or put each prefix on a new line. The prefixes you add should match the Amazon VPC CIDRs for all virtual private gateways. For more information on allowed prefixes, see [Allowed prefixes interactions](allowed-to-prefixes.md).

1. Choose **Edit association**. 

   In the **Gateway association** section the **State** displays **updating**. When complete, the **State** changes to **associated**. This might take several minutes or longer to complete.

**To associate a Transit Gateway using the command line or API**
+ [create-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway-association.html) (AWS CLI)
+ [CreateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociation.html) (Direct Connect API)

**To view the Transit Gateways associated with a Direct Connect gateway using the command line or API**
+ [describe-direct-connect-gateway-associations](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.html) (AWS CLI)
+ [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html) (Direct Connect API)

**To disassociate a Transit Gateway using the command line or API**
+ [delete-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway-association.html) (AWS CLI)
+ [DeleteDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociation.html) (Direct Connect API)

**To update allowed prefixes for a Transit Gateway using the command line or API**
+ [update-direct-connect-gateway-association](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-direct-connect-gateway-association.html) (AWS CLI)
+ [UpdateDirectConnectGatewayAssociation](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGatewayAssociation.html) (Direct Connect API)