

# AWS X-Ray events
<a name="events-ref-xray"></a>

X-Ray sends service events directly to EventBridge, as well as via AWS CloudTrail.

## X-Ray service events
<a name="events-ref-xray-events"></a>

X-Ray sends the following events directly to EventBridge: 
+ AWS X-Ray Insight Update

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.xray

```
{
  "source": ["aws.xray"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.xray"],
  "detail-type": ["{{AWS X-Ray Insight Update}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## X-Ray events delivered via AWS CloudTrail
<a name="event-ref-xray-events-via-CT"></a>

AWS CloudTrail sends events originating from X-Ray to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.xray
+ `eventSource`: xray.amazonaws.com

```
{
  "source": ["aws.xray"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["xray.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.xray"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["xray.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```