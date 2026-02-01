# AWS ARC - Zonal Shift events

AWS ARC - Zonal Shift sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS ARC - Zonal Shift service events

AWS ARC - Zonal Shift sends the following events directly to EventBridge:

- Practice Run Started
- Practice Run Interrupted
- Practice Run Failed
- Practice Run Succeeded
- Autoshift In Progress
- Autoshift Completed
- FIS Experiment Autoshift In Progress
- FIS Experiment Autoshift Completed
- FIS Experiment Autoshift Canceled
- Manual Shift Started
- Manual Shift Updated
- Manual Shift Canceled

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.arc-zonal-shift

```
{
  "source": ["aws.arc-zonal-shift"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.arc-zonal-shift"],
  "detail-type": ["`Practice Run Started`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS ARC - Zonal Shift events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS ARC - Zonal Shift to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.arc-zonal-shift
- `eventSource`: arc-zonal-shift.amazonaws.com

```
{
  "source": ["aws.arc-zonal-shift"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["arc-zonal-shift.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.arc-zonal-shift"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["arc-zonal-shift.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
