# Configuring per-message SMS or MMS fallback

When you send an RCS message, the recipient's device might not support RCS, or the message
might expire before delivery. With per-message fallback, you can specify alternative SMS or MMS
content that AWS End User Messaging delivers automatically when the RCS message cannot reach the
recipient. You configure fallback on each `SendRcsMessage` request by including
the `FallbackConfiguration` parameter.

## When fallback triggers

AWS End User Messaging triggers the fallback message in two situations:

- **Immediate RCS failure**: The recipient's
  device or carrier does not support RCS, or the RCS channel rejects the
  message.
- **TTL expiry**: You set a
  `TimeToLive` value and the message is not delivered before the
  timer expires. For more information about message expiration, see
  [Configuring RCS message expiration](rcs-message-expiration.md "rcs-message-expiration.md").

If you do not include `FallbackConfiguration` in the request and the RCS
message fails or expires, no fallback message is sent.

## Per-message fallback compared to pool-based fallback

Per-message fallback on `SendRcsMessage` differs from the automatic
pool-based fallback available with `SendTextMessage`. For details on
pool-based fallback, see
[RCS to SMS fallback using phone pools](rcs-sms-fallback.md "rcs-sms-fallback.md").

Comparison of fallback mechanisms| Feature | Pool-based fallback (`SendTextMessage`) | Per-message fallback (`SendRcsMessage`) |
| --- | --- | --- |
| Configuration | Automatic when a pool contains both an RCS agent and SMS<br>identities | Explicit: you include `FallbackConfiguration` in<br>each request |
| Fallback channel | SMS (selected by the pool) | SMS or MMS (you choose with `Channel`) |
| Fallback content | Same message body | You provide separate content tailored for SMS or MMS |
| Identity selection | Pool selects the origination identity | You specify a phone number or sender ID |
| Trigger | RCS not supported (timeout-based) | Immediate RCS failure or TTL expiry |

## FallbackConfiguration structure

The `FallbackConfiguration` parameter is a single object on the
`SendRcsMessage` request. You set the `Channel` field to
indicate whether the fallback is SMS or MMS, then provide the corresponding content
fields.

FallbackConfiguration fields| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `Channel` | String | Yes | The fallback channel. Valid values: `SMS` or<br>`MMS`. |
| `MessageBody` | String | Conditional | The text body of the fallback message. Maximum 1,600 characters.<br>Required when `Channel` is `SMS`. For<br>`MMS`, at least one of `MessageBody` or<br>`MediaUrls` must be provided. |
| `MediaUrls` | List of strings | Conditional | One or more media URLs for an MMS fallback. For<br>`MMS`, at least one of `MessageBody` or<br>`MediaUrls` must be provided. |
| `OriginationIdentity` | String | Conditional | The origination identity for the fallback message. Accepts a<br>phone number or sender ID (by value, ID, or ARN); you cannot<br>specify a pool or an RCS agent. If you omit this field and the<br>original message was sent through a pool, the service selects a<br>suitable number from that pool. |

###### Important

The fallback `MessageBody` limit is 1,600 characters. This is
shorter than the 3,072-character limit for the RCS
`TextMessage` body. Craft your fallback content to fit within the
SMS or MMS character constraints.

The following JSON shows the structure of a `FallbackConfiguration`
object for an SMS fallback:

```
{
    "Channel": "SMS",
    "MessageBody": "Your order has shipped. Track at https://example.com/track/12345",
    "OriginationIdentity": "+18005550199"
}
```

The following JSON shows the structure for an MMS fallback:

```
{
    "Channel": "MMS",
    "MessageBody": "Your order has shipped.",
    "MediaUrls": ["https://cdn.example.com/shipping-confirmation.jpg"],
    "OriginationIdentity": "+18005550199"
}
```

## Configuring SMS fallback

To fall back to SMS, set `Channel` to `SMS` and provide a
`MessageBody`. Because SMS does not support suggestion chips or rich
cards, include any important URLs as plain text in the message body.

## Configuring MMS fallback

To fall back to MMS, set `Channel` to `MMS` and provide one
or more media URLs in `MediaUrls`. Use MMS fallback when your RCS message
contains visual content (such as a rich card with an image) and you want to preserve
the visual experience for recipients who do not support RCS.

## Combining fallback with message expiration

When you set both `TimeToLive` and `FallbackConfiguration`
on a request, AWS End User Messaging attempts RCS delivery for the duration of the TTL. If the
message is not delivered before the timer expires, the service sends the fallback
message. This pattern is useful for time-sensitive content such as one-time passwords
or appointment reminders.

For more information about configuring message expiration, see
[Configuring RCS message expiration](rcs-message-expiration.md "rcs-message-expiration.md").

The following example sets a 60-second TTL with SMS fallback:

```
{
    "DestinationPhoneNumber": "+12065550100",
    "OriginationIdentity": "rcs-agent-1234567890",
    "RcsMessageContent": "{\"Content\":{\"TextMessage\":{\"Body\":\"Your verification code is 483291.\"}}}",
    "TimeToLive": 60,
    "FallbackConfiguration": {
        "Channel": "SMS",
        "MessageBody": "Your verification code is 483291.",
        "OriginationIdentity": "+18005550199"
    }
}
```

## Best practices

- **Write fallback content separately.** Rich
  RCS content (suggestion chips, rich cards, carousels) does not translate
  directly to SMS or MMS. Write a concise, self-contained fallback message
  rather than reusing the RCS body verbatim.
- **Include URLs as plain text in SMS fallback.**
  Replace interactive suggestion chips (such as `OpenUrl` actions)
  with inline URLs in the `MessageBody`.
- **Use MMS fallback for visual content.** If
  your RCS message features a rich card or carousel with images, MMS fallback
  preserves the visual context for recipients without RCS support.
- **Set a reasonable TTL.** When you combine
  fallback with `TimeToLive`, choose a TTL that balances delivery
  attempts with timeliness. For time-sensitive messages, a TTL of 30 to
  60 seconds gives a brief RCS delivery window before falling back. For
  general messages, a longer window (minutes to hours) gives the RCS channel
  more opportunity to succeed.
- **Verify your origination identity.** The
  `OriginationIdentity` in the fallback configuration must be a
  phone number or sender ID that is registered in your AWS End User Messaging account and
  capable of sending SMS or MMS to the destination country.

## Related resources

- [RCS to SMS fallback using phone pools](rcs-sms-fallback.md "rcs-sms-fallback.md") for information about automatic
  pool-based fallback with `SendTextMessage`.
- [Configuring RCS message expiration](rcs-message-expiration.md "rcs-message-expiration.md") for information about configuring
  TTL and expiration behavior.
- [Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md") for an overview of RCS rich message
  types and the `SendRcsMessage` API.
