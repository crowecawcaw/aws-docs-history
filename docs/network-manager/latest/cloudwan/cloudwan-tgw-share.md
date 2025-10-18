# Create a shared transit gateway route table attachment in an AWS Cloud WAN core network

The following steps guide you through creating a shared transit gateway attachment.

###### To create a shared transit gateway attachment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, under **Shared by me**, choose
 **Attachments**.
5. Choose **Create attachment**.
6. Enter a `name` to identify the attachment.
7. From the **Core network** dropdown list, choose the core
 network that is shared with you and that is where you want to create the VPC
 attachment.
8. From the **Edge location** dropdown list, choose the location
 where the attachment is located.
9. In the **VPC attachment** section, choose **IPv6
 support** if the attachment supports IPv6.
10. From the **Attachment type** dropdown list, choose
 **Transit gateway route table**.
11. From the **Transit gateway peering** dropdown list in the
 **Transit gateway route table attachment** section, choose
 an existing peering to share.
12. (Optional) In the **Tags** section, add
 **Key** and **Value** pairs to help
 identify this resource. You can add multiple tags by choosing **Add
 tag**, or remove any tag by choosing **Remove
 tag**.
13. Choose **Create attachment**.
14. The **Attachment** page displays the following information about
 your shared attachments:




	* **Attachment ID**
	* **Name**
	* **Edge location**
	* **Resource Type**
	* **Resource ID**
	* **State**
	* **Core network**
	* **Core network status**
15. Choose **Create attachment** to create the new shared VPC or
 transit gateway attachment. See [Attachments in AWS Cloud WAN](cloudwan-create-attachment.md "cloudwan-create-attachment.md") .
