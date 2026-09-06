

# Create a shared transit gateway route table attachment in an AWS Cloud WAN core network
<a name="cloudwan-tgw-share"></a>

The following steps guide you through creating a shared transit gateway attachment.

**To create a shared transit gateway attachment**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, under **Shared by me**, choose **Attachments**.

1. Choose **Create attachment**.

1. Enter a **name** to identify the attachment.

1. From the **Core network** dropdown list, choose the core network that is shared with you and that is where you want to create the VPC attachment.

1. From the **Edge location** dropdown list, choose the location where the attachment is located.

1. In the **VPC attachment** section, choose **IPv6 support** if the attachment supports IPv6.

1. From the **Attachment type** dropdown list, choose **Transit gateway route table**.

1. From the **Transit gateway peering** dropdown list in the **Transit gateway route table attachment** section, choose an existing peering to share.

1. (Optional) In the **Tags** section, add **Key** and **Value** pairs to help identify this resource. You can add multiple tags by choosing **Add tag**, or remove any tag by choosing **Remove tag**.

1. Choose **Create attachment**.

1. The **Attachment** page displays the following information about your shared attachments:
   + **Attachment ID**
   + **Name**
   + **Edge location**
   + **Resource Type**
   + **Resource ID**
   + **State**
   + **Core network**
   + **Core network status**

1. Choose **Create attachment** to create the new shared VPC or transit gateway attachment. See [Attachments in AWS Cloud WAN](cloudwan-create-attachment.md).