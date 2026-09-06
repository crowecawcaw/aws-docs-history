

# Amazon Inspector Classic events
<a name="events-ref-inspector"></a>

Amazon Inspector Classic sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Inspector Classic service events
<a name="events-ref-inspector-events"></a>

Amazon Inspector Classic sends the following events directly to EventBridge: 
+ Inspector Finding
+ Inspector Scan
+ Inspector2 Finding
+ Inspector2 Scan
+ Inspector2 Coverage
+ Inspector2 AutoEnable

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.inspector

```
{
  "source": ["aws.inspector"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.inspector"],
  "detail-type": ["{{Inspector Finding}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Inspector Classic events delivered via AWS CloudTrail
<a name="event-ref-inspector-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Inspector Classic to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.inspector
+ `eventSource`: inspector.amazonaws.com

```
{
  "source": ["aws.inspector"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["inspector.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.inspector"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["inspector.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```