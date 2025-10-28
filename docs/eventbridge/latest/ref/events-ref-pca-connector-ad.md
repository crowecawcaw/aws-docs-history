# AWS Private CA Connector for Active Directory events

AWS Private CA Connector for Active Directory sends service events directly to EventBridge.

## AWS Private CA Connector for Active Directory service events

AWS Private CA Connector for Active Directory sends the following events directly to EventBridge:

- Certificate Enrollment Failed
- Certificate Enrollment Succeeded
- Certificate Policy Retrieval Failed
- Certificate Policy Retrieval Succeeded
- Certificate Policy/Enrollment Request Parsing Failed

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.pca-connector-ad

```
{
  "source": ["aws.pca-connector-ad"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.pca-connector-ad"],
  "detail-type": ["`Certificate Enrollment Failed`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
