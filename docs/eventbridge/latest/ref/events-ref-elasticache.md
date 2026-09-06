

# Amazon ElastiCache events
<a name="events-ref-elasticache"></a>

ElastiCache sends service events directly to EventBridge, as well as via AWS CloudTrail.

## ElastiCache service events
<a name="events-ref-elasticache-events"></a>

ElastiCache sends the following events directly to EventBridge: 
+ Cache Created
+ Cache Creation Failed
+ Cache Deleted
+ Snapshot Created
+ Snapshot Creation Failed
+ Cache Update Failed
+ Cache Updated
+ Cache Limit Approaching
+ Snapshot Export Failed
+ Snapshot Copy Failed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.elasticache

```
{
  "source": ["aws.elasticache"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.elasticache"],
  "detail-type": ["{{Cache Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## ElastiCache events delivered via AWS CloudTrail
<a name="event-ref-elasticache-events-via-CT"></a>

AWS CloudTrail sends events originating from ElastiCache to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.elasticache
+ `eventSource`: elasticache.amazonaws.com

```
{
  "source": ["aws.elasticache"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["elasticache.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.elasticache"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["elasticache.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```