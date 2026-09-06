

# Amazon Route 53 Public Data Plane events
<a name="events-ref-route53"></a>

Route 53 Public Data Plane sends service events to EventBridge via AWS CloudTrail.

## Route 53 Public Data Plane events delivered via AWS CloudTrail
<a name="event-ref-route53-events-via-CT"></a>

AWS CloudTrail sends events originating from Route 53 Public Data Plane to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.route53
+ `eventSource`: route53.amazonaws.com

```
{
  "source": ["aws.route53"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["route53.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.route53"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["route53.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```