

# Recycle Bin Service events
<a name="events-ref-rbin"></a>

Recycle Bin Service sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Recycle Bin Service service events
<a name="events-ref-rbin-events"></a>

Recycle Bin Service sends the following events directly to EventBridge: 
+ Recycle Bin Rule Locked
+ Recycle Bin Rule Change Attempted
+ Recycle Bin Rule Unlock Scheduled
+ Recycle Bin Rule Unlocking Notice
+ Recycle Bin Rule Unlocked

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.rbin

```
{
  "source": ["aws.rbin"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.rbin"],
  "detail-type": ["{{Recycle Bin Rule Locked}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Recycle Bin Service events delivered via AWS CloudTrail
<a name="event-ref-rbin-events-via-CT"></a>

AWS CloudTrail sends events originating from Recycle Bin Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.rbin
+ `eventSource`: rbin.amazonaws.com

```
{
  "source": ["aws.rbin"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rbin.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.rbin"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rbin.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```