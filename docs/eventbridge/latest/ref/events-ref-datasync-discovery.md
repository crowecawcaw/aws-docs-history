# AWS DataSync Discovery events

DataSync Discovery sends service events directly to EventBridge.

## DataSync Discovery service events

DataSync Discovery sends the following events directly to EventBridge:

- Discovery Job Expiration Soon
- Discovery Job State Change
- Storage System Connectivity Status Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.datasync-discovery

```
{
  "source": ["aws.datasync-discovery"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.datasync-discovery"],
  "detail-type": ["`Discovery Job Expiration Soon`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
