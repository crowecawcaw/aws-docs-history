

# AWS Elemental MediaLive events
<a name="events-ref-medialive"></a>

MediaLive sends service events directly to EventBridge, as well as via AWS CloudTrail.

## MediaLive service events
<a name="events-ref-medialive-events"></a>

MediaLive sends the following events directly to EventBridge: 
+ MediaLive Channel State Change
+ MediaLive Channel Alert
+ MediaLive Multiplex State Change
+ MediaLive Multiplex Alert
+ MediaLive Channel Input Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.medialive

```
{
  "source": ["aws.medialive"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.medialive"],
  "detail-type": ["{{MediaLive Channel State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## MediaLive events delivered via AWS CloudTrail
<a name="event-ref-medialive-events-via-CT"></a>

AWS CloudTrail sends events originating from MediaLive to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.medialive
+ `eventSource`: medialive.amazonaws.com

```
{
  "source": ["aws.medialive"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["medialive.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.medialive"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["medialive.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```