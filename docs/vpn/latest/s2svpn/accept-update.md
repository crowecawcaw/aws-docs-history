# Accept an AWS Site-to-Site VPN tunnel maintenance update

When a maintenance update is available, you can accept it using the AWS Management Console or
CLI. You can choose to accept the Site-to-Site VPN tunnel maintenance update at a time that's
convenient for you. Once you accept the maintenance update it will be deployed.

###### Note

If you don't accept the maintenance update, AWS will automatically deploy it
during a regular maintenance update cycle.

###### To accept an available maintenance update using the AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the left-side navigation pane, choose **Site-to-Site VPN
   Connections**.
3. Select the appropriate connection under **VPN
   connections**.
4. Choose **Actions**, then **Replace VPN
   Tunnel**.
5. Select the specific tunnel that you want to replace by choosing the
   appropriate **VPN tunnel outside IP address**.
6. Choose **Replace**.

###### To accept an available maintenance update using the AWS CLI

Use the [replace-vpn-tunnel](../../../cli/latest/reference/ec2/replace-vpn-tunnel.md "../../../cli/latest/reference/ec2/replace-vpn-tunnel.md") command to accept an available maintenance
update.
