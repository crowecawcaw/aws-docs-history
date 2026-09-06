

# Amazon Kendra events
<a name="events-ref-kendra"></a>

Amazon Kendra sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Kendra service events
<a name="events-ref-kendra-events"></a>

Amazon Kendra sends the following events directly to EventBridge: 
+ Document State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.kendra

```
{
  "source": ["aws.kendra"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.kendra"],
  "detail-type": ["{{Document State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Kendra events delivered via AWS CloudTrail
<a name="event-ref-kendra-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Kendra to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.kendra
+ `eventSource`: kendra.amazonaws.com

```
{
  "source": ["aws.kendra"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["kendra.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.kendra"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["kendra.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```