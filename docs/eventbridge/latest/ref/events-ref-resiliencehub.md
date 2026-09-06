

# AWS Resilience Hub events
<a name="events-ref-resiliencehub"></a>

Resilience Hub sends service events to EventBridge via AWS CloudTrail.

## Resilience Hub events delivered via AWS CloudTrail
<a name="event-ref-resiliencehub-events-via-CT"></a>

AWS CloudTrail sends events originating from Resilience Hub to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.resiliencehub
+ `eventSource`: resiliencehub.amazonaws.com

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resiliencehub.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resiliencehub.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```