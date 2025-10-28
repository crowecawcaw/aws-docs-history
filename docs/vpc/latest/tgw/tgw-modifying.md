# Modify a transit gateway in AWS Transit Gateway

You can modify the configuration options for a transit gateway. When you modify a transit
gateway, any existing transit gateway attachments don't experience any service
interruptions.

You cannot modify a transit gateway that has been shared with you.

You cannot remove a CIDR block for the transit gateway if any of the IP addresses
are currently used for a [Connect peer](tgw-connect.md "tgw-connect.md").

###### To modify a transit gateway

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit
   Gateways**.
3. Choose the transit gateway to modify.
4. Choose **Actions**, **Modify transit
   gateway**.
5. Modify the options as needed, and choose **Modify transit
   gateway**.

###### To modify your transit gateway using the AWS CLI

Use the [modify-transit-gateway](../../../cli/latest/reference/ec2/modify-transit-gateway.md "../../../cli/latest/reference/ec2/modify-transit-gateway.md") command.
