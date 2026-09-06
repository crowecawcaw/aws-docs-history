

# AWS WAFV2 events
<a name="events-ref-wafv2"></a>

AWS WAFV2 sends service events to EventBridge via AWS CloudTrail.

## AWS WAFV2 events delivered via AWS CloudTrail
<a name="event-ref-wafv2-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS WAFV2 to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.wafv2
+ `eventSource`: wafv2.amazonaws.com

```
{
  "source": ["aws.wafv2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["wafv2.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.wafv2"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["wafv2.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```