# Amazon Managed Blockchain events

Managed Blockchain sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Managed Blockchain service events

Managed Blockchain sends the following events directly to EventBridge:

- Managed Blockchain Proposal Status Change
- Managed Blockchain Invitation Status Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.managedblockchain

```
{
  "source": ["aws.managedblockchain"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.managedblockchain"],
  "detail-type": ["`Managed Blockchain Proposal Status Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Managed Blockchain events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Managed Blockchain to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.managedblockchain
- `eventSource`: managedblockchain.amazonaws.com

```
{
  "source": ["aws.managedblockchain"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["managedblockchain.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.managedblockchain"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["managedblockchain.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
