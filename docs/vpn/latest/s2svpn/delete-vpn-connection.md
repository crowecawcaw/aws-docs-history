

# Delete an AWS Site-to-Site VPN connection
<a name="delete-vpn-connection"></a>

After you delete your Site-to-Site VPN connection, it remains visible for a short while with a state of `deleted`, and then the entry is automatically removed.

**To delete a VPN connection using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the VPN connection and choose **Actions**, **Delete VPN connection**.

1. When prompted for confirmation, enter **delete** and then choose **Delete**.

**To delete a VPN connection using the command line or API**
+ [DeleteVpnConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnection.html) (Amazon EC2 Query API)
+ [delete-vpn-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpn-connection.html) (AWS CLI)
+ [Remove-EC2VpnConnection](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2VpnConnection.html) (AWS Tools for Windows PowerShell)