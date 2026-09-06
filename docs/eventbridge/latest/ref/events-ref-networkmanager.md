

# AWS Network Manager events
<a name="events-ref-networkmanager"></a>

Network Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Network Manager service events
<a name="events-ref-networkmanager-events"></a>

Network Manager sends the following events directly to EventBridge: 
+ Network Manager Topology Change
+ Network Manager Routing Update
+ Network Manager Status Update
+ Network Manager Service Advisory
+ Network Manager Segment Update
+ Network Manager Network Function Group Update
+ Network Manager Policy Update

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.networkmanager

```
{
  "source": ["aws.networkmanager"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.networkmanager"],
  "detail-type": ["{{Network Manager Topology Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Network Manager events delivered via AWS CloudTrail
<a name="event-ref-networkmanager-events-via-CT"></a>

AWS CloudTrail sends events originating from Network Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.networkmanager
+ `eventSource`: networkmanager.amazonaws.com

```
{
  "source": ["aws.networkmanager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["networkmanager.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.networkmanager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["networkmanager.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```