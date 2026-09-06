

# Amazon Application Recovery Controller (ARC) Region switch events
<a name="events-ref-arc-region-switch"></a>

ARC Region switch sends service events directly to EventBridge.

## ARC Region switch service events
<a name="events-ref-arc-region-switch-events"></a>

ARC Region switch sends the following events directly to EventBridge: 
+ ARC Region Switch Plan Execution
+ ARC Region Switch Plan Evaluation

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.arc-region-switch

```
{
  "source": ["aws.arc-region-switch"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.arc-region-switch"],
  "detail-type": ["{{ARC Region Switch Plan Execution}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.