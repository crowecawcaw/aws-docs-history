# Amazon Chime events

Amazon Chime sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Amazon Chime service events

Amazon Chime sends the following events directly to EventBridge:

- Chime VoiceConnector Streaming Status
- Media Insights State Change
- Chime Meeting State Change
- Chime Streaming Status
- Chime Chat Streaming Status
- Chime Media Pipeline State Change
- Chime ChannelFlow Processing Status
- Call Insights State Change
- Call Insights Rules Matched
- Media Insights Rules Matched
- Chime Messaging AppInstanceUserEndpoint Delivery Failure
- Chime Messaging AppInstanceBot Lex Failure
- Chime Media Pipeline Kinesis Video Pool State Change

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.chime

```
{
  "source": ["aws.chime"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.chime"],
  "detail-type": ["`Chime VoiceConnector Streaming Status`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.

## Amazon Chime events delivered via

AWS CloudTrail

AWS CloudTrail sends events originating from Amazon Chime to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md "event-delivery-level.md") basis. For more information,
see [AWS service events delivered via AWS CloudTrail](../userguide/eb-service-event-cloudtrail.md "../userguide/eb-service-event-cloudtrail.md")
in the _Amazon EventBridge User Guide_.

To match events from this service delivered by AWS CloudTrail, create an event
pattern that matches against the following event attributes:

- `source`: aws.chime
- `eventSource`: chime.amazonaws.com

```
{
  "source": ["aws.chime"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["chime.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an
`eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.chime"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["chime.amazonaws.com"],
    "eventName": ["`api-action-name`"]
  }
}
```
