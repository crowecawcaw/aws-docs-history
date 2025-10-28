# Delete an AWS Site-to-Site VPN customer gateway

If you no longer need a customer gateway, you can delete it. You can't delete a
customer gateway that's being used in a Site-to-Site VPN connection.

###### To delete a customer gateway using the console

1. In the navigation pane, choose **Customer gateways**.
2. Select the customer gateway and choose **Actions**, **Delete customer
   gateway**.
3. When prompted for confirmation, enter `delete` and then choose
   **Delete**.

###### To delete a customer gateway using the command line or API

- [DeleteCustomerGateway](../../../AWSEC2/latest/APIReference/API_DeleteCustomerGateway.md "../../../AWSEC2/latest/APIReference/API_DeleteCustomerGateway.md") (Amazon EC2 Query API)
- [delete-customer-gateway](../../../cli/latest/reference/ec2/delete-customer-gateway.md "../../../cli/latest/reference/ec2/delete-customer-gateway.md") (AWS CLI)
- [Remove-EC2CustomerGateway](../../../powershell/latest/reference/items/Remove-EC2CustomerGateway.md "../../../powershell/latest/reference/items/Remove-EC2CustomerGateway.md") (AWS Tools for Windows PowerShell)
