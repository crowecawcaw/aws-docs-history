# AWS Deadline Cloud events

Deadline Cloud sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Deadline Cloud service events

Deadline Cloud sends the following events directly to EventBridge:

- Fleet Size Recommendation Change
- Worker Status Unhealthy
- Budget Threshold Reached
- Job Lifecycle Status Change
- Job Run Status Change
- Step Lifecycle Status Change
- Step Run Status Change
- Task Run Status Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.deadline

```
{
  "source": ["aws.deadline"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.deadline"],
  "detail-type": ["`Fleet Size Recommendation Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Deadline Cloud events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Deadline Cloud to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.deadline
- `eventSource`: deadline.amazonaws.com

```
{
  "source": ["aws.deadline"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["deadline.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.deadline"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["deadline.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
