# Associate or disassociate

AWS Direct Connect with a transit gateway

Associate or disassociate a transit gateway using either the AWS Direct Connect console or using the command line or API.

###### To associate a transit gateway

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect
   Gateways** and then select the Direct Connect gateway.
3. Choose **View details**.
4. Choose **Gateway associations** and then choose
   **Associate gateway**.
5. For **Gateways**, choose the transit gateway to associate.
6. In **Allowed prefixes**, enter the prefixes (separated by
   a comma, or on a new line) which the Direct Connect gateway advertises to
   the on-premises data center. For more information on allowed prefixes, see
   [Allowed prefixes interactions](allowed-to-prefixes.md "allowed-to-prefixes.md").
7. Choose **Associate gateway**
   You can view all of the gateways that are associated with the Direct Connect
   gateway by choosing **Gateway associations**.

###### To disassociate a transit gateway

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect
   gateways** and then select the Direct Connect gateway.
3. Choose **View details**.
4. Choose **Gateway associations** and then select the
   transit gateway.
5. Choose **Disassociate**.

###### To update allowed prefixes for a transit gateway

You can add or remove allowed prefixes to the transit gateway.

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect gateways**
   and then choose the Direct Connect gateway you want to add or remove allowed
   prefixes for.
3. Choose the **Gateway associations** tab.
4. Choose the gateway you want to modify allowed prefixes for, and then choose
   **Edit**.
5. In **Allowed prefixes**, enter the prefixes which the
   Direct Connect gateway advertises to the on-premises data center. For
   multiple prefixes, separate each prefix by a comma or put each prefix on a
   new line. The prefixes you add should match the Amazon VPC CIDRs for all virtual
   private gateways. For more information on allowed prefixes, see [Allowed prefixes interactions](allowed-to-prefixes.md "allowed-to-prefixes.md").
6. Choose **Edit association**.

In the **Gateway association** section the
**State** displays **updating**. When
complete, the **State** changes to **associated**.
This might take several minutes or longer to complete.

###### To associate a transit gateway using the command line or API

- [create-direct-connect-gateway-association](../../../cli/latest/reference/directconnect/create-direct-connect-gateway-association.md "../../../cli/latest/reference/directconnect/create-direct-connect-gateway-association.md")
  (AWS CLI)
- [CreateDirectConnectGatewayAssociation](../APIReference/API_CreateDirectConnectGatewayAssociation.md "../APIReference/API_CreateDirectConnectGatewayAssociation.md")
  (AWS Direct Connect API)

###### To view the transit gateways associated with a Direct Connect gateway using the command

line or API

- [describe-direct-connect-gateway-associations](../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.md "../../../cli/latest/reference/directconnect/describe-direct-connect-gateway-associations.md")
  (AWS CLI)
- [DescribeDirectConnectGatewayAssociations](../APIReference/API_DescribeDirectConnectGatewayAssociations.md "../APIReference/API_DescribeDirectConnectGatewayAssociations.md")
  (AWS Direct Connect API)

###### To disassociate a transit gateway using the command line or API

- [delete-direct-connect-gateway-association](../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association.md "../../../cli/latest/reference/directconnect/delete-direct-connect-gateway-association.md")
  (AWS CLI)
- [DeleteDirectConnectGatewayAssociation](../APIReference/API_DeleteDirectConnectGatewayAssociation.md "../APIReference/API_DeleteDirectConnectGatewayAssociation.md")
  (AWS Direct Connect API)

###### To update allowed prefixes for a transit gateway using the command line or API

- [update-direct-connect-gateway-association](../../../cli/latest/reference/directconnect/update-direct-connect-gateway-association.md "../../../cli/latest/reference/directconnect/update-direct-connect-gateway-association.md") (AWS CLI)
- [UpdateDirectConnectGatewayAssociation](../APIReference/API_UpdateDirectConnectGatewayAssociation.md "../APIReference/API_UpdateDirectConnectGatewayAssociation.md") (AWS Direct Connect API)
