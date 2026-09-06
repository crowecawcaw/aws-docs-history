

# AWS CodeBuild events
<a name="events-ref-codebuild"></a>

CodeBuild sends service events directly to EventBridge, as well as via AWS CloudTrail.

## CodeBuild service events
<a name="events-ref-codebuild-events"></a>

CodeBuild sends the following events directly to EventBridge: 
+ CodeBuild Build State Change
+ CodeBuild Build Phase Change
+ CodeBuild Fleet State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.codebuild

```
{
  "source": ["aws.codebuild"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.codebuild"],
  "detail-type": ["{{CodeBuild Build State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## CodeBuild events delivered via AWS CloudTrail
<a name="event-ref-codebuild-events-via-CT"></a>

AWS CloudTrail sends events originating from CodeBuild to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.codebuild
+ `eventSource`: codebuild.amazonaws.com

```
{
  "source": ["aws.codebuild"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codebuild.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.codebuild"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codebuild.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```