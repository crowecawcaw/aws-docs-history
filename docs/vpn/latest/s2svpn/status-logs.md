

# View AWS Site-to-Site VPN logs configuration
<a name="status-logs"></a>

View the activity log for a Site-to-Site VPN connection. Here you can view details about the configuration such encryption algorithms, or whether tunnel VPN logs are enabled. You can also view the tunnel state. This helps you to better track any issues or conflicts you might have with a VPN connection. 

**To view current tunnel logging settings**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the VPN connection that you want to view from the **VPN connections** list.

1. Choose the **Tunnel details** tab.

1. Expand the **Tunnel 1 options** and **Tunnel 2 options** sections to view all tunnel configuration details.

1. You can view the current status **Tunnel VPN log** feature, and the currently configured CloudWatch log group (if any) under **CloudWatch log group for tunnel VPN log** and the log output format under **Output format for tunnel VPN log**.

1. You can view the current status **Tunnel BGP log** feature, and the currently configured CloudWatch log group (if any) under **CloudWatch log group for tunnel VPN log** and the log output format under **Output format for tunnel BGP log**.

**To view current tunnel logging settings on a Site-to-Site VPN connection using the AWS command line or API**
+ [DescribeVpnConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html) (Amazon EC2 Query API)
+ [describe-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpn-connections.html) (AWS CLI)