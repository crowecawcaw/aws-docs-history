# AWS HealthImaging events

HealthImaging sends service events directly to EventBridge, as well as via AWS CloudTrail.

## HealthImaging service events

HealthImaging sends the following events directly to EventBridge:

- Data Store Creating
- Data Store Created
- Data Store Creation Failed
- Data Store Deleting
- Data Store Deleted
- Import Job Submitted
- Import Job In Progress
- Import Job Completed
- Import Job Failed
- Image Set Created
- Image Set Copying
- Image Set Copying With Read Only Access
- Image Set Copied
- Image Set Copy Failed
- Image Set Updating
- Image Set Updated
- Image Set Update Failed
- Image Set Deleting
- Image Set Deleted

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.medical-imaging

```
{
  "source": ["aws.medical-imaging"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.medical-imaging"],
  "detail-type": ["`Data Store Creating`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## HealthImaging events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from HealthImaging to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.medical-imaging
- `eventSource`: medical-imaging.amazonaws.com

```
{
  "source": ["aws.medical-imaging"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["medical-imaging.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.medical-imaging"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["medical-imaging.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
