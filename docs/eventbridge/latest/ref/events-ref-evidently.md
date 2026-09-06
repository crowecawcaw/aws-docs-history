

# Amazon CloudWatch Evidently events
<a name="events-ref-evidently"></a>

Amazon CloudWatch Evidently sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon CloudWatch Evidently service events
<a name="events-ref-evidently-events"></a>

Amazon CloudWatch Evidently sends the following events directly to EventBridge: 
+ Evidently Experiment Status Change
+ Evidently Experiment Rollout Traffic Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.evidently

```
{
  "source": ["aws.evidently"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.evidently"],
  "detail-type": ["{{Evidently Experiment Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon CloudWatch Evidently events delivered via AWS CloudTrail
<a name="event-ref-evidently-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon CloudWatch Evidently to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.evidently
+ `eventSource`: evidently.amazonaws.com

```
{
  "source": ["aws.evidently"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["evidently.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.evidently"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["evidently.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```