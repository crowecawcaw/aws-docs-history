

# Amazon Interactive Video Service events
<a name="events-ref-ivs"></a>

Amazon IVS sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon IVS service events
<a name="events-ref-ivs-events"></a>

Amazon IVS sends the following events directly to EventBridge: 
+ IVS Stream State Change
+ IVS Stream Health Change
+ IVS Limit Breach
+ IVS Recording State Change
+ IVS Stage Update
+ IVS Composition State Change
+ IVS Publisher Recording State Change
+ IVS Participant Recording State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.ivs

```
{
  "source": ["aws.ivs"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.ivs"],
  "detail-type": ["{{IVS Stream State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon IVS events delivered via AWS CloudTrail
<a name="event-ref-ivs-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon IVS to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.ivs
+ `eventSource`: ivs.amazonaws.com

```
{
  "source": ["aws.ivs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ivs.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.ivs"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["ivs.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```