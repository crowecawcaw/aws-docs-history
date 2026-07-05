# Configuring RCS message expiration

Time-sensitive messages, such as one-time passwords (OTPs), flash-sale announcements, and
appointment reminders, lose value if delivered after the relevant window has passed. When you
include the `TimeToLive` parameter in a
`SendRcsMessage` request, AWS End User Messaging removes the message if it has not been delivered
within the specified number of seconds. The recipient never sees an expired message.

You can combine `TimeToLive` with per-message fallback so that an SMS or MMS
fallback is sent automatically when the RCS message expires. For details on configuring
fallback, see [Configuring per-message SMS or MMS fallback](rcs-fallback-per-message.md "rcs-fallback-per-message.md").

## How message expiration works

The TTL countdown begins when AWS End User Messaging accepts the `SendRcsMessage` request.
The following outcomes are possible:

- **Delivered before TTL expires**: The message
  reaches the recipient and AWS End User Messaging emits a delivery event. For more information
  about events, see [RCS message events](rcs-events.md "rcs-events.md").
- **TTL expires before delivery (with fallback)**:
  If you set a `FallbackConfiguration` on the request, AWS End User Messaging sends the
  SMS or MMS fallback message to the recipient. The original RCS message is
  removed and the recipient never sees it.
- **TTL expires before delivery (no fallback)**:
  The message fails. AWS End User Messaging removes the RCS message and emits a
  TTL expiration event. The recipient never sees the message.

## TimeToLive parameter reference

You set message expiration by including the `TimeToLive` parameter in your
`SendRcsMessage` request.

TimeToLive parameter details| Property | Value |
| --- | --- |
| Parameter name | `TimeToLive` |
| Type | Integer |
| Unit | Seconds |
| Minimum value | 1 |
| Maximum value | 172800 (48 hours) |
| Default behavior | If you omit `TimeToLive`, AWS End User Messaging does not apply an<br>expiration window. The message remains pending until delivery succeeds or<br>the carrier removes it. |

###### Important

Set `TimeToLive` to at least 10 seconds. Values below 10 increase the
risk that the message expires before the carrier can attempt delivery. A value of 0
or a negative number returns a `ValidationException`.

## Expiration and fallback

When you include both `TimeToLive` and `FallbackConfiguration`
in the same `SendRcsMessage` request, AWS End User Messaging uses the following logic:

1. AWS End User Messaging attempts RCS delivery.
2. If the message is not delivered before `TimeToLive` seconds elapse,
   AWS End User Messaging removes the pending RCS message.
3. AWS End User Messaging sends the fallback message on the channel you specified in
   `FallbackConfiguration.Channel` (either `SMS` or
   `MMS`).

If you set `TimeToLive` without a `FallbackConfiguration`, the
message fails on expiry and no fallback is sent. Monitor expiration events to detect
these cases. For more information, see [RCS message events](rcs-events.md "rcs-events.md").

For complete fallback configuration details, including the
`FallbackConfiguration` structure, see
[Configuring per-message SMS or MMS fallback](rcs-fallback-per-message.md "rcs-fallback-per-message.md").

## Recommended TTL values

Choose a `TimeToLive` value that matches the relevance window of the
content you are sending.

Recommended TTL values by use case| Use case | Recommended TTL | Rationale |
| --- | --- | --- |
| One-time passwords (OTPs) | 30 to 120 seconds | OTP codes have short validity windows. Delivering after expiry<br>confuses recipients. |
| Fraud or security alerts | 60 to 300 seconds | Time-critical security notifications must arrive quickly or trigger<br>a fallback channel. |
| Appointment reminders | 3600 to 7200 seconds (1 to 2 hours) | Useful only before the appointment time. |
| Flash sales | Match the sale duration | A delivered-after-sale message creates a negative customer<br>experience. |
| Daily promotions | 43200 to 86400 seconds (12 to 24 hours) | Relevant for the current day only. |
| Delivery notifications | 1800 to 3600 seconds (30 to 60 minutes) | Package status changes quickly; a stale update is misleading. |

For general content that has no specific time constraint, omit
`TimeToLive` and let AWS End User Messaging attempt delivery indefinitely.

## Best practices

- Always set `TimeToLive` for time-sensitive content such as OTPs,
  security alerts, and appointment reminders.
- Use at least 10 seconds to give the carrier time to attempt delivery.
- Pair `TimeToLive` with a `FallbackConfiguration` for
  critical messages. This ensures the recipient receives the content on an
  alternative channel if the RCS delivery window closes.
- Monitor TTL expiration events to track delivery success rates and tune your
  TTL values over time. For more information about event types, see
  [RCS message events](rcs-events.md "rcs-events.md").
- For rich media messages (rich cards and carousels), consider a longer TTL to
  account for media download time. For information about rich messaging, see
  [Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md").
