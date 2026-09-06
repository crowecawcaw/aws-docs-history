

# AWS Resource Groups events
<a name="events-ref-resource-groups"></a>

Resource Groups sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Resource Groups service events
<a name="events-ref-resource-groups-events"></a>

Resource Groups sends the following events directly to EventBridge: 
+ ResourceGroups Group State Change
+ ResourceGroups Group Membership Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.resource-groups

```
{
  "source": ["aws.resource-groups"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.resource-groups"],
  "detail-type": ["{{ResourceGroups Group State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Resource Groups events delivered via AWS CloudTrail
<a name="event-ref-resource-groups-events-via-CT"></a>

AWS CloudTrail sends events originating from Resource Groups to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.resource-groups
+ `eventSource`: resource-groups.amazonaws.com

```
{
  "source": ["aws.resource-groups"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resource-groups.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.resource-groups"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["resource-groups.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```