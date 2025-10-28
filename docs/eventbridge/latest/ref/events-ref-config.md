# AWS Config events

AWS Config sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Config service events

AWS Config sends the following events directly to EventBridge:

- Config Configuration Item Change
- Config Rules Compliance Change
- Config Configuration Snapshot Delivery Status
- Config Configuration History Delivery Status
- Config Rules Re-evaluation Status

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.config

```
{
  "source": ["aws.config"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.config"],
  "detail-type": ["`Config Configuration Item Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Config events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Config to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.config
- `eventSource`: config.amazonaws.com

```
{
  "source": ["aws.config"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["config.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.config"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["config.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
