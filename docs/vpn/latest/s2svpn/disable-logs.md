

# Disable AWS Site-to-Site VPN logs
<a name="disable-logs"></a>

Disable VPN logging on a connection if you no longer want to track any activity on that connection. This action only disables logging and does not affect anything else for that connection. To enable or re-enable logging on a connection, see [Enable Site-to-Site VPN logs](enable-logs.md).

**To disable tunnel activity logging on a Site-to-Site VPN connection**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN Connections**.

1. Select the VPN connection that you want to modify from the **VPN connections** list.

1. Select **Actions**, **Modify VPN tunnel options**.

1. Select the tunnel that you want to modify by choosing the appropriate IP address from the **VPN tunnel outside IP address** list.

1. Under **Tunnel activity log**, clear **Enable**.

1. Select **Save changes**.

1. (Optional) Repeat steps 4 through 7 for the other tunnel if desired.

**To disable tunnel BGP logging on a Site-to-Site VPN connection**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN Connections**.

1. Select the VPN connection that you want to modify from the **VPN connections** list.

1. Select **Actions**, **Modify VPN tunnel options**.

1. Select the tunnel that you want to modify by choosing the appropriate IP address from the **VPN tunnel outside IP address** list.

1. Under **Tunnel BGP log**, clear **Enable**.

1. Select **Save changes**.

1. (Optional) Repeat steps 4 through 7 for the other tunnel if desired.

**To disable tunnel logging on a Site-to-Site VPN connection using the AWS command line or API**
+ [ModifyVpnTunnelOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.html) (Amazon EC2 Query API)
+ [modify-vpn-tunnel-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpn-tunnel-options.html) (AWS CLI)