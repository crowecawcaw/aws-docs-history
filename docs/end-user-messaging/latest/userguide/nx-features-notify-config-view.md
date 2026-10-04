

# View Notify configurations
<a name="nx-features-notify-config-view"></a>

View the Notify configurations in your account and AWS Region to see each configuration's display name, use case, enabled channels and countries, tier, status, default template, associated pool, and deletion protection setting. You can view a single configuration by its ID or list all of them. In the AWS CLI, a single operation, `describe-notify-configurations`, does both: pass configuration IDs to view specific configurations, or omit them to list all configurations in the account.

------
#### [ AWS Management Console ]

**To view Notify configurations using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Notify configurations**.

1. The **Notify configurations** page lists your configurations. Use the property filter to filter by display name, status, tier, or other properties.

1. To view the full details of a single configuration, choose its **Display name**.

------
#### [ AWS CLI ]

**To view Notify configurations using the AWS CLI**

1. To list all Notify configurations in your account, enter the following command:

   ```
   $ aws pinpoint-sms-voice-v2 describe-notify-configurations
   ```

1. To view a specific configuration, add the **--notify-configuration-ids** option:

   ```
   $ aws pinpoint-sms-voice-v2 describe-notify-configurations \
   > --notify-configuration-ids {{nc-1234567890abcdef0}}
   ```

   Replace {{nc-1234567890abcdef0}} with the ID of the Notify configuration. To filter the list by a property, add **--filters Name=status,Values=ACTIVE**.

------