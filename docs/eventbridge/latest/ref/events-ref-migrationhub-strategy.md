

# AWS Migration Hub Strategy Recommendations events
<a name="events-ref-migrationhub-strategy"></a>

Strategy Recommendations sends service events to EventBridge via AWS CloudTrail.

## Strategy Recommendations events delivered via AWS CloudTrail
<a name="event-ref-migrationhub-strategy-events-via-CT"></a>

AWS CloudTrail sends events originating from Strategy Recommendations to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.migrationhub-strategy
+ `eventSource`: migrationhub-strategy.amazonaws.com

```
{
  "source": ["aws.migrationhub-strategy"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["migrationhub-strategy.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.migrationhub-strategy"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["migrationhub-strategy.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```