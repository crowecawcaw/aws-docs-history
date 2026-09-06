

# AWS Elemental MediaPackage events
<a name="events-ref-mediapackagev2"></a>

MediaPackage sends service events directly to EventBridge, as well as via AWS CloudTrail.

## MediaPackage service events
<a name="events-ref-mediapackagev2-events"></a>

MediaPackage sends the following events directly to EventBridge: 
+ MediaPackageV2 HarvestJob Notification

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.mediapackagev2

```
{
  "source": ["aws.mediapackagev2"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.mediapackagev2"],
  "detail-type": ["{{MediaPackageV2 HarvestJob Notification}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## MediaPackage events delivered via AWS CloudTrail
<a name="event-ref-mediapackagev2-events-via-CT"></a>

AWS CloudTrail sends events originating from MediaPackage to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.mediapackagev2
+ `eventSource`: mediapackagev2.amazonaws.com

```
{
  "source": ["aws.mediapackagev2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediapackagev2.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.mediapackagev2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediapackagev2.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```