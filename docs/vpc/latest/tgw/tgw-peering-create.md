

# Create a peering attachment in AWS Transit Gateway
<a name="tgw-peering-create"></a>

Before you begin, ensure that you have the ID of the transit gateway that you want to attach. If the transit gateway is in another AWS account, ensure that you have the AWS account ID of the owner of the transit gateway. After you create the peering attachment, the owner of the accepter transit gateway must accept or reject the attachment request. 

**To create a peering attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Choose **Create transit gateway attachment**.

1. For **Transit gateway ID**, choose the transit gateway for the attachment. You can choose a transit gateway that you own. Transit gateways that are shared with you are not available for peering.

1. For **Attachment type**, choose **Peering Connection**.

1. Optionally enter a name tag for the attachment.

1. For **Account**, do one of the following:
   + If the transit gateway is in your account, choose **My account**.
   + If the transit gateway is in different AWS account, choose **Other account**. For **Account ID**, enter the AWS account ID.

1. For **Region**, choose the Region that the transit gateway is located in.

1. For **Transit gateway (accepter)**, enter the ID of the transit gateway that you want to attach.

1. Choose **Create transit gateway attachment**.

**To create a peering attachment using the AWS CLI**  
Use the [create-transit-gateway-peering-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-peering-attachment.html) command.