# Create a Connect attachment in AWS Transit Gateway

To create a Connect attachment, you must specify an existing attachment as the
transport attachment. You can specify a VPC attachment or a Direct Connect attachment as
the transport attachment.

###### To create a Connect attachment using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit gateway
   attachments**.
3. Choose **Create transit gateway attachment**.
4. (Optional) For **Name tag**, specify a name tag for the attachment.
5. For **Transit gateway ID**, choose the transit gateway for the
   attachment.
6. For **Attachment type**, choose
   **Connect**.
7. For **Transport attachment ID**, choose the ID of an existing
   attachment (the transport attachment).
8. Choose **Create transit gateway attachment**.

###### To create a Connect attachment using the AWS CLI

Use the [create-transit-gateway-connect](../../../cli/latest/reference/ec2/create-transit-gateway-connect.md "../../../cli/latest/reference/ec2/create-transit-gateway-connect.md") command.
