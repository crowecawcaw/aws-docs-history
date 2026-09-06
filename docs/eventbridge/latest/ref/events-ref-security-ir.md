

# AWS Security Incident Response events
<a name="events-ref-security-ir"></a>

Security Incident Response sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Security Incident Response service events
<a name="events-ref-security-ir-events"></a>

Security Incident Response sends the following events directly to EventBridge: 
+ Case Created
+ Case Updated
+ Case Comment Added
+ Case Comment Updated
+ Case Closed
+ Membership Created
+ Membership Updated
+ Membership Cancelled
+ Membership Terminated

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.security-ir

```
{
  "source": ["aws.security-ir"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.security-ir"],
  "detail-type": ["{{Case Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Security Incident Response events delivered via AWS CloudTrail
<a name="event-ref-security-ir-events-via-CT"></a>

AWS CloudTrail sends events originating from Security Incident Response to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.security-ir
+ `eventSource`: security-ir.amazonaws.com

```
{
  "source": ["aws.security-ir"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["security-ir.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.security-ir"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["security-ir.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```