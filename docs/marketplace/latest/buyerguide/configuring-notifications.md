# Private Marketplace notifications

Private Marketplace administrators and buyers receive notification events from AWS Marketplace when a buyer requests a product, and when a request is approved or declined. Administrators receive notifications for requests from any account in their AWS organization. Buyers only receive notifications for requests from their accounts. The notification events include product details and the seller's name.

For information about the Private Marketplace notification events, see [Amazon EventBridge notifications for AWS Marketplace events](buyer-notifications-eventbridge.md "buyer-notifications-eventbridge.md"), later in this guide.

You can create EventBridge rules with different target types by following the steps in [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md"), in the _Amazon EventBridge User Guide_.

## Creating email notification configurations

You can use the AWS User Notifications service to get notifications for events through multiple channels, including email. The following steps explain how to create an email notification configuration. Notification configurations act as containers for the services and event rules that you want to be notified about. An event rule specifies the events that generate a notification in the AWS console, and which delivery channels to use.

###### To create a notification configuration

1. Sign in to the AWS Management Console and navigate to AWS User Notifications.
2. Choose **Notification configurations**, then choose **Create notification configuration**.
3. In the **Name** box, enter a name for the configuration.
4. In the **Event rules** section of the page, enter the following values:
   1. For **AWS service name**, choose **AWS Marketplace Private Marketplace**.
   2. For **Event type**, choose one or more of the following:
      1. **Product Request Created**
      2. **Product Request Approved**
      3. **Product Request Declined**
      4. **Product Request Cancelled**
      5. **Product Request Expired**

   3. For **Regions**, select **us-east-1**. Private marketplace only operates in that Region.

5. Under **Aggregation settings**, we recommend choosing **Receive within 5 minutes**.
6. Under **Delivery channels**, select the **email** checkbox, then do the following:
   1. In the **Recipient** box, enter the email address of the notification recipient.
   2. As needed, choose **Add another recipient**, the enter another email address in the **Recipient** box. You can enter a maximum of 99 recipients.
   3. (Optional) Under **Manage tags**, choose **Add new tag**, enter values in the **Key** and **Value** boxes.

7. When finished, choose **Create notification configuration**.

In addition to using an email delivery channel, you can also use the AWS Console Mobile App and Chat delivery channels. The following links take you to more information about those channels and about User Notifications.

- [What is the AWS Console Mobile Application](../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md "../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md"), in the _AWS Console Mobile Application User Guide_.
- [What is AWS Chatbot](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md"), in the _Amazon Q Developer in chat applications Administrator Guide_.
- [Creating a notification configuration](../../../notifications/latest/userguide/getting-started.md#getting-started-step1 "../../../notifications/latest/userguide/getting-started.md#getting-started-step1"), in the _User Notifications User Guide_.

###### Note

Private Marketplace supports two user experiences: AWS Console and the legacy website.

To view and manage Private Marketplace in the AWS Marketplace Console, an administrator in the management account of your AWS Organizations must create an integration for Private Marketplace. See [Enabling Private Marketplace](private-marketplace-current.md#enable-private-marketplace "private-marketplace-current.md#enable-private-marketplace") for details. For end users, administrators must also grant the new permissions listed in [AWSPrivateMarketplaceRequests](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplacerequests "buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplacerequests").

Product requests created using the legacy website will be available at [Private Marketplace](https://aws.amazon.com/marketplace/privatemarketplace "https://aws.amazon.com/marketplace/privatemarketplace"). **Important:** The legacy website will be deprecated on March 17, 2026.
