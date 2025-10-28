AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Subscribing an Amazon SNS topic to Amazon Q Developer in chat applications

You can quickly subscribe existing Amazon SNS topics to the Amazon Q Developer in chat applications. You associate the
new subscriptions to a chat channel. After doing so, the messages from those
topics appear in the channel. The Amazon SNS topics must be associated with
AWS services that Amazon Q Developer in chat applications supports, and may also require further configuration, such as
association with a CloudWatch rule. This procedure is most useful if you have Amazon SNS topics that are
already doing significant work with CloudWatch Events and CloudWatch alarms in AWS cloud services supported by
Amazon Q Developer in chat applications.

###### Note

You can set up each supported AWS service to _target_ one or more
Amazon SNS topics to send notifications to Amazon Q Developer in chat applications. You do this using each relevant AWS service
console, or using AWS CloudFormation. If you already have Amazon SNS topics set as targets for supported
services, you can configure Amazon Q Developer in chat applications to use those topics. Notifications from subscribed
topics will automatically appear in your chat channels without further configuration.

###### Note

If your Amazon SNS topic is encrypted, you must add a section to your AWS KMS key policy to give the sending service permissions to post events to the encrypted SNS topics. For more information, see [Setting up Amazon SNS topics](getting-started.md#chatbot-sns "getting-started.md#chatbot-sns").

1. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Under **Configured clients**, choose your chat client.
3. Choose any channel in your chat client
   configuration.
4. Choose **Edit**. The configuration page for the channel
   appears. Note that the **Region** Notifications is already
   configured.
5. In the **Notifications** panel:
   1. If you need to apply an Amazon SNS topic from another region, choose **Add
      another Region**.

6. For each **Region** in the chat channel, select the
   Amazon SNS topic you want to add.
7. When finished, choose **Save**.
8. To check for the subscription, click on any subscription entry in the Amazon Q Developer in chat applications console. The
   Amazon SNS console opens, showing the list of subscriptions for the selected topic.
