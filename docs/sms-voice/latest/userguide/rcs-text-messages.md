# Sending RCS text messages

A `TextMessage` is the simplest content type you can send with the
`SendRcsMessage` API. It consists of a plain-text body (up to 3,072 characters)
with optional suggestion chips that appear as interactive buttons below the message.

## How RCS text messages differ from SMS

Text messages sent through `SendRcsMessage` differ from those sent through
`SendTextMessage` (SMS) in two ways:

- **Suggestion chips**: You can attach up to 11
  suggestion chips to an RCS text message. With these chips, recipients can reply, open a
  URL, dial a phone number, share a location, or create a calendar event in
  one step. SMS does not support suggestions.
- **Single-message delivery**: An RCS text message
  arrives as a single message regardless of length (up to 3,072 characters).
  Carriers split SMS messages longer than 160 characters into multiple segments, which
  might arrive out of order or with delays between segments.

For details on all available suggestion types and their parameters, see
[Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md").

## RcsMessageContent structure for text messages

When you call `SendRcsMessage`, you pass the message payload as the
`RcsMessageContent` parameter. For a text message, set the
`Content` field to a `TextMessage` object containing a
`Body` string. To include suggestion chips, add a `Suggestions`
array as a top-level sibling of `Content`.

The following JSON snippet shows the structure of `RcsMessageContent` for a
text message with suggestions:

```
{
  "Content": {
    "TextMessage": {
      "Body": "What would you like to do?"
    }
  },
  "Suggestions": [
    {
      "Reply": {
        "Text": "Check order status",
        "PostbackData": "action=check_order"
      }
    },
    {
      "OpenUrl": {
        "Text": "View details",
        "PostbackData": "action=view",
        "Url": "https://example.com/orders/1234"
      }
    }
  ]
}
```

In this example:

- `Content.TextMessage.Body` contains the message text (required,
  1 to 3,072 characters).
- `Suggestions` is a top-level array (optional, up to 11 items). Each
  suggestion requires a `Text` field (up to 25 characters) and a
  `PostbackData` field (up to 2,048 characters).

The `Suggestions` array supports six action types: `Reply`,
`OpenUrl`, `DialPhone`, `ShowLocation`,
`RequestLocation`, and `CreateCalendarEvent`. You can mix
different suggestion types in a single message. For complete details on each type, see
[Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md").

## Sending a text message

To send an RCS text message, call `SendRcsMessage` with the following
required parameters:

- `DestinationPhoneNumber`: The recipient's phone number in E.164
  format.
- `OriginationIdentity`: The pool ID or AWS RCS Agent that sends
  the message.
- `RcsMessageContent`: The JSON string containing
  `Content` with a `TextMessage` object.

You call the API using the AWS CLI
(`aws pinpoint-sms-voice-v2 send-rcs-message`) or an AWS SDK such as
the boto3 `pinpoint-sms-voice-v2` client.

## SMS or MMS fallback

If the recipient's device does not support RCS or is temporarily unreachable on the
RCS channel, you can configure the message to fall back to SMS or MMS. To enable
fallback, include a `FallbackConfiguration` object in your
`SendRcsMessage` request. The `FallbackConfiguration` specifies
the fallback channel (`SMS` or `MMS`), the fallback message body,
and the origination identity (a phone number or sender ID) to use for the fallback
message.

Fallback is optional. If you omit `FallbackConfiguration` and the
recipient cannot receive RCS, the message is not delivered.

For more information about configuring fallback behavior, see
[Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md").

## Text message limits

| Resource                         | Limit                    | Notes                                        |
| -------------------------------- | ------------------------ | -------------------------------------------- |
| Message body (`Body`)            | 3,072 characters (UTF-8) | Required. Must contain at least 1 character. |
| Suggestions per message          | 11                       | Combined total of replies and actions.       |
| Suggestion display text (`Text`) | 25 characters            | Applies to all suggestion types.             |
| Postback data (`PostbackData`)   | 2,048 characters         | Required for all suggestion types.           |

## When to use text messages

Use `TextMessage` for:

- Notifications such as order confirmations, shipping updates, and appointment
  reminders.
- One-time passwords and verification codes.
- Conversational prompts that offer reply options as suggestion chips, enabling
  guided interactions without free-text input.
- Short status updates where the content does not require images or structured
  layouts.

For messages that require images, videos, or structured layouts with titles and
descriptions, use rich cards or carousels instead. See
[Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md").
