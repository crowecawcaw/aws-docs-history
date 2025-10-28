# AWS Marketplace Catalog API events

AWS Marketplace Catalog API sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Marketplace Catalog API service events

AWS Marketplace Catalog API sends the following events directly to EventBridge:

- Offer Released
- Change Set Succeeded
- Change Set Failed
- Change Set Cancelled
- Products Security Report Created

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.marketplacecatalog

```
{
  "source": ["aws.marketplacecatalog"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.marketplacecatalog"],
  "detail-type": ["`Offer Released`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS Marketplace Catalog API events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS Marketplace Catalog API to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.marketplacecatalog
- `eventSource`: marketplacecatalog.amazonaws.com

```
{
  "source": ["aws.marketplacecatalog"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["marketplacecatalog.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.marketplacecatalog"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["marketplacecatalog.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
