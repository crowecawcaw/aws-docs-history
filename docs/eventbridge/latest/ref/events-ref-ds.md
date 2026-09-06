

# AWS Directory Service events
<a name="events-ref-ds"></a>

Directory Service sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Directory Service service events
<a name="events-ref-ds-events"></a>

Directory Service sends the following events directly to EventBridge: 
+ Directory Service Domain Controller Discovery Update

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.ds

```
{
  "source": ["aws.ds"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.ds"],
  "detail-type": ["{{Directory Service Domain Controller Discovery Update}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Directory Service events delivered via AWS CloudTrail
<a name="event-ref-ds-events-via-CT"></a>

AWS CloudTrail sends events originating from Directory Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.ds
+ `eventSource`: ds.amazonaws.com

```
{
  "source": ["aws.ds"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ds.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ds"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ds.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```