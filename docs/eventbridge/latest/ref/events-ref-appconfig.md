

# AWS AppConfig events
<a name="events-ref-appconfig"></a>

AWS AppConfig sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS AppConfig service events
<a name="events-ref-appconfig-events"></a>

AWS AppConfig sends the following events directly to EventBridge: 
+ On Deployment Start
+ On Deployment Rollback
+ On Deployment Complete
+ On Deployment Step
+ On Deployment Baking

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.appconfig

```
{
  "source": ["aws.appconfig"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.appconfig"],
  "detail-type": ["{{On Deployment Start}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS AppConfig events delivered via AWS CloudTrail
<a name="event-ref-appconfig-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS AppConfig to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.appconfig
+ `eventSource`: appconfig.amazonaws.com

```
{
  "source": ["aws.appconfig"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["appconfig.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.appconfig"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["appconfig.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```