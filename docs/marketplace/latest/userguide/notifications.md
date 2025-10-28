# Seller notifications for AWS Marketplace events

You can receive timely notifications related to your AWS Marketplace products
through email, Amazon EventBridge events, and Amazon Simple Notification Service (Amazon SNS) topics. AWS Marketplace provides. For example, you
can receive notifications related to private offers, requests for professional services product,
and recurring scan reminders. This topic provides an overview of available notification and
event options.

- **Email notifications** – Within AWS Marketplace , sellers,
  buyers and independent software vendors (ISVs) can receive email notifications. AWS Marketplace uses
  your root account to send automated emails in real time to your AWS account's email,
  updating you on AWS Marketplace offers and agreements. You can also add custom email aliases for
  notifications and unsubscribe recipients from email notifications. For more information, see
  [Managing email notifications for AWS Marketplace events](email-notifications.md "email-notifications.md").
- **Amazon SNS topics** – To receive notifications about
  changes to customer subscriptions for your products, you can subscribe to the Amazon SNS topics
  for AWS Marketplace provided to you during product creation. For example, you can know when customers
  accept a private offer. For information, see the Amazon SNS topic for your product type:
  - [Software as a service
    (SaaS) products](saas-notification.md "saas-notification.md")
  - [Amazon Machine Image
    (AMI) products](ami-notification.md "ami-notification.md")
  - [Container products](container-notification.md "container-notification.md")

- **EventBridge** – You can use EventBridge to receive an event for
  actions that happen in AWS Marketplace, for example, when an offer is created. The event contains
  information like the ID, expiration date, and product details. For more information, see
  [Amazon EventBridge events](notifications-eventbridge.md "notifications-eventbridge.md") and
  the [_Amazon EventBridge User Guide_](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").
  The following topics provide more information about notifications and events in
  AWS Marketplace.

###### Topics

- [Managing email notifications for AWS Marketplace events](email-notifications.md "email-notifications.md")
- [Amazon EventBridge events](notifications-eventbridge.md "notifications-eventbridge.md")
