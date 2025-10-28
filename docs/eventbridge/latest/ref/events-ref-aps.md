# Amazon Managed Service for Prometheus events

Amazon Managed Service for Prometheus sends service events to EventBridge via AWS CloudTrail.

## Amazon Managed Service for Prometheus events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon Managed Service for Prometheus to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.aps
- `eventSource`: aps.amazonaws.com

```
{
  "source": ["aws.aps"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["aps.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.aps"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["aps.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
