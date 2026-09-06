

# Create a VPC attachment for an AWS Cloud WAN core network
<a name="cloudwan-vpc-attachment-add"></a>

## Create a VPC attachment using the console
<a name="cloudwan-vpc-attachment-console"></a>

The following steps create a VPC attachment for a core network using the console. 

**To create a VPC attachment using the console**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.

1. In the navigation pane under the name of the global network, choose **Attachments**.

1. Choose **Create attachment**.

1. Enter a **name** identifying the attachment.

1. From the **Edge location** dropdown list, choose the location where the attachment is located.

1. Choose **VPC**.

1. In the VPC attachment section, choose **Appliance mode support** if appliance mode is supported. For more information about appliance mode, see [Appliance mode](cloudwan-vpc-attachment.md#cloudwan-appliancemode).

1. Choose **IPv6 support** if the attachment supports IPv6. 

1. By default, **DNS support ** is enabled. This allows domain name system resolution for the attachment. Clear the check box if you don't want to enable DNS support. For more information, see [DNS support](cloudwan-vpc-attachment.md#cloudwan-dns-support).

1. By default **Security Group Referencing support** is enabled. When you create a VPC attachment, Cloud WAN automatically enables security group referencing for VPCs attached to the same core network edge. This allows you to reference security groups across VPCs in your security group rules. Clear the check box if you don't want to enable security group referencing. For more information, see [Security group referencing](cloudwan-vpc-attachment.md#cloudwan-sg-referencing).

1. From the **VPC IP** dropdown list, choose the VPC ID to attach to the core network.

1. After choosing the VPC ID, you're prompted to choose the **Availability Zone** and **Subnet Id** in which to create the core network VPC attachment. The Availability Zones that are listed are those edge locations that you chose when you created your core network. You must choose at least one Availability Zone and subnet ID.

1. (Optional) For **Routing policy label**, provide a label that will be used to map this policy to attachments. The policy will automatically be applied to any attachment tagged with the same label.

1. (Optional) In the **Tags** section, add **Key** and **Value** pairs to further help identify this resource. You can add multiple tags by choosing **Add tag**, or remove any tag by choosing **Remove tag**.

1. Choose **Create attachment**.

## Create a VPC attachment using the command line or API
<a name="cloudwan-vpc-attachment-cli"></a>

Use the command line or API to create an AWS Cloud WAN VPC attachment

**To create a VPC attachment using the command line or API**
+ Use `create-vpc-attachment`. See [create-vpc-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-vpc-attachment.html).

To enable appliance mode, add `--options ApplianceModeSupport=true` to the command. 