# Change a message feedback

status record in AWS End User Messaging SMS

Once you have a signal that a customer has received your message you have to provide
feedback for the message by using [PutMessageFeedback](../../../pinpoint/latest/apireference_smsvoicev2/API_PutMessageFeedback.md "../../../pinpoint/latest/apireference_smsvoicev2/API_PutMessageFeedback.md") or [put-message-feedback](../../../cli/latest/reference/pinpoint-sms-voice-v2/put-message-feedback.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/put-message-feedback.md"). If the message feedback status
record isn't updated after one hour it is automatically set to `FAILED` but
the CloudWatch metrics are not updated until you set the record as `RECEIVED` or
`FAILED`. We recommend that you have a timer to set message feedback
status record to `FAILED` if you don't received a signal from your customer.

At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 --region '`us-east-1`' put-message-feedback --message-feedback-status `Status` --message-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

- Replace `us-east-1` with the AWS Region that
  your origination identity is stored in.
- Replace `Status` with `RECEIVED` or
  `FAILED`.
- Replace `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` with message id.
