

# View or edit an AWS Cloud WAN Connect attachment
<a name="cloudwan-attachments-viewing-editing-connect"></a>

You can view information about a Connect attachment. For an existing attachment you can create a GRE or Tunnel-less Connect peer, as well as edit the key-value tags associated with the attachment. If you want to add a new Connect attachment, see [Connect attachments and Connect peers in AWS Cloud WAN](cloudwan-connect-attachment.md).

## View and edit a Connect attachment
<a name="cloudwan-editing-connect"></a>

**To view and edit a Connect peer attachment**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the check box for an attachment where the **Resource Type** is **Connect**. 

1. Details about the attachment are displayed, as well as any Connect peers and tags that are associated with the attachment. Here you can also add a new Connect peer, as well as add, edit, or remove tags.
   + To add a new GRE or Tunnel-less Connect peer attachment, choose the **Connect peers** tab and follow the steps here: [Create an AWS Cloud WAN Connect peer for a core network](cloudwan-connect-peer-attachment.md).
   + To add or edit attachment Tags, choose the **Tags** tab. The current list of tags associated with this attachment are displayed. Choose **Edit tags** to modify or delete current tags, and to add new tags. If you made any changes, choose **Edit attachment** to save the changes. The **Attachments** page displays along with a confirmation that the attachment was modified successfully.

## Manage a Connect routing policy label
<a name="cloudwan-labels-editing-connect"></a>

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

## View a Connect or Connect peer attachment using the command line or API
<a name="edit-attachment-connect-cli"></a>

Use the command line or API to view a Connect or Connect peer attachment.

**To view a Connect or Connect peer attachment using the command line or API**
+ For a Connect attachment, see [get-connect-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-connect-attachment.html).
+ For a Connect peer attachment, see [get-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-connect-peer.html).