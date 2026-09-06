

# Amazon Transcribe Streaming events
<a name="events-ref-transcribestreaming"></a>

Amazon Transcribe Streaming sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Transcribe Streaming service events
<a name="events-ref-transcribestreaming-events"></a>

Amazon Transcribe Streaming sends the following events directly to EventBridge: 
+ MedicalScribe Post Stream Analytics Update

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.transcribestreaming

```
{
  "source": ["aws.transcribestreaming"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.transcribestreaming"],
  "detail-type": ["{{MedicalScribe Post Stream Analytics Update}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Transcribe Streaming events delivered via AWS CloudTrail
<a name="event-ref-transcribestreaming-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Transcribe Streaming to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.transcribestreaming
+ `eventSource`: transcribestreaming.amazonaws.com

```
{
  "source": ["aws.transcribestreaming"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["transcribestreaming.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.transcribestreaming"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["transcribestreaming.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```