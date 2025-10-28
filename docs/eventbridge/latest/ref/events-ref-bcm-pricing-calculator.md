# AWS Pricing Calculator events

AWS Pricing Calculator sends service events directly to EventBridge.

## AWS Pricing Calculator service events

AWS Pricing Calculator sends the following events directly to EventBridge:

- BillEstimate Created
- BillEstimate Succeeded
- BillEstimate Failed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.bcm-pricing-calculator

```
{
  "source": ["aws.bcm-pricing-calculator"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.bcm-pricing-calculator"],
  "detail-type": ["`BillEstimate Created`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
