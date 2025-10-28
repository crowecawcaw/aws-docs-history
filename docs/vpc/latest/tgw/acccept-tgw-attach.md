# Accept a shared attachment in AWS Transit Gateway

If you didn't enable the **Auto accept shared attachments** functionality
when you created your transit gateway, you must manually accept cross-account (shared) attachment
using either the Amazon VPC Console or the AWS CLI.

###### To manually accept a shared attachment

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway
   Attachments**.
3. Select the transit gateway attachment that's pending acceptance.
4. Choose **Actions**, **Accept transit gateway
   attachment**.

###### To accept a shared attachment using the AWS CLI

Use the [accept-transit-gateway-vpc-attachment](../../../cli/latest/reference/ec2/accept-transit-gateway-vpc-attachment.md "../../../cli/latest/reference/ec2/accept-transit-gateway-vpc-attachment.md") command.
