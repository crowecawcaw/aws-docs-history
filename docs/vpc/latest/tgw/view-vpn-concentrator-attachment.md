# View a VPN Concentrator attachment in AWS Transit Gateway

###### To view your VPN Concentrator attachments using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Attachments**.
3. In the **Resource type** column, look for **VPN Concentrator**. These are the VPN Concentrator attachments.
4. Choose an attachment to view its details.

###### To view VPN connections on a VPN Concentrator using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Site-to-Site VPN Connections**.
3. In the list of VPN connections, identify connections that show a VPN Concentrator ID in the **Transit Gateway ID** column. These are the VPN connections hosted on VPN Concentrators.
4. Choose a VPN connection to view its details.

###### To view your VPN Concentrator attachments using the AWS CLI

Use the [describe-vpn-concentrator](../../../cli/latest/reference/ec2/describe-vpn-concentrator.md "../../../cli/latest/reference/ec2/describe-vpn-concentrator.md") command to view VPN Concentrator details, or use the [describe-transit-gateway-attachments](../../../cli/latest/reference/ec2/describe-transit-gateway-attachments.md "../../../cli/latest/reference/ec2/describe-transit-gateway-attachments.md") command with a filter for resource type `vpn-concentrator`.

###### To view VPN connections on a VPN Concentrator using the AWS CLI

Use the [describe-vpn-connections](../../../cli/latest/reference/ec2/describe-vpn-connections.md "../../../cli/latest/reference/ec2/describe-vpn-connections.md") command with a filter for `vpn-concentrator-id` to view VPN connections associated with a specific Concentrator.
