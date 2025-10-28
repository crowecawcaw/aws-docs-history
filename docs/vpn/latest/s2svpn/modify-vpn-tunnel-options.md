# Modify AWS Site-to-Site VPN tunnel options

You can modify the tunnel options for the VPN tunnels in your Site-to-Site VPN connection. You can
modify one VPN tunnel at a time.

###### Important

When you modify a VPN tunnel, connectivity over the tunnel is interrupted for up to several
minutes. Ensure that you plan for the expected downtime.

###### To modify the VPN tunnel options using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Select the Site-to-Site VPN connection, and choose **Actions**, **Modify VPN
   tunnel options**.
4. For **VPN tunnel outside IP address**, choose the tunnel endpoint
   IP of the VPN tunnel.
5. Choose or enter new values for the tunnel options as needed. For more information
   about the tunnel options, see [VPN tunnel options](VPNTunnels.md "VPNTunnels.md").

###### Note

Some tunnel options have multiple default values. Click to remove any default
value. That default value is then removed from the tunnel option. 6. Choose **Save changes**.

###### To modify the VPN tunnel options using the command line or API

- (AWS CLI) Use [describe-vpn-connections](../../../cli/latest/reference/ec2/describe-vpn-connections.md "../../../cli/latest/reference/ec2/describe-vpn-connections.md") to view the current tunnel options, and [modify-vpn-tunnel-options](../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md "../../../cli/latest/reference/ec2/modify-vpn-tunnel-options.md") to modify the tunnel options.
- (Amazon EC2 Query API) Use [DescribeVpnConnections](../../../AWSEC2/latest/APIReference/API_DescribeVpnConnections.md "../../../AWSEC2/latest/APIReference/API_DescribeVpnConnections.md") to view the current tunnel options, and [ModifyVpnTunnelOptions](../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md "../../../AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.md") to modify the tunnel options.
