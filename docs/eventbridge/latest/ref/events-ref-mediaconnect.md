

# AWS Elemental MediaConnect events
<a name="events-ref-mediaconnect"></a>

MediaConnect sends service events directly to EventBridge, as well as via AWS CloudTrail.

## MediaConnect service events
<a name="events-ref-mediaconnect-events"></a>

MediaConnect sends the following events directly to EventBridge: 
+ MediaConnect Alert
+ MediaConnect Source Health
+ MediaConnect Output Health
+ MediaConnect Flow Status Change
+ MediaConnect Flow Maintenance
+ MediaConnect Flow Health
+ MediaConnect Output Status Change
+ MediaConnect Flow Content Quality

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.mediaconnect

```
{
  "source": ["aws.mediaconnect"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.mediaconnect"],
  "detail-type": ["{{MediaConnect Alert}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## MediaConnect events delivered via AWS CloudTrail
<a name="event-ref-mediaconnect-events-via-CT"></a>

AWS CloudTrail sends events originating from MediaConnect to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.mediaconnect
+ `eventSource`: mediaconnect.amazonaws.com

```
{
  "source": ["aws.mediaconnect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediaconnect.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.mediaconnect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediaconnect.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```