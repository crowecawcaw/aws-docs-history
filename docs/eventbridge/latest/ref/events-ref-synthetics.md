

# Amazon CloudWatch Synthetics events
<a name="events-ref-synthetics"></a>

CloudWatch Synthetics sends service events directly to EventBridge, as well as via AWS CloudTrail.

## CloudWatch Synthetics service events
<a name="events-ref-synthetics-events"></a>

CloudWatch Synthetics sends the following events directly to EventBridge: 
+ Synthetics Canary Status Change
+ Synthetics Canary TestRun Failure
+ Synthetics Canary TestRun Successful

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.synthetics

```
{
  "source": ["aws.synthetics"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.synthetics"],
  "detail-type": ["{{Synthetics Canary Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## CloudWatch Synthetics events delivered via AWS CloudTrail
<a name="event-ref-synthetics-events-via-CT"></a>

AWS CloudTrail sends events originating from CloudWatch Synthetics to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.synthetics
+ `eventSource`: synthetics.amazonaws.com

```
{
  "source": ["aws.synthetics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["synthetics.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.synthetics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["synthetics.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```