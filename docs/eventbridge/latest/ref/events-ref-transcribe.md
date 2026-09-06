

# Amazon Transcribe events
<a name="events-ref-transcribe"></a>

Amazon Transcribe sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Transcribe service events
<a name="events-ref-transcribe-events"></a>

Amazon Transcribe sends the following events directly to EventBridge: 
+ Transcribe Job State Change
+ Language Identification State Change
+ Transcribe Language Model State Change
+ Call Analytics Job State Change
+ Vocabulary State Change
+ Call Analytics Post Call Job State Change
+ Multiple Language Identification State Change

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.transcribe

```
{
  "source": ["aws.transcribe"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.transcribe"],
  "detail-type": ["{{Transcribe Job State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Transcribe events delivered via AWS CloudTrail
<a name="event-ref-transcribe-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Transcribe to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.transcribe
+ `eventSource`: transcribe.amazonaws.com

```
{
  "source": ["aws.transcribe"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["transcribe.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.transcribe"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["transcribe.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```