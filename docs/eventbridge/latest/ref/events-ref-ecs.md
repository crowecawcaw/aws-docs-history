

# Amazon Elastic Container Service events
<a name="events-ref-ecs"></a>

Amazon ECS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon ECS service events
<a name="events-ref-ecs-events"></a>

Amazon ECS sends the following events directly to EventBridge: 
+ ECS Container Instance State Change
+ ECS Task State Change
+ ECS Service Action
+ ECS Deployment State Change

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.ecs

```
{
  "source": ["aws.ecs"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.ecs"],
  "detail-type": ["{{ECS Container Instance State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon ECS events delivered via AWS CloudTrail
<a name="event-ref-ecs-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon ECS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.ecs
+ `eventSource`: ecs.amazonaws.com

```
{
  "source": ["aws.ecs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ecs.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ecs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ecs.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```