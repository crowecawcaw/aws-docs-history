# AWS Partner Central Selling events

Partner Central Selling sends service events directly to EventBridge.

## Partner Central Selling service events

Partner Central Selling sends the following events directly to EventBridge:

- Opportunity Created
- Opportunity Updated
- Opportunity Accepted
- Opportunity Rejected
- Engagement Invitation Created
- Engagement Invitation Accepted
- Engagement Invitation Rejected
- Engagement Invitation Expired
- Engagement Member Joined
- Resource Snapshot Created
- Engagement Member Added
- Engagement Resource Snapshot Created

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.partnercentral-selling

```
{
  "source": ["aws.partnercentral-selling"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.partnercentral-selling"],
  "detail-type": ["`Opportunity Created`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
