# Amazon CloudWatch events

CloudWatch sends service events directly to EventBridge.

## CloudWatch service events

CloudWatch sends the following events directly to EventBridge:

- CloudWatch Alarm State Change
- CloudWatch Alarm Configuration Change
- CloudWatch Alarm Contributor State Change

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.cloudwatch

```
{
  "source": ["aws.cloudwatch"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.cloudwatch"],
  "detail-type": ["`CloudWatch Alarm State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
