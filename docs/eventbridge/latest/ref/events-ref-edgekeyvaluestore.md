

# Amazon CloudFront KeyValueStore events
<a name="events-ref-edgekeyvaluestore"></a>

CloudFront KeyValueStore sends service events to EventBridge via AWS CloudTrail.

## CloudFront KeyValueStore events delivered via AWS CloudTrail
<a name="event-ref-edgekeyvaluestore-events-via-CT"></a>

AWS CloudTrail sends events originating from CloudFront KeyValueStore to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.edgekeyvaluestore
+ `eventSource`: edgekeyvaluestore.amazonaws.com

```
{
  "source": ["aws.edgekeyvaluestore"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["edgekeyvaluestore.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.edgekeyvaluestore"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["edgekeyvaluestore.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```