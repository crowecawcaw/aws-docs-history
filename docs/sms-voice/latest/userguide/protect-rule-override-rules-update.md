# Edit a phone number override rule

in AWS End User Messaging SMS

To edit a phone number override rule, you can use the AWS End User Messaging SMS console, the [PutProtectConfigurationRuleSetNumberOverride](../../../pinpoint/latest/apireference_smsvoicev2/API_PutProtectConfigurationRuleSetNumberOverride.md "../../../pinpoint/latest/apireference_smsvoicev2/API_PutProtectConfigurationRuleSetNumberOverride.md") action in
the AWS End User Messaging SMS and voice v2 API, or the [put-protect-configuration-rule-set-number-override](../../../cli/latest/reference/pinpoint-sms-voice-v2/put-protect-configuration-rule-set-number-override.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/put-protect-configuration-rule-set-number-override.md") command in the AWS CLI. This
section shows how to create a phone number override rule using the AWS End User Messaging SMS
console and the
AWS CLI. You can choose multiple phone number override rules at a time to
make bulk edits.

Edit a phone number rule override (Console)
To edit a phone number override rule using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration** and then choose the protect
   configuration.
3. Choose the **Rule overrides** tab and in the **Rules
   override** section choose the phone number override rules to
   change. You can use [Query phone number override rules](protect-rule-override-rules-querying.md#protect-rule-override-rules-querying.title "protect-rule-override-rules-querying.md#protect-rule-override-rules-querying.title") to search for specific rules to
   edit. Choose **Edit**.
4. The **Destination phone numbers** section you can view the
   details about all of you phone number override rule.

You can remove a phone number override rule from being edited by choosing
**Remove** in the **Action**
column. 5. For **Override type** choose either **Always
allow** or **Always block**. 6. For **Expiration date – optional** choose a date for
the rule expire or leave it blank for the rule to never expire. 7. Choose **Save changes**.

Edit a phone number rule override (AWS CLI)
You can use the [put-protect-configuration-rule-set-number-override](../../../cli/latest/reference/pinpoint-sms-voice-v2/put-protect-configuration-rule-set-number-override.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/put-protect-configuration-rule-set-number-override.md") AWS CLI command to
edit a new phone number rule override.

###### Note

Because `--expiration-timestamp` is not specified this rule will never expire.

```
`$` aws pinpoint-sms-voice-v2 put-protect-configuration-rule-set-number-override --protect-configuration-id `ProtectConfigurationID` --destination-phone-number `+12065550150` --action `ACTION`
```

In the preceding command, make the following changes:

- Replace `ProtectConfigurationID` with the
  unique identifier of the protect configuration.
- Replace `+12065550150` with the phone
  number to create a rule for.
- Replace `ACTION` with
  `ALLOW` to allow messages to be sent to
  the phone number or `BLOCK` to not allow
  messages to the phone number.
