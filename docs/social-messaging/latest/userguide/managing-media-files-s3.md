# Uploading media files to send with WhatsApp

When you send or receive a media file, it has to be stored in an Amazon S3 bucket and uploaded or retrieved from WhatsApp. The Amazon S3
bucket must be in the same AWS account and AWS Region as your WhatsApp Business Account (WABA). These
directions show how to create an Amazon S3 bucket, upload a file, and build the URL to the file.
For more information on Amazon S3 commands, see [Use
high-level (s3) commands with the AWS CLI](../../../cli/latest/userguide/cli-services-s3-commands.md "../../../cli/latest/userguide/cli-services-s3-commands.md"). For more information on configuring
the AWS CLI, see [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the
_[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md")_, and [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"), and [Uploading
objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the _[Amazon S3 User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")_.

###### Note

WhatsApp stores media files for 30 days before deleting them, see [Upload Media](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media#upload-media "https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media#upload-media") in the _WhatsApp Business Platform Cloud API
Reference_.

You can also create a [presigned URL](../../../AmazonS3/latest/userguide/using-presigned-url.md "../../../AmazonS3/latest/userguide/using-presigned-url.md") to the media file. With a presigned URL, you
can grant time-limited access to objects and upload them without requiring another party to
have AWS security credentials or permissions.

1. To create an Amazon S3 bucket, use the [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html") AWS CLI command. At the command line, enter the following
   command:

```
aws s3api create-bucket --region '`us-east-1`' --bucket `BucketName`
```

In the preceding command:

    * Replace `us-east-1` with the AWS Region that your WABA
     is in.
    * Replace `BucketName`
     with the name of the new bucket.

2. To copy a file to the Amazon S3 bucket, use the [cp](../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-managing-objects-copy "../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-managing-objects-copy") AWS CLI command. At the command line, enter the following
   command:

```
aws s3 cp `SourceFilePathAndName` s3://`BucketName`/`FileName`
```

In the preceding command:

    * Replace `SourceFilePathAndName` with the file path and name
     of the file to copy.
    * Replace `BucketName`
     with the name of the bucket.
    * Replace `FileName`
     with the name to use for the file.

The url to use when sending is:

```
s3://`BucketName`/`FileName`
```

To create a [presigned URL](../../../AmazonS3/latest/userguide/using-presigned-url.md "../../../AmazonS3/latest/userguide/using-presigned-url.md"), replace the `user input
 placeholders` with your own information.

```
aws s3 presign s3://`amzn-s3-demo-bucket1`/`mydoc.txt` --expires-in `604800` --region `af-south-1` --endpoint-url `https://s3.af-south-1.amazonaws.com`
```

The returned URL will be:
`https://amzn-s3-demo-bucket1.s3.af-south-1.amazonaws.com/mydoc.txt?{Headers}` 3. Upload the media file to WhatsApp using the [post-whatsapp-message-media](../../../cli/latest/reference/socialmessaging/post-whatsapp-message-media.md "../../../cli/latest/reference/socialmessaging/post-whatsapp-message-media.md") command. On
successful completion, the command will return the
`{MEDIA_ID}`, which is required for sending the
media message.

```
aws socialmessaging post-whatsapp-message-media --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}`  --source-s3-file bucketName=`{BUCKET}`,key=`{MEDIA_FILE}`
```

In the preceding command, do the following:

    * Replace `{ORIGINATION_PHONE_NUMBER_ID}` with
     your phone number's ID.
    * Replace `{BUCKET}` with the name of the Amazon S3
     bucket.
    * Replace `{MEDIA_FILE}` with the name of the
     media file.

You can also upload using a [presign url](#managing-media-files-s3.title "#managing-media-files-s3.title") by using `--source-s3-presigned-url` instead
of `--source-s3-file`. You must add `Content-Type` in the
`headers` field. If you use both then an
`InvalidParameterException` is returned.

```
--source-s3-presigned-url headers={"`Name`":"`Value`"},url=`https://BUCKET.s3.REGION/MEDIA_FILE`
```

4. On successful completion the `MEDIA_ID` is returned. The `MEDIA_ID` is used to reference the media file when [sending a media message](send-message-media.md "send-message-media.md").
