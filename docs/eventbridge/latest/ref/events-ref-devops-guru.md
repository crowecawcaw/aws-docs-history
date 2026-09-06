

# Amazon DevOps Guru events
<a name="events-ref-devops-guru"></a>

DevOps Guru sends service events directly to EventBridge, as well as via AWS CloudTrail.

## DevOps Guru service events
<a name="events-ref-devops-guru-events"></a>

DevOps Guru sends the following events directly to EventBridge: 
+ DevOps Guru New Insight Open
+ DevOps Guru New Anomaly Association
+ DevOps Guru Insight Severity Upgraded
+ DevOps Guru New Recommendation Created
+ DevOps Guru Insight Closed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.devops-guru

```
{
  "source": ["aws.devops-guru"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.devops-guru"],
  "detail-type": ["{{DevOps Guru New Insight Open}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## DevOps Guru events delivered via AWS CloudTrail
<a name="event-ref-devops-guru-events-via-CT"></a>

AWS CloudTrail sends events originating from DevOps Guru to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.devops-guru
+ `eventSource`: devops-guru.amazonaws.com

```
{
  "source": ["aws.devops-guru"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["devops-guru.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.devops-guru"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["devops-guru.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```