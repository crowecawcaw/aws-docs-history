

# AWS Parallel Computing Service events
<a name="events-ref-pcs"></a>

AWS PCS sends service events to EventBridge via AWS CloudTrail.

## AWS PCS events delivered via AWS CloudTrail
<a name="event-ref-pcs-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS PCS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.pcs
+ `eventSource`: pcs.amazonaws.com

```
{
  "source": ["aws.pcs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["pcs.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.pcs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["pcs.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```