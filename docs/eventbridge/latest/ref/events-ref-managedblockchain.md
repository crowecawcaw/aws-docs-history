

# Amazon Managed Blockchain events
<a name="events-ref-managedblockchain"></a>

Managed Blockchain sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Managed Blockchain service events
<a name="events-ref-managedblockchain-events"></a>

Managed Blockchain sends the following events directly to EventBridge: 
+ Managed Blockchain Proposal Status Change
+ Managed Blockchain Invitation Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.managedblockchain

```
{
  "source": ["aws.managedblockchain"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.managedblockchain"],
  "detail-type": ["{{Managed Blockchain Proposal Status Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Managed Blockchain events delivered via AWS CloudTrail
<a name="event-ref-managedblockchain-events-via-CT"></a>

AWS CloudTrail sends events originating from Managed Blockchain to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.managedblockchain
+ `eventSource`: managedblockchain.amazonaws.com

```
{
  "source": ["aws.managedblockchain"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["managedblockchain.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.managedblockchain"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["managedblockchain.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```