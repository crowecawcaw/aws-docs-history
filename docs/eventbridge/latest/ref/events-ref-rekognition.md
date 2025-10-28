# Amazon Rekognition events

Amazon Rekognition sends service events to EventBridge via AWS CloudTrail.

## Amazon Rekognition events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon Rekognition to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.rekognition
- `eventSource`: rekognition.amazonaws.com

```
{
  "source": ["aws.rekognition"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rekognition.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.rekognition"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["rekognition.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
