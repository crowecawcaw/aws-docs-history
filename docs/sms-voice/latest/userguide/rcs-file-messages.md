# Sending RCS file messages

You can use the `FileMessage` content type in the
`SendRcsMessage` API to send images, videos, audio files, and PDFs as
standalone messages to your recipients. File messages appear as inline media in the
recipient's messaging app.

File messages are distinct from rich card media. A file message delivers a single
piece of media as the entire message content, while rich cards combine media with text
and suggested actions. For information about rich cards, see
[Sending RCS rich cards](rcs-rich-cards.md "rcs-rich-cards.md").

You can attach message-level suggestions (such as reply chips or action buttons) to
file messages. For details about suggestions, see
[Configuring RCS suggestions](rcs-suggestions.md "rcs-suggestions.md").

## FileMessage structure

The `FileMessage` object is nested inside the `Content`
field of the `RcsMessageContent` parameter. Message-level
`Suggestions` are a sibling of `Content` (not nested inside
it).

```
{
    "Content": {
        "FileMessage": {
            "FileUrl": "s3://my-media-bucket/campaigns/welcome-image.png",
            "ThumbnailUrl": "s3://my-media-bucket/thumbnails/welcome-thumb.jpg"
        }
    },
    "Suggestions": []
}
```

`FileUrl` (required)

The S3 or HTTPS URL of the file to send. Maximum length is
2,000 characters. The URL must match the pattern
`^(https://|s3://).+$`. The maximum file size is
100 MB.

`ThumbnailUrl` (optional)

The S3 or HTTPS URL of a thumbnail image. Maximum length is
2,000 characters. Follows the same URL pattern as
`FileUrl`. Recommended for video and PDF files.

## File URL sources

The `FileUrl` parameter accepts two URL formats:

- **Amazon S3 URLs**
  (`s3://bucket-name/object-key`). When you specify an S3 URL,
  AWS End User Messaging retrieves the object, rehosts it, and generates a time-limited
  presigned URL for delivery to the recipient's device. The S3 bucket must
  have a resource-based policy that grants the service read access. See
  [S3 bucket policy for file delivery](#rcs-file-messages-s3-policy "#rcs-file-messages-s3-policy").
- **HTTPS URLs**
  (`https://cdn.example.com/path/to/file.jpg`). The URL is
  passed through to the carrier for delivery. The URL must be publicly
  accessible without authentication. Plain `http://` URLs are
  not supported.

###### Note

When you use an S3 URL, the API validates at request time that the object
exists, is within size limits, and is accessible. If validation fails, the API
returns a `ValidationException` with a descriptive error message.
HTTPS URLs are not validated at request time in the same way.

## S3 bucket policy for file delivery

To allow AWS End User Messaging to retrieve files from your Amazon S3 bucket, attach the
following resource-based policy to the bucket:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "sms-voice.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET/*"
        }
    ]
}
```

Replace `YOUR-BUCKET` with your bucket name. To restrict access to
a specific prefix, replace `/*` with the desired path (for example,
`arn:aws:s3:::YOUR-BUCKET/rcs-media/*`).

###### Note

If your bucket uses SSE-KMS encryption, you must also grant the
`sms-voice.amazonaws.com` service permission to use the KMS key
in the key policy. SSE-S3 encryption does not require additional
configuration.

## Supported media types and size limits

The following table lists the media types supported by `FileMessage`.

| MIME type         | Extensions  | Maximum size | Notes                                                      |
| ----------------- | ----------- | ------------ | ---------------------------------------------------------- |
| `image/jpeg`      | .jpeg, .jpg | 100 MB       | Recommended for photographs.                               |
| `image/png`       | .png        | 100 MB       | Supports transparency. Recommended for graphics and logos. |
| `image/gif`       | .gif        | 100 MB       | Animated GIFs play on Android. Rendered as static on iOS.  |
| `video/mp4`       | .mp4        | 5 MB         | H.264 codec recommended for broadest compatibility.        |
| `video/webm`      | .webm       | 5 MB         | VP8/VP9 codec. Primarily supported on Android.             |
| `audio/mp3`       | .mp3        | 100 MB       | Broadest playback support for audio.                       |
| `audio/aac`       | .aac        | 100 MB       | Alternative audio format.                                  |
| `application/pdf` | .pdf        | 100 MB       | Support varies by carrier and region.                      |

###### Important

The 100 MB file size limit is enforced at the API layer. Individual
carriers might impose lower limits for delivery to end devices. For video,
carriers commonly enforce a 5 MB maximum. Keep video files under 5 MB to
ensure successful delivery.

## Thumbnails

You can provide a thumbnail image for video and PDF file messages using the
`ThumbnailUrl` parameter. The thumbnail displays as a preview in the
conversation before the recipient opens or downloads the full file.

- Supported thumbnail formats: JPEG, PNG.
- The thumbnail URL follows the same format rules as
  `FileUrl` (S3 or HTTPS, maximum 2,000 characters).
- Use an aspect ratio that matches the original file to avoid cropping
  on the device.

## Sending a file message

To send a file message, call the `SendRcsMessage` API with a
`FileMessage` object inside the `RcsMessageContent`
parameter. You specify the origination identity (a pool or an AWS RCS Agent)
using the `--origination-identity` parameter.

The following JSON shows the `RcsMessageContent` value for a file
message with suggestions:

```
{
    "Content": {
        "FileMessage": {
            "FileUrl": "s3://my-media-bucket/documents/invoice.pdf",
            "ThumbnailUrl": "s3://my-media-bucket/thumbnails/invoice-thumb.jpg"
        }
    },
    "Suggestions": [
        {
            "Reply": {
                "Text": "Download receipt",
                "PostbackData": "action=download_receipt"
            }
        }
    ]
}
```

## Delivery and fallback

When you send a file message, AWS End User Messaging attempts to deliver it over the RCS
channel. If the recipient's device does not support RCS, or if the message
expires before delivery (based on the `TimeToLive` value), the service
can fall back to SMS or MMS depending on your fallback configuration.

You can configure SMS or MMS fallback at the pool level or per message. For
details about fallback behavior, see
[Sending rich RCS messages](rcs-rich-messaging.md "rcs-rich-messaging.md").

###### Important

RCS file messages are available in all countries where RCS is supported. For
the current list, see [Supported countries for RCS](rcs-supported-countries.md "rcs-supported-countries.md").
