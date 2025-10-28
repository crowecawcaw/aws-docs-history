# Change a phone number's capabilities with the AWS CLI

After you request a phone number, you can use the [update-phone-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/update-phone-number.md") CLI to change the settings of that phone number, or to
enable additional features. You can change several phone number settings, including the
pool and opt-out list that are associated with the phone number, as well as the deletion
protection setting.

An example of an additional feature that you can enable by updating a phone number is
two-way messaging. Support for two-way messaging varies depending on which country you
plan to send messages to. For a list of supported countries, see [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").

```
`$` aws pinpoint-sms-voice-v2 update-phone-number \
`>` --phone-number-id `phone-d2b0f5dd4fd14ebdb2a3b9128example` \
`>` --deletion-protection-enabled `true` \
`>` --international-sending-enabled `true` \
`>` --no-international-sending-enabled `true` \
`>` --opt-out-list-name `optOutListName` \
`>` --self-managed-opt-outs-enabled `true` \
`>` --two-way-enabled `true` \
`>` --two-way-channel-arn `arn:aws:sns:us-east-1:111122223333:MyTopic`
```

In the preceding command, do the following:

- Replace `phone-d2b0f5dd4fd14ebdb2a3b9128example` with
  the PhoneNumberID or the Amazon Resource Name (ARN) of the phone number that you
  want to update. You can find both of these values by using the DescribePhoneNumbers
  operation.
- Replace `optOutListName` with the name of the opt-out list that you want to
  associate with this phone number.
- If you want to disable the deletion protection feature, change the value of
  the `DeletionProtectionEnabled` parameter to
  `false`.
- To enable international messaging for this phone number, use the
  `international-sending-enabled` parameter.
- To disable international messaging for this phone number, use the
  `no-international-sending-enabled` parameter.
- If you want to self-managed SMS opt-outs feature, change the value of the
  `SelfManagedOptOutsEnabled` parameter to
  `false`.
- If you want to disable two-way SMS
  messaging for this phone number, change the value of the
  `TwoWayEnabled` parameter to `false`.
- If you enable the two-way messaging feature for the phone number, you must
  specify the ARN of an Amazon SNS topic. Replace
  `arn:aws:sns:us-east-1:111122223333:MyTopic`
  with the ARN of the Amazon SNS topic that you want to use. When you receive incoming
  messages, they are sent to the topic that you specify.
  The `PhoneNumberId` parameter is the only required parameter for this
  command. You can omit any of the other parameters if you don't want to change the
  corresponding settings.
