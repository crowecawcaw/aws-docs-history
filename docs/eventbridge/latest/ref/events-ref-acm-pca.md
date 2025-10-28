# AWS Private Certificate Authority events

AWS Private CA sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Private CA service events

AWS Private CA sends the following events directly to EventBridge:

- ACM Private CA Creation
- ACM Private CA Certificate Issuance
- ACM Private CA CRL Generation
- ACM Private CA Audit Report Generation
- ACM Private CA Certificate Revocation

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.acm-pca

```
{
  "source": ["aws.acm-pca"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.acm-pca"],
  "detail-type": ["`ACM Private CA Creation`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Private CA events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Private CA to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.acm-pca
- `eventSource`: acm-pca.amazonaws.com

```
{
  "source": ["aws.acm-pca"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm-pca.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.acm-pca"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["acm-pca.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
