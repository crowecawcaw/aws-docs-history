

# Enable AWS Site-to-Site VPN logs
<a name="enable-logs"></a>

Enable Site-to-Site VPN logs to log VPN activity, such as tunnel state and other details. You can enable logging on a new connection or modify an existing connection to start logging activity. If you want to disable logging for a connection, see [Disable Site-to-Site VPN logs](disable-logs.md).

**Note**  
When you enable Site-to-Site VPN logs for an existing VPN connection tunnel, your connectivity over that tunnel can be interrupted for several minutes. However, each VPN connection offers two tunnels for high availability, so you can enable logging on one tunnel at a time while maintaining connectivity over the tunnel not being modified. For more information, see [AWS Site-to-Site VPN tunnel endpoint replacements](endpoint-replacements.md).

**To enable VPN logging during creation of a new Site-to-Site VPN connection**  
Follow the procedure [Step 5: Create a VPN connection](SetUpVPNConnections.md#vpn-create-vpn-connection). During Step 9 **Tunnel Options**, you can specify all the options you want to use for both tunnels, including **VPN logging** options. For more information about these options, see [Tunnel options for your AWS Site-to-Site VPN connection](VPNTunnels.md).

**To enable tunnel logging on a new Site-to-Site VPN connection using the AWS command line or API**
+ [CreateVpnConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpnConnection.html) (Amazon EC2 Query API)
+ [create-vpn-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpn-connection.html) (AWS CLI)

**To enable tunnel activity logging on an existing Site-to-Site VPN connection**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the VPN connection that you want to modify from the **VPN connections** list.

1. Select **Actions**, **Modify VPN tunnel options**.

1. Select the tunnel that you want to modify by choosing the appropriate IP address from the **VPN tunnel outside IP address** list.

1. Under **Tunnel activity log**, select **Enable**.

1. Under **Amazon CloudWatch log group**, select the Amazon CloudWatch log group where you want the logs to be sent.

1. (Optional) Under **Output format**, choose the desired format for the log output, either **json** or **text**.

1. Select **Save changes**.

1. (Optional) Repeat steps 4 through 9 for the other tunnel if desired.

**To enable tunnel BGP logging on an existing Site-to-Site VPN connection**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the VPN connection that you want to modify from the **VPN connections** list.

1. Select **Actions**, **Modify VPN tunnel options**.

1. Select the tunnel that you want to modify by choosing the appropriate IP address from the **VPN tunnel outside IP address** list.

1. Under **Tunnel BGP log**, select **Enable**.

1. Under **Amazon CloudWatch log group**, select the Amazon CloudWatch log group where you want the logs to be sent.

1. (Optional) Under **Output format**, choose the desired format for the log output, either **json** or **text**.

1. Select **Save changes**.

1. (Optional) Repeat steps 4 through 9 for the other tunnel if desired.

**To enable tunnel logging on an existing Site-to-Site VPN connection using the AWS command line or API**
+ [ModifyVpnTunnelOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.html) (Amazon EC2 Query API)
+ [modify-vpn-tunnel-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpn-tunnel-options.html) (AWS CLI)