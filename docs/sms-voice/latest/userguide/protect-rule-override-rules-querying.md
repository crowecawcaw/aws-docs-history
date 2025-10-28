# Query phone number override rule

in AWS End User Messaging SMS

To query phone number override rules, you can use the AWS End User Messaging SMS console, the [ListProtectConfigurationRuleSetNumberOverrides](../../../pinpoint/latest/apireference_smsvoicev2/API_ListProtectConfigurationRuleSetNumberOverrides.md "../../../pinpoint/latest/apireference_smsvoicev2/API_ListProtectConfigurationRuleSetNumberOverrides.md") action
in the AWS End User Messaging SMS and voice v2 API, or the [list-protect-configuration-rule-set-number-overrides](../../../cli/latest/reference/pinpoint-sms-voice-v2/list-protect-configuration-rule-set-number-overrides.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/list-protect-configuration-rule-set-number-overrides.md") command in the AWS CLI.
This section shows how to query phone number override rules using the AWS End User Messaging SMS
console and the
AWS CLI.

List phone number rule override (Console)
To query a phone number override rule using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration** and then choose the protect
   configuration.
3. Choose the **Rule overrides** tab.
4. In **Query rule overrides** you can search for rules with a
   combination of all three of the available fields **Destination phone
   number**, **Override type**, and
   **Date**:
   1. For **Destination phone number**:
      - All numbers – Do not filter out any phone
        numbers.
      - Number lookup – Enter a prefix or full phone number to
        filter on.
      - By country – Choose a country to filter on.

   2. For **Override type**:
      - Always allowed – Only return allow rules.
      - Always blocked – Only return block rules.

   3. For **Date**
      - All dates – Do not filter out any dates.
      - Recently added – Return phone number override rules that
        were created in the last 24 hours.
      - Expires before – Return phone number override rules that
        expire before the specified date.
      - Expires on – Return phone number override rules that
        expire on the specified date.
      - Expires after – Return phone number override rules that
        expire after the specified date.

5. Choose **Query**.

Any phone number override rules that match your query are returned in the
**Query results** section. You can choose rules from the
section to edit or delete.

List phone number rule override (AWS CLI)
You can use the [list-protect-configuration-rule-set-number-overrides](../../../cli/latest/reference/pinpoint-sms-voice-v2/list-protect-configuration-rule-set-number-overrides.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/list-protect-configuration-rule-set-number-overrides.md") AWS CLI command to
list all phone number rule overrides in a protect configuration.

```
`$` aws pinpoint-sms-voice-v2 list-protect-configuration-rule-set-number-overrides --protect-configuration-id `ProtectConfigurationID`
```

In the preceding command, make the following changes:

- Replace `ProtectConfigurationID` with the
  unique identifier of the protect configuration.
