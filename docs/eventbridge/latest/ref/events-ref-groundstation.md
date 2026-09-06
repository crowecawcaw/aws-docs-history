

# AWS Ground Station events
<a name="events-ref-groundstation"></a>

AWS Ground Station sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Ground Station service events
<a name="events-ref-groundstation-events"></a>

AWS Ground Station sends the following events directly to EventBridge: 
+ Ground Station Contact State Change
+ Ground Station Dataflow Endpoint Group State Change
+ Ground Station Ephemeris Status Change
+ Ground Station S3 Upload Complete
+ Ground Station Dataflow Endpoint Group Health Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.groundstation

```
{
  "source": ["aws.groundstation"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.groundstation"],
  "detail-type": ["{{Ground Station Contact State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Ground Station events delivered via AWS CloudTrail
<a name="event-ref-groundstation-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Ground Station to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.groundstation
+ `eventSource`: groundstation.amazonaws.com

```
{
  "source": ["aws.groundstation"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["groundstation.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.groundstation"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["groundstation.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```