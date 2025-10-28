# AWS Backup events

AWS Backup sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Backup service events

AWS Backup sends the following events directly to EventBridge:

- Backup Vault State Change
- Backup Plan State Change
- Backup Job State Change
- Copy Job State Change
- Restore Job State Change
- Recovery Point Change
- Recovery Point State Change
- Region Setting State Change
- Recovery Point Index State Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.backup

```
{
  "source": ["aws.backup"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.backup"],
  "detail-type": ["`Backup Vault State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Backup events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Backup to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.backup
- `eventSource`: backup.amazonaws.com

```
{
  "source": ["aws.backup"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["backup.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.backup"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["backup.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
