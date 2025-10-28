# Delete a phone number override rule

in AWS End User Messaging SMS

To delete a phone number override rule, you can use the AWS End User Messaging SMS console, the
[DeleteProtectConfigurationRuleSetNumberOverride](../../../pinpoint/latest/apireference_smsvoicev2/API_DeleteProtectConfigurationRuleSetNumberOverride.md "../../../pinpoint/latest/apireference_smsvoicev2/API_DeleteProtectConfigurationRuleSetNumberOverride.md") action in the AWS End User Messaging SMS and
voice v2 API, or the [delete-protect-configuration-rule-set-number-override](../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-protect-configuration-rule-set-number-override.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-protect-configuration-rule-set-number-override.md") command in the AWS CLI.
This section shows how to delete a phone number override rule using the AWS End User Messaging SMS
console and the
AWS CLI.

Delete a phone number rule override (Console)
To delete a phone number override rule using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration** and then choose the protect
   configuration.
3. Choose the **Rule overrides** tab and in the **Rules
   override** section choose the phone number override rules to
   delete. You can use [Query phone number override rules](protect-rule-override-rules-querying.md#protect-rule-override-rules-querying.title "protect-rule-override-rules-querying.md#protect-rule-override-rules-querying.title") to search for specific rules to
   edit. Choose **Delete**.
4. In the **Delete rule override** window, enter
   `confirm`, and the choose
   **Delete**

Delete a phone number rule override (AWS CLI)
You can use the [delete-protect-configuration-rule-set-number-override](../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-protect-configuration-rule-set-number-override.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-protect-configuration-rule-set-number-override.md") AWS CLI command to
delete a phone number rule override.

```
`$` aws pinpoint-sms-voice-v2 delete-protect-configuration-rule-set-number-override --protect-configuration-id `ProtectConfigurationID` --destination-phone-number `+12065550150`
```

In the preceding command, make the following changes:

- Replace `ProtectConfigurationID` with the
  unique identifier of the protect configuration.
- Replace `+12065550150` with the phone
  number to delete the rule for.
