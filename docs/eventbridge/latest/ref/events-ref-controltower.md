

# AWS Control Tower events
<a name="events-ref-controltower"></a>

AWS Control Tower sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Control Tower service events
<a name="events-ref-controltower-events"></a>

AWS Control Tower sends the following events directly to EventBridge: 
+ Drift Detected

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.controltower

```
{
  "source": ["aws.controltower"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.controltower"],
  "detail-type": ["{{Drift Detected}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Control Tower events delivered via AWS CloudTrail
<a name="event-ref-controltower-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Control Tower to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.controltower
+ `eventSource`: controltower.amazonaws.com

```
{
  "source": ["aws.controltower"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["controltower.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.controltower"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["controltower.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```