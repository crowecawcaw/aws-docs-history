

# Amazon Simple Storage Service Object Lambda events
<a name="events-ref-s3-banner"></a>

Amazon S3 Object Lambda sends service events to EventBridge via AWS CloudTrail.

## Amazon S3 Object Lambda events delivered via AWS CloudTrail
<a name="event-ref-s3-banner-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon S3 Object Lambda to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.s3-banner
+ `eventSource`: s3-banner.amazonaws.com

```
{
  "source": ["aws.s3-banner"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-banner.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.s3-banner"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["s3-banner.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```