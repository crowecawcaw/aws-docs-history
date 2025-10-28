# Subscribe users to Amazon SNS topics that are

targets

Before users can receive notifications, they must be subscribed to the Amazon SNS topic
that is the target of the notification rule. If users are subscribed by email address,
they must confirm their subscription before they receive notifications. To send
notifications to users in Slack channels, Microsoft Teams channels, or Amazon Chime chatrooms, see [Configure integration between notifications and
AWS Chatbot](notifications-chatbot.md "notifications-chatbot.md").

###### To subscribe users to an Amazon SNS topic used for

notifications

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, choose **Topics**, and then choose the
   topic to which you want to subscribe users.
3. In **Subscriptions**, choose **Create
   subscription**.
4. In **Protocol**, choose **Email**. In
   **Endpoint**, enter the email address, and then choose
   **Create subscription**.
