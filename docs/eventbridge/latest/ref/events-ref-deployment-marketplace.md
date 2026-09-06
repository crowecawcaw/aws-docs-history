

# AWS Marketplace Deployment Services events
<a name="events-ref-deployment-marketplace"></a>

AWS Marketplace Deployment Services sends service events to EventBridge via AWS CloudTrail.

## AWS Marketplace Deployment Services events delivered via AWS CloudTrail
<a name="event-ref-deployment-marketplace-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Marketplace Deployment Services to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.deployment-marketplace
+ `eventSource`: deployment-marketplace.amazonaws.com

```
{
  "source": ["aws.deployment-marketplace"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["deployment-marketplace.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.deployment-marketplace"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["deployment-marketplace.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```