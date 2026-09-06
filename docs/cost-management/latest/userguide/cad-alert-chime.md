

# Receiving anomaly alerts in chat applications
<a name="cad-alert-chime"></a>

You can use Amazon Q Developer to receive your AWS Cost Anomaly Detection alerts in Amazon Chime and Slack.

------
#### [ Amazon Chime ]

**To begin receiving your AWS Cost Anomaly Detection alerts in Amazon Chime**

1. Follow [Getting started with AWS Cost Anomaly Detection](getting-started-ad.md) to create a monitor.

1. Create an alert subscription using the `Individual alerts` type. Amazon SNS topics can be configured for `individual alerts` only.

1. Add an Amazon SNS topic as an alert recipient to a specific alert or alerts. To ensure that Cost Anomaly Detection has permissions to publish to your Amazon SNS topics, see [Creating an Amazon SNS topic for anomaly notifications](ad-SNS.md).

1. Attach the alert subscription to the monitor that you want to receive Amazon Chime alerts for.

1. Open [Amazon Chime](http://app.chime.aws/).

1. For **Amazon Chime**, choose the chat room that you want to set up to receive notifications through Amazon Q Developer.

1. Choose the Room settings icon on the top right and choose **Manage webhooks and bots**.

   Amazon Chime displays the webhooks associated with the chat room.

1. For the webhook, choose **Copy URL**, and then choose **Done**.

   If you need to create a new webhook for the chat room, choose **Add webhook**, enter a name for the webhook in the **Name** field, and then choose **Create**.

1. Open the [Amazon Q Developer in chat applications console](https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients).

1. Choose **Configure new client**.

1. Choose **Amazon Chime**, and then choose **Configure**.

1. Under **Configuration details**, enter a name for your configuration. The name must be unique across your account and can't be edited later.

1. To configure Amazon Chime webhook, do the following:

   1. For **Webhook URL**, paste the webhook URL that you copied from Amazon Chime.

   1. For **Webhook description**, use the following naming convention to describe the purpose of the webhook: **Chat\_room\_name/Webhook\_name**. This helps you associate Amazon Chime webhooks with their Amazon Q Developer configurations.

1. If you want to enable logging for this configuration, choose **Publish logs to Amazon CloudWatch Logs**. For more information, see Amazon CloudWatch Logs for Amazon Q Developer.
**Note**  
There is an additional charge for using Amazon CloudWatch Logs.

1. For **Permissions**, set the IAM permissions as follows:

   1. For **IAM role**, choose **Create an IAM role using a template**. If you want to use an existing role instead, choose it from the **IAM role** list. To use an existing IAM role, you might need to modify it for use with Amazon Q Developer. For more information, see Configuring an IAM Role for Amazon Q Developer.

   1. For **Role name**, enter a name. Valid characters: a-z, A-Z, 0-9.

   1. For **Policy templates**, choose **Notification permissions**. This is the IAM policy provided by Amazon Q Developer. It provides the necessary Read and List permissions for CloudWatch alarms, events, and logs, and for Amazon Amazon SNS topics. 

1. Set up the Amazon SNS topics that will send notifications to the Amazon Chime webhook.

   1. For **Amazon SNS Region**, choose the AWS Region that hosts the Amazon SNS topics for this Amazon Q Developer subscription.

   1. For **Amazon SNS topics**, choose the Amazon SNS topic for the client subscription. This topic determines the content that's sent to the Amazon Chime webhook. If the region has additional Amazon SNS topics, you can choose them from the same dropdown list.

   1. If you want to add an Amazon SNS topic from another Region to the notification subscription, choose **Add another Region**.

1. Choose **Configure**.

For any additional details, see [Tutorial: Get started with Amazon Chime](https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

------
#### [ Slack ]

**To begin receiving your AWS Cost Anomaly Detection alerts in Slack**

1. Follow [Getting started with AWS Cost Anomaly Detection](getting-started-ad.md) to create a monitor.

1. Create an alert subscription using the `Individual alerts` type. Amazon SNS topics can be configured for `individual alerts` only.

1. Add an Amazon SNS topic as an alert recipient to a specific alert or alerts. To ensure that Cost Anomaly Detection has permissions to publish to your Amazon SNS topics, see [Creating an Amazon SNS topic for anomaly notifications](ad-SNS.md).

1. Attach the alert subscription to the monitor that you want to receive Slack alerts for.

1. Add Amazon Q Developer to the Slack workspace.

1. Open the [Amazon Q Developer in chat applications console](https://us-east-2.console.aws.amazon.com/chatbot/home?region=us-east-2#/chat-clients).

1. Choose **Configure new client**.

1. Choose **Slack**, and then choose **Configure**.

1. From the dropdown list at the top right, choose the Slack workspace that you want to use with Amazon Q Developer.

1. Choose **Allow**.

For any additional details, see [Tutorial: Get started with Slack](https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

------