# Configure promotional plan expiration notifications

You can use [AWS User Notifications](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md") to configure notifications to inform you when your support plan's promotional period is ending. You can subscribe to receive notifications by email, in the AWS Console Mobile Application, or in other chat channels of your choice.

###### Configure promotional support plan expiration notifications

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/"):
   1. Choose the bell icon in the top navigation bar.
   2. Choose **Notification center**.
   3. In the navigation pane, choose **Notification configuration**.
   4. Choose **Create notification configuration**.
   5. Select at least one **Configuration hub**. For more information, see [Storing, processing, and replicating notifications using notification hubs in AWS User Notifications](../../../notifications/latest/userguide/notification-hubs.md "../../../notifications/latest/userguide/notification-hubs.md").

2. For **Event Rule**, enter the following information:
   - For **AWS service name**, enter **Support Plans**.
   - For **Event type**, enter **Support Plan Promotion Expiration**.
   - For **Regions**, select the source AWS Regions where you want to receive notifications. For this option, choose US East (N. Virginia), US East (Ohio), US West (N. California), and US West (Oregon).

3. Configure aggregation settings to reduce notification frequency. We recommend that you set aggregation to **Receive within 5 minutes**.
4. Configure the delivery channels where you want to receive notifications. If you don't select a delivery channel, you can view notifications by selecting the bell icon in the AWS Management Console navigation bar.
   For detailed instructions on creating user-configured notifications, see [Step 1: creating a notification configuration in the AWS User Notifications User Guide](../../../notifications/latest/userguide/getting-started.md#getting-started-step1 "../../../notifications/latest/userguide/getting-started.md#getting-started-step1").

## View promotional plan notifications

Your notifications are delivered to the delivery channel that you chose during configuration. You can also view notifications by choosing the bell icon in the console navigation bar. The bell icon shows a red badge when new notifications are available.

For more information on viewing notifications, see [Step 2: Viewing notifications](../../../notifications/latest/userguide/getting-started.md#getting-started-step2 "../../../notifications/latest/userguide/getting-started.md#getting-started-step2") in the _AWS User Notifications User Guide_.
