# View or edit an AWS Cloud WAN core network Direct Connect

gateway attachment

You can update the edge locations for a Direct Connect gateway attachment using either the Network Manager
console or using the AWS CLI. The Direct Connect gateway attachment must first be created using
the Direct Connect console. For more information about Direct Connect gateway attachments and
Cloud WAN, see [Direct Connect gateway
attachments](cloudwan-dxattach-about.md "cloudwan-dxattach-about.md").

###### Topics

- [View or edit a Direct Connect gateway
  attachment using the console](#cloudwan-dxattachment-update-console "#cloudwan-dxattachment-update-console")
- [Manage a Direct Connect gateway attachment routing policy label](#cloudwan-labels-editing-dx "#cloudwan-labels-editing-dx")
- [Update a Direct Connect gateway attachment
  using the command line or API](#cloudwan-dxattachment-update-cli "#cloudwan-dxattachment-update-cli")

## View or edit a Direct Connect gateway

attachment using the console

Use the following steps he following steps to update the edge locations for a Direct Connect
gateway attachment. The updated edge locations are automatically associated with the
Direct Connect gateway on Direct Connect console.

###### To add a Direct Connect gateway attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.
4. In the navigation pane under he name of the global network, choose **Attachments**.
5. Choose the Direct Connect gateway attachment you want to update, and then choose
   **Edit**.
6. In the **Direct Connect attachment** section, add or remove
   **Edge locations**, and then choose **Edit
   attachment**.

## Manage a Direct Connect gateway attachment routing policy label

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

## Update a Direct Connect gateway attachment

using the command line or API

Use the command line or API to update a Direct Connect gateway attachment.

###### To create a Direct Connect gateway attachment using the command line or API

- Use `update-direct-connect-gateway-attachment`. See [update-direct-connect-gateway-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-direct-connect-gateway-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-direct-connect-gateway-attachment.html").
