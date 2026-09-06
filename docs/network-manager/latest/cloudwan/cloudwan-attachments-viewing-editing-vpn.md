

# View or edit an AWS Cloud WAN Site-to-Site VPN attachment
<a name="cloudwan-attachments-viewing-editing-vpn"></a>

You can view and edit configuration information for a VPN attachment, as well as adding a new attachment. If you want to add a new VPN attachment, see [Create a Site-to-Site VPN attachment for an AWS Cloud WAN core network](cloudwan-vpn-attachment-add.md).

## View and edit a VPN attachment
<a name="cloudwan-editing-vpn"></a>

**To view and edit a VPC attachment**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the check box for an attachment where the **Resource Type** is **VPN**. Details about the attachment are displayed in the lower part of the page. In this section, you can also edit the attachment Tags by choosing the **Tags** tab.

1. Choose **Edit**.

1. On the **Edit attachment** page, do any of the following:
   + Enable or disable appliance mode support.
   + Enable or disable IPv6 support.
   + Add or remove subnets IDs.
   + Add or remove tags.

1. If you made any changes, choose **Edit attachment** to save the changes. The **Attachments** page displays along with a confirmation that the attachment was modified successfully.

## Manage a VPN attachment routing policy label
<a name="cloudwan-labels-editing-vpn"></a>

You can create, modify, or delete routing policy labels for an attachment. Once you add or modify a routing policy label, you'll need to map or remap it to an attachment routing policy. Deleting a routing policy label removes any association with an attachment routing policy.

**To manage attachment routing policy labels**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network link for the core network with the attachment.

1. In the navigation pane under the name of the global network, choose **Attachments**.

1. Choose the attachment.

1. In the section showing details about the attachment, choose the **Routing policy** tab, choose **Edit**.

1. Choose **Create** to create a new routing policy label, or choose **Edit** modify the **Routing policy label** as needed.

1. After creating or modifying a routing policy label, you can then associate that label with an attachment routing policy.

1. In the **Attachment routing policy association** section choose the attachment routing policy association you want to map to the routing policy label.

You can delete a routing policy labels for an attachment. Once you delete an attachment, the association from an attachment routing policy is removed permanently.

**To delete an attachment routing policy label**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network link for the core network with the attachment.

1. In the navigation pane under the name of the global network, choose **Attachments**.

1. Choose the attachment.

1. In the section showing details about the attachment, choose the **Routing policy** tab, choose **Delete**.

1. Choose **Delete** again to confirm the removal. If the routing policy label was mapped to an attachment routing policy, the **Attachment routing policy association** section updates and removes the policy from the list. 

## View a Site-to-Site VPN attachment using the command line or API
<a name="edit-attachment-vpn-cli"></a>

Use the command line or API to viewt a Site-to-Site VPN attachment.

**To view a Site-to-Site VPN attachment using the command line or API**
+ See [get-site-to-site-vpn-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-site-to-site-vpn-attachment.html).