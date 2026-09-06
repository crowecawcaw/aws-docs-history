

# Amazon Data Lifecycle Manager events
<a name="events-ref-dlm"></a>

Amazon Data Lifecycle Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Data Lifecycle Manager service events
<a name="events-ref-dlm-events"></a>

Amazon Data Lifecycle Manager sends the following events directly to EventBridge: 
+ DLM Policy State Change
+ DLM Pre Post Script Notification

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.dlm

```
{
  "source": ["aws.dlm"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.dlm"],
  "detail-type": ["{{DLM Policy State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Data Lifecycle Manager events delivered via AWS CloudTrail
<a name="event-ref-dlm-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Data Lifecycle Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.dlm
+ `eventSource`: dlm.amazonaws.com

```
{
  "source": ["aws.dlm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["dlm.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.dlm"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["dlm.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```