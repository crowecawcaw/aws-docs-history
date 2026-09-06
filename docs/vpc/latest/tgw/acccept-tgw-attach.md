

# Accept a shared attachment in AWS Transit Gateway
<a name="acccept-tgw-attach"></a>

If you didn't enable the **Auto accept shared attachments** functionality when you created your transit gateway, you must manually accept cross-account (shared) attachment using either the Amazon VPC Console or the AWS CLI.

**To manually accept a shared attachment**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the transit gateway attachment that's pending acceptance.

1. Choose **Actions**, **Accept transit gateway attachment**.

**To accept a shared attachment using the AWS CLI**  
Use the [accept-transit-gateway-vpc-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/accept-transit-gateway-vpc-attachment.html) command.