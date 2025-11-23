# Enable AWS Site-to-Site VPN logs

Enable Site-to-Site VPN logs to log VPN activity, such as tunnel state and other details. You can enable
logging on a new connection or modify an existing connection to start logging
activity. If you want to disable logging for a connection, see [Disable Site-to-Site VPN logs](disable-logs.md "disable-logs.md").

###### Note

When you enable Site-to-Site VPN logs for an existing VPN connection tunnel, your
connectivity over that tunnel can be interrupted for several minutes. However, each VPN
connection offers two tunnels for high availability, so you can enable
logging on one tunnel at a time while maintaining connectivity over the tunnel not being modified.
For more information, see [AWS Site-to-Site VPN tunnel endpoint replacements](endpoint-replacements.md "endpoint-replacements.md").

###### To enable VPN logging during creation of a new Site-to-Site VPN connection

Follow the procedure [Step 5: Create a VPN connection](SetUpVPNConnections.md#vpn-create-vpn-connection "SetUpVPNConnections.md#vpn-create-vpn-connection"). During Step 9 **Tunnel
Options**, you can specify all the options you want to use for both
tunnels, including **VPN logging** options. For more
information about these options, see [Tunnel options for your AWS Site-to-Site VPN connection](VPNTunnels.md "VPNTunnels.md").

###### To enable tunnel logging on a new Site-to-Site VPN connection using the AWS command

line or API

- [CreateVpnConnection](../../../AWSEC2/latest/APIReference/API_CreateVpnConnection.md "../../../AWSEC2/latest/APIReference/API_CreateVpnConnection.md") (Amazon EC2 Query API)
- [create-vpn-connection](../../../cli/latest/reference/ec2/create-vpn-connection.md "../../../cli/latest/reference/ec2/create-vpn-connection.md") (AWS CLI)

###### To enable tunnel activity logging on an existing Site-to-Site VPN connection

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN
   connections**.
3. Select the VPN connection that you want to modify from the **VPN
   connections** list.
4. Select **Actions**, **Modify VPN tunnel
   options**.
5. Select the tunnel that you want to modify by choosing the appropriate IP
   address from the **VPN tunnel outside IP address**
   list.
6. Under **Tunnel activity log**, select
   **Enable**.
7. Under **Amazon CloudWatch log group**, select the Amazon CloudWatch log
   group where you want the logs to be sent.
8. (Optional) Under **Output format**, choose the desired
   format for the log output, either **json** or
   **text**.
9. Select **Save changes**.
10. (Optional) Repeat steps 4 through 9 for the other tunnel if
    desired.

###### To enable tunnel BGP logging on an existing Site-to-Site VPN connection

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN
   connections**.
3. Select the VPN connection that you want to modify from the **VPN
   connections** list.
4. Select **Actions**, **Modify VPN tunnel
   options**.
5. Select the tunnel that you want to modify by choosing the appropriate IP
   address from the **VPN tunnel outside IP address**
   list.
6. Under **Tunnel BGP log**, select
   **Enable**.
7. Under **Amazon CloudWatch log group**, select the Amazon CloudWatch log
   group where you want the logs to be sent.
8. (Optional) Under **Output format**, choose the desired
   format for the log output, either **json** or
   **text**.
9. Select **Save changes**.
10. (Optional) Repeat steps 4 through 9 for the other tunnel if
    desired.

###### To enable tunnel logging on an existing Site-to-Site VPN connection using the AWS command line

or API

- [ModifyVpnTunnelOptions](../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md") (Amazon EC2 Query API)
- [modify-vpn-tunnel-options](../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md "../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md") (AWS CLI)
