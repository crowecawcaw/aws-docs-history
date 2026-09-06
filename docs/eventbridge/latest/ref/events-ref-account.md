

# AWS Account Management events
<a name="events-ref-account"></a>

Account Management sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Account Management service events
<a name="events-ref-account-events"></a>

Account Management sends the following events directly to EventBridge: 
+ Region Opt-In Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.account

```
{
  "source": ["aws.account"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.account"],
  "detail-type": ["{{Region Opt-In Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Account Management events delivered via AWS CloudTrail
<a name="event-ref-account-events-via-CT"></a>

AWS CloudTrail sends events originating from Account Management to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.account
+ `eventSource`: account.amazonaws.com

```
{
  "source": ["aws.account"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["account.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.account"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["account.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```