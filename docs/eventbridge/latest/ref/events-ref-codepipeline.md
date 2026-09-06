

# AWS CodePipeline events
<a name="events-ref-codepipeline"></a>

CodePipeline sends service events directly to EventBridge, as well as via AWS CloudTrail.

## CodePipeline service events
<a name="events-ref-codepipeline-events"></a>

CodePipeline sends the following events directly to EventBridge: 
+ CodePipeline Pipeline Execution State Change
+ CodePipeline Stage Execution State Change
+ CodePipeline Action Execution State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.codepipeline

```
{
  "source": ["aws.codepipeline"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.codepipeline"],
  "detail-type": ["{{CodePipeline Pipeline Execution State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## CodePipeline events delivered via AWS CloudTrail
<a name="event-ref-codepipeline-events-via-CT"></a>

AWS CloudTrail sends events originating from CodePipeline to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.codepipeline
+ `eventSource`: codepipeline.amazonaws.com

```
{
  "source": ["aws.codepipeline"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codepipeline.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.codepipeline"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codepipeline.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```