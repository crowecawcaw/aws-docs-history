# View or edit an AWS Cloud WAN VPC
 attachment

You can view and edit configuration information for a VPC attachment . If you want to add
 a new VPC attachment, see [VPC attachments in AWS Cloud WAN](cloudwan-vpc-attachment.md "cloudwan-vpc-attachment.md").

###### To view and edit a VPC attachment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Attachments**.
5. Select the check box for an attachment where the **Resource
 Type** is **VPC**. Details about the attachment are
 displayed in the lower part of the page.
6. (Optional) Choose **Edit** to modify any of the following options
 for the VPC attachment:




	* Enable or disable appliance mode support.
	* Enable or disable IPv6 support.
	* Enable or disable DNS support.
	* Enable or disable security group referencing support.
	* Add or remove subnet IDs.
7. After making any changes, choose **Edit attachment**.
8. To add, edit, or remove tags, choose the **Tags** tab. The
 current list of tags associated with this attachment are displayed. Choose
 **Edit tags** to modify or delete current tags, and to add new
 tags.
9. If you made any changes, choose **Edit attachment** to
 save the changes. The **Attachments** page displays along
 with a confirmation that the attachment was modified successfully.

## View a VPC attachment using the command line or
 API


Use the command line or API to view a VPC attachment.



###### To view a VPC attachment using the command line or API


* See [get-vpc-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-vpc-attachment.html "https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-vpc-attachment.html").
