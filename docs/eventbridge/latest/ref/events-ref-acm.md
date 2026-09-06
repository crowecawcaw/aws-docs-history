

# AWS Certificate Manager events
<a name="events-ref-acm"></a>

ACM sends service events directly to EventBridge, as well as via AWS CloudTrail.

## ACM service events
<a name="events-ref-acm-events"></a>

ACM sends the following events directly to EventBridge: 
+ ACM Certificate Approaching Expiration
+ ACM Certificate Renewal Action Required
+ ACM Certificate Expired
+ ACM Certificate Available
+ ACM Certificate Rotated
+ ACM Certificate Revoked

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.acm

```
{
  "source": ["aws.acm"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.acm"],
  "detail-type": ["{{ACM Certificate Approaching Expiration}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## ACM events delivered via AWS CloudTrail
<a name="event-ref-acm-events-via-CT"></a>

AWS CloudTrail sends events originating from ACM to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.acm
+ `eventSource`: acm.amazonaws.com

```
{
  "source": ["aws.acm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.acm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```