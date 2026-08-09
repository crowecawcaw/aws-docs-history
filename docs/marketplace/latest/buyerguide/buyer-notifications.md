# Buyer notifications for AWS Marketplace events

AWS Marketplace provides timely notifications to keep you informed about important events related to your purchases. Notifications are delivered through email, chatbots, Amazon EventBridge events, and Amazon Simple Notification Service (Amazon SNS) topics.

###### Notification email address is changing

AWS Marketplace is moving buyer notifications to AWS User Notifications. When you opt in, notification emails are sent from `marketplace@aws.com` instead of `no-reply@marketplace.aws`. If you use email filters or rules for AWS Marketplace messages, update them to allow `marketplace@aws.com` so you continue to receive notifications. All accounts are enrolled automatically by January 2027—opt in earlier to start receiving from the new address and to configure additional recipients and delivery channels.

With AWS User Notifications (managed notifications), you can view your notifications in the console notification center and choose how you receive them—by email, in the AWS Console Mobile Application, and in Amazon Q Developer in chat applications such as Slack and Microsoft Teams. By default, notifications are sent to your account's root user email address; you can add more email addresses and delivery channels and organize notifications by category (Products and Solutions, Agreements and Subscriptions, Private Offers, and Pricing Changes).

For more information about AWS User Notifications, EventBridge and Amazon SNS, see the following topics:

- [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md"), in the _EventBridge User Guide_.
- [Getting started with Notification Configurations](../../../notifications/latest/userguide/managing-notifications.md "../../../notifications/latest/userguide/managing-notifications.md"), in the _AWS User Notifications User Guide_.
- [Learn how to create an Amazon Simple Notification Service topic and publish messages](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md"), in the _Amazon SNS Developer Guide_.

###### Topics in this section

- [Email and chatbot notifications for AWS Marketplace events](buyer-notifications-email.md "buyer-notifications-email.md")
- [Amazon EventBridge notifications for AWS Marketplace events](buyer-notifications-eventbridge.md "buyer-notifications-eventbridge.md")
