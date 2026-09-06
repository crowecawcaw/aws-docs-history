

# AWS Security Token Service events
<a name="events-ref-sts"></a>

AWS STS sends service events to EventBridge via AWS CloudTrail.

## AWS STS events delivered via AWS CloudTrail
<a name="event-ref-sts-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS STS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.sts
+ `eventSource`: sts.amazonaws.com

```
{
  "source": ["aws.sts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sts.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.sts"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sts.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```