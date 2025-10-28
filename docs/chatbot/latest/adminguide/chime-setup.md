AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Get started with Amazon Chime

To get started using Amazon Q Developer in chat applications to help manage your AWS infrastructure, follow the steps below to set up Amazon Q Developer in chat applications with chat channels and Amazon SNS topic subscriptions.

###### Topics

- [Prerequisites](#getting-started-prerequisites-chime "#getting-started-prerequisites-chime")
- [Step 1: Setting up Amazon Q Developer in chat applications with Amazon Chime](#chime-sets "#chime-sets")
- [Step 2: Test notifications from AWS services to Amazon Chime](#test-notifications "#test-notifications")
- [Next steps](#next-steps "#next-steps")

## Prerequisites

Before you get started, make sure you've completed the tasks in [Setting up Amazon Q Developer in chat applications](getting-started.md#setting-up "getting-started.md#setting-up"). You will need to choose a permissions scheme in the following procedure.
This scheme determines the permissions your channel members will have and what Amazon Q Developer in chat applications can do on your behalf. For more information about Amazon Q Developer in chat applications permissions, see [Understanding permissions](understanding-permissions.md "understanding-permissions.md").

## Step 1: Setting up Amazon Q Developer in chat applications with Amazon Chime

To set up Amazon Q Developer in chat applications for Amazon Chime, get the webhook URL for your team's chat room from
Amazon Chime.

**Prerequisite**

You must be an Amazon Chime chat room admin and have the ability to manage webhooks.

###### To configure an Amazon Chime client

1. [Open Amazon Chime](http://app.chime.aws/ "http://app.chime.aws/").
2. For **Amazon Chime**, choose the chat room that you want to set up to
   receive notifications through Amazon Q Developer in chat applications.
3. Choose the Room settings icon
   on the top right and choose **Manage Webhooks and Bots**.

Amazon Chime displays the webhooks associated with the chat room.

###### Note

You can have multiple webhooks in a single Amazon Chime chat room.

For example, in an **Amazon Chime** chat room, one webhook could send
notifications for Amazon CloudWatch alarms and another webhook could send AWS Security Hub security
alerts. Each webhook receives notifications only for the SNS topics subscribed to it.
All chat room members can see all of the notifications from each of the SNS topics. 4. For the webhook, choose **Copy URL** and choose
**Done**.

If you need to create a new webhook for the chat room, choose **Add
webhook**, enter a name for the webhook in the **Name**
field, and choose **Create**. 5. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/"). 6. Choose **Configure new client**. 7. Choose **Amazon Chime** and choose
**Configure**. 8. Under **Configuration details**, enter a name for your configuration. The name must be unique across your account and can't be edited later. 9. If you want to enable logging for this configuration, choose **Send logs to CloudWatch**. For more information, see [Amazon CloudWatch Logs for Amazon Q Developer in chat applications](cloudwatch-logs.md "cloudwatch-logs.md").

###### Note

There is an extra charge for using CloudWatch Logs. 10. For **Configure Amazon Chime webhook**, do the following.

    1. Paste the webhook URL that you copied from Amazon Chime.
    2. For **Webhook description**, use the following naming
     convention to describe the purpose of the webhook:
     `Chat_room_name/Webhook_name`. This helps you associate Amazon Chime
     webhooks with their Amazon Q Developer in chat applications configurations.

11. For **IAM permissions**, set the IAM permissions for
    Amazon Q Developer in chat applications.
    1.  For **Role**, choose **Create a new role from
        template**. If you want to use an existing role instead, choose it from
        the **IAM Role** list. To use an existing IAM role, you might
        need to modify it for use with Amazon Q Developer in chat applications. For more information, see [Configuring an IAM Role
        for Amazon Q Developer in chat applications](editing-iam-roles-for-chatbot.md "editing-iam-roles-for-chatbot.md").
    2.  For **Policy templates**, choose **Notification
        permissions**. This is the IAM policy provided by Amazon Q Developer in chat applications. It
        provides the necessary Read and List permissions for CloudWatch alarms, events and logs,
        and for Amazon SNS topics.
    3.  For **Role name**, enter a name. Valid characters: a-z, A-Z,
        0-9.

12. Set up the SNS topics that will send notifications to the Amazon Chime webhook.
    1.  For **SNS Region**, choose the AWS Region that hosts the SNS
        topics for this Amazon Q Developer in chat applications subscription.
    2.  For **SNS topic**, choose the SNS topic for the client
        subscription. This topic determines the content that's sent to the Amazon Chime webhook. If
        the region has additional SNS topics, you can choose them from the same dropdown
        list.
    3.  If you want to add an SNS topic from another Region to the notification
        subscription, choose **Add another Region**.

    ###### Note

    For a tutorial on subscribing existing Amazon SNS topics to Amazon Q Developer in chat applications, see [Tutorial: Subscribing an Amazon SNS topic to Amazon Q Developer in chat applications](subscribe-sns-topic.md "subscribe-sns-topic.md").

13. Choose **Configure**.

Notifications from supported services that publish to the chosen SNS topics will now
appear in the Amazon Chime chat room.

You can configure as many webhooks as you need. The SNS topics that you choose also must
be configured in the services for which you want to receive notifications. For more
information, see [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md "related-services.md").

## Step 2: Test notifications from AWS services to Amazon Chime

To verify that an Amazon Simple Notification Service (Amazon SNS) topic sends notifications to your Amazon Chime chat
room, you can test your setup by sending a notification. To test your notifications, ensure
your topics are assigned to a service supported by Amazon Q Developer in chat applications. For a list of supported services,
see [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md "related-services.md"). You can also test
notifications by using CloudWatch. For more information, see [Test notifications from AWS services to Amazon Chime using CloudWatch](test-notifications-cw.md "test-notifications-cw.md").

###### Testing notifications with configured clients

1. Open the [Amazon Q Developer in chat applications
   console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Choose the configured client you want to test.
3. In the configured client, choose the webhook to send a test notification to.
4. Choose **Send test message**.
5. View the confirmation message at the top of the screen that shows a message was sent to your
   Amazon SNS topic.
6. Confirm the test message in your Amazon Chime chat room.

## Next steps

After you configure your chat clients and test that your notifications are working, you might want to explore some of the following topics:

- Learn about which other AWS services you can integrate with Amazon Q Developer in chat applications in [Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md "related-services.md").
- Learn about what you can customize using Amazon Q Developer in chat applications in [Customizing Amazon Q Developer in chat applications](customizing-chatbot.md "customizing-chatbot.md").
