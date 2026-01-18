# Manage AWS Health notifications in AWS User Notifications

AWS managed notifications in AWS User Notifications lets you receive and manage notifications about events that affect your AWS accounts and services. When you use AWS managed notifications in AWS User Notifications, you can specify which AWS Health event categories to receive, set up organizational view for emails, and get consolidated notifications instead of multiple similar emails. For information on how to enable this service, see [Enabling or disabling AWS managed notifications for AWS Health in AWS User Notifications](../../../notifications/latest/userguide/managing-notification-features.md "../../../notifications/latest/userguide/managing-notification-features.md").

You can choose the following additional channels to receive your AWS Health events through AWS User Notifications:

- Email
- Chat
- Push notifications to the AWS Console Mobile Application
  While these notifications aren’t as detailed as direct AWS Health tools, they provide an effective way to notify stakeholders of issues and changes.

###### Note

For comprehensive visibility into AWS Health event details, including affected resource IDs, current status (open or closed), and resource status, it's a best practice to use one of the following AWS Health tools:

- The AWS Health API
- The aws.health source in Amazon EventBridge
- The Health Dashboard
  These tools provide the most detailed and real-time information about ongoing events and changes that might affect your workloads.

## Configure your AWS managed notifications subscription for AWS Health events

To configure your AWS managed notifications subscription, complete the following steps:

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications "https://console.aws.amazon.com/notifications").
2. In the navigation pane, choose **AWS managed notifications subscriptions**.
3. You can manage your AWS Health event notifications by category. For more information, see [Adding and removing account contacts for AWS managed notifications in AWS User Notifications](../../../notifications/latest/userguide/manage-mns.md#Add-remove-account-contacts "../../../notifications/latest/userguide/manage-mns.md#Add-remove-account-contacts").

###### Note

AWS Health migrated email delivery to AWS managed notifications in AWS User Notifications. Since December 15, 2025, you receive emails from AWS managed notifications. For more information, see _What changed in the migration to AWS managed notifications?_ in the [AWS managed notifications in AWS User Notifications FAQ](#manage-user-notifications-faq "#manage-user-notifications-faq").

## AWS managed notifications in AWS User Notifications FAQ

By default, emails regarding managed notifications are sent to your existing account contacts (root, operations, billing, and security email addresses). The emails that you receive from AWS managed notifications come from `health@aws.com` instead of `no-reply-aws@amazon.com`, and the format of the email changes. If you previously set up email rules for AWS Health notifications, such as routing an email by sender ID or scraping the content of the email, then you must update this setup to match the new email format. If you require automation through push notifications, then we recommend that you evaluate AWS Health events sent through Amazon EventBridge as an alternative to managed notifications.

AWS managed notification aggregates AWS Health events that impact multiple accounts within the same AWS Organizations organization into a single aggregated notification. You can view the aggregated organization in the management account's notifications center. Managed notifications emails the aggregated notification to the management account's contacts. To reduce duplicate emails, AWS managed notifications sends one notification when account contacts are shared between management and member accounts.

To enable aggregation, you must have AWS Organizations configured and grant trusted access between your management account and the AWS User Notifications service.

For more information, see [AWS managed notifications aggregation in AWS User Notifications](../../../notifications/latest/userguide/managed-notification-aggregation.md "../../../notifications/latest/userguide/managed-notification-aggregation.md").

Yes, trusted access with AWS User Notifications from AWS Organizations is required.

Organizational trust and the associated delegated administrator privileges are assigned by service and act as guardrails against overextended permissions. Trusted access for AWS Health enables organizational view for the Health Dashboard, the AWS Health APIs, AWS Health events sent through Amazon EventBridge, and notification configurations in User Notifications. Trusted access for AWS User Notifications enables aggregate notifications within AWS managed notifications. Because trusted access isn't shared, setting up delegated administrators needs to be added separately for each service.

No. The current plain text AWS Health emails are disabled after the migration completes. If you use email rules to drive different workflows, we recommend that you evaluate AWS Health events sent through Amazon EventBridge as an alternative.

Health operations, Security, and Billing notifications correspond to AWS Health account notifications and scheduled changes that have the operations, security, and billing persona respectively. AWS Health events with more than one persona tag are sent through the Security and Billing categories. Account-specific issues include issue category health events that are specific to an AWS account.

Public service events aren't available through AWS managed notifications.
