

# Oracle Database@AWS events
<a name="events-ref-odb"></a>

Oracle Database@AWS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Oracle Database@AWS service events
<a name="events-ref-odb-events"></a>

Oracle Database@AWS sends the following events directly to EventBridge: 
+ ODB Network Event
+ ODB Zero ETL Event

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.odb

```
{
  "source": ["aws.odb"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.odb"],
  "detail-type": ["{{ODB Network Event}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Oracle Database@AWS events delivered via AWS CloudTrail
<a name="event-ref-odb-events-via-CT"></a>

AWS CloudTrail sends events originating from Oracle Database@AWS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.odb
+ `eventSource`: odb.amazonaws.com

```
{
  "source": ["aws.odb"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["odb.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.odb"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["odb.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```