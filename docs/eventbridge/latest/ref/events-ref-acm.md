# AWS Certificate Manager events

ACM sends service events directly to EventBridge, as well as via AWS CloudTrail.

## ACM service events

ACM sends the following events directly to EventBridge:

- ACM Certificate Approaching Expiration
- ACM Certificate Renewal Action Required
- ACM Certificate Expired
- ACM Certificate Available
- ACM Certificate Rotated
- ACM Certificate Revoked

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.acm

```
{
  "source": ["aws.acm"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.acm"],
  "detail-type": ["`ACM Certificate Approaching Expiration`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## ACM events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from ACM to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.acm
- `eventSource`: acm.amazonaws.com

```
{
  "source": ["aws.acm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.acm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
