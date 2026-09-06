

# AWS managed notifications in AWS User Notifications
<a name="managed-notifications"></a>

 Select AWS services generate AWS managed notifications by default. The following services are supported in User Notifications: 
+ **AWS Health** – Events that affect your AWS accounts and services
+ **AWS Marketplace – Buyer** – Notifications about your Marketplace subscriptions, purchases, and entitlement changes
+ **AWS Partner Central** – Notifications about your AWS Partner Central and AWS Marketplace Seller accounts and services

AWS managed notifications are automatically available in the Console Notification Center and sent to account contacts ([primary contact email](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html) and [alternate contact emails](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html)). You can manage the account contacts subscriptions of AWS managed notifications and set up additional delivery channels, including [notification-contacts](https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/Welcome.html), [Amazon Q Developer chat notifications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html), [AWS Console Mobile App](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html) push notifications, and the [User Notifications API](https://docs.aws.amazon.com/notificationscontacts/latest/APIReference/Welcome.html).

You can aggregate AWS managed notifications across accounts within the same organization to reduce the total number of notifications you receive. For more information, see [Aggregating and deduplicating AWS managed notifications in AWS User Notifications](managed-notification-aggregation.md). 

**Note**  
 Viewing and modifying AWS managed notifications requires specific [read and read-write permissions](resource-level-permissions.md#rlp-table). 

For more information about notifications from specific services, see:
+ [Manage AWS Health notifications in AWS User Notifications](https://docs.aws.amazon.com/health/latest/ug/manage-user-notifications.html) in the *AWS Health User Guide*.
+ [Manage AWS Marketplace Buyer notifications in AWS User Notifications](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-notifications-email.html) in the *AWS Marketplace Buyer Guide*.

**Topics**
+ [AWS managed notification subscriptions in AWS User Notifications](manage-mns.md)
+ [Viewing AWS managed notifications in AWS User Notifications](viewing-managed-notifications.md)
+ [Aggregating and deduplicating AWS managed notifications in AWS User Notifications](managed-notification-aggregation.md)