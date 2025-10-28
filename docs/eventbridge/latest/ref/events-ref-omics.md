# AWS HealthOmics events

HealthOmics sends service events directly to EventBridge, as well as via AWS CloudTrail.

## HealthOmics service events

HealthOmics sends the following events directly to EventBridge:

- Reference Store Status Change
- Reference Status Change
- Reference Import Job Status Change
- Sequence Store Status Change
- Read Set Status Change
- Read Set Import Job Status Change
- Read Set Export Job Status Change
- Read Set Activation Job Status Change
- Workflow Status Change
- RunGroup Status Change
- Run Status Change
- Task Status Change
- Variant Import Job Status Change
- Annotation Import Job Status Change
- Variant Store Status Change
- Annotation Store Status Change
- Variant Store Share Status Change
- Annotation Store Share Status Change
- Workflow Share Status Change
- S3 Access Policy Status Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.omics

```
{
  "source": ["aws.omics"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.omics"],
  "detail-type": ["`Reference Store Status Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## HealthOmics events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from HealthOmics to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.omics
- `eventSource`: omics.amazonaws.com

```
{
  "source": ["aws.omics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["omics.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.omics"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["omics.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
