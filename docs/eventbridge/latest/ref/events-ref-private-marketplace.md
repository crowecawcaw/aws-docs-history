

# AWS Marketplace Private Marketplace events
<a name="events-ref-private-marketplace"></a>

AWS Marketplace Private Marketplace sends service events directly to EventBridge.

## AWS Marketplace Private Marketplace service events
<a name="events-ref-private-marketplace-events"></a>

AWS Marketplace Private Marketplace sends the following events directly to EventBridge: 
+ Product Request Created
+ Product Request Approved
+ Product Request Declined

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.private-marketplace

```
{
  "source": ["aws.private-marketplace"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.private-marketplace"],
  "detail-type": ["{{Product Request Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.