# Seller notifications for AWS Marketplace events

You can receive notifications about important events related to your AWS Marketplace products, such as subscription changes, private offer acceptances, and professional services requests. Amazon EventBridge is the recommended approach for programmatic integration, while email notifications are also available. SNS topics remain available for existing integrations but are being replaced by Amazon EventBridge. This topic provides an overview of available notification and event options.

- **EventBridge** – You can use EventBridge to receive an event for
  actions that happen in AWS Marketplace, for example, when an offer is created. The event contains
  information like the ID, expiration date, and product details. For more information, see
  [Amazon EventBridge events](notifications-eventbridge.md "notifications-eventbridge.md") and
  the [_Amazon EventBridge User Guide_](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md"). For SaaS products specifically, see
  [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md "saas-eventbridge-integration.md").
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

###### Important

SNS notifications for AWS Marketplace SaaS products are being replaced with Amazon EventBridge notifications. If you have existing SaaS products integrated with SNS, they will continue to function. New listings will eventually transition to using Amazon EventBridge instead of SNS. For more information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md "saas-eventbridge-integration.md").

    + [Software as a service
     (SaaS) products](saas-notification.md "saas-notification.md")
    + [Amazon Machine Image
     (AMI) products](ami-notification.md "ami-notification.md")
    + [Container products](container-notification.md "container-notification.md")

The following topics provide more information about notifications and events in
AWS Marketplace.

###### Topics

- [Managing email notifications for AWS Marketplace events](email-notifications.md "email-notifications.md")
- [Amazon EventBridge events](notifications-eventbridge.md "notifications-eventbridge.md")
