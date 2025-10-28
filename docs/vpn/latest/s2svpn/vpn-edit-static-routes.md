# Edit static routes for an AWS Site-to-Site VPN connection

For a Site-to-Site VPN connection on a virtual private gateway that's configured for static routing,
you can add or remove static routes from your VPN configuration.

###### To add or remove a static route using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select the VPN connection.
4. Choose **Edit static routes**.
5. Add or remove routes as needed.
6. Choose **Save changes**.
7. If you have not enabled route propagation for your route table, you must manually update the
   routes in your route table to reflect the updated static IP prefixes in your VPN connection.
   For more information, see [(Virtual private gateway) Enable route propagation in your
   route table](SetUpVPNConnections.md#vpn-configure-routing "SetUpVPNConnections.md#vpn-configure-routing").
8. For a VPN connection on a transit gateway, you add, modify, or remove the static routes in
   the transit gateway route table. For more information, see [Transit gateway route tables](../../../vpc/latest/tgw/tgw-route-tables.md "../../../vpc/latest/tgw/tgw-route-tables.md") in
   _Amazon VPC Transit Gateways_.

###### To add a static route using the command line or API

- [CreateVpnConnectionRoute](../../../AWSEC2/latest/APIReference/API_CreateVpnConnectionRoute.md "../../../AWSEC2/latest/APIReference/API_CreateVpnConnectionRoute.md") (Amazon EC2 Query API)
- [create-vpn-connection-route](../../../cli/latest/reference/ec2/create-vpn-connection-route.md "../../../cli/latest/reference/ec2/create-vpn-connection-route.md") (AWS CLI)
- [New-EC2VpnConnectionRoute](../../../powershell/latest/reference/items/New-EC2VpnConnectionRoute.md "../../../powershell/latest/reference/items/New-EC2VpnConnectionRoute.md") (AWS Tools for Windows PowerShell)

###### To delete a static route using the command line or API

- [DeleteVpnConnectionRoute](../../../AWSEC2/latest/APIReference/API_DeleteVpnConnectionRoute.md "../../../AWSEC2/latest/APIReference/API_DeleteVpnConnectionRoute.md") (Amazon EC2 Query API)
- [delete-vpn-connection-route](../../../cli/latest/reference/ec2/delete-vpn-connection-route.md "../../../cli/latest/reference/ec2/delete-vpn-connection-route.md") (AWS CLI)
- [Remove-EC2VpnConnectionRoute](../../../powershell/latest/reference/items/Remove-EC2VpnConnectionRoute.md "../../../powershell/latest/reference/items/Remove-EC2VpnConnectionRoute.md") (AWS Tools for Windows PowerShell)
