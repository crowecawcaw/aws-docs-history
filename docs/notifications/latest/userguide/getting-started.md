# Creating your first notification configuration in AWS User Notifications

To get started using User Notifications to help manage your notifications, use the following steps to create a notification configuration.

###### Topics

- [Step 1: Creating a notification configuration](#getting-started-step1 "#getting-started-step1")
- [Step 2: Viewing notifications](#getting-started-step2 "#getting-started-step2")
- [Next steps](#getting-started-next-steps "#getting-started-next-steps")
- [Filtering event rules using customized JSON event patterns in AWS User Notifications](common-usecases.md "common-usecases.md")

## Step 1: Creating a notification configuration

To receive AWS notifications, you must first create notification configurations. A
notification configuration is a container for the services and event rules that you want
to be notified about. An event rule specifies what events generate a notification and which delivery channels to use.

You can also create notification configurations and receive notifications using the AWS User Notifications API. For more information, see the [AWS User Notifications API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### Note

You must select a notification hub in the following procedure. A notification hub is where
User Notifications stores your notification data. For more information about notification hubs, see [Storing, processing, and replicating notifications using notification hubs in AWS User Notifications](notification-hubs.md "notification-hubs.md").

###### To create a notification configuration

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/"):
   1. Choose
      the
      bell icon in the top navigation bar.
   2. Choose **Notification center**.
   3. In the navigation pane, choose **Notification configurations**.
   4. Choose **Create notification configuration**.
   5. Select at least one notification hub.

2. ###### Add a name and description:
   1. Enter a name for your configuration.
   2. (Optional) Enter a description for your configuration.

3. ###### Create an Event Rule:
   1. For **AWS service name**, select the name of an AWS service to use
      as the event source.
   2. For **Event type**,
      select
      event types.
   3. For **Regions**, select the AWS Regions where your service data is
      located.

   ###### Note

   You can filter event rules further by using the code editor under **Advanced
   filter (optional)**. The **Advanced filter** doesn't currently support wildcards. To view examples of Event Patterns that you can use, see
   [Filtering event rules using customized JSON event patterns in AWS User Notifications](common-usecases.md "common-usecases.md").

4. ###### Define aggregation settings:

###### Tip

Aggregation settings reduce the number of notifications that you receive by combining
multiple events into fewer notifications based on the option you choose. Aggregation settings
are turned on by default. We recommend you use aggregation settings.

    1. Choose if you would like to **Receive within 5 minutes (recommended)**, **Receive within 12 hours**, or **Do not aggregate**.


    ###### Tip

    Choose **Receive fewer notifications** for low priority notifications.
     Choose **Reduce notifications delivery time** for high priority
     notifications.

5.  ###### (Optional) Add delivery channels:
    1. Select your delivery channels. We recommend that you view an event before adding
       additional recipients.

    Email

    ###### Note

    A verification email is sent to newly added email addresses once you create the
    notification configuration. You can generate another verification email for pending
    addresses by choosing **Reverify**.

        1. Choose **Add emails**.


        ###### Tip

        You can use your email distribution lists as an email delivery channel to easily subscribe multiple email addresses to User Notifications with a single verification flow.
         You can separately add and remove emails to the distribution list without requiring further verification with User Notifications.
        2. For **Recipient**, enter or choose the recipient's email
         address.
        3. For **Name**, enter the recipient's name.
        4. (Optional) Choose **Add another recipient** to add more
         recipients.
        5. Choose **Add emails**.

    Amazon Q Developer

        1. For **Channel**, add a new channel or select the existing channels
         you want to send notifications to.

    ###### Note

    For more information about Amazon Q Developer in chat applications, see [What is Amazon Q Developer in chat applications?](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md") in the
    _Amazon Q Developer in chat applications Administrator Guide_.

    AWS Console Mobile Application

    ###### Note

    Before you add a mobile device as a delivery channel, you must:

        * Add the appropriate IAM permissions to make mobile device available in theUser Notifications
         console. For more information, see [IAM permissions for
         listing mobile devices as delivery channels](../../../consolemobileapp/latest/userguide/permissions-policies.md "../../../consolemobileapp/latest/userguide/permissions-policies.md") in the *AWS Console Mobile Application User
         Guide*.
        * Install the AWS Console Mobile Application on to your device with push notifications enabled. Note
         that the notifications you receive are push notifications, not Short Message Service
         (SMS). For more information, see [Step 1: Get started with push notifications](../../../consolemobileapp/latest/userguide/managing-notifications.md#step-1-get-started-with-push-notifications "../../../consolemobileapp/latest/userguide/managing-notifications.md#step-1-get-started-with-push-notifications") in the *AWS Console Mobile Application User
         Guide*.

        1. For **Device**, select the devices you want to send notifications
         to.

6.  ###### (Optional) Manage tags:

###### Tip

A tag is a label that you assign to an AWS resource. Tags help you organize your
resources. For more information, see [Tagging your resources](tagging-resources.md "tagging-resources.md").

    1. For **Key**, enter the key name you want to use.
    2. (Optional) For **Value**, enter a value for the specified key.
    3. (Optional) Choose **Add new tag** to add more tags.

7. Review your configuration and confirm its details.
8. Choose **Create notification configuration**.

### Configuring notifications across accounts

If you want to receive notifications from multiple accounts, follow the instructions in
[Sending
and receiving Amazon EventBridge events between AWS accounts](../../../eventbridge/latest/userguide/eb-cross-account.md "../../../eventbridge/latest/userguide/eb-cross-account.md"). Once you set up a receiver
account, create a notification configuration that reacts to events by following the previous
instructions.

## Step 2: Viewing notifications

Once you create your notification configurations in your account, any events matching an
event rule generate a notification in the AWS Management Console. You can view notifications from the console
Navigation bar and in the **Console Notification Center**. You can also view
notifications from your chosen delivery channels.

###### To view notifications from the Navigation bar

###### Note

The bell icon in the console Navigation bar shows a red badge when new notifications are
available.

1. Choose the bell icon to view notifications related to your account.
2. To view additional details about a notification, select the notification.

###### To view notifications in the Console Notification Center

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. View the list of **Notifications** available in the account.
3. To view additional details about a notification, select the notification.

###### To view notifications in the AWS Console Mobile Application

###### Note

The bell icon in the tab menu of the app shows a blue badge when new notifications are
available.

1. Open the Console Mobile Application.
2. Choose **Notifications** from the tab menu at the bottom of your device.
3. To view additional details about a notification, select the notification in your inbox.

###### To view notifications in your chat channel

1. Open your chat client.
2. Open the chat channel that you selected when you set up your delivery channels.
3. View the notifications available in the chat channel.

###### Tip

If you're not seeing any notifications, see [Troubleshooting AWS User Notifications](user-notifications-troubleshooting.md "user-notifications-troubleshooting.md")

## Next steps

After you create a notification configuration, you can explore some of the following
topics:

- [Filtering event rules using customized JSON event patterns in AWS User Notifications](common-usecases.md "common-usecases.md")
- [Delivery channels in AWS User Notifications](managing-delivery-channels.md "managing-delivery-channels.md")
