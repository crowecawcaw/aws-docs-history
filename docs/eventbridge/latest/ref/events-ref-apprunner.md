

# AWS App Runner events
<a name="events-ref-apprunner"></a>

App Runner sends service events directly to EventBridge, as well as via AWS CloudTrail.

## App Runner service events
<a name="events-ref-apprunner-events"></a>

App Runner sends the following events directly to EventBridge: 
+ AppRunner Service Operation Status Change
+ AppRunner Service Status Change
+ AppRunner Custom Domain Validation Status Update

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.apprunner

```
{
  "source": ["aws.apprunner"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.apprunner"],
  "detail-type": ["{{AppRunner Service Operation Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## App Runner events delivered via AWS CloudTrail
<a name="event-ref-apprunner-events-via-CT"></a>

AWS CloudTrail sends events originating from App Runner to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.apprunner
+ `eventSource`: apprunner.amazonaws.com

```
{
  "source": ["aws.apprunner"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["apprunner.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.apprunner"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["apprunner.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```