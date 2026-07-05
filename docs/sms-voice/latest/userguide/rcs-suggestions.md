# Configuring RCS suggestions

Suggestions are interactive chips that appear below or within an RCS message. They guide
recipients through a conversation by presenting predefined replies and actions, such as
opening a URL, calling a phone number, or sharing a location, without requiring the
recipient to type. Suggestions are how you build interactive, conversational
experiences with `SendRcsMessage`.

You can add suggestions to any content type (text, file, rich card, and carousel) at
two levels:

- **Message-level**. Provided in the top-level
  `Suggestions` list of `RcsMessageContent`, alongside
  `Content`. You can include up to 11 suggestions per message.
- **Card-level**. Provided in the
  `Suggestions` list of an individual rich card or carousel card. You
  can include up to 4 suggestions per card.
  AWS End User Messaging supports six suggestion types: `Reply`, `OpenUrl`,
  `DialPhone`, `ShowLocation`, `RequestLocation`, and
  `CreateCalendarEvent`. Every suggestion requires a `Text` label
  (up to 25 characters) and `PostbackData` (up to 2,048 characters).

###### Topics

- [How postback data works](#rcs-suggestions-postback "#rcs-suggestions-postback")
- [Suggestion display](#rcs-suggestions-display "#rcs-suggestions-display")
- [Reply](#rcs-suggestions-reply "#rcs-suggestions-reply")
- [OpenUrl](#rcs-suggestions-openurl "#rcs-suggestions-openurl")
- [DialPhone](#rcs-suggestions-dialphone "#rcs-suggestions-dialphone")
- [ShowLocation](#rcs-suggestions-showlocation "#rcs-suggestions-showlocation")
- [RequestLocation](#rcs-suggestions-requestlocation "#rcs-suggestions-requestlocation")
- [CreateCalendarEvent](#rcs-suggestions-calendar "#rcs-suggestions-calendar")
- [Receiving suggestion taps](#rcs-suggestions-receiving "#rcs-suggestions-receiving")
- [Suggestion limits](#rcs-suggestions-limits "#rcs-suggestions-limits")
- [Best practices](#rcs-suggestions-best-practices "#rcs-suggestions-best-practices")
- [Related topics](#rcs-suggestions-related "#rcs-suggestions-related")

## How postback data works

Each suggestion includes a `PostbackData` string of up to 2,048
characters that AWS End User Messaging sends back to your application when the recipient chooses the
suggestion. Postback data is not visible to the recipient. Use it to encode routing
information, intent identifiers, session context, or any metadata your backend needs
to process the selection.

When a recipient chooses a suggestion, AWS End User Messaging delivers an inbound message event to
the Amazon SNS topic that you configure for two-way messaging. Route your logic on
`postbackData` rather than the display text. For details about inbound
events, see [RCS message events](rcs-events.md "rcs-events.md").

## Suggestion display

Transient suggestions (default)

Transient suggestions appear outside the message bubble, below the
most recent message. They disappear after the recipient chooses one or
sends any message.

Persistent suggestions

Persistent suggestions appear inside the message bubble and remain
visible after the recipient scrolls past or interacts with later
messages. Persistent display is determined by the suggestion's position
within a rich card. Suggestions attached to standalone rich cards render
as persistent on supported clients.

## Reply

A `Reply` suggestion sends a predefined text reply back to your agent.
The display text appears as a sent message in the conversation, and the
`PostbackData` is delivered to your application.

```
{ "Reply": { "Text": "Yes, confirm", "PostbackData": "confirm_order_12345" } }
```

| Field          | Required | Constraint             |
| -------------- | -------- | ---------------------- |
| `Text`         | Yes      | Up to 25 characters    |
| `PostbackData` | Yes      | Up to 2,048 characters |

## OpenUrl

An `OpenUrl` suggestion opens a URL. By default the URL opens in the
device browser. To open the URL in a webview that keeps the recipient inside the
messaging app, set `Application` to `WEBVIEW` and specify a
`WebviewViewMode`.

```
{
  "OpenUrl": {
    "Text": "Complete payment",
    "PostbackData": "pay_12345",
    "Url": "https://example.com/pay",
    "Application": "WEBVIEW",
    "WebviewViewMode": "TALL"
  }
}
```

| Field             | Required    | Constraint                                                          |
| ----------------- | ----------- | ------------------------------------------------------------------- |
| `Text`            | Yes         | Up to 25 characters                                                 |
| `PostbackData`    | Yes         | Up to 2,048 characters                                              |
| `Url`             | Yes         | Must begin with `https://`. Up to 2,048 characters                  |
| `Application`     | No          | `WEBVIEW` to open in an in-app webview                              |
| `WebviewViewMode` | Conditional | Required when `Application` is `WEBVIEW`: `FULL`, `HALF`, or `TALL` |

###### Note

The `Url` must use the `https://` protocol. An
`s3://` URL is rejected. Unlike a standard browser open, a webview
keeps the recipient inside the conversation, which is useful for short flows
such as a payment or a form.

## DialPhone

A `DialPhone` suggestion starts a phone call to the number you
specify.

```
{ "DialPhone": { "Text": "Call support", "PostbackData": "dial_support", "PhoneNumber": "+18005551234" } }
```

| Field          | Required | Constraint                               |
| -------------- | -------- | ---------------------------------------- |
| `Text`         | Yes      | Up to 25 characters                      |
| `PostbackData` | Yes      | Up to 2,048 characters                   |
| `PhoneNumber`  | Yes      | E.164 format, for example `+18005551234` |

## ShowLocation

A `ShowLocation` suggestion opens a map at the coordinates you
specify.

```
{
  "ShowLocation": {
    "Text": "View on map",
    "PostbackData": "show_store_loc",
    "Latitude": 47.6062,
    "Longitude": -122.3321,
    "Label": "Seattle store"
  }
}
```

| Field          | Required | Constraint                    |
| -------------- | -------- | ----------------------------- |
| `Text`         | Yes      | Up to 25 characters           |
| `PostbackData` | Yes      | Up to 2,048 characters        |
| `Latitude`     | Yes      | -90.0 to 90.0                 |
| `Longitude`    | Yes      | -180.0 to 180.0               |
| `Label`        | No       | Display label for the map pin |

## RequestLocation

A `RequestLocation` suggestion prompts the recipient to share their
current location. The shared coordinates arrive as a separate inbound
location event.

```
{ "RequestLocation": { "Text": "Share location", "PostbackData": "request_user_location" } }
```

| Field          | Required | Constraint             |
| -------------- | -------- | ---------------------- |
| `Text`         | Yes      | Up to 25 characters    |
| `PostbackData` | Yes      | Up to 2,048 characters |

## CreateCalendarEvent

A `CreateCalendarEvent` suggestion creates a calendar event on the
recipient's device with the details you specify.

```
{
  "CreateCalendarEvent": {
    "Text": "Add to calendar",
    "PostbackData": "calendar_appt_5678",
    "Title": "Service appointment",
    "StartTime": "2026-05-28T14:00:00Z",
    "EndTime": "2026-05-28T15:00:00Z",
    "Description": "Downtown location. Arrive 10 minutes early."
  }
}
```

| Field          | Required | Constraint             |
| -------------- | -------- | ---------------------- |
| `Text`         | Yes      | Up to 25 characters    |
| `PostbackData` | Yes      | Up to 2,048 characters |
| `Title`        | Yes      | Up to 100 characters   |
| `StartTime`    | Yes      | Event start time       |
| `EndTime`      | Yes      | Event end time         |
| `Description`  | No       | Up to 500 characters   |

## Receiving suggestion taps

When a recipient chooses a suggestion, AWS End User Messaging publishes an inbound message to your
two-way SNS topic. The `messageBody` contains a JSON object with the
suggestion type, the display text, and the `postbackData` you set. Route
your logic on `postbackData`.

```
{
  "originationNumber": "+12065551234",
  "destinationNumber": "rcs-a1b2c3d4",
  "messageBody": "{\"type\":\"SUGGESTION\",\"text\":\"Yes, confirm\",\"postbackData\":\"confirm_order_12345\"}",
  "inboundMessageId": "msg-abc123def456"
}
```

For a `RequestLocation` tap, the recipient's coordinates arrive in a
separate inbound location event. For the full inbound event reference, see
[RCS message events](rcs-events.md "rcs-events.md").

## Suggestion limits

| Constraint                        | Limit            |
| --------------------------------- | ---------------- |
| Suggestion `Text` length          | 25 characters    |
| `PostbackData` length             | 2,048 characters |
| Suggestions per message           | 11               |
| Suggestions per card              | 4                |
| `CreateCalendarEvent` title       | 100 characters   |
| `CreateCalendarEvent` description | 500 characters   |

## Best practices

- Keep text action-oriented. Use verbs such as _Track order_, _Call support_, or _View menu_.
- Offer 3 to 5 options. More than 5 can overwhelm recipients.
- Route on `PostbackData`, not display text. Text is for people, postback data is for your application.
- Structure postback data consistently, for example as `action:value` pairs or JSON.
- Handle the case where a recipient types free text instead of tapping a suggestion.
- Combine suggestion types in a single message, such as a `Reply`, an `OpenUrl`, and a `DialPhone`.

For deeper guidance, see [RCS best practices](rcs-best-practices.md "rcs-best-practices.md").

## Related topics

- [Sending RCS text messages](rcs-text-messages.md "rcs-text-messages.md")
- [Sending RCS rich cards](rcs-rich-cards.md "rcs-rich-cards.md")
- [RCS message events](rcs-events.md "rcs-events.md")
