

# Delete an AWS Site-to-Site VPN customer gateway
<a name="delete-cgw"></a>

If you no longer need a customer gateway, you can delete it. You can't delete a customer gateway that's being used in a Site-to-Site VPN connection.

**To delete a customer gateway using the console**

1. In the navigation pane, choose **Customer gateways**.

1. Select the customer gateway and choose **Actions**, **Delete customer gateway**.

1. When prompted for confirmation, enter **delete** and then choose **Delete**.

**To delete a customer gateway using the command line or API**
+ [DeleteCustomerGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCustomerGateway.html) (Amazon EC2 Query API)
+ [delete-customer-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-customer-gateway.html) (AWS CLI)
+ [Remove-EC2CustomerGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2CustomerGateway.html) (AWS Tools for Windows PowerShell)