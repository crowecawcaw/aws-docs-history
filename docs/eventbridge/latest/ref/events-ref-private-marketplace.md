# AWS Marketplace Private Marketplace events

AWS Marketplace Private Marketplace sends service events directly to EventBridge.

## AWS Marketplace Private Marketplace service events

AWS Marketplace Private Marketplace sends the following events directly to EventBridge:

- Product Request Created
- Product Request Approved
- Product Request Declined

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.private-marketplace

```
{
  "source": ["aws.private-marketplace"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.private-marketplace"],
  "detail-type": ["`Product Request Created`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
