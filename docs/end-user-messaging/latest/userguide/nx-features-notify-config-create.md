

# Create a Notify configuration
<a name="nx-features-notify-config-create"></a>

A Notify configuration is the central resource for Notify. When you create one, you provide a display name for your brand, a use case, and the channels to enable. AWS validates your account, configures fraud protection, assigns templates, and sets tier-appropriate limits. The display name is automatically reviewed for profanity, URLs, and other disallowed content using Amazon Bedrock; if it is rejected, the status is set to `REJECTED` with a rejection reason you can appeal through a support case.

------
#### [ AWS Management Console ]

**To create a Notify configuration using the console**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Notify**, choose **Notify configurations**.

1. Choose **Create Notify configuration**.

1. For **Display name**, enter a name for your brand. Alphanumeric characters, underscores, hyphens, and spaces are allowed, up to 15 characters.

1. For **Use case**, choose **CODE\_VERIFICATION**.

1. Select the channels to enable (**SMS**, **VOICE**, or both).

1. (Optional) Expand **Advanced settings** to select countries, a default template, an associated pool, or to enable deletion protection.

1. (Optional) Expand **Tags** to add tags.

1. Choose **Create Notify configuration**.

------
#### [ AWS CLI ]

**To create a Notify configuration using the AWS CLI**
+ At the command line, enter the following command:

  ```
  $ aws pinpoint-sms-voice-v2 create-notify-configuration \
  > --display-name {{MyBrand}} \
  > --use-case CODE_VERIFICATION \
  > --enabled-channels SMS VOICE \
  > --enabled-countries US CA GB
  ```

  In the preceding command, make the following changes:
  + Replace {{MyBrand}} with your brand display name (up to 15 characters).
  + Set **--enabled-channels** to `SMS`, `VOICE`, or both.
  + Set **--enabled-countries** to the ISO country codes you want to send to. Available countries depend on your tier.

  To apply tags, add **--tags Key={{Environment}},Value={{Production}}**.

------