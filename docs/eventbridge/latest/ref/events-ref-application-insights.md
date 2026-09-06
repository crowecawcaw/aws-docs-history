

# Amazon CloudWatch Application Insights events
<a name="events-ref-application-insights"></a>

CloudWatch Application Insights sends service events to EventBridge via AWS CloudTrail.

## CloudWatch Application Insights events delivered via AWS CloudTrail
<a name="event-ref-application-insights-events-via-CT"></a>

AWS CloudTrail sends events originating from CloudWatch Application Insights to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.application-insights
+ `eventSource`: application-insights.amazonaws.com

```
{
  "source": ["aws.application-insights"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["application-insights.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.application-insights"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["application-insights.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```