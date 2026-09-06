

# Modify a VPC attachment in AWS Transit Gateway
<a name="modify-vpc-attachment"></a>

**To modify your VPC attachments using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the VPC attachment, and then choose **Actions**, **Modify transit gateway attachment**.

1. Enable or disable any of the following:
   + **DNS support**
   + **IPv6 support**
   + **Appliance mode support**

1. To add or remove a subnet from the attachment, choose or clear the checkbox by the **Subnet ID** you want to add or remove.
**Note**  
Adding or modifying a VPC attachment subnet might impact data traffic while the attachment is in a modifying state.

1. To be able to reference a security group across VPCs attached to a transit gateway, select **Security Group Referencing support**. For more information about security group referencing, see [Security group referencing](tgw-vpc-attachments.md#vpc-attachment-security). 
**Note**  
If you disable security group referencing for an existing transit gateway, it will be disabled on all VPC attachments. 

1. Choose **Modify transit gateway attachment**. 

**To modify your VPC attachments using the AWS CLI**  
Use the [modify-transit-gateway-vpc-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-transit-gateway-vpc-attachment.html) command.