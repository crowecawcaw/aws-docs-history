# Managing experiences

You can create an experience, view a list of all the experiences, and make edits from the **Experiences** page. This includes active and archived experiences.

###### Topics

- [Viewing and updating experiences](#view-and-update-experiences "#view-and-update-experiences")
- [Updating experience configuration](#update-experience-configuration "#update-experience-configuration")
- [Managing audience
  associations for an experience](#manage-audience-associations-for-an-experience "#manage-audience-associations-for-an-experience")
- [Managing products in an experience](#manage-products-in-an-experience "#manage-products-in-an-experience")
- [Customizing branding settings](#customize-branding-settings "#customize-branding-settings")

## Viewing and updating experiences

**Active experiences** can be used to govern users. You can continue to make updates and manage products in active experiences. When an active experience is **Live** and associated with an audience, all users in that audience will be governed by the experience. When an active experience is **Not live**, it will not govern any users even when it is associated with an audience.

**Archived experiences** cannot be modified and used to govern users. An archived experience has to be reactivated, if you want to use it again.

###### To view and update experiences

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Experiences** under **Private Marketplace**.
3. Choose the experience you want to update.
4. Choose **View details** to view a page with all the details for the experience. To edit, see [Updating experience configuration](#update-experience-configuration "#update-experience-configuration"), [Managing audience
   associations for an experience](#manage-audience-associations-for-an-experience "#manage-audience-associations-for-an-experience"), [Managing products in an experience](#manage-products-in-an-experience "#manage-products-in-an-experience"), and [Customizing branding settings](#customize-branding-settings "#customize-branding-settings").
5. Choose **Save changes**.

## Updating experience configuration

You can update the internal name and description for the experience, the status, and admin mode. You can also enable or disable product procurement requests.

Setting the status of an experience that is associated with an audience to **Live** does not disrupt existing subscriptions and usage for the users in that audience. For example, it does not disrupt active Amazon Machine Images (AMIs) running on Amazon Elastic Compute Cloud (Amazon EC2) instances. When an experience is **Live** and associated with an audience, all new subscriptions or renewals are limited to the products approved in the experience.

###### To edit the configuration for an experience

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Experiences** under **Private Marketplace**.
3. Choose the experience you want to update.
4. Choose **View details** to view a page with all the details for the experience. To edit the configuration, choose **Edit** on the **Details** tab.
5. Choose **Live** as **Experience status** if you want the experience to take effect and govern the associated audience. Choose **Not live** as **Experience status** if you do not want the experience to take effect or turn off the experience.
6. You can update the admin mode of an experience only when the status is **Not live**. Choose **Active** to allow edits or **Archived** to disallow edits.
7. Choose **Enabled** in **Product procurement requests** if you want to allow your end users to request products for procurement. If you choose **Disabled**, your end users will not be able to create product procurement requests.
8. You can edit the name and description for the experience in the **Experience details** section. This is the internal name and description used by administrators to keep track of this experience. End users do not see these fields.
9. Choose **Save changes**.

## Managing audience

associations for an experience

You can associate additional audiences with an experience or disassociate existing audiences from the experience. This section describes how you can associate and disassociate audiences from an experience using the experience details page.

###### To associate additional audiences with an experience

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Experiences** under **Private Marketplace**.
3. Choose the experience you want to update.
4. Choose **View details** to view a page with all the details for the experience.
5. Choose **Associated audiences** tab and **Add additional audience**.
6. Navigate the tree structure to choose your target audiences. The hierarchy shown reflects your organization structure, displaying the organizational units (OUs) and accounts that you manage in Organizations.
7. You can choose the entire organization, organizational units (OUs), or accounts. If you choose an audience that is directly associated with another experience, it will be disassociated from that experience and associated with the current experience.
8. After making your selections, choose **Next**.
9. Review the selected audiences to associate with the experience, and edit as needed.
10. When you are satisfied with your selections, choose **Associate**.

## Managing products in an experience

You can manage the products in an experience in multiple ways. This section covers how you can approve or decline products in a specific experience using its details page.

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Experiences** under **Private Marketplace**.
3. Choose the experience you want to update.
4. Choose **View details** to view a page with all the details for the experience.
5. Choose **Products** tab.
6. Select products and choose **Approve** or **Deny** from the **Managed products** or **All products** tables.
7. In the modal, choose **Approve** or **Deny** to approve or decline the products.

You can also approve or decline products from experiences in following ways:

- From the dashboard – see [Bulk managing products](bulk-manage-products.md "bulk-manage-products.md").
- From a product detail page – see [Approval status of a product in experiences](approval-status-of-a-product-in-experience.md "approval-status-of-a-product-in-experience.md").

## Customizing branding settings

You can brand an experience with a name and description so your users know they're procuring products in an approved catalog.

###### To customize branding for an experience

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Experiences** under **Private Marketplace**.
3. Choose the experience you want to update.
4. Choose **View details** to view a page with all the details for the experience.
5. Choose **Branding settings** tab.
6. Update the name and description for branding the experience you are creating. This name and description is shown to users on their **Your Private Marketplace** page. You can use these to provide details to your users about the Private Marketplace experience you are curating for them.
7. Choose **Save changes** to update the branding.
