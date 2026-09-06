

# Amazon Connect Campaigns events
<a name="events-ref-connect-campaigns"></a>

Amazon Connect Campaigns sends service events to EventBridge via AWS CloudTrail.

## Amazon Connect Campaigns events delivered via AWS CloudTrail
<a name="event-ref-connect-campaigns-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Connect Campaigns to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.connect-campaigns
+ `eventSource`: connect-campaigns.amazonaws.com

```
{
  "source": ["aws.connect-campaigns"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["connect-campaigns.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.connect-campaigns"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["connect-campaigns.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```