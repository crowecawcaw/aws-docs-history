# Application Auto Scaling events

Application Auto Scaling sends service events directly to EventBridge.

## Application Auto Scaling service events

Application Auto Scaling sends the following events directly to EventBridge:

- Application Auto Scaling Scaling Activity State Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.application-autoscaling

```
{
  "source": ["aws.application-autoscaling"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.application-autoscaling"],
  "detail-type": ["`Application Auto Scaling Scaling Activity State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
