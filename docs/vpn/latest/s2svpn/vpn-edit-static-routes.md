

# Edit static routes for an AWS Site-to-Site VPN connection
<a name="vpn-edit-static-routes"></a>

For a Site-to-Site VPN connection on a virtual private gateway that's configured for static routing, you can add or remove static routes from your VPN configuration. 

**To add or remove a static route using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the VPN connection.

1. Choose **Edit static routes**.

1. Add or remove routes as needed.

1. Choose **Save changes**.

1. If you have not enabled route propagation for your route table, you must manually update the routes in your route table to reflect the updated static IP prefixes in your VPN connection. For more information, see [(Virtual private gateway) Enable route propagation in your route table](SetUpVPNConnections.md#vpn-configure-routing).

1. For a VPN connection on a transit gateway, you add, modify, or remove the static routes in the transit gateway route table. For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) in *Amazon VPC Transit Gateways*.

**To add a static route using the command line or API**
+ [CreateVpnConnectionRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnectionRoute.html) (Amazon EC2 Query API)
+ [create-vpn-connection-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpn-connection-route.html) (AWS CLI)
+ [New-EC2VpnConnectionRoute](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpnConnectionRoute.html) (AWS Tools for Windows PowerShell)

**To delete a static route using the command line or API**
+ [DeleteVpnConnectionRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnectionRoute.html) (Amazon EC2 Query API)
+ [delete-vpn-connection-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpn-connection-route.html) (AWS CLI)
+ [Remove-EC2VpnConnectionRoute](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2VpnConnectionRoute.html) (AWS Tools for Windows PowerShell)