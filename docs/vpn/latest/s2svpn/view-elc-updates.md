# Check for available AWS Site-to-Site VPN tunnel updates

After you enable the tunnel endpoint lifecycle control feature, you can view
whether a maintenance update is available for your VPN connection by using the
AWS Management Console or CLI. Checking for an available Site-to-Site VPN tunnel update does not
automatically download and deploy the update. You can choose when you want to deploy
it. For the steps to download and deploy an update, see [Accept a maintenance update](accept-update.md "accept-update.md").

###### To check for available updates using the AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left-side navigation pane, choose **Site-to-Site VPN
   Connections**.
3. Select the appropriate connection under **VPN
   connections**.
4. Select the **Tunnel details** tab.
5. Check the **Pending maintenance** column. The status will
   be either **Available** or
   **None**.

###### To check for available updates using the AWS CLI

Use the [get-vpn-tunnel-replacement-status](../../../cli/latest/reference/ec2/get-vpn-tunnel-replacement-status.md "../../../cli/latest/reference/ec2/get-vpn-tunnel-replacement-status.md") command to check for available
updates.
