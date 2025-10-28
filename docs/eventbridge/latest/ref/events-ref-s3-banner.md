# Amazon Simple Storage Service Object Lambda events

Amazon S3 Object Lambda sends service events to EventBridge via AWS CloudTrail.

## Amazon S3 Object Lambda events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon S3 Object Lambda to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.s3-banner
- `eventSource`: s3-banner.amazonaws.com

```
{
  "source": ["aws.s3-banner"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-banner.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.s3-banner"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-banner.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
