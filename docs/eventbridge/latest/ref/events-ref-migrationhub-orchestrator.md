

# AWS Migration Hub Orchestrator events
<a name="events-ref-migrationhub-orchestrator"></a>

Migration Hub Orchestrator sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Migration Hub Orchestrator service events
<a name="events-ref-migrationhub-orchestrator-events"></a>

Migration Hub Orchestrator sends the following events directly to EventBridge: 
+ Migration Hub Orchestrator Resource Status Changed

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.migrationhub-orchestrator

```
{
  "source": ["aws.migrationhub-orchestrator"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.migrationhub-orchestrator"],
  "detail-type": ["{{Migration Hub Orchestrator Resource Status Changed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Migration Hub Orchestrator events delivered via AWS CloudTrail
<a name="event-ref-migrationhub-orchestrator-events-via-CT"></a>

AWS CloudTrail sends events originating from Migration Hub Orchestrator to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.migrationhub-orchestrator
+ `eventSource`: migrationhub-orchestrator.amazonaws.com

```
{
  "source": ["aws.migrationhub-orchestrator"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["migrationhub-orchestrator.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.migrationhub-orchestrator"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["migrationhub-orchestrator.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```