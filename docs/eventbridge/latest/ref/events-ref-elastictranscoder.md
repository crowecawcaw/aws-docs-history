

# Amazon Elastic Transcoder events
<a name="events-ref-elastictranscoder"></a>

Elastic Transcoder sends service events to EventBridge via AWS CloudTrail.

## Elastic Transcoder events delivered via AWS CloudTrail
<a name="event-ref-elastictranscoder-events-via-CT"></a>

AWS CloudTrail sends events originating from Elastic Transcoder to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.elastictranscoder
+ `eventSource`: elastictranscoder.amazonaws.com

```
{
  "source": ["aws.elastictranscoder"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["elastictranscoder.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.elastictranscoder"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["elastictranscoder.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```