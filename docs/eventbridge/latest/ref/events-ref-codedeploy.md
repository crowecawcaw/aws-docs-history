

# AWS CodeDeploy events
<a name="events-ref-codedeploy"></a>

CodeDeploy sends service events directly to EventBridge, as well as via AWS CloudTrail.

## CodeDeploy service events
<a name="events-ref-codedeploy-events"></a>

CodeDeploy sends the following events directly to EventBridge: 
+ CodeDeploy Deployment State-change Notification
+ CodeDeploy Instance State-change Notification

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.codedeploy

```
{
  "source": ["aws.codedeploy"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.codedeploy"],
  "detail-type": ["{{CodeDeploy Deployment State-change Notification}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## CodeDeploy events delivered via AWS CloudTrail
<a name="event-ref-codedeploy-events-via-CT"></a>

AWS CloudTrail sends events originating from CodeDeploy to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.codedeploy
+ `eventSource`: codedeploy.amazonaws.com

```
{
  "source": ["aws.codedeploy"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codedeploy.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.codedeploy"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codedeploy.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```