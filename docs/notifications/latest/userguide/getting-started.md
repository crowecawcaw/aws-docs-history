

# Creating your first notification configuration in AWS User Notifications
<a name="getting-started"></a>

To get started using User Notifications to help manage your notifications, use the following steps to create a notification configuration.

**Topics**
+ [Step 1: Creating a notification configuration](#getting-started-step1)
+ [Step 2: Viewing notifications](#getting-started-step2)
+ [Next steps](#getting-started-next-steps)
+ [Filtering event rules using customized JSON event patterns in AWS User Notifications](common-usecases.md)

## Step 1: Creating a notification configuration
<a name="getting-started-step1"></a>

To receive AWS notifications, you must first create notification configurations. A notification configuration is a container for the services and event rules that you want to be notified about. An event rule specifies what events generate a notification and which delivery channels to use.

You can also create notification configurations and receive notifications using the AWS User Notifications API. For more information, see the [AWS User Notifications API Reference](https://docs.aws.amazon.com/notifications/latest/APIReference/Welcome.html).

**Note**  
You must select a notification hub in the following procedure. A notification hub is where User Notifications stores your notification data. For more information about notification hubs, see [Storing, processing, and replicating notifications using notification hubs in AWS User Notifications](notification-hubs.md). 

**To create a notification configuration**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/):

   1. Choose the bell icon in the top navigation bar.

   1. Choose **Notification center**.

   1. In the navigation pane, choose **Notification configurations**.

   1. Choose **Create notification configuration**.

   1. Select at least one notification hub.

1. 

**Add a name and description:**

   1. Enter a name for your configuration.

   1. (Optional) Enter a description for your configuration.

1. 

**Create an Event Rule:**

   1. For **AWS service name**, select the name of an AWS service to use as the event source.

   1. For **Event type**, select event types.

   1. For **Regions**, select the AWS Regions where your service data is located.
**Note**  
You can filter event rules further by using the code editor under **Advanced filter (optional)**. The **Advanced filter** doesn't currently support wildcards. To view examples of Event Patterns that you can use, see [Filtering event rules using customized JSON event patterns in AWS User Notifications](common-usecases.md).

1. 

**Define aggregation settings:**
**Tip**  
Aggregation settings reduce the number of notifications that you receive by combining multiple events into fewer notifications based on the option you choose. Aggregation settings are turned on by default. We recommend you use aggregation settings.

   1. Choose if you would like to **Receive within 5 minutes (recommended)**, **Receive within 12 hours**, or **Do not aggregate**.
**Tip**  
Choose **Receive fewer notifications** for low priority notifications. Choose **Reduce notifications delivery time** for high priority notifications.

1. 

**(Optional) Add delivery channels:**

   1. Select your delivery channels. We recommend that you view an event before adding additional recipients.

------
#### [ Email ]

**Note**  
A verification email is sent to newly added email addresses once you create the notification configuration. You can generate another verification email for pending addresses by choosing **Reverify**.  
The recipient must be signed in to the AWS account that added the email address to complete the verification process. The verification link directs to the AWS Management Console.

     1. Choose **Add emails**.
**Tip**  
You can use your email distribution lists as an email delivery channel to easily subscribe multiple email addresses to User Notifications with a single verification flow. You can separately add and remove emails to the distribution list without requiring further verification with User Notifications. 

     1. For **Recipient**, enter or choose the recipient's email address.

     1. For **Name**, enter the recipient's name.

     1. (Optional) Choose **Add another recipient** to add more recipients.

     1. Choose **Add emails**.

------
#### [ Amazon Q Developer ]

     1. For **Channel**, add a new channel or select the existing channels you want to send notifications to.

**Note**  
For more information about Amazon Q Developer in chat applications, see [What is Amazon Q Developer in chat applications?](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

------
#### [ AWS Console Mobile Application ]
**Note**  
Before you add a mobile device as a delivery channel, you must:   
Add the appropriate IAM permissions to make mobile device available in theUser Notifications console. For more information, see [IAM permissions for listing mobile devices as delivery channels](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/permissions-policies.html) in the *AWS Console Mobile Application User Guide*.
Install the AWS Console Mobile Application on to your device with push notifications enabled. Note that the notifications you receive are push notifications, not Short Message Service (SMS). For more information, see [Step 1: Get started with push notifications](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/managing-notifications.html#step-1-get-started-with-push-notifications) in the *AWS Console Mobile Application User Guide*.

     1. For **Device**, select the devices you want to send notifications to.

------

1. 

**(Optional) Manage tags:**
**Tip**  
A tag is a label that you assign to an AWS resource. Tags help you organize your resources. For more information, see [Tagging your resources](tagging-resources.md).

   1. For **Key**, enter the key name you want to use.

   1. (Optional) For **Value**, enter a value for the specified key.

   1. (Optional) Choose **Add new tag** to add more tags.

1. Review your configuration and confirm its details.

1. Choose **Create notification configuration**.

### Configuring notifications across accounts
<a name="cross-account"></a>

If you want to receive notifications from multiple accounts, follow the instructions in [ Sending and receiving Amazon EventBridge events between AWS accounts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html). Once you set up a receiver account, create a notification configuration that reacts to events by following the previous instructions.

## Step 2: Viewing notifications
<a name="getting-started-step2"></a>

Once you create your notification configurations in your account, any events matching an event rule generate a notification in the AWS Management Console. You can view notifications from the console Navigation bar and in the **Console Notification Center**. You can also view notifications from your chosen delivery channels.

**To view notifications from the Navigation bar**
**Note**  
The bell icon in the console Navigation bar shows a red badge when new notifications are available.

1. Choose the bell icon to view notifications related to your account.

1. To view additional details about a notification, select the notification.

**To view notifications in the Console Notification Center**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. View the list of **Notifications** available in the account.

1. To view additional details about a notification, select the notification.

**To view notifications in the AWS Console Mobile Application**
**Note**  
The bell icon in the tab menu of the app shows a blue badge when new notifications are available.

1. Open the Console Mobile Application.

1. Choose **Notifications** from the tab menu at the bottom of your device.

1. To view additional details about a notification, select the notification in your inbox.

**To view notifications in your chat channel**

1. Open your chat client.

1. Open the chat channel that you selected when you set up your delivery channels.

1. View the notifications available in the chat channel.

**Tip**  
If you're not seeing any notifications, see [Troubleshooting AWS User Notifications](user-notifications-troubleshooting.md)

## Next steps
<a name="getting-started-next-steps"></a>

After you create a notification configuration, you can explore some of the following topics:
+ [Filtering event rules using customized JSON event patterns in AWS User Notifications](common-usecases.md)
+ [Delivery channels in AWS User Notifications](managing-delivery-channels.md)