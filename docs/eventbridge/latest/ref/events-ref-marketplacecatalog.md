

# AWS Marketplace Catalog API events
<a name="events-ref-marketplacecatalog"></a>

AWS Marketplace Catalog API sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Marketplace Catalog API service events
<a name="events-ref-marketplacecatalog-events"></a>

AWS Marketplace Catalog API sends the following events directly to EventBridge: 
+ Offer Released
+ Change Set Succeeded
+ Change Set Failed
+ Change Set Cancelled
+ Products Security Report Created

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.marketplacecatalog

```
{
  "source": ["aws.marketplacecatalog"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.marketplacecatalog"],
  "detail-type": ["{{Offer Released}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Marketplace Catalog API events delivered via AWS CloudTrail
<a name="event-ref-marketplacecatalog-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Marketplace Catalog API to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.marketplacecatalog
+ `eventSource`: marketplacecatalog.amazonaws.com

```
{
  "source": ["aws.marketplacecatalog"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["marketplacecatalog.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.marketplacecatalog"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["marketplacecatalog.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```