

# AWS Elemental MediaPackage events
<a name="events-ref-mediapackage"></a>

MediaPackage sends service events directly to EventBridge, as well as via AWS CloudTrail.

## MediaPackage service events
<a name="events-ref-mediapackage-events"></a>

MediaPackage sends the following events directly to EventBridge: 
+ MediaPackage Key Provider Notification
+ MediaPackage Input Notification
+ MediaPackage Throttle
+ MediaPackage HarvestJob Notification

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.mediapackage

```
{
  "source": ["aws.mediapackage"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.mediapackage"],
  "detail-type": ["{{MediaPackage Key Provider Notification}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## MediaPackage events delivered via AWS CloudTrail
<a name="event-ref-mediapackage-events-via-CT"></a>

AWS CloudTrail sends events originating from MediaPackage to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.mediapackage
+ `eventSource`: mediapackage.amazonaws.com

```
{
  "source": ["aws.mediapackage"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediapackage.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.mediapackage"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediapackage.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```