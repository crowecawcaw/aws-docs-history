# AWS Elastic Disaster Recovery events

Elastic Disaster Recovery sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Elastic Disaster Recovery service events

Elastic Disaster Recovery sends the following events directly to EventBridge:

- DRS Source Server Launch Result
- DRS Source Server Data Replication Stalled Change
- DRS PIT Snapshot Taken
- DRS Recovery Instance Failback State Change
- DRS Source Network Protection Status Change
- DRS Source Network Recovery Result

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.drs

```
{
  "source": ["aws.drs"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.drs"],
  "detail-type": ["`DRS Source Server Launch Result`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Elastic Disaster Recovery events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Elastic Disaster Recovery to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.drs
- `eventSource`: drs.amazonaws.com

```
{
  "source": ["aws.drs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["drs.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.drs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["drs.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
