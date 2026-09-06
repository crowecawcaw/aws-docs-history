

# AWS Marketplace Vendor Insights events
<a name="events-ref-vendor-insights"></a>

AWS Marketplace Vendor Insights sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Marketplace Vendor Insights service events
<a name="events-ref-vendor-insights-events"></a>

AWS Marketplace Vendor Insights sends the following events directly to EventBridge: 
+ Entitled Security Profile Snapshot Available

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.vendor-insights

```
{
  "source": ["aws.vendor-insights"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.vendor-insights"],
  "detail-type": ["{{Entitled Security Profile Snapshot Available}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Marketplace Vendor Insights events delivered via AWS CloudTrail
<a name="event-ref-vendor-insights-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Marketplace Vendor Insights to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.vendor-insights
+ `eventSource`: vendor-insights.amazonaws.com

```
{
  "source": ["aws.vendor-insights"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["vendor-insights.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.vendor-insights"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["vendor-insights.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```