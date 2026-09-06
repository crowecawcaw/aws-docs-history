

# View or edit an AWS Cloud WAN transit gateway route table attachment
<a name="cloudwan-attachments-viewing-editing-rtb"></a>

You can view and edit the key-value tags associated with a transit gateway route table attachment, as well as adding a new attachment or for managing route labels For the steps to add a new transit gateway route table attachment, see[Transit gateway route table attachments in AWS Cloud WAN](cloudwan-tgw-attachment.md).

## View and edit a route table attachment
<a name="cloudwan-editing-rtb"></a>

**To view and edit a route table attachment**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the check box for an attachment where the **Resource Type** is **Transit gateway route table**. 

1. To add, edit, or remove tags, choose the **Tags** tab. The current list of tags associated with this attachment are displayed. Choose **Edit tags** to modify or delete current tags, and to add new tags.

## Manage a route table attachment routing policy label
<a name="cloudwan-labels-editing-rtb"></a>

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

## View a transit gateway route table attachment using the command line or API
<a name="edit-attachment-connect-cli"></a>

Use the command line or API to view a transit gateway route table attachment.

**To view a transit gateway route table attachment using the command line or API**
+ See [get-transit-gateway-route-table-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-transit-gateway-route-table-attachment.html).