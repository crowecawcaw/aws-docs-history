

# View a VPN Concentrator attachment in AWS Transit Gateway
<a name="view-vpn-concentrator-attachment"></a>

**To view your VPN Concentrator attachments using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. In the **Resource type** column, look for **VPN Concentrator**. These are the VPN Concentrator attachments.

1. Choose an attachment to view its details.

**To view VPN connections on a VPN Concentrator using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Site-to-Site VPN Connections**.

1. In the list of VPN connections, identify connections that show a VPN Concentrator ID in the **Transit Gateway ID** column. These are the VPN connections hosted on VPN Concentrators.

1. Choose a VPN connection to view its details.

**To view your VPN Concentrator attachments using the AWS CLI**  
Use the [describe-vpn-concentrator](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpn-concentrator.html) command to view VPN Concentrator details, or use the [describe-transit-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-attachments.html) command with a filter for resource type `vpn-concentrator`.

**To view VPN connections on a VPN Concentrator using the AWS CLI**  
Use the [describe-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpn-connections.html) command with a filter for `vpn-concentrator-id` to view VPN connections associated with a specific Concentrator.