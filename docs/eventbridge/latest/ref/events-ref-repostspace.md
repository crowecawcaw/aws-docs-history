

# AWS re:Post Private events
<a name="events-ref-repostspace"></a>

re:Post Private sends service events to EventBridge via AWS CloudTrail.

## re:Post Private events delivered via AWS CloudTrail
<a name="event-ref-repostspace-events-via-CT"></a>

AWS CloudTrail sends events originating from re:Post Private to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.repostspace
+ `eventSource`: repostspace.amazonaws.com

```
{
  "source": ["aws.repostspace"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["repostspace.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.repostspace"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["repostspace.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```