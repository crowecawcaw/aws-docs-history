# Delete an AWS Site-to-Site VPN connection

After you delete your Site-to-Site VPN connection, it remains visible for a short while with a
state of `deleted`, and then the entry is automatically removed.

###### To delete a VPN connection using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select the VPN connection and choose **Actions**, **Delete VPN
   connection**.
4. When prompted for confirmation, enter `delete` and then choose
   **Delete**.

###### To delete a VPN connection using the command line or API

- [DeleteVpnConnection](../../../AWSEC2/latest/APIReference/API_DeleteVpnConnection.md "../../../AWSEC2/latest/APIReference/API_DeleteVpnConnection.md") (Amazon EC2 Query API)
- [delete-vpn-connection](../../../cli/latest/reference/ec2/delete-vpn-connection.md "../../../cli/latest/reference/ec2/delete-vpn-connection.md") (AWS CLI)
- [Remove-EC2VpnConnection](../../../powershell/latest/reference/items/Remove-EC2VpnConnection.md "../../../powershell/latest/reference/items/Remove-EC2VpnConnection.md") (AWS Tools for Windows PowerShell)
