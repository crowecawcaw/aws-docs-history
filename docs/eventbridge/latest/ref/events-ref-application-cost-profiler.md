

# AWS Application Cost Profiler events
<a name="events-ref-application-cost-profiler"></a>

Application Cost Profiler sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Application Cost Profiler service events
<a name="events-ref-application-cost-profiler-events"></a>

Application Cost Profiler sends the following events directly to EventBridge: 
+ Application Cost Profiler Report Generated
+ Application Cost Profiler Report Generation Failure
+ Application Cost Profiler Report Delivery Failure
+ Application Cost Profiler Ingestion Data Access Failure
+ Application Cost Profiler Ingestion Data Validation Failure

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.application-cost-profiler

```
{
  "source": ["aws.application-cost-profiler"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.application-cost-profiler"],
  "detail-type": ["{{Application Cost Profiler Report Generated}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Application Cost Profiler events delivered via AWS CloudTrail
<a name="event-ref-application-cost-profiler-events-via-CT"></a>

AWS CloudTrail sends events originating from Application Cost Profiler to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.application-cost-profiler
+ `eventSource`: application-cost-profiler.amazonaws.com

```
{
  "source": ["aws.application-cost-profiler"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["application-cost-profiler.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.application-cost-profiler"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["application-cost-profiler.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```