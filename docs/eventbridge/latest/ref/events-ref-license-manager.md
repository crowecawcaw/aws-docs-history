

# AWS License Manager events
<a name="events-ref-license-manager"></a>

License Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## License Manager service events
<a name="events-ref-license-manager-events"></a>

License Manager sends the following events directly to EventBridge: 
+ Grant Change
+ License Change
+ License Consumption Change
+ License Token Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.license-manager

```
{
  "source": ["aws.license-manager"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.license-manager"],
  "detail-type": ["{{Grant Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## License Manager events delivered via AWS CloudTrail
<a name="event-ref-license-manager-events-via-CT"></a>

AWS CloudTrail sends events originating from License Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.license-manager
+ `eventSource`: license-manager.amazonaws.com

```
{
  "source": ["aws.license-manager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.license-manager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["license-manager.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```