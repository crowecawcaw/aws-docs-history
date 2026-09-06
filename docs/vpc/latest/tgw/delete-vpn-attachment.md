

# Delete a VPN attachment in AWS Transit Gateway
<a name="delete-vpn-attachment"></a>

**To delete a VPN attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the VPN attachment.

1. Choose the resource ID of the VPN connection to navigate to the **VPN Connections** page.

1. Choose **Actions**, **Delete**.

1. When prompted for confirmation, choose **Delete**.

**To delete a VPN attachment using the AWS CLI**  
Use the [delete-vpn-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpn-connection.html) command.