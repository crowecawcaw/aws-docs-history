

# AWS CodeArtifact events
<a name="events-ref-codeartifact"></a>

CodeArtifact sends service events directly to EventBridge, as well as via AWS CloudTrail.

## CodeArtifact service events
<a name="events-ref-codeartifact-events"></a>

CodeArtifact sends the following events directly to EventBridge: 
+ Goshawk Repository State Change
+ CodeArtifact Package Version State Change

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.codeartifact

```
{
  "source": ["aws.codeartifact"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.codeartifact"],
  "detail-type": ["{{Goshawk Repository State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## CodeArtifact events delivered via AWS CloudTrail
<a name="event-ref-codeartifact-events-via-CT"></a>

AWS CloudTrail sends events originating from CodeArtifact to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.codeartifact
+ `eventSource`: codeartifact.amazonaws.com

```
{
  "source": ["aws.codeartifact"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codeartifact.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.codeartifact"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["codeartifact.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```