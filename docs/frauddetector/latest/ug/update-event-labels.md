Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Updating event labels in event data stored in Amazon Fraud Detector

You might need to add or update fraud labels for events that are already stored in Amazon Fraud Detector, such as when you perform an offline
fraud investigation for an event and want to close the machine learning feed back loop. To update the label for an event that is already
stored in Amazon Fraud Detector, use the `UpdateEventLabel` API operation. The following shows an example UpdateEventLabel API call.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.update_event_label(
            eventId        = '802454d3-f7d8-482d-97e8-c4b6db9a0428',
            eventTypeName  = 'sample_registration',
            assignedLabel  = 'fraud',
            labelTimestamp = '2020-07-13T23:18:21Z'
)


```
