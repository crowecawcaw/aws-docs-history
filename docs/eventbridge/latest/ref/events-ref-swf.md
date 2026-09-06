

# Amazon Simple Workflow Service events
<a name="events-ref-swf"></a>

Amazon SWF sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon SWF service events
<a name="events-ref-swf-events"></a>

Amazon SWF sends the following events directly to EventBridge: 
+ Simple Workflow Execution State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.swf

```
{
  "source": ["aws.swf"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.swf"],
  "detail-type": ["{{Simple Workflow Execution State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon SWF events delivered via AWS CloudTrail
<a name="event-ref-swf-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon SWF to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.swf
+ `eventSource`: swf.amazonaws.com

```
{
  "source": ["aws.swf"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["swf.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.swf"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["swf.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```