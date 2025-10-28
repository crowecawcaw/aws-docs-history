# Amazon GuardDuty events

GuardDuty sends service events directly to EventBridge, as well as via AWS CloudTrail.

## GuardDuty service events

GuardDuty sends the following events directly to EventBridge:

- GuardDuty Finding
- GuardDuty Runtime Protection Healthy
- GuardDuty Runtime Protection Unhealthy
- GuardDuty Malware Protection Object Scan Result
- GuardDuty Malware Protection Resource Status Active
- GuardDuty Malware Protection Resource Status Warning
- GuardDuty Malware Protection Resource Status Error
- GuardDuty Malware Protection Post Scan Action Failed

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.guardduty

```
{
  "source": ["aws.guardduty"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.guardduty"],
  "detail-type": ["`GuardDuty Finding`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## GuardDuty events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from GuardDuty to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.guardduty
- `eventSource`: guardduty.amazonaws.com

```
{
  "source": ["aws.guardduty"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["guardduty.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.guardduty"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["guardduty.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
