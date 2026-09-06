

# AWS IoT Greengrass events
<a name="events-ref-greengrass"></a>

AWS IoT Greengrass sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS IoT Greengrass service events
<a name="events-ref-greengrass-events"></a>

AWS IoT Greengrass sends the following events directly to EventBridge: 
+ Greengrass Deployment Status Change
+ Greengrass Telemetry Data
+ Greengrass Device Health Notification
+ Greengrass V2 Effective Deployment Status Change
+ Greengrass V2 Installed Component Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.greengrass

```
{
  "source": ["aws.greengrass"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.greengrass"],
  "detail-type": ["{{Greengrass Deployment Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS IoT Greengrass events delivered via AWS CloudTrail
<a name="event-ref-greengrass-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS IoT Greengrass to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.greengrass
+ `eventSource`: greengrass.amazonaws.com

```
{
  "source": ["aws.greengrass"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["greengrass.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.greengrass"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["greengrass.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```