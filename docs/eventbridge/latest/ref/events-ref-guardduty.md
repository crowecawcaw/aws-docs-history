

# Amazon GuardDuty events
<a name="events-ref-guardduty"></a>

GuardDuty sends service events directly to EventBridge, as well as via AWS CloudTrail.

## GuardDuty service events
<a name="events-ref-guardduty-events"></a>

GuardDuty sends the following events directly to EventBridge: 
+ GuardDuty Finding
+ GuardDuty Runtime Protection Healthy
+ GuardDuty Runtime Protection Unhealthy
+ GuardDuty Malware Protection Object Scan Result
+ GuardDuty Malware Protection Resource Status Active
+ GuardDuty Malware Protection Resource Status Warning
+ GuardDuty Malware Protection Resource Status Error
+ GuardDuty Malware Protection Post Scan Action Failed

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.guardduty

```
{
  "source": ["aws.guardduty"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.guardduty"],
  "detail-type": ["{{GuardDuty Finding}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## GuardDuty events delivered via AWS CloudTrail
<a name="event-ref-guardduty-events-via-CT"></a>

AWS CloudTrail sends events originating from GuardDuty to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.guardduty
+ `eventSource`: guardduty.amazonaws.com

```
{
  "source": ["aws.guardduty"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["guardduty.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.guardduty"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["guardduty.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```