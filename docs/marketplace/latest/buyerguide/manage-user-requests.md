

# Managing user requests
<a name="manage-user-requests"></a>

If you enabled product procurement requests for the experiences in your organization, the end users can request for additional products to be approved. You will receive Amazon EventBridge events when a user requests a product. Refer [Private Marketplace notifications](configuring-notifications.md) for details on how you can configure email notifications for these events.

Product procurement request is enabled by default for an experience. You can view and edit this setting for each experience.

**To update the product procurement request setting for an experience**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

1. In the navigation pane, choose **Experiences** under **Private Marketplace**.

1. Choose the experience you want to update.

1. Choose **View details** to view a page with all the details for the experience.

1. Choose **Edit** from the **Details** tab.

1. Choose **Enabled** in **Product procurement requests** if you want to allow your end users to request products for procurement. Otherwise, choose **Disabled**.

1. Choose **Save changes**.

**To take action on pending user requests**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

1. In the navigation pane, choose **Approval requests** under **Private Marketplace**.

1. You can approve or decline multiple requests from this page by first selecting the check box next to the name of each request, and then choosing **Approve** or **Decline**.

1. To view more information about the request, choose **View details** for that request.

   1. You can view the reason for request, optional purchase order number, and the Private Marketplace experience associated with the user.

   1. You can choose to **Approve** or **Decline** and inform your buyer about your decision using an optional approver note.

   1. All users associated with the Private Marketplace experience will be allowed to subscribe to the products in the request, if approved. If declined, all users associated with the Private Marketplace experience will not be able to subscribe to the products in the request.