

# AWS DataSync Discovery events
<a name="events-ref-datasync-discovery"></a>

DataSync Discovery sends service events directly to EventBridge.

## DataSync Discovery service events
<a name="events-ref-datasync-discovery-events"></a>

DataSync Discovery sends the following events directly to EventBridge: 
+ Discovery Job Expiration Soon
+ Discovery Job State Change
+ Storage System Connectivity Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.datasync-discovery

```
{
  "source": ["aws.datasync-discovery"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.datasync-discovery"],
  "detail-type": ["{{Discovery Job Expiration Soon}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.