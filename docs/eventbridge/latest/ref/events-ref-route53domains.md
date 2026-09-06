

# Amazon Route 53 domain registration events
<a name="events-ref-route53domains"></a>

Route 53 domain registration sends service events to EventBridge via AWS CloudTrail.

## Route 53 domain registration events delivered via AWS CloudTrail
<a name="event-ref-route53domains-events-via-CT"></a>

AWS CloudTrail sends events originating from Route 53 domain registration to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.route53domains
+ `eventSource`: route53domains.amazonaws.com

```
{
  "source": ["aws.route53domains"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["route53domains.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.route53domains"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["route53domains.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```