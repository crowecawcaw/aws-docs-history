

# Tags events
<a name="events-ref-tag"></a>

Tags sends service events directly to EventBridge.

## Tags service events
<a name="events-ref-tag-events"></a>

Tags sends the following events directly to EventBridge: 
+ Tag Change on Resource
+ Invalid Effective Tag Policy

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.tag

```
{
  "source": ["aws.tag"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.tag"],
  "detail-type": ["{{Tag Change on Resource}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.