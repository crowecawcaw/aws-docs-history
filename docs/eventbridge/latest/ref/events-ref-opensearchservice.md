# Amazon OpenSearch Service events

OpenSearch Service sends service events to EventBridge via AWS CloudTrail.

## OpenSearch Service events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from OpenSearch Service to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.opensearchservice
- `eventSource`: opensearchservice.amazonaws.com

```
{
  "source": ["aws.opensearchservice"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["opensearchservice.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.opensearchservice"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["opensearchservice.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
