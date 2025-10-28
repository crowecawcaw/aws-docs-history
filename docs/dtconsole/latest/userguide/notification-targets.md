# Working with notification rule targets

A notification rule target is a destination that defines where you want notifications to
be sent when a notification rule's event conditions are met. You can choose between Amazon SNS
topics and AWS Chatbot clients that are configured for Slack or Microsoft Teams channels. You can create an Amazon SNS
topic as a target as part of creating a notification rule (recommended). You can also choose
an existing Amazon SNS topic in the same AWS Region as the notification rule, but you must
configure it with the required policy. If you choose to use an AWS Chatbot client as a target,
you must first create that client in AWS Chatbot.

If you want to extend the reach of notifications, you can manually configure integration
between notifications and AWS Chatbot so that notifications are sent to Amazon Chime chatrooms. You can
then choose the Amazon SNS topic configured for that AWS Chatbot client as the target for the
notification rule. For more information, see [To integrate notifications with AWS Chatbot
and Amazon Chime](notifications-chatbot.md#notifications-chatbot-chime "notifications-chatbot.md#notifications-chatbot-chime").

You can use the Developer Tools console or the AWS CLI to manage notification targets. You can use the
console or the AWS CLI to create and configure Amazon SNS topics and AWS Chatbot clients as [targets](concepts.md#targets "concepts.md#targets"). You can also configure integration between the Amazon SNS
topics that you configure as targets and AWS Chatbot. This makes it possible for you to send
notifications to Amazon Chime chatrooms. For more information, see [Configure integration between notifications and
AWS Chatbot](notifications-chatbot.md "notifications-chatbot.md").

###### Topics

- [Create or configure a notification rule
  target](notification-target-create.md "notification-target-create.md")
- [View notification rule targets](notification-target-view.md "notification-target-view.md")
- [Add or remove a target for a
  notification rule](notification-target-change-rule.md "notification-target-change-rule.md")
- [Delete a notification rule target](notification-target-delete.md "notification-target-delete.md")
