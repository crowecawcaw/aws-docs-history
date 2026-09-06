

# Amazon QLDB events
<a name="events-ref-qldb"></a>

QLDB sends service events directly to EventBridge, as well as via AWS CloudTrail.

## QLDB service events
<a name="events-ref-qldb-events"></a>

QLDB sends the following events directly to EventBridge: 
+ QLDB Ledger State Change

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.qldb

```
{
  "source": ["aws.qldb"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.qldb"],
  "detail-type": ["{{QLDB Ledger State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## QLDB events delivered via AWS CloudTrail
<a name="event-ref-qldb-events-via-CT"></a>

AWS CloudTrail sends events originating from QLDB to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.qldb
+ `eventSource`: qldb.amazonaws.com

```
{
  "source": ["aws.qldb"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["qldb.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.qldb"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["qldb.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```