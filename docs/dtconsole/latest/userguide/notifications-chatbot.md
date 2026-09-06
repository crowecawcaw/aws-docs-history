

# Configure integration between notifications and AWS Chatbot
<a name="notifications-chatbot"></a>

AWS Chatbot is an AWS service that makes it possible for DevOps and software development teams to use Amazon Chime chat rooms, Slack channels, and Microsoft Team channels to monitor and respond to operational events in the AWS Cloud. You can configure integration between notification rule targets and AWS Chatbot so that notifications about events appear in the Amazon Chime room, Slack channel, or Microsoft Teams channel you choose. For more information, see the [AWS Chatbot documentation](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html).

Before you configure integration with AWS Chatbot, you must configure a notification rule and a rule target. For more information, see [Setting up](setting-up.md) and [Create a notification rule](notification-rule-create.md). You must also configure a Slack channel, Microsoft Teams channel, or an Amazon Chime chatroom in AWS Chatbot. For more information, see the documentation for these services.

**Topics**
+ [Configure an AWS Chatbot client for a Slack channel](#notifications-chatbot-configure-client)
+ [Configure an AWS Chatbot client for a Microsoft Teams channel](#notifications-chatbot-configure-client-ts)
+ [Configure clients for Slack or Amazon Chime manually](#notifications-chatbot-configure-manual-client)

## Configure an AWS Chatbot client for a Slack channel
<a name="notifications-chatbot-configure-client"></a>

You can create notification rules that use an AWS Chatbot client as a target. If you create a client for a Slack channel, you can use this client directly as a target in the workflow for creating a notification rule. This is the easiest way to set up notifications that appear in Slack channels.

## To create an AWS Chatbot client with Slack to use as a target


1. Follow the instructions in [Setting up AWS Chatbot with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html#slack-client-setup) in the *AWS Chatbot Administrator Guide*. When you do so, consider the following choices for optimal integration with notifications:
   + When creating an IAM role, consider choosing a role name that makes it easy to identify the purpose of this role (for example, **AWSCodeStarNotifications-Chatbot-Slack-Role**). This can help you identify the purpose of the role in the future.
   + In **SNS topics**, you don't have to choose a topic or an AWS Region. When you choose the AWS Chatbot client as a [target](concepts.md#targets), an Amazon SNS topic with all the required permissions is created and configured for the AWS Chatbot client as part of the notification rule creation process.

1. Complete the client creation process. This client is then available for you to choose as a target when creating notification rules. For more information, see [Create a notification rule](notification-rule-create.md).
**Note**  
Do not remove the Amazon SNS topic from the AWS Chatbot client after it has been configured for you. Doing so will prevent notifications from being sent to Slack.

## Configure an AWS Chatbot client for a Microsoft Teams channel
<a name="notifications-chatbot-configure-client-ts"></a>

You can create notification rules that use an AWS Chatbot client as a target. If you create a client for a Microsoft Teams channel, you can use this client directly as a target in the workflow for creating a notification rule. This is the easiest way to set up notifications that appear in Microsoft Teams channels.

## To create an AWS Chatbot client with Microsoft Teams to use as a target


1. Follow the instructions in [Setting up AWS Chatbot with Microsoft Teams](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the *AWS Chatbot Administrator Guide*. When you do so, consider the following choices for optimal integration with notifications:
   + When creating an IAM role, consider choosing a role name that makes it easy to identify the purpose of this role (for example, **AWSCodeStarNotifications-Chatbot-Microsoft-Teams-Role**). This can help you identify the purpose of the role in the future.
   + In **SNS topics**, you don't have to choose a topic or an AWS Region. When you choose the AWS Chatbot client as a [target](concepts.md#targets), an Amazon SNS topic with all the required permissions is created and configured for the AWS Chatbot client as part of the notification rule creation process.

1. Complete the client creation process. This client is then available for you to choose as a target when creating notification rules. For more information, see [Create a notification rule](notification-rule-create.md).
**Note**  
Do not remove the Amazon SNS topic from the AWS Chatbot client after it has been configured for you. Doing so will prevent notifications from being sent to Microsoft Teams.

## Configure clients for Slack or Amazon Chime manually
<a name="notifications-chatbot-configure-manual-client"></a>

You can choose to create the integration between notifications and Slack or Amazon Chime directly. This is the only method available for configuring notifications to Amazon Chime chatrooms. When you configure this integration manually, you create an AWS Chatbot client that uses an Amazon SNS topic that you have previously configured as the target for a notification rule.<a name="notification-rule-chatbot-console-manual"></a>

## To manually integrate notifications with AWS Chatbot and slack
<a name="notification-rule-chatbot-console-manual"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. Choose **Settings**, and then choose **Notification rules**.

1. In **Notification rule targets**, find and copy the target.
**Note**  
You can configure more than one notification rule to use the same Amazon SNS topic as its target. This can help you consolidate messaging, but can have unintended consequences if the subscription list is intended for one notification rule or resource. 

1. Open the AWS Chatbot console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/).

1. Choose **Configure new client**, and then choose **Slack**.

1. Choose **Configure**.

1. Sign in to your Slack workspace.

1. When you are prompted to confirm the choices, choose **Allow**.

1. Choose **Configure new channel**.

1. In **Configuration details**, in **Configuration name**, enter a name for your client. This is the name that will appear in the list of available targets for the **AWS Chatbot (Slack)** target type when you create notification rules.

1. In **Configure Slack Channel**, in **Channel type**, choose **Public** or **Private**, depending on the type of channel with which you want to integrate. 
   + In **Public channel**, choose the name of the Slack channel from the list.
   + In **Private channel ID**, enter the channel code or URL.

1. In **IAM permissions**, in **Role**, choose **Create an IAM role using a template**. In **Policy templates**, choose **Notification permissions**. In **Role name**, enter a name for this role (for example, **AWSCodeStarNotifications-Chatbot-Slack-Role**). In **Policy templates**, choose **Notification permissions**.

1. In **SNS topics**, in **SNS Region**, choose the AWS Region where you created the notification rule target. In **SNS topics**, choose the name of the Amazon SNS topic that you configured as the notification rule target.
**Note**  
This step is not necessary if you will create a notification rule using this client as a target.

1. Choose **Configure**.
**Note**  
If you configured integration with a private channel, you must invite AWS Chatbot to the channel before you will see notifications in that channel. For more information, see the [AWS Chatbot documentation](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html).

1. (Optional) To test the integration, make a change in the resource that matches an event type for a notification rule that is configured to use the Amazon SNS topic as its target. For example, if you have a notification rule configured to send notifications when comments are made on a pull request, comment on a pull request and then watch the Slack channel in the browser to see when the notification appears.<a name="notifications-chatbot-chime"></a>

## To integrate notifications with AWS Chatbot and Amazon Chime
<a name="notifications-chatbot-chime"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. Choose **Settings**, and then choose **Notification rules**.

1. In **Notification rule targets**, find and copy the target.
**Note**  
You can configure more than one notification rule to use the same Amazon SNS topic as its target. This can help you consolidate messaging, but can have unintended consequences if the subscription list is for one notification rule or resource.

1. In Amazon Chime, open the chatroom that you want to configure for integration.

1. Choose the gear icon in the upper-right corner, and then choose **Manage webhooks**. 

1. In the **Manage webhooks** dialog box, choose **New**, enter a name for the webhook, and then choose **Create**. 

1. Verify that the webhook appears, and then choose **Copy webhook URL**. 

1. Open the AWS Chatbot console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/).

1. Choose **Configure new client**, and then choose **Amazon Chime**.

1. In **Configuration details**, in **Configuration name**, enter a name for your client. 

1. In **Webhook URL**, paste the URL. In **Webhook description**, provide an optional description.

1. In **IAM permissions**, in **Role**, choose **Create an IAM role using a template**. In **Policy templates**, choose **Notification permissions**. In **Role name**, enter a name for this role (for example, **AWSCodeStarNotifications-Chatbot-Chime-Role**). 

1. In **SNS topics**, in **SNS Region**, choose the AWS Region where you created the notification rule target. In **SNS topics**, choose the name of the Amazon SNS topic you configured as the notification rule target.

1. Choose **Configure**.

1. (Optional) To test the integration, make a change in the resource that matches an event type for a notification rule that is configured to use the Amazon SNS topic as its target. For example, if you have a notification rule configured to send notifications when comments are made on a pull request, comment on a pull request and then watch the Amazon Chime chatroom to see when the notification appears.