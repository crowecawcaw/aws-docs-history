

# Amazon Location Service Maps events
<a name="events-ref-geo-maps"></a>

Amazon Location Maps sends service events directly to EventBridge.

## Amazon Location Maps service events
<a name="events-ref-geo-maps-events"></a>

Amazon Location Maps sends the following events directly to EventBridge: 
+ AWS API Call via CloudTrail

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.geo-maps

```
{
  "source": ["aws.geo-maps"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.geo-maps"],
  "detail-type": ["{{AWS API Call via CloudTrail}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.