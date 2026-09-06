

# Amazon Translate events
<a name="events-ref-translate"></a>

Amazon Translate sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Translate service events
<a name="events-ref-translate-events"></a>

Amazon Translate sends the following events directly to EventBridge: 
+ Translate Parallel Data State Change
+ Translate TextTranslationJob State Change

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.translate

```
{
  "source": ["aws.translate"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.translate"],
  "detail-type": ["{{Translate Parallel Data State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Amazon Translate events delivered via AWS CloudTrail
<a name="event-ref-translate-events-via-CT"></a>

AWS CloudTrail sends events originating from Amazon Translate to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.translate
+ `eventSource`: translate.amazonaws.com

```
{
  "source": ["aws.translate"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["translate.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.translate"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["translate.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```