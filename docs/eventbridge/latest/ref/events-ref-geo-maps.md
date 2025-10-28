# Amazon Location Service Maps events

Amazon Location Maps sends service events directly to EventBridge.

## Amazon Location Maps service events

Amazon Location Maps sends the following events directly to EventBridge:

- AWS API Call via CloudTrail

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.geo-maps

```
{
  "source": ["aws.geo-maps"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.geo-maps"],
  "detail-type": ["`AWS API Call via CloudTrail`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
