# Amazon EMR events

Amazon EMR sends service events directly to EventBridge.

## Amazon EMR service events

Amazon EMR sends the following events directly to EventBridge:

- EMR Auto Scaling Policy State Change
- EMR Step Status Change
- EMR Cluster State Change
- EMR Instance Group State Change
- EMR Instance Fleet State Change
- EMR Instance Group Status Notification
- EMR Instance Fleet Status Notification
- EMR Configuration Error
- EMR Application Health State Change
- EMR Managed Scaling Action
- EMR Instance Fleet Resize
- EMR Instance Group Resize
- EMR Instance Fleet Cluster Start
- EMR Instance Group Cluster Start
- EMR Unhealthy Node Replacement
- EMR Instance Fleet Provisioning
- EMR Instance Group Provisioning
- EMR Instance Fleet Termination
- EMR Instance Group Termination
- EMR Instance Fleet Update

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.emr

```
{
  "source": ["aws.emr"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.emr"],
  "detail-type": ["`EMR Auto Scaling Policy State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
