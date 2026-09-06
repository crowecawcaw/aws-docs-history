

# AWS Trusted Advisor events
<a name="events-ref-trustedadvisor"></a>

Trusted Advisor sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Trusted Advisor service events
<a name="events-ref-trustedadvisor-events"></a>

Trusted Advisor sends the following events directly to EventBridge: 
+ Trusted Advisor Check Item Refresh Notification
+ Trusted Advisor Pursuit Weekly Digest
+ Trusted Advisor Pursuit Daily Digest

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.trustedadvisor

```
{
  "source": ["aws.trustedadvisor"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.trustedadvisor"],
  "detail-type": ["{{Trusted Advisor Check Item Refresh Notification}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Trusted Advisor events delivered via AWS CloudTrail
<a name="event-ref-trustedadvisor-events-via-CT"></a>

AWS CloudTrail sends events originating from Trusted Advisor to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.trustedadvisor
+ `eventSource`: trustedadvisor.amazonaws.com

```
{
  "source": ["aws.trustedadvisor"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["trustedadvisor.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.trustedadvisor"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["trustedadvisor.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```