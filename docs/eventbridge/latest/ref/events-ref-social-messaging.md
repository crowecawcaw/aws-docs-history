# AWS End User Messaging Social events

End User Messaging Social sends service events directly to EventBridge.

## End User Messaging Social service events

End User Messaging Social sends the following events directly to EventBridge:

- WhatsApp Message Sent
- WhatsApp Message Delivered
- WhatsApp Message Read
- WhatsApp Message Failed
- WhatsApp Message Undeliverable
- WhatsApp Message Received
- WhatsApp Unknown Notification Received
- WhatsApp Message Handover Succeeded
- WhatsApp Message Handover Failed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.social-messaging

```
{
  "source": ["aws.social-messaging"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.social-messaging"],
  "detail-type": ["`WhatsApp Message Sent`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
