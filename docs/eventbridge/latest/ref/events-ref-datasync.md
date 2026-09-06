

# AWS DataSync events
<a name="events-ref-datasync"></a>

DataSync sends service events directly to EventBridge, as well as via AWS CloudTrail.

## DataSync service events
<a name="events-ref-datasync-events"></a>

DataSync sends the following events directly to EventBridge: 
+ DataSync Agent State Change
+ DataSync Task State Change
+ DataSync Task Execution State Change
+ DataSync Location State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.datasync

```
{
  "source": ["aws.datasync"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.datasync"],
  "detail-type": ["{{DataSync Agent State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## DataSync events delivered via AWS CloudTrail
<a name="event-ref-datasync-events-via-CT"></a>

AWS CloudTrail sends events originating from DataSync to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.datasync
+ `eventSource`: datasync.amazonaws.com

```
{
  "source": ["aws.datasync"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["datasync.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.datasync"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["datasync.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```