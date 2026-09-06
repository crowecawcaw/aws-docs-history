

# Amazon CloudWatch Observability Access Manager events
<a name="events-ref-oam"></a>

Amazon CloudWatch Observability Access Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon CloudWatch Observability Access Manager service events
<a name="events-ref-oam-events"></a>

Amazon CloudWatch Observability Access Manager sends the following events directly to EventBridge: 
+ Attached Link Created
+ Attached Link Updated
+ Attached Link Deleted

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.oam

```
{
  "source": ["aws.oam"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.oam"],
  "detail-type": ["{{Attached Link Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon CloudWatch Observability Access Manager events delivered via AWS CloudTrail
<a name="event-ref-oam-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon CloudWatch Observability Access Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.oam
+ `eventSource`: oam.amazonaws.com

```
{
  "source": ["aws.oam"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["oam.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.oam"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["oam.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```