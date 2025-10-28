# Amazon Application Recovery Controller (ARC) Region switch events

ARC Region switch sends service events directly to EventBridge.

## ARC Region switch service events

ARC Region switch sends the following events directly to EventBridge:

- ARC Region Switch Plan Execution
- ARC Region Switch Plan Evaluation

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.arc-region-switch

```
{
  "source": ["aws.arc-region-switch"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.arc-region-switch"],
  "detail-type": ["`ARC Region Switch Plan Execution`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
