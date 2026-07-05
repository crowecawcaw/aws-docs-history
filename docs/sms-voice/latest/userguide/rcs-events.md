# RCS message events

When you send RCS messages with AWS End User Messaging, the RCS platform generates events that
report message lifecycle changes, recipient interactions, and system-level outcomes.
These events provide richer signals than traditional SMS delivery receipts, giving you
real-time visibility into whether a message was delivered, read, expired, or fell back
to SMS or MMS.

Outbound status events (delivery, read, expiration, and fallback) are delivered
through configuration set event destinations. Inbound interaction events (typing
indicators and suggestion taps) are delivered to the two-way Amazon SNS topic that you
configure on your RCS agent. To set up event destinations, see
[Event destinations in AWS End User Messaging SMS](configuration-sets-event-destinations.md "configuration-sets-event-destinations.md").

For details on the messages that generate these events, see
[Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md").

###### Topics

- [Common fields on RCS events](#rcs-events-common-fields "#rcs-events-common-fields")
- [Delivery status events](#rcs-events-delivery-status "#rcs-events-delivery-status")
- [Read receipts](#rcs-events-read-receipts "#rcs-events-read-receipts")
- [Typing indicators](#rcs-events-typing-indicators "#rcs-events-typing-indicators")
- [TTL expiration events](#rcs-events-ttl-expiration "#rcs-events-ttl-expiration")
- [Fallback events](#rcs-events-fallback "#rcs-events-fallback")
- [Suggestion tap (postback) events](#rcs-events-postback "#rcs-events-postback")
- [Conversational pricing events and fields](#rcs-events-conversational "#rcs-events-conversational")
- [Routing events to destinations](#rcs-events-routing "#rcs-events-routing")
- [Best practices for event processing](#rcs-events-best-practices "#rcs-events-best-practices")

## Common fields on RCS events

All RCS events, including delivery status events, read receipts, and inbound
interaction events, include the following fields that identify the RCS agent:

`rcsBusinessId`

The platform identifier for the RCS agent that sent or received the
message.

`agentIsoCountryCode`

The ISO country code of the country in which the RCS agent is
registered, for example `US` or `CA`.

These fields are present on all RCS events. They are not included on SMS or MMS
events.

## Delivery status events

Delivery status events indicate the lifecycle state of an outbound RCS message.
You use these events to confirm delivery, trigger fallback logic, or alert your
operations team to content violations.

Each outbound status event has an `eventType` of
`RCS_DELIVERED` (and related RCS status event types) and a
`messageStatus` field that holds one of the following values:

`DELIVERED`

The message reached the recipient's device. Use this event to cancel
any pending fallback timers.

`PENDING`

The RCS platform accepted the message but has not yet delivered it.
Start your fallback timer when you receive this event.

`UNDELIVERABLE`

The platform permanently cannot deliver the message (for example,
the recipient's device does not support RCS). Trigger your SMS or MMS
fallback and flag the phone number for future routing decisions.

`REJECTED`

The message was rejected due to a content policy violation. Alert
your operations team and review the message content.

The following example shows a delivery event payload:

```
{
    "eventType": "RCS_DELIVERED",
    "eventVersion": "1.0",
    "eventTimestamp": 1781661267660,
    "isFinal": true,
    "originationPhoneNumber": "rcs-c020de2520714385964ebf7b095c4b60",
    "destinationPhoneNumber": "+13022640220",
    "isoCountryCode": "US",
    "isInternationalSend": false,
    "messageId": "test-sc1-004",
    "messageRequestTimestamp": 1781300397157,
    "messageEncoding": "UNICODE",
    "messageType": "TRANSACTIONAL",
    "messageStatus": "DELIVERED",
    "messageStatusDescription": "Message has been accepted by phone",
    "totalMessageParts": 1,
    "totalMessagePrice": 0.007,
    "totalCarrierFee": 0.00494,
    "rcsMetadata": { "billingEventType": "RICH" },
    "rcsBusinessId": "endusermessagingtesting1_06fr8x6o_agent",
    "agentIsoCountryCode": "US"
}
```

###### Note

Status events for rich RCS messages include billing metadata. The
`rcsMetadata.billingEventType` value is `RICH` for rich
RCS messages.

## Read receipts

A read receipt indicates that the recipient opened or viewed your message. Use
read receipts to track engagement and measure read rates.

`READ`

The recipient viewed the message. A `RCS_DELIVERED` event
is always sent before or together with the `RCS_READ` event,
so if you did not process a separate delivery event, treat the message
as delivered when you receive the read event.

The read event uses an `eventType` of `RCS_READ` with
`messageStatus` set to `READ`:

```
{
    "eventType": "RCS_READ",
    "eventVersion": "1.0",
    "eventTimestamp": 1781661267203,
    "isFinal": true,
    "originationPhoneNumber": "rcs-c020de2520714385964ebf7b095c4b60",
    "destinationPhoneNumber": "+13022640220",
    "isoCountryCode": "US",
    "isInternationalSend": false,
    "messageId": "test-sc1-004",
    "messageRequestTimestamp": 1781300397157,
    "messageEncoding": "UNICODE",
    "messageType": "TRANSACTIONAL",
    "messageStatus": "READ",
    "messageStatusDescription": "Message has been read by recipient",
    "totalMessageParts": 1,
    "totalMessagePrice": 0.0,
    "totalCarrierFee": 0.0,
    "rcsBusinessId": "endusermessagingtesting1_06fr8x6o_agent",
    "agentIsoCountryCode": "US"
}
```

You can calculate your read rate as the number of `READ` events
divided by the number of `DELIVERED` events, multiplied by 100.

## Typing indicators

Typing indicator events signal that a participant is composing a message. These
events flow in both directions:

- **Inbound (user to agent)**: When the
  recipient begins composing a reply, you receive an inbound notification on
  your two-way Amazon SNS topic. The `messageBody` contains a JSON
  object with a `type` of `RCS_TYPING`. Use this to
  prepare your conversational logic or display status in your dashboard.
- **Outbound (agent to user)**: Agent-initiated
  typing indicators, which show the recipient that your agent is preparing a
  response, are a planned capability. Check the AWS End User Messaging release notes for
  current availability.

The following example shows an inbound typing notification:

```
{
    "originationNumber": "12679164820",
    "destinationNumber": "rcs-cb1e6e519e9049fabf8c0ae38e4d876b",
    "messageBody": "{\"type\":\"RCS_TYPING\",\"receivedAt\":\"2026-06-17T17:36:29.937+0000\"}",
    "inboundMessageId": "12679164820-2026-06-17T17:36:29.937+0000"
}
```

###### Note

Agent-initiated typing indicators and agent-initiated read receipts, which your
agent sends to a recipient, are planned capabilities. Check the AWS End User Messaging release notes
for current availability.

## TTL expiration events

When you set a `TimeToLive` value on a message and the TTL elapses
before the message is delivered, the RCS platform attempts to revoke (delete) the
message. The outcome generates one of the following events:

`TTL_EXPIRATION_REVOKED`

The expired message was successfully removed before the recipient
viewed it. You can safely trigger your SMS or MMS fallback to ensure
the recipient receives the content.

`TTL_EXPIRATION_REVOKE_FAILED`

The revocation failed and the message might still be delivered to the
recipient. In this case, evaluate whether sending a fallback message
would result in a duplicate before proceeding.

TTL expiration events work together with your fallback strategy. For details on
configuring message expiration, see
[Configuring RCS message expiration](rcs-message-expiration.md "rcs-message-expiration.md").

## Fallback events

When an RCS message cannot be delivered and AWS End User Messaging triggers an SMS or MMS
fallback (either through pool-based configuration or per-message
`FallbackConfiguration`), the service generates events that indicate
the fallback outcome.

Fallback events indicate:

- Whether the fallback message was sent successfully.
- The channel used for fallback (SMS or MMS).
- The reason the original RCS message was not delivered (for example,
  device not RCS-capable, TTL expiration, or platform unavailability).

Monitor these events to measure your fallback rate and identify phone numbers
that consistently require fallback delivery. For details on configuring per-message
fallback, see
[Configuring per-message SMS or MMS fallback](rcs-fallback-per-message.md "rcs-fallback-per-message.md").

## Suggestion tap (postback) events

When a recipient chooses a suggestion (a suggested reply or suggested action), you
receive a postback event containing the `PostbackData` string that you
configured on that suggestion. Use postback data to route your conversational logic,
not the display text.

###### Important

Suggestion tap (postback) events are delivered only to your two-way Amazon
SNS topic, not to configuration set event destinations.

The notification's `messageBody` contains a JSON object with a
`type` of `SUGGESTION`, the display `text`, and
the `postbackData` you set on the suggestion:

```
{
    "originationNumber": "12679164820",
    "destinationNumber": "rcs-cb1e6e519e9049fabf8c0ae38e4d876b",
    "messageBody": "{\"type\":\"SUGGESTION\",\"text\":\"Open\",\"postbackData\":\"Open\"}",
    "inboundMessageId": "nIMYZGrBUILWng0Qck0deqVaAoTSJY5PsktKYOBYJhVaTsrdMdrs714e8SLZAjD3"
}
```

For details on how to configure suggestions and their postback data, see
[Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md").

###### Important

Design your `PostbackData` values as structured identifiers (for
example, `action:confirm_order:12345`) so that you can parse them
programmatically. Avoid relying on display text, which can change without
affecting your routing logic.

## Conversational pricing events and fields

If you register your RCS agent to use conversational pricing, AWS End User Messaging adds fields to
delivery and inbound events while a message is part of an active conversation session,
and sends a `CONVERSATION_STARTED` event when a session begins. For an
overview of the conversational pricing model, see
[Conversational pricing](rcs-billing.md#rcs-billing-conversational "rcs-billing.md#rcs-billing-conversational").

### Conversation fields

The following fields appear on a delivery or inbound event only when the message
is part of an active conversation session. When the message is not part of a
conversation, AWS End User Messaging omits these fields entirely.

`conversationInitiatingMessageId`

The message ID that started the conversation session. Present on
delivery and inbound events.

`conversationInitiatingMessageType`

How the conversation started: `OUTBOUND` when your agent
sent the first message, or `INBOUND` when the recipient sent
the first message. Present on delivery and inbound events.

`conversationSessionFee`

The one-time session fee, in US dollars, charged once per 24-hour
conversation session. Present on delivery events only.

When a message is part of an active conversation session, its delivery event
reports a `totalMessagePrice` and `totalCarrierFee` of
`0.0`, because the session fee covers the message. The following example
shows a delivery event for a message within an active conversation:

```
{
    "eventType": "RCS_DELIVERED",
    "eventVersion": "1.0",
    "eventTimestamp": 1751234567890,
    "isFinal": true,
    "originationPhoneNumber": "rcs-f4e4252a5abe48bea50a6c176a056124",
    "destinationPhoneNumber": "+14376638816",
    "isoCountryCode": "CA",
    "isInternationalSend": false,
    "messageId": "b4a3196d-5b61-4884-a0d9-745acf1f6235",
    "messageRequestTimestamp": 1751234565000,
    "messageEncoding": "UNICODE",
    "messageType": "TRANSACTIONAL",
    "messageStatus": "DELIVERED",
    "messageStatusDescription": "Message has been accepted by phone",
    "totalMessageParts": 1,
    "totalMessagePrice": 0.0,
    "totalCarrierFee": 0.0,
    "rcsMetadata": {
        "billingEventType": "BASIC"
    },
    "rcsBusinessId": "endusermessagingtesting1_06fr8x6o_agent",
    "agentIsoCountryCode": "CA",
    "conversationInitiatingMessageId": "177930985040408106521449",
    "conversationInitiatingMessageType": "OUTBOUND",
    "conversationSessionFee": 0.012
}
```

### CONVERSATION\_STARTED event

AWS End User Messaging sends a `CONVERSATION_STARTED` event to your RCS event Amazon SNS
topic when a conversation session begins. A session begins when your agent sends a
message and the recipient replies within 24 hours (business-initiated), or when the
recipient sends a message and your agent responds (user-initiated).

The `messageBody` contains a JSON object with the following
fields:

`type`
Always `CONVERSATION_STARTED`.

`startTime`
The session start time, in ISO 8601 format.

`endTime`
The session expiry time, in ISO 8601 format. This is always
24 hours after `startTime`.

`conversationInitiatingMessageId`
The message ID that started the
conversation.

`conversationInitiatingMessageType`
`OUTBOUND` when your agent sent the first message,
or `INBOUND` when the recipient sent the first
message.

The following example shows a `CONVERSATION_STARTED` event:

```
{
    "originationNumber": "14376638816",
    "destinationNumber": "rcs-e138fa39eabf4d6d8e95546248c8dfa7",
    "messageBody": "{\"type\":\"CONVERSATION_STARTED\",\"startTime\":\"2026-06-28T04:03:08.002+0000\",\"endTime\":\"2026-06-29T04:08:08.002+0000\",\"conversationInitiatingMessageId\":\"7e7da6ec-234a-4d4f-bbc5-943bcca663ab\",\"conversationInitiatingMessageType\":\"OUTBOUND\"}",
    "inboundMessageId": "7e7da6ec-234a-4d4f-bbc5-943bcca663ab"
}
```

## Routing events to destinations

AWS End User Messaging routes RCS events through configuration set event destinations. You
configure event destinations on the configuration set that is associated with your
sending operations. Supported destinations include:

Amazon SNS

Use an Amazon SNS topic for real-time event processing, including
triggering AWS Lambda functions to respond to delivery receipts or
suggestion taps.

Amazon Data Firehose

Use a Firehose delivery stream to send events to Amazon S3, Amazon
Redshift, or other analytics destinations for long-term storage and
reporting.

Amazon CloudWatch Logs

Use CloudWatch Logs for debugging, log analysis, and setting up
CloudWatch alarms on event patterns (for example, alerting on high
rejection rates).

To learn how to create and configure event destinations, see
[Event destinations in AWS End User Messaging SMS](configuration-sets-event-destinations.md "configuration-sets-event-destinations.md").

When you call `SendRcsMessage`, specify the
`ConfigurationSetName` parameter to associate the message with your
configuration set. Outbound status events generated by that message are routed to
the destinations you configured.

When you configure the event types that an event destination matches, you can select
`RCS_ALL` to subscribe to all RCS event types with a single matching type,
instead of listing each RCS event type individually (such as `RCS_DELIVERED`
and `RCS_READ`).

###### Note

Inbound interaction events, including typing indicators and suggestion taps
(postbacks), are delivered to the two-way Amazon SNS topic configured on your
RCS agent, not to configuration set event destinations.

## Best practices for event processing

- Configure event destinations before you begin sending production
  messages. This ensures you capture all events from the start.
- Use `DELIVERED` events to cancel fallback timers. If you
  receive a delivery confirmation, do not send an SMS or MMS fallback.
- Process subscription events (`UNSUBSCRIBE`) immediately
  to maintain compliance with messaging regulations.
- Implement idempotent event processing. Use the message identifier
  combined with the event type as a deduplication key to handle duplicate
  event deliveries.
- Handle out-of-order events by comparing event timestamps. Events might
  arrive in a different order than they occurred.
- Monitor rejection and undeliverable rates with CloudWatch alarms to
  detect content issues or targeting problems early.
