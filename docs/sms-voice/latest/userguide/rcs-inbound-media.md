

# Receiving inbound RCS media
<a name="rcs-inbound-media"></a>

Users can send media (images, videos, audio files, and documents) in RCS conversations with your agent. When you configure inbound media storage, AWS End User Messaging downloads the media from the RCS provider, uploads it to your Amazon S3 bucket, and publishes a notification to your two-way Amazon SNS topic with the S3 location and file metadata.

For general information about receiving inbound RCS messages (text, location, and suggestion responses), see [Receiving inbound RCS messages](rcs-inbound.md). For information about sending rich media to users, see [Sending rich RCS messages](rcs-rich-messaging.md).

## How inbound media works
<a name="rcs-inbound-media-how-it-works"></a>

When a user sends a media file in an RCS conversation, AWS End User Messaging processes the message through the following steps:

1. The user sends an image, video, audio file, or document from their RCS messaging app.

1. AWS End User Messaging downloads the media from the RCS provider.

1. AWS End User Messaging uploads the media to your configured S3 bucket using the IAM role you specify.

1. AWS End User Messaging publishes a notification to your two-way SNS topic. The notification includes the S3 bucket, key, MIME type, and message metadata.

For `LOCATION` and `SUGGESTION` message types, no S3 upload occurs. The content is delivered directly in the SNS notification body. For details about these message types, see [Receiving inbound RCS messages](rcs-inbound.md).

## Configuring inbound media storage
<a name="rcs-inbound-media-config"></a>

To receive inbound media, configure the following fields on your RCS agent using the `UpdateRcsAgent` API. Two-way messaging must be enabled on the agent before you configure media storage.


**Inbound media configuration fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| TwoWayMediaS3BucketName | Yes | The name of the S3 bucket where AWS End User Messaging stores inbound media files. | 
| TwoWayMediaS3KeyPrefix | No | An optional prefix for S3 object keys. If specified, media objects are stored under this prefix in the bucket. | 
| TwoWayMediaS3Role | Yes | The ARN of the IAM role that AWS End User Messaging assumes to upload media files to your S3 bucket. | 

The S3 bucket and IAM role are required together. If you specify one, you must specify both.

### S3 key format
<a name="rcs-inbound-media-s3-key-format"></a>

Media objects are stored with the following key format, where the original file name is appended after a `#` separator:

```
{prefix}/rcs/{messageId}#{fileName}
```

For example, if you set the key prefix to `inbound-media`, a media file might be stored as:

```
inbound-media/rcs/msg-abc123def456#photo_2026.jpg
```

## Creating the IAM role for inbound media
<a name="rcs-inbound-media-iam-role"></a>

Create an IAM role that allows the AWS End User Messaging service to upload media files to your S3 bucket. The role requires a trust policy that permits the service to assume it, and a permission policy that grants `s3:PutObject` access to your bucket.

### Trust policy
<a name="rcs-inbound-media-trust-policy"></a>

The following trust policy allows the AWS End User Messaging service principal to assume the role. Replace `123456789012` with your AWS account ID.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "sms-voice.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                }
            }
        }
    ]
}
```

### Permission policy
<a name="rcs-inbound-media-permission-policy"></a>

The following permission policy grants the role access to write objects to your S3 bucket. Replace `my-rcs-media-bucket` with your bucket name.

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::my-rcs-media-bucket/*"
        }
    ]
}
```

**Note**  
Scope the IAM role narrowly to `s3:PutObject` only. The service does not require `s3:GetObject`, `s3:DeleteObject`, or other permissions for inbound media delivery.

## Configuring media storage (CLI)
<a name="rcs-inbound-media-cli-example"></a>

The following AWS CLI command configures inbound media storage on an existing RCS agent:

```
aws pinpoint-sms-voice-v2 update-rcs-agent \
    --rcs-agent-id rcs-agent-1234567890abcdef0 \
    --two-way-media-s3-bucket-name my-rcs-media-bucket \
    --two-way-media-s3-key-prefix "inbound-media" \
    --two-way-media-s3-role arn:aws:iam::123456789012:role/RcsInboundMediaRole \
    --region us-east-1
```

## Inbound media notification payload
<a name="rcs-inbound-media-notification"></a>

When AWS End User Messaging receives a media file, it publishes a notification to your two-way SNS topic. The notification is a JSON object with a `messageBody` field that contains a stringified JSON document with the media status and, on success, the S3 location and file metadata.

