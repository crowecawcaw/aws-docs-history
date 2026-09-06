

# Amazon CloudWatch Application Insights events
<a name="events-ref-applicationinsights"></a>

CloudWatch Application Insights sends service events directly to EventBridge.

## CloudWatch Application Insights service events
<a name="events-ref-applicationinsights-events"></a>

CloudWatch Application Insights sends the following events directly to EventBridge: 
+ Application Insights Problem Detected
+ Application Insights Problem Created
+ Application Insights Problem Updated

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.applicationinsights

```
{
  "source": ["aws.applicationinsights"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.applicationinsights"],
  "detail-type": ["{{Application Insights Problem Detected}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.