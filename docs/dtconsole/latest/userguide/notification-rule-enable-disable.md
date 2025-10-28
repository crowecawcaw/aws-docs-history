# Enable or disable notifications for a notification rule

When you create a notification rule, notifications are enabled by default. You do not
have to delete the rule to prevent it from sending notifications. You can simply change
its notification status.

# To change the notification status for a

notification rule (console)

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/ "https://console.aws.amazon.com/codesuite/settings/notifications/").
2. In the navigation bar, expand **Settings**, and then choose
   **Notification rules**.
3. In **Notification rules**, review the rules configured for
   resources in your AWS account in the AWS Region where you are currently
   signed in. Use the selector to change the AWS Region.
4. Find the notification rule you want to enable or disable, and choose it to
   display its details.
5. In **Notification status**, choose the slider to change the
   status of the rule:
   - **Sending notifications**: This is the default.
   - **Notifications paused**: No notifications are sent
     to the specified targets.

# To change notification status for a

notification rule (AWS CLI)

1. Follow the steps in [To edit a notification rule
   (AWS CLI)](notification-rule-edit.md#notification-rule-edit-cli "notification-rule-edit.md#notification-rule-edit-cli") to obtain the JSON for the
   notification rule.
2. Edit the `Status` field to `ENABLED` (default) or
   `DISABLED` (no notifications), and then run the
   **update-notification-rule** command to change the
   status.

```
"Status": "ENABLED"
```
