

# Amazon Voice ID events
<a name="events-ref-voiceid"></a>

Amazon Voice ID sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Voice ID service events
<a name="events-ref-voiceid-events"></a>

Amazon Voice ID sends the following events directly to EventBridge: 
+ VoiceId Start Session Action
+ VoiceId Update Session Action
+ VoiceId Evaluate Session Action
+ VoiceId Speaker Action
+ VoiceId Fraudster Action
+ VoiceId Session Speaker Enrollment Action
+ VoiceId Batch Speaker Enrollment Action
+ VoiceId Batch Fraudster Registration Action

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.voiceid

```
{
  "source": ["aws.voiceid"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.voiceid"],
  "detail-type": ["{{VoiceId Start Session Action}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Voice ID events delivered via AWS CloudTrail
<a name="event-ref-voiceid-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Voice ID to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.voiceid
+ `eventSource`: voiceid.amazonaws.com

```
{
  "source": ["aws.voiceid"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["voiceid.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.voiceid"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["voiceid.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```