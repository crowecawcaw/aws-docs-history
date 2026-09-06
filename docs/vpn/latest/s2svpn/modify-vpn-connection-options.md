

# Modify AWS Site-to-Site VPN connection options
<a name="modify-vpn-connection-options"></a>

You can modify the connection options for your Site-to-Site VPN connection. You can modify the following options:
+ The IPv4 CIDR ranges on the local (customer gateway) side and the remote (AWS) side of the VPN connection that can communicate over the VPN tunnels. The default is `0.0.0.0/0` for both ranges.
+ The IPv6 CIDR ranges on the local (customer gateway) and the remote (AWS) side of the VPN connection that can communicate over the VPN tunnels. The default is `::/0` for both ranges.
+ The tunnel bandwidth for the VPN connection. `standard` supports up to 1.25 Gbps per tunnel, while `large` supports up to 5 Gbps per tunnel. Large bandwidth is only available for VPN connections attached to a transit gateway or to Cloud WAN. For more information, see [Large Bandwidth Tunnels](VPNTunnels.md#large-bandwidth-tunnels).

When you modify the VPN connection options, the VPN endpoint IP addresses on the AWS side do not change, and the tunnel options do not change. Your VPN connection will be temporarily unavailable for a brief period while the VPN connection is updated.

**To modify the VPN connection options using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select your VPN connection, and choose **Actions**, **Modify VPN connection options**.

1. Enter new CIDR ranges as needed.

1. Choose **Save changes**.

**To modify the VPN connection options using the command line or API**
+ [modify-vpn-connection-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpn-connection-options.html) (AWS CLI)
+ [ModifyVpnConnectionOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnConnectionOptions.html) (Amazon EC2 Query API)

## Modify tunnel bandwidth
<a name="modify-vpn-connection-options-tunnel-bandwidth"></a>

You can modify the tunnel bandwidth of existing VPN connections, switching between `standard` (up to 1.25 Gbps per tunnel) and `large` (up to 5 Gbps per tunnel) without recreating VPN connections. This allows you to perform an in-place modification to scale your tunnel bandwidth up or down based on your requirements.

The ability to modify tunnel bandwidth is available in the following AWS Regions:
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Mumbai)
+ Asia Pacific (New Zealand)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Sydney)
+ Asia Pacific (Taipei)
+ Asia Pacific (Thailand)
+ Asia Pacific (Tokyo)
+ Europe (Frankfurt)
+ Europe (London)
+ Europe (Paris)
+ Europe (Spain)
+ Europe (Stockholm)
+ Mexico (Central)
+ South America (São Paulo)
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ AWS GovCloud (US-West)

In regions where modifying tunnel bandwidth is not supported, you'll need to first delete the VPN connection, and then create a new VPN connection and set the tunnel bandwidth to **Large**.