# Amazon Interactive Video Service events

Amazon IVS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon IVS service events

Amazon IVS sends the following events directly to EventBridge:

- IVS Stream State Change
- IVS Stream Health Change
- IVS Limit Breach
- IVS Recording State Change
- IVS Stage Update
- IVS Composition State Change
- IVS Publisher Recording State Change
- IVS Participant Recording State Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.ivs

```
{
  "source": ["aws.ivs"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.ivs"],
  "detail-type": ["`IVS Stream State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon IVS events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon IVS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.ivs
- `eventSource`: ivs.amazonaws.com

```
{
  "source": ["aws.ivs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ivs.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ivs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ivs.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
