# EC2 Image Builder events

Image Builder sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Image Builder service events

Image Builder sends the following events directly to EventBridge:

- EC2 Image Builder Image State Change
- EC2 Image Builder CVE Detected
- EC2 Image Builder Workflow Step Waiting
- EC2 Image Builder Image Pipeline Automatically Disabled

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.imagebuilder

```
{
  "source": ["aws.imagebuilder"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.imagebuilder"],
  "detail-type": ["`EC2 Image Builder Image State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Image Builder events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Image Builder to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.imagebuilder
- `eventSource`: imagebuilder.amazonaws.com

```
{
  "source": ["aws.imagebuilder"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["imagebuilder.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.imagebuilder"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["imagebuilder.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
