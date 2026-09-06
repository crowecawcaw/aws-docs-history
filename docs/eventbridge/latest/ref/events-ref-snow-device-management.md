

# AWS Snowball Edge Device Management events
<a name="events-ref-snow-device-management"></a>

Snowball Edge Device Management sends service events to EventBridge via AWS CloudTrail.

## Snowball Edge Device Management events delivered via AWS CloudTrail
<a name="event-ref-snow-device-management-events-via-CT"></a>

AWS CloudTrail sends events originating from Snowball Edge Device Management to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.snow-device-management
+ `eventSource`: snow-device-management.amazonaws.com

```
{
  "source": ["aws.snow-device-management"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["snow-device-management.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.snow-device-management"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["snow-device-management.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```