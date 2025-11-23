# Disable AWS Site-to-Site VPN logs

Disable VPN logging on a connection if you no longer want to track any activity on
that connection. This action only disables logging and does not affect anything else
for that connection. To enable or re-enable logging on a connection, see [Enable Site-to-Site VPN logs](enable-logs.md "enable-logs.md").

###### To disable tunnel activity logging on a Site-to-Site VPN connection

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN
   Connections**.
3. Select the VPN connection that you want to modify from the **VPN
   connections** list.
4. Select **Actions**, **Modify VPN tunnel
   options**.
5. Select the tunnel that you want to modify by choosing the appropriate IP
   address from the **VPN tunnel outside IP address**
   list.
6. Under **Tunnel activity log**, clear **Enable**.
7. Select **Save changes**.
8. (Optional) Repeat steps 4 through 7 for the other tunnel if desired.

###### To disable tunnel BGP logging on a Site-to-Site VPN connection

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN
   Connections**.
3. Select the VPN connection that you want to modify from the **VPN
   connections** list.
4. Select **Actions**, **Modify VPN tunnel
   options**.
5. Select the tunnel that you want to modify by choosing the appropriate IP
   address from the **VPN tunnel outside IP address**
   list.
6. Under **Tunnel BGP log**, clear **Enable**.
7. Select **Save changes**.
8. (Optional) Repeat steps 4 through 7 for the other tunnel if desired.

###### To disable tunnel logging on a Site-to-Site VPN connection using the AWS command line or API

- [ModifyVpnTunnelOptions](../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md") (Amazon EC2 Query API)
- [modify-vpn-tunnel-options](../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md "../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md") (AWS CLI)
