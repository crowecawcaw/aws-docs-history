# Enabling AWS Organizations in AWS User Notifications

###### Note

If you previously enabled trusted access for User Notifications using the AWS Organizations API,
you might be missing User Notifications configurations that allow the service to function properly. Use the AWS Organizations API or AWS CLI to disable trusted access, then use the following
procedure to [enable trusted access](#enable-ta "#enable-ta").

To enable AWS Organizations in User Notifications, you must enable trusted access. Enabling trusted access between AWS Organizations and User Notifications allows User Notifications to make API calls to AWS Organizations.
User Notifications uses information from AWS Organizations for User-configured and AWS managed notifications.

###### Note

Trusted access is granted to individual services. You must enable trusted access for User Notifications, even if you've previously enabled trusted access for other services like AWS Health.

###### Topics

- [User-configured notifications with organizations](#ucns-orgs "#ucns-orgs")
- [AWS managed notifications with organizations](#managed-notifications-orgs "#managed-notifications-orgs")
- [Enabling trusted access](#enable-ta "#enable-ta")
- [Disabling trusted access](#disable-ta "#disable-ta")
- [Registering delegated administrators in AWS User Notifications](#register-admins "#register-admins")
- [Removing delegated administrators in AWS User Notifications](#deregister-admins "#deregister-admins")

## User-configured notifications with organizations

You can create notification configurations to filter events across acounts in your organiation. When an event from any member account matches the event rules,
User Notifications generates a notification in the management account.

Configuring notifications for organization accounts creates read-only notification configurations in member accounts.
These configurations don't generate notifications in member accounts, only the
management account receives organization notifications. For more information, see [Managing notifications across your organization with AWS User Notifications](managing-org-notifications.md "managing-org-notifications.md").

## AWS managed notifications with organizations

User Notifications uses AWS Organizations in accounts that [enable AWS managed notifications](managing-notification-features.md "managing-notification-features.md") and aggregation and deduplication to:

- [Aggregate AWS managed notifications across accounts](managed-notification-aggregation.md#notification-aggregation "managed-notification-aggregation.md#notification-aggregation") in management and delegated administrator accounts
- [Deduplicate AWS managed notifications across accounts](managed-notification-aggregation.md#managed-notification-dedupe "managed-notification-aggregation.md#managed-notification-dedupe")

For example, if management and member accounts within the same organization share a billing contact, and the same event occurs in both accounts, the billing contact receives only one notification that references the event in both accounts.

If management and member accounts within the same organization both enable AWS managed notifications and an event occurs in a member account, both the management and member account receive a notification. However, if an event occurs in a member account and only the management account
enabled AWS managed notifications, only the management account receives a notification.

## Enabling trusted access

###### Important

You must be logged in with the management account to enable trusted access.

You
can enable AWS Organizations in User Notifications by enabling trusted access. Enabling trusted access allows User Notifications to [aggregate and deduplicate AWS managed notifications](managed-notification-aggregation.md "managed-notification-aggregation.md")
in accounts that [enable AWS managed notifications](managing-notification-features.md "managing-notification-features.md").

###### To enable trusted access

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **Organizations settings**.
3. Choose **Enable trusted access**.

## Disabling trusted access

###### Important

You must be logged in with the management account to disable trusted access.

You can disable trusted access at any time from the User Notifications console.

###### To disable trusted access

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **Organizations settings**.
3. Choose **Disable trusted access**.

## Registering delegated administrators in AWS User Notifications

Delegated administrators share administrator access for User Notifications. They're able to view notifications about member accounts in the organization.
You must [enable trusted access](#enable-ta "#enable-ta") before registering delegated administrators. You can register up to five delegated administrators.
You must also [enable AWS managed notifications](managing-notification-features.md "managing-notification-features.md") to allow delegated administrators to view AWS managed notifications.

###### To register delegated administrators

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **Organizations settings**.
3. In **Delegated Administrators**, choose **Register administrator**.
4. Follow the on screen instructions and select an AWS account to register.
5. Choose **Register**.

## Removing delegated administrators in AWS User Notifications

You can remove delegated administrators to restrict a user's access to User Notifications

###### To remove delegated administrators

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **Organizations settings**.
3. In **Delegated Administrators**, select which delegated administrator you want to remove.
4. Choose **Remove**.
5. Confirm removal by choosing **Remove**.
