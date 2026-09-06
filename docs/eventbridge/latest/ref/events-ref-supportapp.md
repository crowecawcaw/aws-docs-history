

# AWS Support App in Slack events
<a name="events-ref-supportapp"></a>

AWS Support App sends service events to EventBridge via AWS CloudTrail.

## AWS Support App events delivered via AWS CloudTrail
<a name="event-ref-supportapp-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Support App to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.supportapp
+ `eventSource`: supportapp.amazonaws.com

```
{
  "source": ["aws.supportapp"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["supportapp.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.supportapp"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["supportapp.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```