

# Private Marketplace notifications
<a name="configuring-notifications"></a>

Private Marketplace administrators and buyers receive notification events from AWS Marketplace when a buyer requests a product, and when a request is approved or declined. Administrators receive notifications for requests from any account in their AWS organization. Buyers only receive notifications for requests from their accounts. The notification events include product details and the seller's name.

For information about the Private Marketplace notification events, see [Amazon EventBridge notifications for AWS Marketplace events](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-notifications-eventbridge.html), later in this guide.

You can create EventBridge rules with different target types by following the steps in [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html), in the *Amazon EventBridge User Guide*.

## Creating email notification configurations
<a name="creating-email-notification-configurations"></a>

You can use the AWS User Notifications service to get notifications for events through multiple channels, including email. The following steps explain how to create an email notification configuration. Notification configurations act as containers for the services and event rules that you want to be notified about. An event rule specifies the events that generate a notification in the AWS console, and which delivery channels to use.

**To create a notification configuration**

1. Sign in to the AWS Management Console and navigate to AWS User Notifications.

1. Choose **Notification configurations**, then choose **Create notification configuration**.

1. In the **Name** box, enter a name for the configuration.

1. In the **Event rules** section of the page, enter the following values:

   1. For **AWS service name**, choose **AWS Marketplace Private Marketplace**.

   1. For **Event type**, choose one or more of the following:

      1. **Product Request Created**

      1. **Product Request Approved**

      1. **Product Request Declined**

      1. **Product Request Cancelled**

      1. **Product Request Expired**

   1. For **Regions**, select **us-east-1**. Private marketplace only operates in that Region.

1. Under **Aggregation settings**, we recommend choosing **Receive within 5 minutes**.

1. Under **Delivery channels**, select the **email** checkbox, then do the following:

   1. In the **Recipient** box, enter the email address of the notification recipient.

   1. As needed, choose **Add another recipient**, the enter another email address in the **Recipient** box. You can enter a maximum of 99 recipients.

   1. (Optional) Under **Manage tags**, choose **Add new tag**, enter values in the **Key** and **Value** boxes.

1. When finished, choose **Create notification configuration**.

In addition to using an email delivery channel, you can also use the AWS Console Mobile App and Chat delivery channels. The following links take you to more information about those channels and about User Notifications.
+ [What is the AWS Console Mobile Application](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html), in the *AWS Console Mobile Application User Guide*.
+ [What is AWS Chatbot](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html), in the *Amazon Q Developer in chat applications Administrator Guide*.
+ [Creating a notification configuration](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html#getting-started-step1), in the *User Notifications User Guide*.