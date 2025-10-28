# Amazon Macie events

Macie sends service events directly to EventBridge.

## Macie service events

Macie sends the following events directly to EventBridge:

- Macie Finding

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.macie

```
{
  "source": ["aws.macie"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.macie"],
  "detail-type": ["`Macie Finding`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
