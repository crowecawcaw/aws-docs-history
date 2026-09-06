

# Amazon EC2 Auto Scaling events
<a name="events-ref-autoscaling"></a>

Auto Scaling sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Auto Scaling service events
<a name="events-ref-autoscaling-events"></a>

Auto Scaling sends the following events directly to EventBridge: 
+ EC2 Instance Launch Successful
+ EC2 Instance Launch Unsuccessful
+ EC2 Instance Terminate Successful
+ EC2 Instance Terminate Unsuccessful
+ EC2 Instance Detach Successful
+ EC2 Instance Detach Unsuccessful
+ EC2 Instance-launch Lifecycle Action
+ EC2 Instance-terminate Lifecycle Action
+ EC2 Auto Scaling Instance Refresh Checkpoint Reached
+ EC2 Auto Scaling Instance Refresh Started
+ EC2 Auto Scaling Instance Refresh Succeeded
+ EC2 Auto Scaling Instance Refresh Failed
+ EC2 Auto Scaling Instance Refresh Cancelled
+ EC2 Auto Scaling Instance Refresh Rollback Started
+ EC2 Auto Scaling Instance Refresh Rollback Succeeded
+ EC2 Auto Scaling Instance Refresh Rollback Failed
+ EC2 Auto Scaling Instance Refresh Started Baking

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.autoscaling

```
{
  "source": ["aws.autoscaling"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.autoscaling"],
  "detail-type": ["{{EC2 Instance Launch Successful}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Auto Scaling events delivered via AWS CloudTrail
<a name="event-ref-autoscaling-events-via-CT"></a>

AWS CloudTrail sends events originating from Auto Scaling to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.autoscaling
+ `eventSource`: autoscaling.amazonaws.com

```
{
  "source": ["aws.autoscaling"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["autoscaling.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.autoscaling"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["autoscaling.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```