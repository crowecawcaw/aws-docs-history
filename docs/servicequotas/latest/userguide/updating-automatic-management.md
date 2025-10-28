# Updating Service Quotas Automatic Management

configuration

You can update your Service Quotas Automatic Management by adding service quotas to the exclusion list or changing
your Automatic Management notification configuration. Use the following procedure to update
Automatic Management configuration for your AWS account using the AWS Management Console or AWS CLI.

AWS Management Console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, choose
   **Automatic Management**.
3. Make the changes to your Automatic Management configuration.
   1. **Exclusion list update** - You can add service quotas
      from the exclusion list. See [Excluding service quotas from Service Quotas Automatic Management](excluding-quotas.md "excluding-quotas.md").
   2. **Notification configuration update** - Under
      **Notification configuration**, choose
      **Edit**. You're directed to the AWS User Notifications
      console where you can edit the notifications for Automatic Management.
      For more information, see [Creating your first notification configuration in
      AWS User Notifications](../../../notifications/latest/userguide/getting-started.md "../../../notifications/latest/userguide/getting-started.md") in the _AWS User Notifications User
      Guide_.

AWS CLI
To update Automatic Management notifications with the AWS CLI, use the AWS User Notifications command,
[update-notification-configuration](../../../cli/latest/reference/notifications/update-notification-configuration.md "../../../cli/latest/reference/notifications/update-notification-configuration.md") or [UpdateNotificationConfiguration](../../../notifications/latest/APIReference/API_UpdateNotificationConfiguration.md "../../../notifications/latest/APIReference/API_UpdateNotificationConfiguration.md") in the _AWS User Notifications API
Reference_.

###### Example Exclude Amazon DynamoDB quota from Automatic Management

The following example excludes DynamoDB from Automatic Management for an
AWS account in the Canada (Central) AWS Region. Replace the
`italicized placeholder text` in the
example command with your information.

```
aws service-quotas update-auto-management \
  --opt-in-type NotifyOnly \
  --region `ca-central-1` \
  --exclusion-list '{"`dynamodb`":["`L-E123ABC4`"]}'
```
