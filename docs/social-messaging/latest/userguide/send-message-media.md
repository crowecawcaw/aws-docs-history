# Example of sending a media message in

AWS End User Messaging Social

The following example shows how to send a media message to your customer using the
AWS CLI. For more information on configuring the AWS CLI, see [Configure
the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). For a list of supported media file types,
see [Supported media file types and sizes in WhatsApp](supported-media-types.md "supported-media-types.md").

###### Note

WhatsApp stores media files for 30 days before deleting them, see [Upload Media](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media#upload-media "https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media#upload-media") in the _WhatsApp Business Platform Cloud API
Reference_.

1. Upload the media file to an Amazon S3 bucket. For more information, see [Uploading media files to send with WhatsApp](managing-media-files-s3.md "managing-media-files-s3.md").
2. Upload the media file to WhatsApp using the [post-whatsapp-message-media](../../../cli/latest/reference/socialmessaging/post-whatsapp-message-media.md "../../../cli/latest/reference/socialmessaging/post-whatsapp-message-media.md") command. On
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

You can also upload using a [presign url](managing-media-files-s3.md#managing-media-files-s3.title "managing-media-files-s3.md#managing-media-files-s3.title") by using `--source-s3-presigned-url` instead
of `--source-s3-file`. You must add `Content-Type` in the
`headers` field. If you use both then an
`InvalidParameterException` is returned.

```
--source-s3-presigned-url headers={"`Name`":"`Value`"},url=`https://BUCKET.s3.REGION/MEDIA_FILE`
```

3. Use the [send-whatsapp-message](../../../cli/latest/reference/socialmessaging/send-whatsapp-message.md "../../../cli/latest/reference/socialmessaging/send-whatsapp-message.md") command to send the media
   message.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","to":"'`{PHONE_NUMBER}`'","type":"image","image":{"id":"'`{MEDIA_ID}`'"}}' --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --meta-api-version v20.0
```

###### Note

You must specify base64 encoding when you use the AWS CLI version 2. This
can be done by adding the AWS CLI paramater `--cli-binary-format
 raw-in-base64-out` or changing the AWS CLI global configuration file. For more
information, see [`cli_binary_format`](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-settings") in the
_AWS Command Line Interface User Guide for Version
2_.

```
aws socialmessaging send-whatsapp-message --message '{"messaging_product":"whatsapp","to":"'`{PHONE_NUMBER}`'","type":"image","image":{"id":"'`{MEDIA_ID}`'"}}' --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --meta-api-version v20.0 --cli-binary-format raw-in-base64-out
```

In the preceding command, do the following:

    * Replace `{PHONE_NUMBER}` with your customer's
     phone number.
    * Replace `{ORIGINATION_PHONE_NUMBER_ID}` with
     your phone number's ID.
    * Replace `{MEDIA_ID}` with the media ID
     returned from the previous step.

4. When you no longer need the media file, you can delete it from WhatsApp using
   the [delete-whatsapp-message-media](../../../cli/latest/reference/socialmessaging/delete-whatsapp-media-message.md "../../../cli/latest/reference/socialmessaging/delete-whatsapp-media-message.md") command. This
   only removes the media file from WhatsApp and not your Amazon S3 bucket.

```
aws socialmessaging delete-whatsapp-message-media --media-id `{MEDIA_ID}` --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}`
```

In the preceding command, do the following:

    * Replace `{ORIGINATION_PHONE_NUMBER_ID}` with
     your phone number's ID.
    * Replace `{MEDIA_ID}` with the media ID.
