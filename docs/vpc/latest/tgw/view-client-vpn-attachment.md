

# View a Client VPN attachment in AWS Transit Gateway
<a name="view-client-vpn-attachment"></a>

**To view your Client VPN attachments using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit gateways**.

1. Choose **Transit gateway attachments**.

1. In the **Resource type** column, look for **Client VPN**.

1. Choose an attachment to view its details.

**To view your Client VPN attachments using the AWS CLI**  
Use the [describe-transit-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-attachments.html) command with a filter for resource type `client-vpn`.