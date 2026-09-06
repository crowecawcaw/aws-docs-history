

# Amazon Braket events
<a name="events-ref-braket"></a>

Braket sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Braket service events
<a name="events-ref-braket-events"></a>

Braket sends the following events directly to EventBridge: 
+ Braket Task State Change
+ Braket Job State Change
+ Braket QPU Status Change
+ Braket Device Status Change

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.braket

```
{
  "source": ["aws.braket"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.braket"],
  "detail-type": ["{{Braket Task State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Braket events delivered via AWS CloudTrail
<a name="event-ref-braket-events-via-CT"></a>

AWS CloudTrail sends events originating from Braket to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.braket
+ `eventSource`: braket.amazonaws.com

```
{
  "source": ["aws.braket"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["braket.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.braket"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["braket.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```