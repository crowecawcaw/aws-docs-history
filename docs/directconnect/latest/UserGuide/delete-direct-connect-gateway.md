# Delete an AWS Direct Connect

gateway

If you no longer require a Direct Connect gateway, you can delete it. You must first
disassociate all associated virtual private gateways and delete the attached private virtual
interface. Once you've disassociated any associated virtual private gateways and deleted any
attached private virtual interfaces, you can delete the Direct Connect gateway using either the AWS Direct Connect console or using the command line or API.

- For the steps to disassociate a virutal private gateway, see [Associate or disassociate virtual private gateways](associate-vgw-with-direct-connect-gateway.md "associate-vgw-with-direct-connect-gateway.md").
- For the steps to delete a virtual interface, see [Delete a virtual interface](deletevif.md "deletevif.md").

###### To delete a Direct Connect gateway

1. Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2. In the navigation pane, choose **Direct Connect
   Gateways**.
3. Select the gateways and choose **Delete**.

###### To delete a Direct Connect gateway using the command line or API

- [delete-direct-connect-gateway](../../../cli/latest/reference/directconnect/delete-direct-connect-gateway.md "../../../cli/latest/reference/directconnect/delete-direct-connect-gateway.md") (AWS CLI)
- [DeleteDirectConnectGateway](../APIReference/API_DeleteDirectConnectGateway.md "../APIReference/API_DeleteDirectConnectGateway.md") (AWS Direct Connect API)
