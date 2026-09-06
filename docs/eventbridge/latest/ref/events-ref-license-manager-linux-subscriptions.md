

# Linux subscriptions in AWS License Manager events
<a name="events-ref-license-manager-linux-subscriptions"></a>

Linux subscriptions in License Manager sends service events to EventBridge via AWS CloudTrail.

## Linux subscriptions in License Manager events delivered via AWS CloudTrail
<a name="event-ref-license-manager-linux-subscriptions-events-via-CT"></a>

AWS CloudTrail sends events originating from Linux subscriptions in License Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.license-manager-linux-subscriptions
+ `eventSource`: license-manager-linux-subscriptions.amazonaws.com

```
{
  "source": ["aws.license-manager-linux-subscriptions"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager-linux-subscriptions.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.license-manager-linux-subscriptions"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager-linux-subscriptions.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```