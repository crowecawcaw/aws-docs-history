# Recycle Bin Service events

Recycle Bin Service sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Recycle Bin Service service events

Recycle Bin Service sends the following events directly to EventBridge:

- Recycle Bin Rule Locked
- Recycle Bin Rule Change Attempted
- Recycle Bin Rule Unlock Scheduled
- Recycle Bin Rule Unlocking Notice
- Recycle Bin Rule Unlocked

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.rbin

```
{
  "source": ["aws.rbin"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.rbin"],
  "detail-type": ["`Recycle Bin Rule Locked`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Recycle Bin Service events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Recycle Bin Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.rbin
- `eventSource`: rbin.amazonaws.com

```
{
  "source": ["aws.rbin"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rbin.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.rbin"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rbin.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
