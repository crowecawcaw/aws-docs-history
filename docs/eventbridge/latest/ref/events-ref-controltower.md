# AWS Control Tower events

AWS Control Tower sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Control Tower service events

AWS Control Tower sends the following events directly to EventBridge:

- Drift Detected

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.controltower

```
{
  "source": ["aws.controltower"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.controltower"],
  "detail-type": ["`Drift Detected`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Control Tower events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Control Tower to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.controltower
- `eventSource`: controltower.amazonaws.com

```
{
  "source": ["aws.controltower"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["controltower.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.controltower"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["controltower.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
