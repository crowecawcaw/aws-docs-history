

# AWS Private CA Connector for Active Directory events
<a name="events-ref-pca-connector-ad"></a>

AWS Private CA Connector for Active Directory sends service events directly to EventBridge.

## AWS Private CA Connector for Active Directory service events
<a name="events-ref-pca-connector-ad-events"></a>

AWS Private CA Connector for Active Directory sends the following events directly to EventBridge: 
+ Certificate Enrollment Failed
+ Certificate Enrollment Succeeded
+ Certificate Policy Retrieval Failed
+ Certificate Policy Retrieval Succeeded
+ Certificate Policy/Enrollment Request Parsing Failed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.pca-connector-ad

```
{
  "source": ["aws.pca-connector-ad"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.pca-connector-ad"],
  "detail-type": ["{{Certificate Enrollment Failed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.