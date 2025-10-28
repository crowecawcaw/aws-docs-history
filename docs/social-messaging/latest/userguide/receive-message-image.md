# Download a media file from WhatsApp to Amazon S3

To retrieve a media file and save it to an Amazon S3 bucket, use the [get-whatsapp-message-media](../../../cli/latest/reference/socialmessaging/get-whatsapp-message-media.md "../../../cli/latest/reference/socialmessaging/get-whatsapp-message-media.md") command.

```
aws socialmessaging get-whatsapp-message-media --media-id `{MEDIA_ID}` --origination-phone-number-id `{ORIGINATION_PHONE_NUMBER_ID}` --destination-s3-file bucketName=`{BUCKET}`,key=inbound_
{
    "mimeType": "image/jpeg",
    "fileSize": 78144
}
```

In the preceding command, do the following:

- Replace `{BUCKET}` with the name of the Amazon S3
  bucket.
- Replace `{MEDIA_ID}` with the value of the `id` field from
  the received event. For an example incoming media event, see [Example WhatsApp JSON for receiving a media message](managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-media "managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-media").
- Replace `{ORIGINATION_PHONE_NUMBER_ID}` with your phone number's ID.
  To retrieve the media from the Amazon S3 bucket, use the following command:

```
aws s3 cp s3://`{BUCKET}`/inbound_`{MEDIA_ID}`.jpeg
```

In the preceding command, do the following:

- Replace `{BUCKET}` with the name of the Amazon S3
  bucket.
- Replace `{MEDIA_ID}` with the MEDIA_ID returned from the previous
  step.
