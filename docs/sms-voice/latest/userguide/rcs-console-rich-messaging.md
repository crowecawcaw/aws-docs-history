# Sending rich RCS messages from the console

The AWS End User Messaging console provides a visual message composer that you can use to build and
send rich RCS messages without writing code. The composer maps directly to the
`SendRcsMessage` API and supports all content types: text messages, file
messages, rich cards, and carousels. You can attach interactive suggestions to any
message type, configure time-to-live (TTL) settings, and set up SMS or MMS fallback
for recipients whose devices do not support RCS.

You compose and send rich messages from the **Outbound test
messages** tab of the RCS testing interface. Messages are sent to verified
RBM testers so that you can validate rendering and delivery before you integrate the
`SendRcsMessage` API into your application.

As you configure the message, a real-time phone preview displays how the message
renders on the recipient's device. You can also copy the equivalent JSON payload or
AWS CLI command to use the same message structure in your application code.

For more information about the message types and their API structure, see
[Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md"). For details
on suggestion types and behavior, see
[Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md").

## Prerequisites

Before you send rich RCS messages from the console, confirm the following:

- Your RCS agent is in **Testing** or
  **Active** state.
- You have at least one verified RBM tester phone number associated with
  your agent. For setup instructions, see
  [Testing RCS messages](rcs-testing.md "rcs-testing.md").
- If you plan to send media files from Amazon S3, the S3 bucket must have
  a bucket policy that grants `sms-voice.amazonaws.com` read
  access. For details, see
  [Sending RCS file messages](rcs-file-messages.md "rcs-file-messages.md").

## Sending a rich RCS message

Use the following procedure to compose and send a rich RCS message from the
AWS End User Messaging console.

1. Open the AWS End User Messaging console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under
   **Configurations**, choose
   **RCS agents**.
3. Choose the agent that you want to use as the origination identity. The
   agent status must be **Testing** or
   **Active**.
4. Choose the **Testing** tab.
5. In the **RCS testing interface**, choose the
   **Outbound test messages** tab.
6. In the **Send test RCS message** section,
   for **Select RBM tester**, choose a verified
   RBM tester phone number.
7. (Optional) For **Configuration set**, choose
   a configuration set to track message events.
8. For **Select API**, choose
   **SendRcsMessage**.
9. For **Select message format**, choose the
   message type that you want to send:

   - **Text**: Enter a message body
     (up to 3,072 characters).
   - **File**: For the media source,
     choose **S3 bucket** or
     **Public URL**, and then enter the
     **S3 URI** (or HTTPS URL) of the file
     to send. Choose **Browse S3** to
     select a file from a bucket, or
     **View** to open the referenced file
     in a new browser tab. The maximum file size is 100 MB. Optionally,
     provide a thumbnail URL for video or PDF files.
   - **Rich card**: Configure the
     following card fields. At least one of title, description, or
     media is required.

     - **Card orientation**: Choose
       `VERTICAL` or `HORIZONTAL`.
     - **Card title**: Enter a
       title (up to 200 characters).
     - **Card description**: Enter
       a description (up to 2,000 characters).
     - **Media URL**: For the media
       source, choose **S3 bucket**
       or **Public URL**, and then
       enter the **S3 URI** (or HTTPS
       URL). Choose **Browse S3** to
       select a file, or **View** to
       open it in a new browser tab. The maximum file size is
       100 MB.
     - (Optional) **Media thumbnail
       URL**: A preview image shown before the full media
       loads.
     - (**HORIZONTAL** orientation
       only) **Thumbnail alignment**:
       Choose `LEFT` or `RIGHT` to position
       the thumbnail image.
     - **Card suggestions**:
       Add up to 4 suggestions that render as buttons within the
       card boundary. For suggestion types, see
       [Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md").

   - **Carousel**: Configure the
     following:

     - **Card width**: Choose
       `SMALL` or `MEDIUM`.
     - **Media height (all
       cards)**: Choose `SHORT` or
       `MEDIUM`. All cards in a carousel use the same
       media height.
     - **Cards**: Add between
       2 and 10 cards. Each card includes a card title, card
       description, a media URL (S3 bucket or public URL, maximum
       100 MB), and up to 4 card suggestions. At least one of
       title, description, or media is required for each
       card.

   - **JSON**: Paste a raw
     `RcsMessageContent` JSON payload directly. Choose
     **Format JSON** to format the payload.
     The console validates the structure and updates the phone preview
     in real time.

10. (Optional) Configure media files using the S3 browser:

    1. Choose **Browse S3**.
    2. Select a bucket from the dropdown list.
    3. Navigate through prefixes (folders) to locate your file.
    4. Select the file. The URL field populates automatically.###### Note

The S3 bucket must have a bucket policy that grants
`sms-voice.amazonaws.com` read access to the objects. For
the required policy, see
[Sending RCS file messages](rcs-file-messages.md "rcs-file-messages.md"). 11. (Optional) Add message-level suggestions. In the
**Suggestions** section:

    1. Choose **Add suggestion**.
    2. For **Suggestion type**, choose one
     of **Reply**,
     **Open URL**,
     **Dial Phone**,
     **Show Location**,
     **Request Location**, or
     **Calendar Event**.
    3. Enter the required fields for the selected type. All suggestion
     types require a `Text` value (up to 25 characters)
     and `PostbackData` (up to 2,048 characters).
    4. Repeat to add up to 11 message-level suggestions.Message-level suggestions render as a chip list below the entire

message. You can attach message-level suggestions to any content type
(text, file, rich card, or carousel). For details, see
[Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md"). 12. (Optional) Configure the time-to-live (TTL) setting. Expand
**Advanced options** and enter a value in the
**Time to live (seconds)** field. Valid values
range from 1 to 172,800 seconds (48 hours). We recommend a minimum value of 10 seconds.

If the message is not delivered before the TTL expires, the service
triggers a TTL expiration event. If you configured fallback, the fallback
message is sent at that time.

The **Advanced options** section also
contains **Max price (USD)**,
**Dry run**,
**Message feedback**,
**Protect configuration**, and
**Context** (optional key-value
metadata). 13. (Optional) Configure SMS or MMS fallback. Expand the
**Fallback configuration** section:

    1. For **Fallback channel**, choose
     **SMS** or
     **MMS**.
    2. For **Fallback message body**, enter
     the message text (up to 1,600 characters). A message body is
     required when a fallback channel is selected.
    3. For MMS, you can also provide one or more media URLs.
    4. For **Origination identity**, enter
     the phone number or sender ID to use for the fallback SMS or MMS
     message. This is required when sending from an RCS agent.Fallback is triggered when the message cannot be delivered over RCS

(for example, when the recipient's device does not support RCS or when
the TTL expires). For more information, see
[Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md"). 14. (Optional) In **Advanced options**, enable
**Dry run** to validate the message structure
without sending. This does not incur charges and does not deliver the
message to the recipient. 15. Review the phone preview on the right side of the composer. The
preview updates in real time and shows:

    * Content rendering (text, media, card layout, carousel
     scroll)
    * Suggestion chips below the message
    * Card-level buttons within cards

###### Note

The preview approximates Android rendering. Display on iOS or
other RCS clients might differ. The preview does not simulate
suggestion selection behavior. 16. Choose **Send test message** to send the
message to the selected RBM tester, or use one of the following
options:

    * **Copy JSON**: Copies the message
     JSON to your clipboard. Choose
     **RcsMessageContent** to copy only the
     content portion, or **Full API request**
     to copy the complete `SendRcsMessage` request
     body.
    * **Copy CLI command**: Copies the
     equivalent `aws pinpoint-sms-voice-v2 send-rcs-message`
     command.

## Input validation

The console performs real-time validation as you configure the message.
Validation errors display inline next to the affected field. The following
table summarizes the validation rules.

Console validation rules| Field | Rule |
| --- | --- |
| Phone number | Must be E.164 format |
| Media URL | Must start with `https://` or `s3://` |
| Media file size | Maximum 100 MB |
| Suggestion text | Maximum 25 characters |
| Postback data | Maximum 2,048 characters |
| Card title | Maximum 200 characters |
| Card description | Maximum 2,000 characters |
| Carousel cards | Minimum 2, maximum 10 |
| Card-level suggestions | Maximum 4 per card |
| Message-level suggestions | Maximum 11 |
| Text message body | Maximum 3,072 characters |
| TTL | 1 to 172,800 seconds |
| Fallback message body | Maximum 1,600 characters |

## Related resources

- [Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md")
- [Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md")
- [Testing RCS messages](rcs-testing.md "rcs-testing.md")
- [Sending RCS file messages](rcs-file-messages.md "rcs-file-messages.md")