The following example shows a successful inbound media notification:

```
{
    "originationNumber": "+14255551234",
    "destinationNumber": "rcs-cb1e6e519e9049fabf8c0ae38e4d876b",
    "messageBody": "{\"mediaStatus\":\"SUCCESS\",\"s3Bucket\":\"my-rcs-media-bucket\",\"s3Key\":\"inbound-media/rcs/msg-abc123def456#photo_2026.jpg\",\"mimeType\":\"image/jpeg\",\"fileName\":\"photo_2026.jpg\",\"fileSizeBytes\":1211843}",
    "inboundMessageId": "8821d750-4bc5-4cb1-a8c3-c3d64a38d019"
}
```

The top-level notification contains the following fields:

`originationNumber`  
The phone number of the user who sent the media.

`destinationNumber`  
The RCS agent identifier that received the message.

`messageBody`  
A stringified JSON document describing the media. It contains the fields in the following table.

`inboundMessageId`  
The unique identifier for the inbound message.

The `messageBody` JSON contains the following fields:

`mediaStatus`  
The outcome of media processing. Valid values are `SUCCESS`, `UPLOAD_FAILED`, and `ROLE_ASSUME_FAILED`.

`mediaStatusMessage`  
A human-readable description of the status. Present when `mediaStatus` is a failure value.

`s3Bucket`  
The name of the S3 bucket where the media file is stored. Present on success.

`s3Key`  
The S3 object key for the stored media file. Present on success.

`mimeType`  
The MIME type of the media file (for example, `image/jpeg`, `video/mp4`, `application/pdf`).

`fileName`  
The original file name as provided by the user's device.

`fileSizeBytes`  
The size of the media file in bytes.

**Note**  
The inbound media notification does not currently include a message-type field. Use `mediaStatus` to determine the outcome.

## Media download failure handling
<a name="rcs-inbound-media-failure-handling"></a>

If AWS End User Messaging cannot download or store media from the RCS provider, the service still publishes a notification to your two-way SNS topic. The `messageBody` carries a failure `mediaStatus` (`UPLOAD_FAILED` or `ROLE_ASSUME_FAILED`) and a `mediaStatusMessage` describing the cause, with no S3 location fields.

For example, an IAM role assumption failure produces the following `messageBody` content:

```
{
    "mediaStatus": "ROLE_ASSUME_FAILED",
    "mediaStatusMessage": "Media received but could not assume the configured IAM role",
    "mimeType": "image/heic",
    "fileName": "IMG_7115.heic",
    "fileSizeBytes": 1211843
}
```

Common causes of media download failures include:
+ The media is no longer available from the RCS provider (for example, it expired or was deleted).
+ The IAM role does not have permission to write to the specified S3 bucket.
+ The S3 bucket does not exist or is in a different region than expected.

To troubleshoot delivery failures, verify that your IAM role trust and permission policies are correctly configured, and that the S3 bucket exists and is accessible from the service. Monitor your agent's CloudWatch metrics for media upload failures.

## Accepted media types
<a name="rcs-inbound-media-filtering"></a>

AWS End User Messaging accepts the following inbound media MIME types:
+ **Images:** `image/jpeg`, `image/jpg`, `image/gif`, `image/png`
+ **Audio:** `audio/aac`, `audio/mp3`, `audio/mpeg`, `audio/mpg`, `audio/mp4`, `audio/mp4-latm`, `audio/3gpp`, `audio/ogg`, `application/ogg`
+ **Video:** `video/h263`, `video/m4v`, `video/mp4`, `video/mpeg`, `video/mpeg4`, `video/webm`
+ **Documents:** `application/pdf`

**Note**  
AWS End User Messaging does not impose a size limit on inbound media.

## Best practices
<a name="rcs-inbound-media-best-practices"></a>
+ Always configure media storage if you expect users to send images, videos, or files in RCS conversations.
+ Use a dedicated S3 bucket for RCS inbound media to isolate access controls and lifecycle policies.
+ Set an S3 lifecycle policy to expire old media objects (for example, after 90 days) to manage storage costs.
+ Process inbound media asynchronously using an AWS Lambda function triggered by your SNS topic.
+ Scope the IAM role to `s3:PutObject` only. The service does not require broader permissions.
+ Monitor CloudWatch metrics for media upload failures and set alarms to detect configuration issues.