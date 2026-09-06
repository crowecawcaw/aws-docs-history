

# Amazon GameLift Servers events
<a name="events-ref-gamelift"></a>

Amazon GameLift Servers sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon GameLift Servers service events
<a name="events-ref-gamelift-events"></a>

Amazon GameLift Servers sends the following events directly to EventBridge: 
+ GameLift Matchmaking Event
+ GameLift Queue Placement Event

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.gamelift

```
{
  "source": ["aws.gamelift"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.gamelift"],
  "detail-type": ["{{GameLift Matchmaking Event}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon GameLift Servers events delivered via AWS CloudTrail
<a name="event-ref-gamelift-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon GameLift Servers to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.gamelift
+ `eventSource`: gamelift.amazonaws.com

```
{
  "source": ["aws.gamelift"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["gamelift.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.gamelift"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["gamelift.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```