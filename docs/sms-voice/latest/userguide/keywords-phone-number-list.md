# View the keywords used by a phone number in AWS End User Messaging SMS

You can use the [describe-keywords](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-keywords.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-keywords.md") command to view information about the keywords associated with an origination identity.

To view a list of keywords using the AWS CLI at the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-keywords \
`>` --origination-identity `OriginationIdentity`
```

In the preceding command, make the following changes:

Replace `OriginationIdentity` with the unique ID or Amazon Resource
Name (ARN) of the phone number or sender ID that you want a list of keywords from.
