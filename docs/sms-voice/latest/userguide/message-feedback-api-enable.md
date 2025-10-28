# Send a message with message feedback in AWS End User Messaging SMS

To enable message feedback when sending a message with [SendTextMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendTextMessage.md"), or [SendMediaMessage](../../../pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.md "../../../pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.md"), set the
`MessageFeedbackEnabled` parameter to true. When you use message feedback
you have to set the message feedback status record to update your [message feedback metrics](monitoring-cloudwatch.md#cw-metrics-message-conversion.title "monitoring-cloudwatch.md#cw-metrics-message-conversion.title") .

The following is a partial example of sending an SMS with message feedback enabled by using the `--message-feedback-enabled` parameter.

###### Sending an SMS message with message feedback enabled with the API

- At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 --region '`us-east-1`' send-text-message --destination-phone-number `+12065550150` --origination-identity `+14255550120` --message-body '`text body`' --message-feedback-enabled
```

In the preceding command, make the following changes:

    + Replace `us-east-1` with the AWS Region that
     your origination identity is stored in.
    + Replace `+12065550150` with the destination phone
     number.
    + Replace `+14255550120` with your origination
     identity. The origination identity must be `ACTIVE` and able to send to the
     destination phone number.
    + Replace `text body` with your text
     message.
    + Leave `--message-feedback-enabled` to have message feedback enabled.

The following is a partial example of sending an SMS with message feedback enabled in a configuration set. By using a configuration set you can also take advantage of any event logging specified by the configuration set.

###### Example of sending an SMS message with message feedback with a configuration set

- At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 --region '`us-east-1`' send-text-message --destination-phone-number `+12065550150` --origination-identity `+14255550120` --message-body '`text body`' --configuration-set-name `ConfigSetName`
```

In the preceding command, make the following changes:

    + Replace `us-east-1` with the AWS Region that
     your origination identity is stored in.
    + Replace `+12065550150` with the destination phone
     number.
    + Replace `+14255550120` with your origination
     identity. The origination identity must be `ACTIVE` and able to send to the
     destination phone number.
    + Replace `text body` with your text
     message.
    + Replace `ConfigSetName` with the name of the configuration set.

If AWS End User Messaging SMS accepts the command you will receive the `MessageId`. This only
means the command was successfully received and not that the destination device has
received the message yet.

```
{
   "MessageId": "string"
}
```

You need to save the `MessageId` to update that your customer [received the message](message-feedback-change-status.md#message-feedback-change-status.title "message-feedback-change-status.md#message-feedback-change-status.title").
