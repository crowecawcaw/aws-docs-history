

# Amazon Inspector events
<a name="events-ref-inspector2"></a>

Amazon Inspector sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Inspector service events
<a name="events-ref-inspector2-events"></a>

Amazon Inspector sends the following events directly to EventBridge: 
+ Inspector Finding
+ Inspector Scan
+ Inspector2 Finding
+ Inspector2 Scan
+ Inspector2 Coverage
+ Inspector2 AutoEnable

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.inspector2

```
{
  "source": ["aws.inspector2"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["{{Inspector Finding}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Inspector events delivered via AWS CloudTrail
<a name="event-ref-inspector2-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Inspector to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.inspector2
+ `eventSource`: inspector2.amazonaws.com

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["inspector2.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["inspector2.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```