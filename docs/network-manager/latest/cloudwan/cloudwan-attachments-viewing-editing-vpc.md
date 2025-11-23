# View or edit an AWS Cloud WAN VPC

attachment

You can view and edit configuration information for a VPC attachment . If you want to add
a new VPC attachment, see [VPC attachments in AWS Cloud WAN](cloudwan-vpc-attachment.md "cloudwan-vpc-attachment.md").

## View and edit a VPC attachment

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
   - Enable or disable appliance mode support.
   - Enable or disable IPv6 support.
   - Enable or disable DNS support.
   - Enable or disable security group referencing support.
   - Add or remove subnet IDs.

7. After making any changes, choose **Edit attachment**.
8. To add, edit, or remove tags, choose the **Tags** tab. The
   current list of tags associated with this attachment are displayed. Choose
   **Edit tags** to modify or delete current tags, and to add new
   tags.
9. If you made any changes, choose **Edit attachment** to
   save the changes. The **Attachments** page displays along
   with a confirmation that the attachment was modified successfully.

## Manage a VPC attachment routing policy label

You can create, modify, or delete routing policy labels for an attachment. Once you add or modify a routing policy label, you'll need to map or remap it to an attachment routing policy. Deleting a routing policy label removes any association with an attachment routing policy.

###### To manage attachment routing policy labels

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network link for the core network with the attachment.
4. In the navigation pane under the name of the global network, choose **Attachments**.
5. Choose the attachment.
6. In the section showing details about the attachment, choose the **Routing policy** tab, choose **Edit**.
7. Choose **Create** to create a new routing policy label, or choose **Edit** modify the **Routing policy label** as needed.
8. After creating or modifying a routing policy label, you can then associate that label with an attachment routing policy.
9. In the **Attachment routing policy association** section choose the attachment routing policy association you want to map to the routing policy label.

You can delete a routing policy labels for an attachment. Once you delete an attachment, the association from an attachment routing policy is removed permanently.

###### To delete an attachment routing policy label

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network link for the core network with the attachment.
4. In the navigation pane under the name of the global network, choose **Attachments**.
5. Choose the attachment.
6. In the section showing details about the attachment, choose the **Routing policy** tab, choose **Delete**.
7. Choose **Delete** again to confirm the removal. If the routing policy label was mapped to an attachment routing policy, the **Attachment routing policy association** section updates and removes the policy from the list.

## View a VPC attachment using the command line or

API

Use the command line or API to view a VPC attachment.

###### To view a VPC attachment using the command line or API

- See [get-vpc-attachment](../../../cli/latest/reference/networkmanager/get-vpc-attachment.md "../../../cli/latest/reference/networkmanager/get-vpc-attachment.md").
