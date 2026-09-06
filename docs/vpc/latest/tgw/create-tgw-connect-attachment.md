

# Create a Connect attachment in AWS Transit Gateway
<a name="create-tgw-connect-attachment"></a>

To create a Connect attachment, you must specify an existing attachment as the transport attachment. You can specify a VPC attachment or a Direct Connect attachment as the transport attachment.

**To create a Connect attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Choose **Create transit gateway attachment**.

1. (Optional) For **Name tag**, specify a name tag for the attachment.

1. For **Transit gateway ID**, choose the transit gateway for the attachment.

1. For **Attachment type**, choose **Connect**.

1. For **Transport attachment ID**, choose the ID of an existing attachment (the transport attachment).

1. Choose **Create transit gateway attachment**.

**To create a Connect attachment using the AWS CLI**  
Use the [create-transit-gateway-connect](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-connect.html) command.