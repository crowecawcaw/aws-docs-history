# Example of sending an MMS message using AWS End User Messaging SMS

If you are using a shared resource then you must use the full Amazon Resource Name (ARN) of the resource. You can use the AWS CLI or AWS End User Messaging SMS and voice v2 API to send MMS messages to your
customers.

Use the [send-media-message](../../../cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.md") AWS CLI command to send an MMS message. For more information on configuring the AWS CLI, see [Configure the
AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### Important

MMS capabilities are only available in some countries. For more information on
supported countries for SMS and MMS, see [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md") and [Supported countries and regions for MMS messaging in AWS End User Messaging SMS](phone-numbers-mms-by-country.md "phone-numbers-mms-by-country.md").

To check if you origination identity is MMS capable, see [View a phone number status and capabilities in AWS End User Messaging SMS](phone-numbers-status.md "phone-numbers-status.md").

To use a shared resource you must use the full Amazon Resource Name (ARN).

## Prerequisites

Before you begin, the following prerequisites must be met:

- You must have an origination identity that [supports sending an MMS message](phone-numbers-mms-by-country.md#phone-numbers-mms-by-country.title "phone-numbers-mms-by-country.md#phone-numbers-mms-by-country.title").
- You must upload your media files to an Amazon S3 bucket
  that is in the same AWS Region as your MMS capable origination identity, see [Setting up an Amazon S3 bucket for MMS files](#send-mms-message-bucket "#send-mms-message-bucket").

For a list of support file types and sizes, see

- The S3 URIs of each MMS file.
- The identity used to call `send-media-message` must have read access to
  the Amazon S3 bucket that contains your media files. For more information on setting read
  access, see [Identity-based policy examples for Amazon S3](../../../AmazonS3/latest/userguide/example-policies-s3.md "../../../AmazonS3/latest/userguide/example-policies-s3.md") in the [Amazon S3 User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").

## Send an MMS with the AWS CLI

The only required parameters for [send-media-message](../../../cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.md") are `destination-phone-number` and
`origination-identity`. You can send a message that is only text by
omitting the `media-urls` parameter. You can also send a message the is only
media files by omitting the `message-body` parameter.

###### To send an MMS message

- At the command line, enter the following command:

```
aws pinpoint-sms-voice-v2 --region '`us-east-1`' send-media-message --destination-phone-number `+12065550150` --origination-identity `+14255550120` --message-body '`text body`' --media-urls '`s3://s3-bucket/media_file.jpg`'
```

In the preceding command, make the following changes:

    + Replace `us-east-1` with the AWS Region that
     your origination identity is stored in.
    + Replace `+12065550150` with the destination phone
     number.
    + Replace `+14255550120` with your origination
     identity. The origination identity must be `ACTIVE` and able to send the
     destination phone number.
    + Replace `text body` with your text
     message.
    + Replace `s3://s3-bucket/media_file.jpg` with the
     S3 URI of the MMS file. Supported media file formats are listed in [MMS file types, size and character limits](mms-limitations-character.md "mms-limitations-character.md"). For more information about
     creating an S3 bucket and managing objects, see [Setting up an Amazon S3 bucket for MMS files](#send-mms-message-bucket "#send-mms-message-bucket") or [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") and [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the
     [Amazon S3 User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").

If AWS End User Messaging SMS accepts the command you will receive the `MessageID`. This only means
the command was successfully received and not that the destination device has received the
message yet. For a list of error codes, see [SendMediaMessage Errors](../../../pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.md#API_SendMediaMessage_Errors "../../../pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.md#API_SendMediaMessage_Errors").

```
{
   "MessageId": "string"
}
```

## Setting up an Amazon S3 bucket for MMS files

Your MMS files must be stored in an Amazon S3 bucket. The Amazon S3 bucket must be in the same AWS account and
AWS Region as your MMS capable origination identity. These directions show how to
create an Amazon S3 bucket, upload a file, and build the URI to the file. For more
information on Amazon S3 commands, see [Use
high-level (s3) commands with the AWS CLI](../../../cli/latest/userguide/cli-services-s3-commands.md "../../../cli/latest/userguide/cli-services-s3-commands.md"). For more information on
configuring the AWS CLI, see [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

To create an Amazon S3 bucket use the [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html") AWS CLI command. At the command line, enter the following
command:

```
aws s3api create-bucket --region '`us-east-1`' --bucket `BucketName`
```

In the preceding command:

- Replace `us-east-1` with the AWS Region your MMS
  capable origination identity is in.
- Replace `BucketName`
  with the name of the new bucket.

To copy a file to the Amazon S3 bucket use the [cp](../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-managing-objects-copy "../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-managing-objects-copy") AWS CLI command. At the command line, enter the following
command:

```
aws s3 cp `SourceFilePathAndName` s3://`BucketName`/`FileName`
```

In the preceding command:

- Replace `SourceFilePathAndName` with the file path and name
  of the file to copy.
- Replace `BucketName`
  with the name of the bucket.
- Replace `FileName`
  with the name to use for the file.

The URI to use when sending is:

```
s3://`BucketName`/`FileName`
```
