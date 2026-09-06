

# AWS Elastic Beanstalk events
<a name="events-ref-elasticbeanstalk"></a>

Elastic Beanstalk sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Elastic Beanstalk service events
<a name="events-ref-elasticbeanstalk-events"></a>

Elastic Beanstalk sends the following events directly to EventBridge: 
+ Elastic Beanstalk resource status change
+ Other resource status change
+ Health status change
+ Managed update status change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.elasticbeanstalk

```
{
  "source": ["aws.elasticbeanstalk"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.elasticbeanstalk"],
  "detail-type": ["{{Elastic Beanstalk resource status change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Elastic Beanstalk events delivered via AWS CloudTrail
<a name="event-ref-elasticbeanstalk-events-via-CT"></a>

AWS CloudTrail sends events originating from Elastic Beanstalk to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.elasticbeanstalk
+ `eventSource`: elasticbeanstalk.amazonaws.com

```
{
  "source": ["aws.elasticbeanstalk"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["elasticbeanstalk.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.elasticbeanstalk"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["elasticbeanstalk.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```