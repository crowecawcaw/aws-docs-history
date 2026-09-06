

# Configure promotional plan expiration notifications
<a name="configure-promo-plan-notifications"></a>

You can use [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) to configure notifications to inform you when your support plan's promotional period is ending. You can subscribe to receive notifications by email, in the AWS Console Mobile Application, or in other chat channels of your choice.

**Configure promotional support plan expiration notifications**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/):

   1. Choose the bell icon in the top navigation bar.

   1. Choose **Notification center**.

   1. In the navigation pane, choose **Notification configuration**.

   1. Choose **Create notification configuration**.

   1. Select at least one **Configuration hub**. For more information, see [Storing, processing, and replicating notifications using notification hubs in AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html).

1. For **Event Rule**, enter the following information:
   + For **AWS service name**, enter **Support Plans**.
   + For **Event type**, enter **Support Plan Promotion Expiration**.
   + For **Regions**, select the source AWS Regions where you want to receive notifications. For this option, choose US East (N. Virginia), US East (Ohio), US West (N. California), and US West (Oregon).

1. Configure aggregation settings to reduce notification frequency. We recommend that you set aggregation to **Receive within 5 minutes**.

1. Configure the delivery channels where you want to receive notifications. If you don't select a delivery channel, you can view notifications by selecting the bell icon in the AWS Management Console navigation bar.

For detailed instructions on creating user-configured notifications, see [Step 1: creating a notification configuration in the AWS User Notifications User Guide](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html#getting-started-step1).

## View promotional plan notifications
<a name="view-promo-plan-notifications"></a>

Your notifications are delivered to the delivery channel that you chose during configuration. You can also view notifications by choosing the bell icon in the console navigation bar. The bell icon shows a red badge when new notifications are available.

For more information on viewing notifications, see [Step 2: Viewing notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html#getting-started-step2) in the *AWS User Notifications User Guide*.