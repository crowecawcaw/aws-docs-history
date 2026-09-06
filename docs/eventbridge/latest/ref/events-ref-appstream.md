

# Amazon AppStream events
<a name="events-ref-appstream"></a>

Amazon AppStream sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon AppStream service events
<a name="events-ref-appstream-events"></a>

Amazon AppStream sends the following events directly to EventBridge: 
+ AppStream Session Notification

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.appstream

```
{
  "source": ["aws.appstream"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.appstream"],
  "detail-type": ["{{AppStream Session Notification}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon AppStream events delivered via AWS CloudTrail
<a name="event-ref-appstream-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon AppStream to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.appstream
+ `eventSource`: appstream.amazonaws.com

```
{
  "source": ["aws.appstream"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["appstream.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.appstream"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["appstream.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```