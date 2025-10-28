# AWS Proton events

AWS Proton sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Proton service events

AWS Proton sends the following events directly to EventBridge:

- AWS Proton Environment Status Change
- AWS Proton Environment Account Connection Status Change
- AWS Proton Environment Template Status Change
- AWS Proton Environment Template Version Status Change
- AWS Proton Service Status Change
- AWS Proton Service Instance Status Change
- AWS Proton Service Pipeline Status Change
- AWS Proton Service Template Status Change
- AWS Proton Service Template Version Status Change
- AWS Proton Component Status Change
- AWS Proton Deployment Status Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.proton

```
{
  "source": ["aws.proton"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.proton"],
  "detail-type": ["`AWS Proton Environment Status Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Proton events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Proton to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.proton
- `eventSource`: proton.amazonaws.com

```
{
  "source": ["aws.proton"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["proton.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.proton"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["proton.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
