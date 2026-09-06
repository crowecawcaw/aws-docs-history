

# AWS Elemental MediaStore events
<a name="events-ref-mediastore"></a>

MediaStore sends service events directly to EventBridge, as well as via AWS CloudTrail.

## MediaStore service events
<a name="events-ref-mediastore-events"></a>

MediaStore sends the following events directly to EventBridge: 
+ MediaStore Object Upload State Change
+ MediaStore Container State Change
+ MediaStore Object State Change

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.mediastore

```
{
  "source": ["aws.mediastore"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.mediastore"],
  "detail-type": ["{{MediaStore Object Upload State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## MediaStore events delivered via AWS CloudTrail
<a name="event-ref-mediastore-events-via-CT"></a>

AWS CloudTrail sends events originating from MediaStore to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.mediastore
+ `eventSource`: mediastore.amazonaws.com

```
{
  "source": ["aws.mediastore"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediastore.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.mediastore"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediastore.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```