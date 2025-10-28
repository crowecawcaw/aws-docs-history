# Delete a peering attachment in AWS Transit Gateway

You can delete a transit gateway peering attachment. The owner of either of the transit
gateways can delete the attachment.

###### To delete a peering attachment using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway
   Attachments**.
3. Select the transit gateway peering attachment.
4. Choose **Actions**, **Delete transit gateway
   attachment**.
5. Enter `delete` and choose **Delete**.

###### To delete a peering attachment using the AWS CLI

Use the [delete-transit-gateway-peering-attachment](../../../cli/latest/reference/ec2/delete-transit-gateway-peering-attachment.md "../../../cli/latest/reference/ec2/delete-transit-gateway-peering-attachment.md") command.
