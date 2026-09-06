

# Create a VPC attachment in AWS Transit Gateway
<a name="create-vpc-attachment"></a>

**To create a VPC attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Choose **Create transit gateway attachment**.

1. For **Name tag**, optionally enter a name for the transit gateway attachment.

1. For **Transit gateway ID**, choose the transit gateway for the attachment. You can choose a transit gateway that you own or a transit gateway that was shared with you.

1. For **Attachment type**, choose **VPC**.

1. Choose whether to enable **DNS Support**, **IPv6 Support** and **Appliance mode support**.

   If appliance mode is chosen, traffic flow between a source and destination uses the same Availability Zone for the VPC attachment for the lifetime of that flow.

1. Choose whether to enable **Security Group Referencing support**. Enable this feature to reference a security group across VPCs attached to a transit gateway. For more information about security group referencing, see [Security group referencing](tgw-vpc-attachments.md#vpc-attachment-security). 

1. Choose whether to enable **IPv6 Support**. When enabled, the transit gateway network interface receives an IPv6 address. IPv6 VPC CIDRs propagate to transit gateway route tables when route propagation is configured. When disabled, the network interface does not receive an IPv6 address, and IPv6 CIDRs do not propagate. For more information, see [IPv6 support](tgw-vpc-attachments.md#tgw-vpc-attachment-ipv6).

1. For **VPC ID**, choose the VPC to attach to the transit gateway.

   This VPC must have at least one subnet associated with it.

1. For **Subnet IDs**, select one subnet for each Availability Zone to be used by the transit gateway to route traffic. You must select at least one subnet. You can select only one subnet per Availability Zone.

1. Choose **Create transit gateway attachment**.

**To create a VPC attachment using the AWS CLI**  
Use the [create-transit-gateway-vpc-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-vpc-attachment.html) command.