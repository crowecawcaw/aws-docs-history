# AWS Elemental MediaConnect events

MediaConnect sends service events directly to EventBridge, as well as via AWS CloudTrail.

## MediaConnect service events

MediaConnect sends the following events directly to EventBridge:

- MediaConnect Alert
- MediaConnect Source Health
- MediaConnect Output Health
- MediaConnect Flow Status Change
- MediaConnect Flow Maintenance
- MediaConnect Flow Health
- MediaConnect Output Status Change
- MediaConnect Flow Content Quality

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.mediaconnect

```
{
  "source": ["aws.mediaconnect"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.mediaconnect"],
  "detail-type": ["`MediaConnect Alert`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## MediaConnect events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from MediaConnect to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.mediaconnect
- `eventSource`: mediaconnect.amazonaws.com

```
{
  "source": ["aws.mediaconnect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediaconnect.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.mediaconnect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["mediaconnect.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
