# Configure integration between notifications and

AWS Chatbot

AWS Chatbot is an AWS service that makes it possible for DevOps and software development
teams to use Amazon Chime chat rooms, Slack channels, and Microsoft Team channels to monitor
and respond to operational events in the AWS Cloud. You can configure integration between
notification rule targets and AWS Chatbot so that notifications about events appear in the Amazon Chime
room, Slack channel, or Microsoft Teams channel you choose. For more information, see the
[AWS Chatbot
documentation](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md").

Before you configure integration with AWS Chatbot, you must configure a notification rule and a
rule target. For more information, see [Setting up](setting-up.md "setting-up.md") and [Create a notification rule](notification-rule-create.md "notification-rule-create.md").
You must also configure a Slack channel, Microsoft Teams channel, or an Amazon Chime chatroom in
AWS Chatbot. For more information, see the documentation for these services.

###### Topics

- [Configure an AWS Chatbot client for
  a Slack channel](#notifications-chatbot-configure-client "#notifications-chatbot-configure-client")
- [Configure an AWS Chatbot client for
  a Microsoft Teams channel](#notifications-chatbot-configure-client-ts "#notifications-chatbot-configure-client-ts")
- [Configure clients for
  Slack or Amazon Chime manually](#notifications-chatbot-configure-manual-client "#notifications-chatbot-configure-manual-client")

## Configure an AWS Chatbot client for

a Slack channel

You can create notification rules that use an AWS Chatbot client as a target. If you create
a client for a Slack channel, you can use this client directly as a target in the
workflow for creating a notification rule. This is the easiest way to set up
notifications that appear in Slack channels.

## To create an AWS Chatbot client with

Slack
to use as a target

1. Follow the instructions in [Setting up
   AWS Chatbot with
   Slack](../../../chatbot/latest/adminguide/slack-setup.md#slack-client-setup "../../../chatbot/latest/adminguide/slack-setup.md#slack-client-setup")
   in the _AWS Chatbot Administrator Guide_. When you do so, consider the
   following choices for optimal integration with notifications:
   - When creating an IAM role, consider choosing a role name that makes it easy to identify the
     purpose of this role (for example,
     `AWSCodeStarNotifications-Chatbot-Slack-Role`). This
     can help you identify the purpose of the role in the future.
   - In **SNS topics**, you don't have to choose a topic or an AWS Region. When
     you choose the AWS Chatbot client as a [target](concepts.md#targets "concepts.md#targets"), an
     Amazon SNS topic with all the required permissions is created and configured for the
     AWS Chatbot client as part of the notification rule creation process.

2. Complete the client creation process. This client is then available for you to choose
   as a target when creating notification rules. For more information, see [Create a notification rule](notification-rule-create.md "notification-rule-create.md").

###### Note

Do not remove the Amazon SNS topic from the AWS Chatbot client after it has been configured
for you. Doing so will prevent notifications from being sent to Slack.

## Configure an AWS Chatbot client for

a Microsoft Teams channel

You can create notification rules that use an AWS Chatbot client as a target. If you create
a client for a Microsoft Teams channel, you can use this client directly as a target in the
workflow for creating a notification rule. This is the easiest way to set up
notifications that appear in Microsoft Teams channels.

## To create an AWS Chatbot client with

Microsoft Teams to use as a target

1. Follow the instructions in [Setting up
   AWS Chatbot with Microsoft Teams](../../../chatbot/latest/adminguide/teams-setup.md#teams-client-setup "../../../chatbot/latest/adminguide/teams-setup.md#teams-client-setup")
   in the _AWS Chatbot Administrator Guide_. When you do so, consider the
   following choices for optimal integration with notifications:
   - When creating an IAM role, consider choosing a role name that makes it easy to identify the
     purpose of this role (for example,
     `AWSCodeStarNotifications-Chatbot-Microsoft-Teams-Role`). This
     can help you identify the purpose of the role in the future.
   - In **SNS topics**, you don't have to choose a topic or an AWS Region. When
     you choose the AWS Chatbot client as a [target](concepts.md#targets "concepts.md#targets"), an
     Amazon SNS topic with all the required permissions is created and configured for the
     AWS Chatbot client as part of the notification rule creation process.

2. Complete the client creation process. This client is then available for you to choose
   as a target when creating notification rules. For more information, see [Create a notification rule](notification-rule-create.md "notification-rule-create.md").

###### Note

Do not remove the Amazon SNS topic from the AWS Chatbot client after it has been configured
for you. Doing so will prevent notifications from being sent to Microsoft Teams.

## Configure clients for

Slack or Amazon Chime manually

You can choose to create the integration between notifications and Slack or Amazon Chime
directly. This is the only method available for configuring notifications to Amazon Chime
chatrooms. When you configure this integration manually, you create an AWS Chatbot client
that uses an Amazon SNS topic that you have previously configured as the target for a
notification rule.

## To manually integrate

notifications with AWS Chatbot and slack

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/ "https://console.aws.amazon.com/codesuite/settings/notifications/").
2. Choose **Settings**, and then choose **Notification
   rules**.
3. In **Notification rule targets**, find and copy the
   target.

###### Note

You can configure more than one notification rule to use the same Amazon SNS
topic as its target. This can help you consolidate messaging, but can have
unintended consequences if the subscription list is intended for one
notification rule or resource. 4. Open the AWS Chatbot console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/"). 5. Choose **Configure new client**, and then choose
**Slack**. 6. Choose **Configure**. 7. Sign in to your Slack workspace. 8. When you are prompted to confirm the choices, choose
**Allow**. 9. Choose **Configure new channel**. 10. In **Configuration details**, in **Configuration
name**, enter a name for your client. This is the name that will
appear in the list of available targets for the **AWS Chatbot
(Slack)** target type when you create notification rules. 11. In **Configure Slack Channel**, in **Channel
type**, choose **Public** or
**Private**, depending on the type of channel with which
you want to integrate.

    * In **Public channel**, choose the name of the Slack
     channel from the list.
    * In **Private channel ID**, enter the channel code or
     URL.

12. In **IAM permissions**, in **Role**,
    choose **Create an IAM role using a template**. In
    **Policy templates**, choose **Notification
    permissions**. In **Role name**, enter a name for
    this role (for example,
    `AWSCodeStarNotifications-Chatbot-Slack-Role`). In
    **Policy templates**, choose **Notification
    permissions**.
13. In **SNS topics**, in **SNS Region**, choose
    the AWS Region where you created the notification rule target. In **SNS
    topics**, choose the name of the Amazon SNS topic that you configured as
    the notification rule target.

###### Note

This step is not necessary if you will create a notification rule using
this client as a target. 14. Choose **Configure**.

###### Note

If you configured integration with a private channel, you must invite
AWS Chatbot to the channel before you will see notifications in that channel. For
more information, see the [AWS Chatbot
documentation](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md"). 15. (Optional) To test the integration, make a change in the resource that matches
an event type for a notification rule that is configured to use the Amazon SNS topic
as its target. For example, if you have a notification rule configured to send
notifications when comments are made on a pull request, comment on a pull
request and then watch the Slack channel in the browser to see when the
notification appears.

## To integrate notifications with AWS Chatbot

and Amazon Chime

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/ "https://console.aws.amazon.com/codesuite/settings/notifications/").
2. Choose **Settings**, and then choose **Notification
   rules**.
3. In **Notification rule targets**, find and copy the
   target.

###### Note

You can configure more than one notification rule to use the same Amazon SNS
topic as its target. This can help you consolidate messaging, but can have
unintended consequences if the subscription list is for one notification
rule or resource. 4. In Amazon Chime, open the chatroom that you want to configure for integration. 5. Choose the gear icon in the upper-right corner, and then choose **Manage webhooks**. 6. In the **Manage webhooks** dialog box, choose
**New**, enter a name for the webhook, and then
choose **Create**. 7. Verify that the webhook appears, and then choose **Copy
webhook URL**. 8. Open the AWS Chatbot console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/"). 9. Choose **Configure new client**, and then choose
**Amazon Chime**. 10. In **Configuration details**, in **Configuration
name**, enter a name for your client. 11. In **Webhook URL**, paste the URL. In **Webhook
description**, provide an optional description. 12. In **IAM permissions**, in **Role**,
choose **Create an IAM role using a template**. In
**Policy templates**, choose **Notification
permissions**. In **Role name**, enter a name for
this role (for example,
`AWSCodeStarNotifications-Chatbot-Chime-Role`). 13. In **SNS topics**, in **SNS Region**, choose
the AWS Region where you created the notification rule target. In **SNS
topics**, choose the name of the Amazon SNS topic you configured as the
notification rule target. 14. Choose **Configure**. 15. (Optional) To test the integration, make a change in the resource that matches
an event type for a notification rule that is configured to use the Amazon SNS topic
as its target. For example, if you have a notification rule configured to send
notifications when comments are made on a pull request, comment on a pull
request and then watch the Amazon Chime chatroom to see when the notification
appears.
