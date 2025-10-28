# AWS End User Messaging SMS-Voice events

AWS End User Messaging SMS-Voice sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS End User Messaging SMS-Voice service events

AWS End User Messaging SMS-Voice sends the following events directly to EventBridge:

- Text Message Delivery Status Updated
- Media Message Delivery Status Updated
- Voice Message Delivery Status Updated
- Registration Status Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.sms-voice

```
{
  "source": ["aws.sms-voice"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.sms-voice"],
  "detail-type": ["`Text Message Delivery Status Updated`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## AWS End User Messaging SMS-Voice events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from AWS End User Messaging SMS-Voice to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.sms-voice
- `eventSource`: sms-voice.amazonaws.com

```
{
  "source": ["aws.sms-voice"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sms-voice.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.sms-voice"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["sms-voice.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
