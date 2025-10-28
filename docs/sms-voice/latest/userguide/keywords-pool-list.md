# View keywords used by a phone pool in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to view the keyword responses for your phone pool.

View keywords (Console)
Use the AWS End User Messaging SMS console to view keywords to your pool.

###### Add a keyword

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone pools**.
3. On the **Phone Pools** page, choose the pool.
4. On the **Keywords** tab, you can view the keyword, response message, and actions.

List keywords (AWS CLI)
You can use the [describe-keywords](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-keywords.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-keywords.md") command to view information about the keywords associated with an origination identity.

To view a list of keywords using the AWS CLI at the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-keywords \
`>` --origination-identity `OriginationIdentity`
```

In the preceding command, make the following changes:

Replace `OriginationIdentity` with the unique ID or Amazon Resource
Name (ARN) of the phone number or sender ID that you want a list of keywords from.
