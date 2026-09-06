

# AWS Health events
<a name="events-ref-health"></a>

AWS Health sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Health service events
<a name="events-ref-health-events"></a>

AWS Health sends the following events directly to EventBridge: 
+ AWS Health Event
+ AWS Health Abuse Event

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.health

```
{
  "source": ["aws.health"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.health"],
  "detail-type": ["{{AWS Health Event}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Health events delivered via AWS CloudTrail
<a name="event-ref-health-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Health to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.health
+ `eventSource`: health.amazonaws.com

```
{
  "source": ["aws.health"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["health.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.health"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["health.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```