# View a Client VPN attachment in AWS Transit Gateway

###### To view your Client VPN attachments using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit gateways**.
3. Choose **Transit gateway attachments**.
4. In the **Resource type** column, look for **Client VPN**.
5. Choose an attachment to view its details.

###### To view your Client VPN attachments using the AWS CLI

Use the [describe-transit-gateway-attachments](../../../cli/latest/reference/ec2/describe-transit-gateway-attachments.md "../../../cli/latest/reference/ec2/describe-transit-gateway-attachments.md") command with a filter for resource type `client-vpn`.
