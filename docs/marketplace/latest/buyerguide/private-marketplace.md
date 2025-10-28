# Private marketplaces in AWS Marketplace (legacy version)

###### Important

This documentation is for legacy version of Private Marketplace, which will be deprecated on November 15, 2025. For documentation of the current version, see [Private Marketplace](private-marketplace-current.md "private-marketplace-current.md"). To use the current version, an administrator in the management account of your AWS Organizations must create an integration for Private Marketplace. To check integration status, see [Viewing Private Marketplace settings](view-private-marketplace-settings.md "view-private-marketplace-settings.md").

A private marketplace controls which products users in your AWS account, such as business
users and engineering teams, can procure from AWS Marketplace. It is built on top of AWS Marketplace, and
enables your administrators to create and customize curated digital catalogs of approved
independent software vendors (ISVs) and products that conform to their in-house policies. Users
in your AWS account can find, buy, and deploy approved products from your private marketplace,
and ensure that all available products comply with your organization’s policies and standards.

With [AWS Organizations](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md"), you can centralize management of all of your accounts, group your accounts
into organizational units (OUs), and attach different access policies to each OU. You can create
multiple private marketplace experiences that are associated with your entire organization, one
or more OUs, or one or more accounts in your organization, each with its own set of approved
products. Your AWS administrators can also apply company branding to each private marketplace
experience with your company or team’s logo, messaging, and color scheme.

###### Notes

- You can add private products that have been shared with you (through a [private offer](buyer-private-offers.md "buyer-private-offers.md")) to a private marketplace. For more information, see [Subscribing to a private product in a private marketplace](subscribing-to-a-private-product-in-a-private-marketplace.md "subscribing-to-a-private-product-in-a-private-marketplace.md") .
- In a private marketplace, customers are automatically entitled to any products whose
  EULAs are governed by the AWS Customer Agreement or other agreement with AWS governing
  use of AWS services. Customers are already entitled to these products by default;
  therefore, they are not included in the list of products that you approved within your
  private marketplace. Customers can use Service Catalog to manage the deployment of these
  products.

###### Topics

- [Viewing product detail pages](#product-detail-page-visit "#product-detail-page-visit")
- [Configuring notifications](#pmp-notifications "#pmp-notifications")
- [Private marketplaces for users](subscribing-to-a-product-in-a-private-marketplace.md "subscribing-to-a-product-in-a-private-marketplace.md")
- [Private marketplaces for administrators](private-catalog-administration.md "private-catalog-administration.md")

## Viewing product detail pages

Users can only subscribe to products that you allow in the private marketplace that
governs the account. They can browse and see the detail page for any product, but subscription
is enabled only for products you have added to your private marketplace. If a product is not
currently in your private marketplace, the user sees a red banner at the top of the page,
noting that the product is not approved for procurement in AWS Marketplace.

If software requests are enabled, users can choose **Create request** on
the product details page. When users choose **Create request**, they submit a
request to the administrator to make the product available on your private marketplace. For
more information about this feature, see [Managing user requests for products
in a private marketplace](manage-user-requests-private-marketplace.md "manage-user-requests-private-marketplace.md").

## Configuring notifications

Private marketplace administrators and buyers receive notification events from AWS Marketplace when a buyer requests a product, and when a request is approved or denied.
Administrators receive notifications for requests from any account in their AWS organization. Buyers only receive notifications for requests from their accounts.
The notification events include product details and the seller's name.

For information about the Private Marketplace notification events, see
[Amazon EventBridge notifications for AWS Marketplace events](buyer-notifications-eventbridge.md "buyer-notifications-eventbridge.md"), later in this guide.

You can create EventBridge rules with different target types by following the steps in
[Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md"),
in the _Amazon EventBridge User Guide_.

### Creating email notification configurations

You can use the AWS User Notifications service to receive notifications for events through multiple channels, including email.
The following steps explain how to create an email notification configuration. Notification configurations act as
containers for the services and event rules that you want to be notified about. An event rule specifies the events that generate a notification
in the AWS console, and which delivery channels to use.

###### To create a notification configuration

1. Sign in to the AWS Management Console and navigate to AWS User Notifications.
2. Choose **Notification configurations**, then choose **Create notification configuration**.
3. In the **Name** box, enter a name for the configuration.
4. In the **Event rules** section of the page, enter the following values:
   - For **AWS service name**, choose **AWS Marketplace Private Marketplace**.
   - For **Event type**, choose one of the following:
     - **Product Request Created**
     - **Product Request Approved**
     - **Product Request Declined**

     ###### Note

     As needed, you can create notification configurations for each event type.

   - For **Regions**, select **us-east-1**. Private marketplace only operates in that Region.

5. Under **Aggregation settings**, we recommend choosing **Receive within 5 minutes**.
6. Under **Delivery channels**, select the **email** checkbox, then do the following:
   1. In the **Recipient** box, enter the email address of the notification recipient.
   2. As needed, choose **Add another recipient**, the enter another email address in the **Recipient** box. You can enter a maximum of 99 recipients.
   3. (Optional) Under **Manage tags**, choose **Add new tag**,
      enter values in the **Key** and **Value** boxes.###### Note

For more information about using the **AWS Console Mobile App** and **Chat channels** delivery options, see
the links below. 7. When finished, choose **Create notification configuration**.

In addition to using an email delivery channel, you can also use the AWS Console
Mobile App and Chat delivery channels. The following links take you to more information
about those channels and about User Notifications.

- [What is the AWS Console Mobile Application](../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md "../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md"),
  in the _AWS Console Mobile Application User Guide_.
- [What is AWS Chatbot](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md"), in the
  _Amazon Q Developer in chat applications Administrator Guide_.
- [Creating a notification configuration](../../../notifications/latest/userguide/getting-started.md#getting-started-step1 "../../../notifications/latest/userguide/getting-started.md#getting-started-step1"), in the _User Notifications User Guide_.
