

# Amazon Location Service events
<a name="events-ref-geo"></a>

Amazon Location sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Location service events
<a name="events-ref-geo-events"></a>

Amazon Location sends the following events directly to EventBridge: 
+ Geofence Enter
+ Geofence Exit
+ Location Geofence Event
+ Location Device Position Event

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.geo

```
{
  "source": ["aws.geo"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.geo"],
  "detail-type": ["{{Geofence Enter}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Location events delivered via AWS CloudTrail
<a name="event-ref-geo-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Location to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.geo
+ `eventSource`: geo.amazonaws.com

```
{
  "source": ["aws.geo"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["geo.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.geo"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["geo.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```