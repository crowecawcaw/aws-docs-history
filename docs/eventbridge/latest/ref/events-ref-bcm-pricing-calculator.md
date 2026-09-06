

# AWS Pricing Calculator events
<a name="events-ref-bcm-pricing-calculator"></a>

AWS Pricing Calculator sends service events directly to EventBridge.

## AWS Pricing Calculator service events
<a name="events-ref-bcm-pricing-calculator-events"></a>

AWS Pricing Calculator sends the following events directly to EventBridge: 
+ BillEstimate Created
+ BillEstimate Succeeded
+ BillEstimate Failed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.bcm-pricing-calculator

```
{
  "source": ["aws.bcm-pricing-calculator"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.bcm-pricing-calculator"],
  "detail-type": ["{{BillEstimate Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.