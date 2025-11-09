Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Update label

If your event dataset is stored with Amazon Fraud Detector, you might need to add or update labels for the stored events, such as when you perform an offline
fraud investigation for an event and want to close the machine learning feed back loop.

You can add or update labels for stored events using the
[update-event-label](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-event-label.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-event-label.html") command, using the [UpdateEventLabel](../api/API_UpdateEventLabel.md "../api/API_UpdateEventLabel.md") API, or using the AWS SDK for Python (Boto3)

The following AWS SDK for Python (Boto3) example code adds a label _fraud_ that is associated with the event type _registration_ using the `UpdateEventLabel` API.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.update_event_label(
            eventId        = '802454d3-f7d8-482d-97e8-c4b6db9a0428',
            eventTypeName  = 'registration',
            assignedLabel  = 'fraud',
            labelTimestamp = '2020-07-13T23:18:21Z'
)



```
