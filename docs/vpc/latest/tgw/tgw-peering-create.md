# Create a peering attachment in AWS Transit Gateway

Before you begin, ensure that you have the ID of the transit gateway that you want to attach. If the
transit gateway is in another AWS account, ensure that you have the AWS account ID of the owner of
the transit gateway. After you create the peering attachment, the owner of the accepter transit gateway must
accept or reject the attachment request.

###### To create a peering attachment using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway
   Attachments**.
3. Choose **Create transit gateway attachment**.
4. For **Transit gateway ID**, choose the transit gateway for the
   attachment. You can choose a transit gateway that you own. Transit gateways that are
   shared with you are not available for peering.
5. For **Attachment type**, choose **Peering
   Connection**.
6. Optionally enter a name tag for the attachment.
7. For **Account**, do one of the following:
   - If the transit gateway is in your account, choose **My
     account**.
   - If the transit gateway is in different AWS account, choose **Other
     account**. For **Account ID**, enter the
     AWS account ID.

8. For **Region**, choose the Region that the transit gateway is located
   in.
9. For **Transit gateway (accepter)**, enter the ID of the
   transit gateway that you want to attach.
10. Choose **Create transit gateway attachment**.

###### To create a peering attachment using the AWS CLI

Use the [create-transit-gateway-peering-attachment](../../../cli/latest/reference/ec2/create-transit-gateway-peering-attachment.md "../../../cli/latest/reference/ec2/create-transit-gateway-peering-attachment.md") command.
