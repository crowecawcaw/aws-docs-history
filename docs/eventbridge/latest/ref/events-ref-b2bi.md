

# AWS B2B Data Interchange events
<a name="events-ref-b2bi"></a>

B2B Data Interchange sends service events directly to EventBridge, as well as via AWS CloudTrail.

## B2B Data Interchange service events
<a name="events-ref-b2bi-events"></a>

B2B Data Interchange sends the following events directly to EventBridge: 
+ Transformation Completed
+ Transformation Failed
+ Acknowledgement Completed
+ Acknowledgement Failed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.b2bi

```
{
  "source": ["aws.b2bi"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.b2bi"],
  "detail-type": ["{{Transformation Completed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## B2B Data Interchange events delivered via AWS CloudTrail
<a name="event-ref-b2bi-events-via-CT"></a>

AWS CloudTrail sends events originating from B2B Data Interchange to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.b2bi
+ `eventSource`: b2bi.amazonaws.com

```
{
  "source": ["aws.b2bi"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["b2bi.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.b2bi"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["b2bi.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```