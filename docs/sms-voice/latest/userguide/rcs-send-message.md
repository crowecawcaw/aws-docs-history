# Sending RCS messages

AWS End User Messaging uses the same `SendTextMessage` API for both RCS and SMS
delivery. How the service routes your message depends on the origination identity
you specify in the request. You can send messages through a phone pool (recommended),
at the account level, or directly through an AWS RCS Agent ARN.

This section explains the three sending patterns, how to interpret delivery
receipts, and provides code examples. For details on sticky sending, origination
identity priority order, and automatic SMS fallback, see
[RCS to SMS fallback using phone pools](rcs-sms-fallback.md "rcs-sms-fallback.md"). For details
on managing AWS RCS Agents, see
[Managing RCS agents](rcs-agents.md "rcs-agents.md").

###### Note

This page describes sending text messages over RCS and SMS with the
`SendTextMessage` API. To send rich RCS content, such as rich cards,
carousels, media files, and interactive suggestions, use the `SendRcsMessage`
API instead. For a comparison of the two API actions and guidance on which to choose,
see [Choosing between SendTextMessage and SendRcsMessage](rcs-rich-messaging.md#rcs-rich-messaging-choosing "rcs-rich-messaging.md#rcs-rich-messaging-choosing").

###### Topics

- [Sending patterns](#rcs-send-message-patterns "#rcs-send-message-patterns")
- [Sticky sending, priority order, and SMS fallback](#rcs-send-message-fallback-summary "#rcs-send-message-fallback-summary")
- [Code examples](#rcs-send-message-examples "#rcs-send-message-examples")
- [AI agent prompt for sending RCS messages](#rcs-send-message-ai-prompt "#rcs-send-message-ai-prompt")
- [Delivery receipt handling](#rcs-send-message-delivery-receipts "#rcs-send-message-delivery-receipts")

## Sending patterns

AWS End User Messaging supports three patterns for sending RCS messages. Each pattern
determines how the service selects an origination identity and whether automatic
SMS fallback is available.

RCS sending patterns| Pattern | How it works | SMS fallback | When to use |
| --- | --- | --- | --- |
| Pool-based (recommended) | Specify a pool ID as the origination identity. The service<br>selects the best identity from the pool. | Yes | All use cases. Provides automatic channel selection and SMS<br>fallback with compliance-safe routing. |
| Account-level | Omit the origination identity. The service selects from all<br>available identities in your account. | Yes | Simple setups with a single use case. Not recommended for<br>accounts with multiple use cases. |
| Direct send | Specify an AWS RCS Agent ARN as the origination identity.<br>The message is sent via RCS only. | No | RCS-or-nothing use cases, or when you manage SMS fallback<br>outside of AWS End User Messaging. |

### Pool-based sending (recommended)

Pool-based sending is the recommended approach for all RCS use cases.
When you specify a pool ID as the origination identity in your
`SendTextMessage` request, AWS End User Messaging selects the best
origination identity from the pool based on the destination, channel
availability, and sticky sending history.

If the pool contains both an AWS RCS Agent and SMS phone numbers, the
service attempts RCS delivery first. If RCS delivery fails, the service
automatically falls back to SMS using a phone number from the same pool.
Because all identities in the pool are registered for the same use case,
the fallback message is always sent from an appropriate number.

For details on creating and configuring pools with AWS RCS Agents, see
[RCS to SMS fallback using phone pools](rcs-sms-fallback.md "rcs-sms-fallback.md").

### Account-level sending

When you omit the origination identity from your
`SendTextMessage` request, AWS End User Messaging selects an origination
identity from all available identities in your account. The service uses
the origination identity priority order to determine which
identity to use. For details, see
[Fallback logic and priority order](rcs-sms-fallback.md#rcs-sms-fallback-logic "rcs-sms-fallback.md#rcs-sms-fallback-logic").

###### Important

Account-level sending creates a compliance risk if your account
contains phone numbers registered for different use cases. When RCS
delivery fails and the service falls back to SMS, it may select a phone
number that does not match the content of your message. For example, an
OTP message could fall back to a toll-free number registered for
appointment reminders, violating the registration terms for that number.
To avoid this risk, use pool-based sending with one pool per use case.
For details, see
[Compliance risk with account-level sending](rcs-sms-fallback.md#rcs-sms-fallback-compliance-risk "rcs-sms-fallback.md#rcs-sms-fallback-compliance-risk").

### Direct send (RCS only)

When you specify an AWS RCS Agent ARN as the origination identity in your
`SendTextMessage` request, AWS End User Messaging sends the message via RCS
only. There is no automatic SMS fallback. If RCS delivery fails, the message
is not retried on another channel.

Use direct sending when:

- You want RCS-or-nothing delivery. The message should only
  be delivered via RCS, and you prefer no delivery over SMS
  delivery.
- You manage SMS fallback outside of AWS End User Messaging. Your
  application handles fallback logic independently, for example by
  detecting RCS delivery failure and sending a separate SMS through
  a different system or provider.

###### Note

Direct sending bypasses all SMS fallback logic. If the recipient's
device or carrier does not support RCS, the message is not delivered.
For most use cases, pool-based sending is recommended because it provides
automatic SMS fallback at no additional cost.

## Sticky sending, priority order, and SMS fallback

When you send messages through a pool or at the account level, AWS End User Messaging uses
sticky sending (a 25-hour routing optimization), an origination identity priority
order, and automatic SMS fallback to select the best channel and identity for each
message. For complete details on how these mechanisms work, including
automatic fallback, delivery receipts during fallback, and billing
implications, see
[RCS to SMS fallback using phone pools](rcs-sms-fallback.md "rcs-sms-fallback.md").

## Code examples

The following Python examples demonstrate how to send RCS messages using each
of the three sending patterns. All examples use the boto3
`pinpoint-sms-voice-v2` client and the
`SendTextMessage` API.

### Pool-based sending example

The following example sends a message through a phone pool. The service
selects the best origination identity from the pool and automatically falls
back to SMS if RCS delivery is not possible.

```

import boto3

client = boto3.client('pinpoint-sms-voice-v2')

response = client.send_text_message(
    DestinationPhoneNumber='+12065550100',
    OriginationIdentity='pool-a1b2c3d4e5f6g7h8i',
    MessageBody='Your appointment is confirmed for tomorrow at 2:00 PM.',
    MessageType='TRANSACTIONAL'
)

print(f"Message ID: {response['MessageId']}")

```

### Account-level sending example

The following example sends a message at the account level by omitting the
origination identity. The service selects an identity from all available
identities in your account using the priority order.

```

import boto3

client = boto3.client('pinpoint-sms-voice-v2')

response = client.send_text_message(
    DestinationPhoneNumber='+12065550100',
    MessageBody='Your verification code is 123456.',
    MessageType='TRANSACTIONAL'
)

print(f"Message ID: {response['MessageId']}")

```

###### Important

If your account contains phone numbers registered for different use
cases, account-level sending may route SMS fallback through a number
that does not match your message content. Use pool-based sending with
one pool per use case to avoid compliance risk.

### Direct send example

The following example sends a message directly through an AWS RCS Agent
ARN. The message is delivered via RCS only, with no SMS fallback.

```

import boto3

client = boto3.client('pinpoint-sms-voice-v2')

response = client.send_text_message(
    DestinationPhoneNumber='+12065550100',
    OriginationIdentity='arn:aws:sms-voice:us-east-1:123456789012:rcs-agent/rcs-a1b2c3d4',
    MessageBody='Welcome to our RCS channel! Reply HELP for assistance.'
)

print(f"Message ID: {response['MessageId']}")

```

###### Note

If the recipient's device or carrier does not support RCS, the
message is not delivered. No SMS fallback is attempted. Use this pattern
only when you want RCS-or-nothing delivery or when you manage SMS
fallback outside of AWS End User Messaging.

## AI agent prompt for sending RCS messages

If you use a generative AI coding assistant or AI agent, you can use the
following prompt to get help sending RCS messages using the AWS CLI or
SDK.

###### Note

Copy the following prompt and paste it into your AI agent or coding
assistant:

```

## RCS Messaging Assistant Prompt

Help me send RCS messages using AWS End User Messaging SMS with the
`pinpoint-sms-voice-v2` service. Show me exact CLI commands and Python/boto3
examples. Ask me for my details before generating any commands.

**Important rules for generating commands:**
- The API is `send-text-message` — the same command used for SMS. There is
  NO separate RCS send API.
- There is NO `describe-messages` API. Do not generate it.
- The boto3 method is `send_text_message` on the
  `pinpoint-sms-voice-v2` client.
- Use the term "testing" — NOT "sandbox".

**Prerequisites:** I have an existing RCS agent (created via the setup process)
and a verified test device.

### Pattern 1: Direct RCS sending (simplest, good for testing)

Send directly through my RCS Agent ARN. RCS-only delivery, no SMS fallback.
If the recipient's device doesn't support RCS, the message is not delivered.

CLI: `send-text-message --destination-phone-number <E.164>
--origination-identity <agent-arn> --message-body "<text>"
--message-type <TRANSACTIONAL|PROMOTIONAL>`

Returns `MessageId`.

### Pattern 2: Pool-based sending (recommended for production)

Send through a phone pool containing my RCS agent (and optionally SMS phone
numbers for fallback). The service tries RCS first, then falls back to SMS
asynchronously if no RCS signal within 25 seconds. This is NOT synchronous
fallback — the SMS is sent as a separate attempt after the timeout.

To set up a pool:
- `create-pool --origination-identity <rcs-agent-id> --message-type TRANSACTIONAL` → returns `PoolId`
- Optionally add SMS numbers: `associate-origination-identity --pool-id <id>
  --origination-identity <phone-number-id>`

CLI: `send-text-message --destination-phone-number <E.164>
--origination-identity <pool-id> --message-body "<text>"
--message-type <TRANSACTIONAL|PROMOTIONAL>`

### Pattern 3: Account-level sending

Send without specifying `--origination-identity`. The service auto-selects
the best identity from the account.

CLI: `send-text-message --destination-phone-number <E.164>
--message-body "<text>" --message-type <TRANSACTIONAL|PROMOTIONAL>`

**Compliance warning:** If the account has multiple RCS agents, SMS numbers,
or different use cases, the service picks an identity automatically — which
may not be the intended one. Use pool-based or direct sending for explicit
control over which identity is used.

### Delivery verification

- For testing: check the test device directly — the message appears from
  the branded RCS agent.
- For production: configure event destinations BEFORE sending using
  `create-event-destination` (SNS, CloudWatch Logs, or Firehose). Event
  destinations do not retroactively capture events for already-sent messages.
- CloudWatch metrics in `AWS/SMSVoice` namespace provide aggregate delivery
  statistics.

### Behavioral notes

- Sticky sending: the service remembers the last successful identity per
  destination number for 25 hours.
- Pool-based sending is recommended for production because it provides
  automatic SMS fallback.
- All three patterns use the same `send-text-message` API — the only
  difference is what you pass (or don't pass) as `--origination-identity`.

---

**Before generating commands, ask me for:**
- Which sending pattern I want to use (direct, pool-based, or account-level)
- My RCS Agent ARN
- My pool ID (if using pool-based sending)
- Destination phone number in E.164 format
- Message type (TRANSACTIONAL or PROMOTIONAL)
- Message text

```

## Delivery receipt handling

AWS End User Messaging provides delivery receipts for RCS messages through Amazon
EventBridge and configuration set event destinations. Delivery receipts
indicate the final status of your message and which channel was used for
delivery. To learn how to set up event destinations to capture delivery
receipts and other message events, see
[Event destinations in AWS End User Messaging SMS](configuration-sets-event-destinations.md "configuration-sets-event-destinations.md").

### Delivery status values

The following delivery status values apply to RCS messages:

DELIVERED

The message was successfully delivered to the
recipient's device.

PENDING

The message has been accepted by the RCS infrastructure
but delivery confirmation has not yet been received. The
message may still be delivered.

EXPIRED

The message was not delivered within the allowed time
window. For RCS messages with SMS fallback, this status
applies to the RCS attempt before fallback occurs.

UNDELIVERABLE

The message could not be delivered. This can occur when
the recipient's device is permanently unreachable or
the phone number is invalid.

REJECTED

The message was rejected by the RCS infrastructure or
carrier. This can occur due to content policy violations
or carrier-level filtering.

### Channel attribution

Delivery receipts include channel attribution that indicates whether the
message was delivered via RCS or SMS. This is important for understanding
your delivery mix and for billing purposes.

- When a message is delivered via RCS, the delivery receipt
  indicates RCS as the delivery channel and includes the AWS RCS
  Agent identity.
- When a message falls back to SMS, the delivery receipt indicates
  SMS as the delivery channel and includes the SMS phone number
  identity that was used for delivery.
- When a direct send (AWS RCS Agent ARN) fails, the delivery
  receipt indicates RCS as the attempted channel with a failure
  status. No SMS fallback receipt is generated.

For details on RCS CloudWatch metrics and monitoring delivery patterns,
see [RCS CloudWatch metrics and monitoring](rcs-monitoring.md "rcs-monitoring.md"). For
information about how delivery channel affects billing, see
[RCS billing and pricing model](rcs-billing.md "rcs-billing.md").
