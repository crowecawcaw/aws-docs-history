

# Amazon EventBridge events
<a name="events-ref-events"></a>

EventBridge sends service events directly to EventBridge, as well as via AWS CloudTrail.

## EventBridge service events
<a name="events-ref-events-events"></a>

EventBridge sends the following events directly to EventBridge: 
+ Scheduled Event
+ Connection Creation Started
+ Connection Update Started
+ Connection Deletion Started
+ Connection Activated
+ Connection Authorized
+ Connection Authorization Started
+ Connection Deauthorization Started
+ Connection Deauthorized
+ Connection Failed Connectivity
+ API Destination Activated
+ API Destination Deactivated

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.events

```
{
  "source": ["aws.events"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.events"],
  "detail-type": ["{{Scheduled Event}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## EventBridge events delivered via AWS CloudTrail
<a name="event-ref-events-events-via-CT"></a>

AWS CloudTrail sends events originating from EventBridge to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.events
+ `eventSource`: events.amazonaws.com

```
{
  "source": ["aws.events"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["events.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.events"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["events.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```