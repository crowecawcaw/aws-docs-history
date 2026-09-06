

# Amazon CloudWatch Internet Monitor events
<a name="events-ref-internetmonitor"></a>

Internet Monitor sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Internet Monitor service events
<a name="events-ref-internetmonitor-events"></a>

Internet Monitor sends the following events directly to EventBridge: 
+ Health Event Created
+ Health Event Updated
+ Health Event Closed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.internetmonitor

```
{
  "source": ["aws.internetmonitor"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.internetmonitor"],
  "detail-type": ["{{Health Event Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Internet Monitor events delivered via AWS CloudTrail
<a name="event-ref-internetmonitor-events-via-CT"></a>

AWS CloudTrail sends events originating from Internet Monitor to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.internetmonitor
+ `eventSource`: internetmonitor.amazonaws.com

```
{
  "source": ["aws.internetmonitor"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["internetmonitor.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.internetmonitor"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["internetmonitor.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```