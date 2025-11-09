Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Get details of a stored event data

After you store event data in Amazon Fraud Detector, you can check the latest data that was stored for an event using the [GetEvent](../api/API_GetEvent.md "../api/API_GetEvent.md") API.
The following example code checks the latest data stored for the `sample_registration` event.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.get_event(
            eventId        = '802454d3-f7d8-482d-97e8-c4b6db9a0428',
            eventTypeName  = 'sample_registration'
)


```
