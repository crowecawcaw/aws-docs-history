

# Amazon CodeGuru Profiler events
<a name="events-ref-codeguru-profiler"></a>

CodeGuru Profiler sends service events directly to EventBridge, as well as via AWS CloudTrail.

## CodeGuru Profiler service events
<a name="events-ref-codeguru-profiler-events"></a>

CodeGuru Profiler sends the following events directly to EventBridge: 
+ CodeGuru Profiler Recommendations State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.codeguru-profiler

```
{
  "source": ["aws.codeguru-profiler"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.codeguru-profiler"],
  "detail-type": ["{{CodeGuru Profiler Recommendations State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## CodeGuru Profiler events delivered via AWS CloudTrail
<a name="event-ref-codeguru-profiler-events-via-CT"></a>

AWS CloudTrail sends events originating from CodeGuru Profiler to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.codeguru-profiler
+ `eventSource`: codeguru-profiler.amazonaws.com

```
{
  "source": ["aws.codeguru-profiler"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codeguru-profiler.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.codeguru-profiler"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codeguru-profiler.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```