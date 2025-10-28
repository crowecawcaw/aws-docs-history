# AWS Audit Manager events

Audit Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Audit Manager service events

Audit Manager sends the following events directly to EventBridge:

- Assessment Created
- Assessment Updated
- Assessment Deleted
- Assessment ControlSet Delegation Created
- Assessment ControlSet Under Review
- Assessment ControlSet Reviewed
- Assessment Control Reviewed
- Daily Assessment Evidence Collected
- Assessment Report Created
- Assessment Report Failed
- Custom Framework Created
- Custom Framework Updated
- Custom Framework Deleted
- Framework Share Created
- Framework Share Accepted
- Framework Share Declined
- Framework Share Revoked
- Framework Share Expired
- Custom Control Created
- Custom Control Updated
- Custom Control Deleted

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.auditmanager

```
{
  "source": ["aws.auditmanager"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.auditmanager"],
  "detail-type": ["`Assessment Created`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Audit Manager events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Audit Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.auditmanager
- `eventSource`: auditmanager.amazonaws.com

```
{
  "source": ["aws.auditmanager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["auditmanager.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.auditmanager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["auditmanager.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
