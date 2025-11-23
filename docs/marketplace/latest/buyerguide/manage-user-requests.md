# Managing user requests

If you enabled product procurement requests for the experiences in your organization, the end users can request for additional products to be approved. You will receive Amazon EventBridge events when a user requests a product. Refer [Private Marketplace notifications](configuring-notifications.md "configuring-notifications.md") for details on how you can configure email notifications for these events.

Product procurement request is enabled by default for an experience. You can view and edit this setting for each experience.

###### To update the product procurement request setting for an experience

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Experiences** under **Private Marketplace**.
3. Choose the experience you want to update.
4. Choose **View details** to view a page with all the details for the experience.
5. Choose **Edit** from the **Details** tab.
6. Choose **Enabled** in **Product procurement requests** if you want to allow your end users to request products for procurement. Otherwise, choose **Disabled**.
7. Choose **Save changes**.

###### To take action on pending user requests

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Approval requests** under **Private Marketplace**.
3. You can approve or decline multiple requests from this page by first selecting the check box next to the name of each request, and then choosing **Approve** or **Decline**.
4. To view more information about the request, choose **View details** for that request.
   1. You can view the reason for request, optional purchase order number, and the Private Marketplace experience associated with the user.
   2. You can choose to **Approve** or **Decline** and inform your buyer about your decision using an optional approver note.
   3. All users associated with the Private Marketplace experience will be allowed to subscribe to the products in the request, if approved. If declined, all users associated with the Private Marketplace experience will not be able to subscribe to the products in the request.

###### Note

Private Marketplace supports two user experiences: AWS Console and the legacy website.

To view and manage Private Marketplace in the AWS Marketplace Console, an administrator in the management account of your AWS Organizations must create an integration for Private Marketplace. See [Enabling Private Marketplace](private-marketplace-current.md#enable-private-marketplace "private-marketplace-current.md#enable-private-marketplace") for details. For end users, administrators must also grant the new permissions listed in [AWSPrivateMarketplaceRequests](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplacerequests "buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplacerequests").

Product requests created using the legacy website will be available at [Private Marketplace](https://aws.amazon.com/marketplace/privatemarketplace "https://aws.amazon.com/marketplace/privatemarketplace"). **Important:** The legacy website will be deprecated on March 17, 2026.
