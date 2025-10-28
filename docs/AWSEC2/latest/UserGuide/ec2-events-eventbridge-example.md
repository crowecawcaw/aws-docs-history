# Create an alarm that sends an email

when an Amazon EC2 instance changes state

To receive email notifications when your instance changes state, create an Amazon SNS
topic and then create an EventBridge rule for the `EC2 Instance State-change
 Notification` event.

###### To create an SNS topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose **Create topic**.
4. For **Type**, choose
   **Standard**.
5. For **Name**, enter a name for your topic.
6. Choose **Create topic**.
7. Choose **Create subscription**.
8. For **Protocol**, choose
   **Email**.
9. For **Endpoint**, enter the email address that receives
   the notifications.
10. Choose **Create subscription**.
11. You'll receive an email message with the following subject line:
    AWS Notification - Subscription Confirmation. Follow
    the directions to confirm your subscription.

###### To create an EventBridge rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Choose **Create rule**.
3. For **Name**, enter a name for your rule.
4. For **Rule type**, choose **Rule with an event
   pattern**.
5. Choose **Next**.
6. For **Event pattern**, do the following:
   1. For **Event source**, choose
      **AWS services**.
   2. For **AWS service**, choose
      **EC2**.
   3. For **Event type**, choose **EC2 Instance
      State-change Notification**.
   4. By default, we send notifications for any state change for any
      instance. If you prefer, you can select specific states or specific
      instances.

7. Choose **Next**.
8. Specify a target as follows:
   1. For **Target types**, choose
      **AWS service**.
   2. For **Select a target**, choose **SNS
      topic**.
   3. For **Topic**, choose the SNS topic that you
      created in the previous procedure.

9. Choose **Next**.
10. (Optional) Add tags to your rule.
11. Choose **Next**.
12. Choose **Create rule**.
13. To test your rule, initiate a state change. For example, start a stopped
    instance, stop a running instance, or launch an instance. You'll receive
    email messages with the following subject line: AWS Notification
    Message. The body of the email contains the event data.
