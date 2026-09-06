

# Multi-party approval events
<a name="events-ref-multi-party-approval"></a>

Multi-party approval sends service events to EventBridge via AWS CloudTrail.

## Multi-party approval events delivered via AWS CloudTrail
<a name="event-ref-multi-party-approval-events-via-CT"></a>

AWS CloudTrail sends events originating from Multi-party approval to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.multi-party-approval
+ `eventSource`: multi-party-approval.amazonaws.com

```
{
  "source": ["aws.multi-party-approval"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["multi-party-approval.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.multi-party-approval"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["multi-party-approval.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```