# Delete a Client VPN attachment in AWS Transit Gateway

###### To delete a Client VPN attachment using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit gateways**.
3. Choose **Transit gateway attachments**.
4. Select the Client VPN attachment that you want to delete.
5. Choose **Actions**, **Delete transit gateway attachment**.
6. When prompted for confirmation, enter `delete` and choose **Delete**.
   The Client VPN attachment enters the **Deleting** state and will be removed from your account. This process may take some time to complete.

###### To delete a Client VPN attachment using the AWS CLI

Use the [delete-transit-gateway-client-vpn-attachment](../../../cli/latest/reference/ec2/delete-transit-gateway-client-vpn-attachment.md "../../../cli/latest/reference/ec2/delete-transit-gateway-client-vpn-attachment.md") command.
