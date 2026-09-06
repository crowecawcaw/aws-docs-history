

# Enable or disable notifications for a notification rule
<a name="notification-rule-enable-disable"></a>

When you create a notification rule, notifications are enabled by default. You do not have to delete the rule to prevent it from sending notifications. You can simply change its notification status.<a name="notification-rule-enable-disable-console"></a>

# To change the notification status for a notification rule (console)
<a name="notification-rule-enable-disable-console"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. In the navigation bar, expand **Settings**, and then choose **Notification rules**.

1. In **Notification rules**, review the rules configured for resources in your AWS account in the AWS Region where you are currently signed in. Use the selector to change the AWS Region.

1. Find the notification rule you want to enable or disable, and choose it to display its details.

1. In **Notification status**, choose the slider to change the status of the rule:
   + **Sending notifications**: This is the default. 
   + **Notifications paused**: No notifications are sent to the specified targets.<a name="notification-rule-enable-cli"></a>

# To change notification status for a notification rule (AWS CLI)
<a name="notification-rule-enable-cli"></a>

1. Follow the steps in [To edit a notification rule (AWS CLI)](notification-rule-edit.md#notification-rule-edit-cli) to obtain the JSON for the notification rule.

1. Edit the `Status` field to `ENABLED` (default) or `DISABLED` (no notifications), and then run the **update-notification-rule** command to change the status.

   ```
   "Status": "ENABLED"
   ```