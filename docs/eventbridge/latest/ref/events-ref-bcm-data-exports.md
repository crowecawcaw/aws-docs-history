

# AWS Billing and Cost Management Data Exports events
<a name="events-ref-bcm-data-exports"></a>

Billing and Cost Management Data Exports sends service events to EventBridge via AWS CloudTrail.

## Billing and Cost Management Data Exports events delivered via AWS CloudTrail
<a name="event-ref-bcm-data-exports-events-via-CT"></a>

AWS CloudTrail sends events originating from Billing and Cost Management Data Exports to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.bcm-data-exports
+ `eventSource`: bcm-data-exports.amazonaws.com

```
{
  "source": ["aws.bcm-data-exports"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["bcm-data-exports.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.bcm-data-exports"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["bcm-data-exports.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```