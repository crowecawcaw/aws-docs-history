

# Seller notifications for AWS Marketplace events
<a name="notifications"></a>

You can receive notifications about important events related to your AWS Marketplace products, such as subscription changes, private offer acceptances, and professional services requests. Amazon EventBridge is the recommended approach for programmatic integration, while email notifications are also available. SNS topics remain available for existing integrations but are being replaced by Amazon EventBridge. This topic provides an overview of available notification and event options.
+ **EventBridge** – You can use EventBridge to receive an event for actions that happen in AWS Marketplace, for example, when an offer is created. The event contains information like the ID, expiration date, and product details. For more information, see [Amazon EventBridge events](notifications-eventbridge.md) and the [*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). For SaaS products specifically, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md).
+ **Email notifications** – Within AWS Marketplace, sellers, buyers, and independent software vendors (ISVs) can receive email notifications. AWS Marketplace uses your root account to send automated emails in real time to your AWS account's email, updating you on AWS Marketplace offers and agreements. You can also add custom email aliases for notifications and unsubscribe recipients from email notifications. For more information, see [Managing email notifications for AWS Marketplace events](https://docs.aws.amazon.com/marketplace/latest/userguide/email-notifications.html).

  Sellers can optionally use AWS User Notifications (managed notifications) to view notifications in the console notification center and choose how to receive them: by email, in the AWS Console Mobile Application, or in Amazon Q Developer in chat applications such as Slack and Microsoft Teams. You can receive notifications by category: Product listings, Offers and agreements, Payments and disbursements, and Account management. After you enable managed notifications, you can choose which contacts and channels receive notifications for each category. By default, notifications go to your account's root email address. To notify additional recipients, add them manually. For more information, see [AWS managed notifications](https://docs.aws.amazon.com/notifications/latest/userguide/managed-notifications.html) in the *AWS User Notifications User Guide*.
+ **Amazon SNS topics** – To receive notifications about changes to customer subscriptions for your products, you can subscribe to the Amazon SNS topics for AWS Marketplace provided to you during product creation. For example, you can know when customers accept a private offer. For information, see the Amazon SNS topic for your product type:
**Important**  
SNS notifications for AWS Marketplace SaaS products are being replaced with Amazon EventBridge notifications. If you have existing SaaS products integrated with SNS, they will continue to function. New listings will eventually transition to using Amazon EventBridge instead of SNS. For more information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md).
  + [Software as a service (SaaS) products](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-notification.html)
  + [Amazon Machine Image (AMI) products](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-notification.html)
  + [Container products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-notification.html)

The following topics provide more information about notifications and events in AWS Marketplace.

**Topics**
+ [Managing email notifications for AWS Marketplace events](email-notifications.md)
+ [Amazon EventBridge events](notifications-eventbridge.md)