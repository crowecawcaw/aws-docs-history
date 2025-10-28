# Receiving budget alerts in chat applications

You can use Amazon Q Developer to receive and monitor your budget alerts in Amazon Chime,
Microsoft Teams, and Slack.

Amazon Chime

###### To begin receiving your budget alerts in

Amazon Chime

1. Go to AWS Budgets and either create a new budget or edit an existing one.
2. In the budget configuration, choose **Configure
   alerts**.
3. Add an Amazon SNS topic as an alert recipient to a specific alert or alerts.

###### Note

To ensure AWS Budgets has permissions to publish to your Amazon SNS
topics, see [Creating an Amazon SNS
topic for budget notifications](budgets-sns-policy.md "budgets-sns-policy.md"). 4. Complete and save your budget configuration. 5. Open [Amazon Chime](http://app.chime.aws/ "http://app.chime.aws/"). 6. For **Amazon Chime**, choose the chat room that you
want to set up to receive notifications through Amazon Q
Developer. 7. Choose the Room settings icon on the top right and choose
**Manage webhooks and bots**.

Amazon Chime displays the webhooks associated with the chat
room. 8. For the webhook, choose **Copy URL**, and then choose
**Done**.

If you need to create a new webhook for the chat room, choose
**Add webhook**, enter a name for the webhook in
the **Name** field, and then choose
**Create**. 9. Open the [Amazon Q Developer in chat applications console](https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients "https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients"). 10. Choose **Configure new client**. 11. Choose **Amazon Chime**, and then choose
**Configure**. 12. Under **Configuration details**, enter a name for
your configuration. The name must be unique across your account and
can't be edited later. 13. To configure Amazon Chime webhook, do the following:

    1. For **Webhook URL**, paste the webhook URL
     that you copied from Amazon Chime.
    2. For **Webhook description**, use the
     following naming convention to describe the purpose of the
     webhook: **Chat\_room\_name/Webhook\_name**. This
     helps you associate Amazon Chime webhooks with their Amazon Q
     Developer configurations.

14. If you want to enable logging for this configuration, choose
    **Publish logs to Amazon CloudWatch Logs**. For
    more information, see Amazon CloudWatch Logs for Amazon Q
    Developer.

###### Note

There is an additional charge for using Amazon CloudWatch
Logs. 15. For **Permissions**, set the IAM permissions as
follows:

    1. For **IAM role**, choose **Create an
     IAM role using a template**. If you want to use an
     existing role instead, choose it from the **IAM
     role** list. To use an existing IAM role, you might
     need to modify it for use with Amazon Q Developer. For more
     information, see Configuring an IAM Role for Amazon Q
     Developer.
    2. For **Role name**, enter a name. Valid
     characters: a-z, A-Z, 0-9.
    3. For **Policy templates**, choose
     **Notification permissions**. This is the
     IAM policy provided by Amazon Q Developer. It provides the
     necessary Read and List permissions for CloudWatch alarms,
     events, and logs, and for Amazon SNS topics.

16. Set up the SNS topics that will send notifications to the Amazon Chime
    webhook.
    1.  For **SNS Region**, choose the AWS Region
        that hosts the SNS topics for this Amazon Q Developer
        subscription.
    2.  For **SNS topics**, choose the SNS topic for
        the client subscription. This topic determines the content
        that's sent to the Amazon Chime webhook. If the region has
        additional SNS topics, you can choose them from the same
        dropdown list.

    ###### Note

    You can send budget alerts to multiple Amazon SNS topics and Regions.

    At least one of the Amazon SNS topics must match the Amazon SNS
    topic or topics of your budget or budgets. 3. If you want to add an SNS topic from another Region to the
    notification subscription, choose **Add another
    Region**.

17. Choose **Configure**.

For any additional details, see [Tutorial: Get started with Amazon Chime](../../../chatbot/latest/adminguide/chime-setup.md "../../../chatbot/latest/adminguide/chime-setup.md") in the _Amazon Q
Developer in chat applications Administrator Guide_.

Microsoft Teams

###### To begin receiving your budget alerts in Microsoft Teams

1. Go to AWS Budgets and either create a new budget or edit an existing
   one.
2. In the budget configuration, choose **Configure
   alerts**.
3. Add an Amazon SNS topic as an alert recipient to a specific alert or
   alerts.

###### Note

To ensure AWS Budgets has permissions to publish to your Amazon SNS
topics, see [Creating an Amazon SNS
topic for budget notifications](budgets-sns-policy.md "budgets-sns-policy.md"). 4. Complete and save your budget configuration. 5. Add Amazon Q Developer to your team. 6. Open the [Amazon Q Developer in chat applications console](https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients "https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients"). 7. Choose **Configure new client**. 8. Choose **Microsoft Teams**, and then choose
**Configure**. 9. Copy and paste your Microsoft Teams channel URL. 10. Choose **Configure**. 11. On the Microsoft Teams authorization page, choose
**Accept**.

For any additional details, see [Tutorial: Get started with Microsoft Teams](../../../chatbot/latest/adminguide/teams-setup.md "../../../chatbot/latest/adminguide/teams-setup.md") in the _Amazon
Q Developer in chat applications Administrator Guide_.

Slack

###### To begin receiving your budget alerts in Slack

1. Go to AWS Budgets and either create a new budget or edit an existing
   one.
2. In the budget configuration, choose **Configure
   alerts**.
3. Add an Amazon SNS topic as an alert recipient to a specific alert or
   alerts.

###### Note

To ensure AWS Budgets has permissions to publish to your Amazon SNS
topics, see [Creating an Amazon SNS
topic for budget notifications](budgets-sns-policy.md "budgets-sns-policy.md"). 4. Complete and save your budget configuration. 5. Add Amazon Q Developer to the Slack workspace. 6. Open the [Amazon Q Developer in chat applications console](https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients "https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients"). 7. Choose **Configure new client**. 8. Choose **Slack**, and then choose
**Configure**. 9. From the dropdown list at the top right, choose the Slack workspace
that you want to use with Amazon Q Developer. 10. Choose **Allow**.

For any additional details, see [Tutorial: Get started with Slack](../../../chatbot/latest/adminguide/slack-setup.md "../../../chatbot/latest/adminguide/slack-setup.md") in the _Amazon Q
Developer in chat applications Administrator Guide_.
