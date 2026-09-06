

# AWS Mainframe Modernization events
<a name="events-ref-m2"></a>

AWS Mainframe Modernization sends service events to EventBridge via AWS CloudTrail.

## AWS Mainframe Modernization events delivered via AWS CloudTrail
<a name="event-ref-m2-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Mainframe Modernization to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.m2
+ `eventSource`: m2.amazonaws.com

```
{
  "source": ["aws.m2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["m2.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.m2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["m2.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```