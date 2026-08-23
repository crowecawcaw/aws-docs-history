# AWS managed notifications in AWS User Notifications

Select AWS services generate AWS managed notifications by default. The following services are supported in User Notifications:

- **AWS Health** – Events that affect your AWS accounts and services
- **AWS Marketplace – Buyer** – Notifications about your Marketplace subscriptions, purchases, and entitlement changes
- **AWS Partner Central** – Notifications about your AWS Partner Central and AWS Marketplace Seller accounts and services
  AWS managed notifications are automatically available in the Console Notification Center and sent to account contacts ([primary contact email](../../../accounts/latest/reference/manage-acct-update-root-user.md "../../../accounts/latest/reference/manage-acct-update-root-user.md") and [alternate contact emails](../../../accounts/latest/reference/manage-acct-update-contact-alternate.md "../../../accounts/latest/reference/manage-acct-update-contact-alternate.md")). You can manage the account contacts subscriptions of
  AWS managed notifications and set up additional delivery channels, including [notification-contacts](../../../notificationscontacts/latest/APIReference/Welcome.md "../../../notificationscontacts/latest/APIReference/Welcome.md"),
  [Amazon Q Developer chat
  notifications](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md"), [AWS Console Mobile
  App](../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md "../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md") push notifications, and the [User Notifications
  API](../../../notificationscontacts/latest/APIReference/Welcome.md "../../../notificationscontacts/latest/APIReference/Welcome.md").

You can aggregate AWS managed notifications across accounts within the same organization
to reduce the total number of notifications you receive. For more information, see [Aggregating and deduplicating AWS managed notifications in AWS User Notifications](managed-notification-aggregation.md "managed-notification-aggregation.md").

###### Note

Viewing and modifying AWS managed notifications requires specific [read and read-write permissions](resource-level-permissions.md#rlp-table "resource-level-permissions.md#rlp-table").

For more information about notifications from specific services, see:

- [Manage AWS Health notifications in AWS User Notifications](../../../health/latest/ug/manage-user-notifications.md "../../../health/latest/ug/manage-user-notifications.md") in the _AWS Health User Guide_.
- [Manage AWS Marketplace Buyer notifications in AWS User Notifications](../../../marketplace/latest/buyerguide/buyer-notifications-email.md "../../../marketplace/latest/buyerguide/buyer-notifications-email.md") in the _AWS Marketplace Buyer Guide_.

###### Topics

- [AWS managed notification subscriptions in AWS User Notifications](manage-mns.md "manage-mns.md")
- [Viewing AWS managed notifications in AWS User Notifications](viewing-managed-notifications.md "viewing-managed-notifications.md")
- [Aggregating and deduplicating AWS managed notifications in AWS User Notifications](managed-notification-aggregation.md "managed-notification-aggregation.md")
