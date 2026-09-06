

# Example of sending an MMS message using AWS End User Messaging SMS
<a name="send-mms-message"></a>

If you are using a shared resource then you must use the full Amazon Resource Name (ARN) of the resource. You can use the AWS CLI or AWS End User Messaging SMS and voice v2 API to send MMS messages to your customers.

Use the [send-media-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.html) AWS CLI command to send an MMS message. For more information on configuring the AWS CLI, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

**Important**  
MMS capabilities are only available in some countries. For more information on supported countries for SMS and MMS, see [Supported countries and regions for SMS messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md) and [Supported countries and regions for MMS messaging in AWS End User Messaging SMS](phone-numbers-mms-by-country.md).  
To check if you origination identity is MMS capable, see [View a phone number status and capabilities in AWS End User Messaging SMS](phone-numbers-status.md).   
To use a shared resource you must use the full Amazon Resource Name (ARN).

## Prerequisites
<a name="send-mms-message-prerequisite"></a>

Before you begin, the following prerequisites must be met:
+ You must have an origination identity that [supports sending an MMS message](phone-numbers-mms-by-country.md#phone-numbers-mms-by-country.title). 
+ You must upload your media files to an Amazon S3 bucket that is in the same AWS Region as your MMS capable origination identity, see [Setting up an Amazon S3 bucket for MMS files](#send-mms-message-bucket).

  For a list of support file types and sizes, see [ MMS file types, size and character limits  Learn about MMS file size, file type limitations, and maximum number of charters an mms can contain.  MMS file typesMMS file sizemms character limit  A single MMS media file can be up to 2 MB for all image types (gif, jpeg, png) and 600 KB in size for all audio and video media file types. The text message body of an MMS can contain 1600 from any character set. Unlike SMS, MMS message are not broken into multiple parts when they are sent. If you are sending large text message you may get better throughput sending an MMS message since they are not broken into multiple parts. 



| File type | MIME types | Maximum file size | 
| --- | --- | --- | 
| Graphics Interchange Format | `image/gif` | 2 MB | 
| Joint Photographic Experts Group | `image/jpeg` | 2 MB | 
| Portable Network Graphics  | `image/png` | 2 MB | 
| Tag image file format | `image/tiff` | 600 KB | 
| Third generation partnership project  | `audio/3gpp`, `video/3gpp` | 600 KB | 
| Third generation partnership project 2  | `audio/3gpp2`, `video/3gpp2` | 600 KB | 
| Adaptive Multi-Rate | `audio/amr` | 600 KB | 
| MPEG-4 | `audio/mp4`, `video/mp4` | 600 KB | 
| Moving picture experts group | `audio/mpeg`<br />Only MP3 files are supported for `audio/mpeg` | 600 KB | 
| Ogg | `audio/ogg` | 600 KB | 
| QuickTime | `video/quicktime` | 600 KB | 
| WebM | `video/webm` | 600 KB | 
| iCalendar | `text/calendar` | 600 KB | 
| vCard | `text/vcard`, `text/x-vcard` | 600 KB | 
| Portable Document Format | `application/pdf` | 600 KB |  ](mms-limitations-character.md#mms-limitations-character.title)
+ The S3 URIs of each MMS file. 
+ The identity used to call `send-media-message` must have read access to the Amazon S3 bucket that contains your media files. For more information on setting read access, see [Identity-based policy examples for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html) in the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

## Send an MMS with the AWS CLI
<a name="send-mms-message-steps"></a>

The only required parameters for [send-media-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.html) are `destination-phone-number` and `origination-identity`. You can send a message that is only text by omitting the `media-urls` parameter. You can also send a message the is only media files by omitting the `message-body` parameter.

**To send an MMS message**
+ At the command line, enter the following command:

  ```
  aws pinpoint-sms-voice-v2 --region '{{us-east-1}}' send-media-message --destination-phone-number {{+12065550150}} --origination-identity {{+14255550120}} --message-body '{{text body}}' --media-urls '{{s3://s3-bucket/media_file.jpg}}'
  ```

  In the preceding command, make the following changes:
  + Replace {{us-east-1}} with the AWS Region that your origination identity is stored in.
  + Replace {{\+12065550150}} with the destination phone number.
  + Replace {{\+14255550120}} with your origination identity. The origination identity must be `ACTIVE` and able to send the destination phone number.
  + Replace {{text body}} with your text message.
  + Replace {{s3://s3-bucket/media\_file.jpg}} with the S3 URI of the MMS file. Supported media file formats are listed in [MMS file types, size and character limits](mms-limitations-character.md). For more information about creating an S3 bucket and managing objects, see [Setting up an Amazon S3 bucket for MMS files](#send-mms-message-bucket) or [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

If AWS End User Messaging SMS accepts the command you will receive the `MessageID`. This only means the command was successfully received and not that the destination device has received the message yet. For a list of error codes, see [SendMediaMessage Errors](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.html#API_SendMediaMessage_Errors).

```
{
   "MessageId": "string"
}
```

## Setting up an Amazon S3 bucket for MMS files
<a name="send-mms-message-bucket"></a>

Your MMS files must be stored in an Amazon S3 bucket. The Amazon S3 bucket must be in the same AWS account and AWS Region as your MMS capable origination identity. These directions show how to create an Amazon S3 bucket, upload a file, and build the URI to the file. For more information on Amazon S3 commands, see [Use high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html). For more information on configuring the AWS CLI, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

To create an Amazon S3 bucket use the [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html) AWS CLI command. At the command line, enter the following command:

```
aws s3api create-bucket --region '{{us-east-1}}' --bucket {{BucketName}}
```

In the preceding command:
+ Replace {{us-east-1}} with the AWS Region your MMS capable origination identity is in.
+ Replace {{BucketName}} with the name of the new bucket.

To copy a file to the Amazon S3 bucket use the [cp](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-copy) AWS CLI command. At the command line, enter the following command:

```
aws s3 cp {{SourceFilePathAndName}} s3://{{BucketName}}/{{FileName}} 
```

In the preceding command:
+ Replace {{SourceFilePathAndName}} with the file path and name of the file to copy.
+ Replace {{BucketName}} with the name of the bucket.
+ Replace {{FileName}} with the name to use for the file.

The URI to use when sending is:

```
s3://{{BucketName}}/{{FileName}}
```