

# Amazon Connect Customer Cases events
<a name="events-ref-cases"></a>

Connect Customer Cases sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Connect Customer Cases service events
<a name="events-ref-cases-events"></a>

Connect Customer Cases sends the following events directly to EventBridge: 
+ Amazon Connect Cases Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.cases

```
{
  "source": ["aws.cases"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.cases"],
  "detail-type": ["{{Amazon Connect Cases Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Connect Customer Cases events delivered via AWS CloudTrail
<a name="event-ref-cases-events-via-CT"></a>

AWS CloudTrail sends events originating from Connect Customer Cases to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.cases
+ `eventSource`: cases.amazonaws.com

```
{
  "source": ["aws.cases"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cases.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.cases"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cases.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```