

# Amazon Chime SDK Media Pipelines events
<a name="events-ref-chime-sdk-media-pipelines"></a>

Amazon Chime SDK Media Pipelines sends service events to EventBridge via AWS CloudTrail.

## Amazon Chime SDK Media Pipelines events delivered via AWS CloudTrail
<a name="event-ref-chime-sdk-media-pipelines-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Chime SDK Media Pipelines to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.chime-sdk-media-pipelines
+ `eventSource`: chime-sdk-media-pipelines.amazonaws.com

```
{
  "source": ["aws.chime-sdk-media-pipelines"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["chime-sdk-media-pipelines.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.chime-sdk-media-pipelines"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["chime-sdk-media-pipelines.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```