

# Enabling AWS Organizations in AWS User Notifications
<a name="uno-orgs"></a>

**Note**  
If you previously enabled trusted access for User Notifications using the AWS Organizations API, you might be missing User Notifications configurations that allow the service to function properly. Use the AWS Organizations API or AWS CLI to disable trusted access, then use the following procedure to [enable trusted access](#enable-ta).

To enable AWS Organizations in User Notifications, you must enable trusted access. Enabling trusted access between AWS Organizations and User Notifications allows User Notifications to make API calls to AWS Organizations. User Notifications uses information from AWS Organizations for User-configured and AWS managed notifications.

**Note**  
Trusted access is granted to individual services. You must enable trusted access for User Notifications, even if you've previously enabled trusted access for other services like AWS Health.

**Topics**
+ [User-configured notifications with organizations](#ucns-orgs)
+ [AWS managed notifications with organizations](#managed-notifications-orgs)
+ [Enabling trusted access](#enable-ta)
+ [Disabling trusted access](#disable-ta)
+ [Registering delegated administrators in AWS User Notifications](#register-admins)
+ [Removing delegated administrators in AWS User Notifications](#deregister-admins)

## User-configured notifications with organizations
<a name="ucns-orgs"></a>

You can create notification configurations in management or Delegated Admin account to filter events across accounts in your organization. When an event from any member account matches the event rules, User Notifications generates a notification in the respective account.

Configuring notifications for organization accounts creates read-only notification configurations in member accounts. These configurations don't generate notifications in member accounts, only the management or Delegated Admin account receives organization notifications. For more information, see [Managing notifications across your organization with AWS User Notifications](managing-org-notifications.md).

## AWS managed notifications with organizations
<a name="managed-notifications-orgs"></a>

User Notifications uses AWS Organizations in accounts that enable AWS managed notifications and aggregation and deduplication to:
+ [Aggregate AWS managed notifications across accounts](managed-notification-aggregation.md#notification-aggregation) in management and delegated administrator accounts
+  [Deduplicate AWS managed notifications across accounts](managed-notification-aggregation.md#managed-notification-dedupe) 

For example, if management and member accounts within the same organization share a billing contact, and the same event occurs in both accounts, the billing contact receives only one notification that references the event in both accounts.

If management and member accounts within the same organization both enable AWS managed notifications and an event occurs in a member account, both the management and member account receive a notification. However, if an event occurs in a member account and only the management account enabled AWS managed notifications, only the management account receives a notification.

## Enabling trusted access
<a name="enable-ta"></a>

**Important**  
You must be logged in with the management account to enable trusted access.

You can enable AWS Organizations in User Notifications by enabling trusted access. Enabling trusted access allows User Notifications to [aggregate and deduplicate AWS managed notifications](managed-notification-aggregation.md) in accounts that enable AWS managed notifications.

**To enable trusted access**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation pane, choose **Organizations settings**.

1. Choose **Enable trusted access**.

## Disabling trusted access
<a name="disable-ta"></a>

**Important**  
You must be logged in with the management account to disable trusted access.

You can disable trusted access at any time from the User Notifications console.

**To disable trusted access**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation pane, choose **Organizations settings**.

1. Choose **Disable trusted access**.

## Registering delegated administrators in AWS User Notifications
<a name="register-admins"></a>

Delegated administrators have independent administrator access for User Notifications. Each delegated administrator can independently configure their own notification contacts, delivery channels, notification configurations, and can associate with OUs of an organization to receive notifications about the member accounts attached to those OUs. You must [enable trusted access](#enable-ta) before registering delegated administrators. You can register up to five delegated administrators. You must also enable AWS managed notifications to allow delegated administrators to view AWS managed notifications.

**To register delegated administrators**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation pane, choose **Organizations settings**.

1. In **Delegated Administrators**, choose **Register administrator**.

1. Follow the on screen instructions and select an AWS account to register.

1. Choose **Register**.

## Removing delegated administrators in AWS User Notifications
<a name="deregister-admins"></a>

You can remove delegated administrators to restrict a user's access to User Notifications

**To remove delegated administrators**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation pane, choose **Organizations settings**.

1. In **Delegated Administrators**, select which delegated administrator you want to remove.

1. Choose **Remove**.

1. Confirm removal by choosing **Remove**.