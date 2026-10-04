

# Change a protect configuration country rules in AWS End User Messaging
<a name="nx-features-sms-protect-edit-countries"></a>

Protect configuration country rules either *Allow*, *Block*, *Monitor*, or *Filter* messages for each destination country. To update protect configuration country rules, you can use the AWS End User Messaging console or the `aws sms-voice update-protect-configuration-country-rule-set` command in the AWS CLI. This section shows how to update the protect configuration country rules using the AWS End User Messaging console and the AWS CLI.

**Note**  
You can only change your MMS country rules list through the AWS End User Messaging and voice v2 API or AWS CLI.

------
#### [ Edit a protect configuration (Console) ]

To edit a protect configuration using the AWS End User Messaging console, follow these steps:

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Protect**, choose **Protect configuration**.

1. On the **Protect configuration** page, choose a protect configuration and then choose **Edit**.

1. In the protect configuration details table choose the **SMS rules** or **Voice rules** tab.

1. In the **SMS/Voice country rules** tab check the countries to change the rules for and then choose **Allow**, **Block**, **Monitor**, or **Filter**. For more information on country rule modes, see country rule modes. You can sort and filter the country list based on **Country**, **Region** and **Rule**.

1. In the **Status change confirmation** window review your changes and then choose **Confirm** to apply them.

The new country rule set is now used for the protect configuration.

------
#### [ Edit a protect configuration (AWS CLI) ]

You can use the update-protect-configuration-country-set command to change a protect configuration's country rules. You can change up to 300 country rules at a time.

**To edit a protect configuration**
+ To edit two country rules at the command line, enter the following command:

  ```
  aws pinpoint-sms-voice-v2 update-protect-configuration-country-rule-set --protect-configuration-id {{ProtectConfigId}} --number-capability {{Capability}} --country-rule-set-updates '{"{{CountryISO1}}":{"ProtectStatus": "{{Rule1}}"}, "{{CountryISO2}}": {"ProtectStatus":"{{Rule2}}"}}'
  ```

  In the preceding command, make the following changes:
  + Replace {{ProtectConfigId}} with the unique identifier of the protect configuration.
  + Replace {{Capability}} with `SMS`, `MMS`, or `VOICE`.
  + Replace {{CountryISO1}} with the two letter ISO country code. For a list of ISO country codes, see the list of countries you can send SMS messages to.
  + Replace {{Rule1}} with `ALLOW` or `BLOCK`.
  + Replace {{CountryISO2}} with the two letter ISO country code. For a list of ISO country codes, see the list of countries you can send SMS messages to.
  + Replace {{Rule2}} with `ALLOW` or `BLOCK`.

------