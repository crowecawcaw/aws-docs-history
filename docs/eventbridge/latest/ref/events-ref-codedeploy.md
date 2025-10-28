# AWS CodeDeploy events

CodeDeploy sends service events directly to EventBridge, as well as via AWS CloudTrail.

## CodeDeploy service events

CodeDeploy sends the following events directly to EventBridge:

- CodeDeploy Deployment State-change Notification
- CodeDeploy Instance State-change Notification

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.codedeploy

```
{
  "source": ["aws.codedeploy"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.codedeploy"],
  "detail-type": ["`CodeDeploy Deployment State-change Notification`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## CodeDeploy events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from CodeDeploy to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.codedeploy
- `eventSource`: codedeploy.amazonaws.com

```
{
  "source": ["aws.codedeploy"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codedeploy.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.codedeploy"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codedeploy.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
