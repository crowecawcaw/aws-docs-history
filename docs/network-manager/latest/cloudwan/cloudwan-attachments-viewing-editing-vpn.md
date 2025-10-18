# View or edit an AWS Cloud WAN Site-to-Site VPN
 attachment

You can view and edit configuration information for a VPN attachment, as well as adding a
 new attachment. If you want to add a new VPN attachment, see [Create a Site-to-Site VPN attachment for an AWS Cloud WAN core
 network](cloudwan-vpn-attachment-add.md "cloudwan-vpn-attachment-add.md").

###### To view and edit a VPC attachment

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Attachments**.
5. Select the check box for an attachment where the **Resource
 Type** is **VPN**. Details about the attachment are
 displayed in the lower part of the page. In this section, you can also edit the
 attachment Tags by choosing the **Tags** tab.
6. Choose **Edit**.
7. On the **Edit attachment** page, do any of the
 following:




	* Enable or disable appliance mode support.
	* Enable or disable IPv6 support.
	* Add or remove subnets IDs.
	* Add or remove tags.
8. If you made any changes, choose **Edit attachment** to
 save the changes. The **Attachments** page displays along
 with a confirmation that the attachment was modified successfully.

## View a Site-to-Site VPN attachment using the command line or
 API


Use the command line or API to viewt a Site-to-Site VPN attachment.



###### To view a Site-to-Site VPN attachment using the command line or API


* See [get-site-to-site-vpn-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-site-to-site-vpn-attachment.html "https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-site-to-site-vpn-attachment.html").
