

# Check for available AWS Site-to-Site VPN tunnel updates
<a name="view-elc-updates"></a>

After you enable the tunnel endpoint lifecycle control feature, you can view whether a maintenance update is available for your VPN connection by using the AWS Management Console or CLI. Checking for an available Site-to-Site VPN tunnel update does not automatically download and deploy the update. You can choose when you want to deploy it. For the steps to download and deploy an update, see [Accept a maintenance update](accept-update.md). 

**To check for available updates using the AWS Management Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left-side navigation pane, choose **Site-to-Site VPN Connections**.

1. Select the appropriate connection under **VPN connections**.

1. Select the **Tunnel details** tab.

1. Check the **Pending maintenance** column. The status will be either **Available** or **None**.

**To check for available updates using the AWS CLI**  
Use the [get-vpn-tunnel-replacement-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-vpn-tunnel-replacement-status.html) command to check for available updates.