

# AWS Network Firewall events
<a name="events-ref-network-firewall"></a>

Network Firewall sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Network Firewall service events
<a name="events-ref-network-firewall-events"></a>

Network Firewall sends the following events directly to EventBridge: 
+ Firewall Configuration Changed
+ Firewall Attachment Status Changed
+ Firewall Transit Gateway Attachment Status Changed

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.network-firewall

```
{
  "source": ["aws.network-firewall"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.network-firewall"],
  "detail-type": ["{{Firewall Configuration Changed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Network Firewall events delivered via AWS CloudTrail
<a name="event-ref-network-firewall-events-via-CT"></a>

AWS CloudTrail sends events originating from Network Firewall to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.network-firewall
+ `eventSource`: network-firewall.amazonaws.com

```
{
  "source": ["aws.network-firewall"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["network-firewall.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.network-firewall"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["network-firewall.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```