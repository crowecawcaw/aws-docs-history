# AWS Artifact events

AWS Artifact sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Artifact service events

AWS Artifact sends the following events directly to EventBridge:

- AWS Artifact Document Update
- AWS Artifact Agreement Status Changed
- AWS Artifact Report Update
- AWS Artifact Agreement Update

_Delivery type_:
[Durable](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.artifact

```
{
  "source": ["aws.artifact"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.artifact"],
  "detail-type": ["`AWS Artifact Document Update`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Artifact events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Artifact to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.artifact
- `eventSource`: artifact.amazonaws.com

```
{
  "source": ["aws.artifact"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["artifact.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.artifact"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["artifact.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
