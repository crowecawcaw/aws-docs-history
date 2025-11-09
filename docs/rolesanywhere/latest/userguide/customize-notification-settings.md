# Customize notification settings in IAM Roles Anywhere

You can customize notification settings based on your [public key infrastructure](public-key-infrastructure.md "public-key-infrastructure.md").
These settings are attached to your trust anchor and allow you to define custom thresholds for a notification event.
IAM Roles Anywhere will consume these settings while evaluating for a notification event to send metrics/events/notifications through their respective notification channels.

###### Topics

- [Notification events](#notification-setting-event "#notification-setting-event")
- [Notification channels](#notification-setting-channel "#notification-setting-channel")
- [IAM Roles Anywhere default notification settings](#notification-settings-default "#notification-settings-default")
- [Notification evaluation criteria](#notification-evaluation "#notification-evaluation")
- [Configuring custom notification threshold (console)](how-to-configure-custom-notification-settings.md "how-to-configure-custom-notification-settings.md")
- [Disabling a notification setting (console)](how-to-disable-notification-for-end-entity-certificate-expiry.md "how-to-disable-notification-for-end-entity-certificate-expiry.md")

## Notification events

- **CA certificate expiry**: IAM Roles Anywhere sends notification when a certificate authority (CA) in your trust anchor is approaching expiry.
- **End-entity certificate expiry**: IAM Roles Anywhere sends notification when your end-entity certificate used to vend temporary security credentials is expiring soon.

## Notification channels

###### Note

Notification channel with a value of `ALL` will apply the custom settings to all the channels listed below.

- [Amazon CloudWatch metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Amazon EventBridge events](monitoring-events.md "monitoring-events.md")
- [AWS Health notifications](monitoring-events.md "monitoring-events.md")

## IAM Roles Anywhere default notification settings

Following are the default notification settings IAM Roles Anywhere has defined. These values are applied in the absence of custom notification settings.

| Event                         | Channel                                | Threshold             | Enabled |
| ----------------------------- | -------------------------------------- | --------------------- | ------- |
| CA certificate expiry         | CloudWatch, EventBridge and AWS Health | 45 days before expiry | True    |
| End entity certificate expiry | EventBridge and AWS Health             | 45 days before expiry | True    |

## Notification evaluation criteria

Following are the evaluation criteria used to send notification events.

These criteria do not apply if your notification setting is in a `disabled` state.

| Event                         | Channel                    | Starts when                                         | Ends at                           |
| ----------------------------- | -------------------------- | --------------------------------------------------- | --------------------------------- |
| CA certificate expiry         | CloudWatch                 | Number of days until certificate expiry ≤ threshold | Day of certificate expiry         |
| CA certificate expiry         | EventBridge and AWS Health | Number of days until certificate expiry ≤ threshold | 14 days after certificate expires |
| End-entity certificate expiry | EventBridge and AWS Health | Number of days until certificate expiry ≤ threshold | Day of certificate expiry         |
