

# AWS Security Hub CSPM events
<a name="events-ref-securityhub"></a>

Security Hub CSPM sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Security Hub CSPM service events
<a name="events-ref-securityhub-events"></a>

Security Hub CSPM sends the following events directly to EventBridge: 
+ Security Hub Insight Results
+ Security Hub Standard Results
+ Security Hub Findings
+ Security Hub Findings - Custom Action
+ Security Hub Findings - Imported
+ Findings Imported V2

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.securityhub

```
{
  "source": ["aws.securityhub"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.securityhub"],
  "detail-type": ["{{Security Hub Insight Results}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Security Hub CSPM events delivered via AWS CloudTrail
<a name="event-ref-securityhub-events-via-CT"></a>

AWS CloudTrail sends events originating from Security Hub CSPM to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.securityhub
+ `eventSource`: securityhub.amazonaws.com

```
{
  "source": ["aws.securityhub"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["securityhub.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.securityhub"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["securityhub.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```