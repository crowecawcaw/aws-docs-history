# Network Access Analyzer events

Network Access Analyzer sends service events directly to EventBridge.

## Network Access Analyzer service events

Network Access Analyzer sends the following events directly to EventBridge:

- Analysis Completed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.networkaccessanalyzer

```
{
  "source": ["aws.networkaccessanalyzer"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.networkaccessanalyzer"],
  "detail-type": ["`Analysis Completed`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
