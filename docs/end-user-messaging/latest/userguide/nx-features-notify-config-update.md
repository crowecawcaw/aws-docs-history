

# Update a Notify configuration
<a name="nx-features-notify-config-update"></a>

You can update the enabled channels, enabled countries, default template, associated pool, and deletion protection settings of a Notify configuration.

------
#### [ AWS Management Console ]

**To update a Notify configuration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to the Notify configuration you want to update.

1. Choose **Edit** to update channels, or use the individual tabs (**Countries**, **Templates**, **Use Dedicated Numbers**, **Deletion protection**) to update specific settings.

1. Make your changes and choose **Save**.

------
#### [ AWS CLI ]

**To update a Notify configuration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 update-notify-configuration \
  > --notify-configuration-id {{nc-1234567890abcdef0}} \
  > --enabled-countries US CA GB DE FR
  ```

  Replace {{nc-1234567890abcdef0}} with the ID of the configuration and set the values you want to change. Common updates:
  + Set a default template with **--default-template-id {{notify-code-verification-english-001}}**, or clear it with **--default-template-id UNSET\_DEFAULT\_TEMPLATE**.
  + Associate a pool with **--pool-id {{pool-1234567890abcdef0}}**, or disassociate it with **--pool-id UNSET\_DEFAULT\_POOL\_FOR\_NOTIFY**.
  + Enable deletion protection with **--deletion-protection-enabled**.

------