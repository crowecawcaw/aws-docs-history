

# AWS Cost Explorer events
<a name="events-ref-ce"></a>

Cost Explorer sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Cost Explorer service events
<a name="events-ref-ce-events"></a>

Cost Explorer sends the following events directly to EventBridge: 
+ Anomaly Detected

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.ce

```
{
  "source": ["aws.ce"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.ce"],
  "detail-type": ["{{Anomaly Detected}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Cost Explorer events delivered via AWS CloudTrail
<a name="event-ref-ce-events-via-CT"></a>

AWS CloudTrail sends events originating from Cost Explorer to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.ce
+ `eventSource`: ce.amazonaws.com

```
{
  "source": ["aws.ce"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ce.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ce"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ce.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```