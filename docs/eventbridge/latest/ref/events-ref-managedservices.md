

# AWS Managed Services events
<a name="events-ref-managedservices"></a>

AMS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AMS service events
<a name="events-ref-managedservices-events"></a>

AMS sends the following events directly to EventBridge: 
+ AMS RFC State Change
+ AMS Patch Window Execution State Change
+ EKS Cluster Health State Change
+ EKS Node Health State Change
+ EKS Workload Health State Change
+ EKS Pod Health State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.managedservices

```
{
  "source": ["aws.managedservices"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.managedservices"],
  "detail-type": ["{{AMS RFC State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AMS events delivered via AWS CloudTrail
<a name="event-ref-managedservices-events-via-CT"></a>

AWS CloudTrail sends events originating from AMS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.managedservices
+ `eventSource`: managedservices.amazonaws.com

```
{
  "source": ["aws.managedservices"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["managedservices.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.managedservices"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["managedservices.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```