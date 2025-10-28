# AWS HealthLake events

HealthLake sends service events directly to EventBridge, as well as via AWS CloudTrail.

## HealthLake service events

HealthLake sends the following events directly to EventBridge:

- Import Job Submitted
- Import Job Queued
- Import Job In Progress
- Import Job Completed
- Import Job Completed With Errors
- Import Job Failed
- Export Job Submitted
- Export Job Queued
- Export Job In Progress
- Export Job Completed
- Export Job Completed With Errors
- Export Job Failed
- Data Store Creating
- Data Store Creation Failed
- Data Store Active
- Data Store Deleting
- Data Store Deleted

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.healthlake

```
{
  "source": ["aws.healthlake"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.healthlake"],
  "detail-type": ["`Import Job Submitted`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## HealthLake events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from HealthLake to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.healthlake
- `eventSource`: healthlake.amazonaws.com

```
{
  "source": ["aws.healthlake"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["healthlake.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.healthlake"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["healthlake.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
