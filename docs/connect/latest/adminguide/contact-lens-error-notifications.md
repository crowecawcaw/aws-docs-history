# Error notifications: When

Contact Lens can't analyze a contact

It's possible that Contact Lens can't analyze a contact file, even
though analysis is enabled on the flow. When this happens, Contact Lens
sends error notifications using Amazon EventBridge events.

Events are emitted on a
[best effort](../../../eventbridge/latest/userguide/eb-service-event.md "../../../eventbridge/latest/userguide/eb-service-event.md")
basis.

## Subscribe to

EventBridge notifications

To subscribe to these notifications, create a custom EventBridge rule that
matches the following:

- "source" = "aws.connect"
- "detail-type" = "Contact Lens Analysis State Change"

You can also add to the pattern to be notified when a specific event code
occurs. For more information, see [Event Patterns](../../../eventbridge/latest/userguide/filtering-examples-structure.md "../../../eventbridge/latest/userguide/filtering-examples-structure.md") in the
_Amazon EventBridge User Guide_.

The format of a notification looks like the following sample:

```
{
    "version": "0", // set by CloudWatch Events
    "id": "55555555-1111-1111-1111-111111111111", // set by CloudWatch Events
    "source": "aws.connect",
    "detail-type": "Contact Lens Analysis State Change",
    "account": "111122223333",
    "time": "2020-04-27T18:43:48Z",
    "region": "us-east-1", // set by CloudWatch Events
    "resources": [
        "arn:aws:connect:us-east-1:111122223333:instance/abcd1234-defg-5678-h9j0-7c822889931e",
        "arn:aws:connect:us-east-1:111122223333:instance/abcd1234-defg-5678-h9j0-7c822889931e/contact/efgh4567-pqrs-5678-t9c0-111111111111"
    ],
    "detail": {
        "instance": "arn:aws:connect:us-east-1:111122223333:instance/abcd1234-defg-5678-h9j0-7c822889931e",
        "contact": "arn:aws:connect:us-east-1:111122223333:instance/abcd1234-defg-5678-h9j0-7c822889931e/contact/efgh4567-pqrs-5678-t9c0-111111111111",
        "channel": "VOICE",
        "state": "FAILED",
        "reasonCode": "RECORDING_FILE_CANNOT_BE_READ"
    }
}
```

## Event codes

The following table lists the event codes that may result when
Contact Lens can't analyze a contact.

| Event reason code                   | Description                                                                                                                                                                      |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INVALID_ANALYSIS_CONFIGURATION      | Contact Lens received invalid values when the flow was initiated, such as an unsupported or invalid language code, or an unsupported value for redaction behavior.               |
| RECORDING_FILE_CANNOT_BE_READ       | Contact Lens can't get the recording file. This might be because file isn't present in the S3 bucket, or there are problems with permissions.                                    |
| RECORDING_FILE_TOO_SMALL            | The recording file is too small for analysis (less than 105 ms). If file doesn’t have expected format, an INVALID error occurs. Empty JSON is also an unexpected object.         |
| RECORDING_FILE_TOO_LARGE            | The recording file exceeds the duration limit for analysis. <br>• Voice: More than 14,400 seconds, or 4 hours <br>• Chat: More than 20K messages in a transcript                 |
| RECORDING_FILE_INVALID              | The recording file is invalid.                                                                                                                                                   |
| RECORDING_FILE_CANNOT_BE_READ       | An error occurred when Contact Lens tried to read the recording file.                                                                                                            |
| RECORDING_FILE_EMPTY                | The recording file is empty.                                                                                                                                                     |
| RECORDING_SAMPLE_RATE_NOT_SUPPORTED | The sample rate of the audio file is not supported. Contact Lens currently supports audio files with an 8kHz sample rate. That is the sample rate for Amazon Connect recordings. |
