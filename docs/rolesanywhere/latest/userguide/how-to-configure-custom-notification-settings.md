# Configuring custom notification threshold (console)

1. Sign in to [IAM Roles Anywhere console](https://console.aws.amazon.com/rolesanywhere/home "https://console.aws.amazon.com/rolesanywhere/home").
2. Scroll to find trust anchor table and **choose the trust anchor** to apply custom notification settings.
3. Within trust anchor detail page scroll towards **Notification settings** section and choose **Manage settings**.
4. **Customize threshold** for the [notification event](customize-notification-settings.md#notification-setting-event "customize-notification-settings.md#notification-setting-event").
   IAM Roles Anywhere will start sending metrics/events/notifications when number of days until your X.509 certificate expires is less than or equal this threshold. See IAM Roles Anywhere notification evaluation criteria.
5. Choose **Save changes** to apply custom notification threshold.
