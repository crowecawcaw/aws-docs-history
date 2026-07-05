# Sending RCS rich cards

A rich card combines media, text, and suggested actions into a single structured
message. Recipients see the card as a native UI element in their messaging client,
providing an app-like experience. Use rich cards to present information that
encourages interaction, such as product details, booking confirmations, or
promotional offers.

###### Important

You can use RCS rich media messaging (including rich cards) in all countries where
RCS is supported. For more information, see
[Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md").

To group multiple cards into a scrollable set, see
[Sending RCS carousels](rcs-carousels.md "rcs-carousels.md").

###### Topics

- [When to use a rich card](#rcs-rich-cards-when "#rcs-rich-cards-when")
- [Rich card components](#rcs-rich-cards-components "#rcs-rich-cards-components")
- [Card orientation](#rcs-rich-cards-orientation "#rcs-rich-cards-orientation")
- [Media and heights](#rcs-rich-cards-media "#rcs-rich-cards-media")
- [Card-level suggestions](#rcs-rich-cards-suggestions "#rcs-rich-cards-suggestions")
- [RcsMessageContent structure](#rcs-rich-cards-structure "#rcs-rich-cards-structure")
- [Sending a rich card](#rcs-rich-cards-sending "#rcs-rich-cards-sending")
- [Cross-platform rendering](#rcs-rich-cards-rendering "#rcs-rich-cards-rendering")
- [Rich card limits](#rcs-rich-cards-limits "#rcs-rich-cards-limits")

## When to use a rich card

Rich cards are well suited for messages that benefit from a visual layout
with interactive elements. Common use cases include:

- **Product showcases**: Display an image,
  product name, price, and a purchase button in one message.
- **Booking confirmations**: Show reservation
  details with a calendar link and directions button.
- **Appointment details**: Present date, time,
  location, and options to confirm or reschedule.
- **Promotional offers**: Highlight a deal
  with media and a clear call to action.

If your message requires only text with optional suggestions, use a
[Sending RCS text messages](rcs-text-messages.md "rcs-text-messages.md") instead.
If you need to send a file without additional card structure, see
[Sending RCS file messages](rcs-file-messages.md "rcs-file-messages.md").

## Rich card components

A standalone rich card consists of the following components. At least one of
`Media`, `Title`, or `Description` is
required in `CardContent`.

Rich card components| Component | Required | Description |
| --- | --- | --- |
| `Media` | No | An image, GIF, or video displayed within the card. Supported<br>formats include JPEG, PNG, GIF, and MP4. The maximum file size is<br>100 MB. |
| `Title` | No | A short headline for the card. Maximum 200 characters. |
| `Description` | No | Body text providing additional detail. Maximum 2,000<br>characters. |
| `Suggestions` | No | Up to 4 suggested actions or replies attached to the card.<br>See [Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md"). |

## Card orientation

The `CardOrientation` field controls the layout relationship between
media and text content. This field is required.

`VERTICAL`
Media displays at the top of the card with title, description,
and suggestions below. Vertical orientation is the recommended default
for cross-platform compatibility.

`HORIZONTAL`
Media displays on the left or right side of the card with
text content beside it. The media area has a fixed width of
128 density-independent pixels (DP). Use
`ThumbnailImageAlignment` to control whether the media
appears on the left or right.

###### Warning

Horizontal orientation causes image truncation on iOS devices. Use
`VERTICAL` orientation for cross-platform deployments.

## Media and heights

The `Media` object contains a `FileUrl` (required),
an optional `ThumbnailUrl`, and an optional `Height`
value. The `FileUrl` must match the pattern
`^(https://|s3://).+$` and can be a maximum of 2,000 characters.
The maximum media file size is 100 MB.

For details on supported media formats, delivery options, and S3 presigned URLs,
see [Sending RCS file messages](rcs-file-messages.md "rcs-file-messages.md").

Media height values| Height | Size | Description |
| --- | --- | --- |
| `SHORT` | 112 DP | Compact display. Use for thumbnails or when text content is<br>the primary focus. |
| `MEDIUM` | 168 DP | Balanced display. Recommended default for most use<br>cases. |
| `TALL` | 264 DP | Maximum display area. Use when media is the primary<br>content. |

###### Note

iOS renders all media height values identically, ignoring the specified
height setting. Use `TALL` to maximize the display area on
Android devices while maintaining acceptable rendering on iOS.

## Card-level suggestions

You can attach up to 4 suggestions to a rich card by including them in the
`CardContent.Suggestions` array. Card-level suggestions appear
directly below the card content.

In addition to card-level suggestions, you can include up to 11 message-level
suggestions in the top-level `Suggestions` array of the
`RcsMessageContent` structure. Message-level suggestions appear as
persistent chips below the entire message.

For the full list of suggestion types (including `Reply`,
`OpenUrl`, `DialPhone`, `ShowLocation`,
`RequestLocation`, and `CreateCalendarEvent`), see
[Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md").

## RcsMessageContent structure

The following JSON shows the structure of the `RcsMessageContent`
parameter for a standalone rich card. Pass this JSON as a string to the
`--rcs-message-content` parameter in the AWS CLI or as the
`RcsMessageContent` parameter in the SDK.

```
{
  "Content": {
    "RichCard": {
      "StandaloneCard": {
        "CardOrientation": "VERTICAL",
        "CardContent": {
          "Title": "Your card title",
          "Description": "Additional details about the card content.",
          "Media": {
            "FileUrl": "https://example.com/image.jpg",
            "ThumbnailUrl": "https://example.com/thumb.jpg",
            "Height": "MEDIUM"
          },
          "Suggestions": [
            {
              "Reply": {
                "Text": "Confirm",
                "PostbackData": "confirm_action"
              }
            },
            {
              "OpenUrl": {
                "Text": "View details",
                "PostbackData": "view_details",
                "Url": "https://www.example.com/details"
              }
            }
          ]
        }
      }
    }
  },
  "Suggestions": [
    {
      "Reply": {
        "Text": "Help",
        "PostbackData": "help_menu"
      }
    }
  ]
}
```

In this structure:

- `Content.RichCard.StandaloneCard` contains the card
  definition.
- `CardOrientation` is required and accepts
  `VERTICAL` or `HORIZONTAL`.
- `ThumbnailImageAlignment` is optional and applies
  only to horizontal cards.
- `CardContent.Suggestions` holds card-level
  suggestions (maximum 4).
- The top-level `Suggestions` array holds message-level
  suggestions (maximum 11).

## Sending a rich card

Use the `SendRcsMessage` API action to send a rich card. Specify
your pool or AWS RCS Agent as the `--origination-identity` and
pass the rich card JSON structure as the `--rcs-message-content`
parameter.

## Cross-platform rendering

Rich card rendering varies between Android and iOS devices. Follow these
recommendations for consistent results:

Cross-platform recommendations| Recommendation | Reason |
| --- | --- |
| Use `VERTICAL` orientation | Horizontal orientation causes image truncation on iOS. |
| Use `TALL` media height | iOS ignores the height value. `TALL` maximizes the<br>display area on Android. |
| Keep the title to 3 lines or fewer | Prevents media cropping on iOS with accessibility<br>settings enabled. |
| Use `OpenUrl` suggestions for links | URLs in the description text are not clickable on either<br>platform. |
| Test GIF media on iOS | Confirm the static first frame renders<br>acceptably. |

## Rich card limits

Rich card limits| Resource | Limit |
| --- | --- |
| Title length | 200 characters |
| Description length | 2,000 characters |
| Card-level suggestions | 4 per card |
| Message-level suggestions | 11 per message |
| Total message payload | 250 KB |
| Media file size | 100 MB |
| `FileUrl` length | 2,000 characters |
