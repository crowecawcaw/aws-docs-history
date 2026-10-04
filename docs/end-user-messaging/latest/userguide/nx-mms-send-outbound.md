

# Outbound messaging
<a name="nx-mms-send-outbound"></a>

You send an MMS message with the `SendMediaMessage` operation, referencing media that you store in Amazon S3. Use the AWS CLI to send from your application. The example uses a phone pool as the origination identity, which is the recommended approach; you can also specify a single phone number instead. Before you send, make sure you have an MMS-capable origination identity and your media stored in Amazon S3. For setup, see [How to get set up](nx-mms-get-set-up.md).

**To send an MMS message**
+ Use the [send-media-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-media-message.html) command. The only required parameters are `destination-phone-number` and `origination-identity`. Omit `media-urls` for a text-only message, or `message-body` for a media-only message. You can include only one media file per message, so `media-urls` takes a single Amazon S3 URI.

  ```
  aws pinpoint-sms-voice-v2 --region {{us-east-1}} send-media-message \\
      --destination-phone-number {{+12065550150}} \\
      --origination-identity {{pool-a1b2c3d4e5f6g7h8i}} \\
      --message-body {{"text body"}} \\
      --media-urls {{s3://s3-bucket/media_file.jpg}}
  ```

  Replace the AWS Region, the destination phone number, the text body, and the Amazon S3 URI of the MMS file. For the origination identity, using a phone pool is recommended; to send from a specific resource instead, provide a single MMS-capable phone number (which must be `ACTIVE` and able to send to the destination).

If AWS End User Messaging accepts the command, you receive a `MessageId`. This means only that the command was received, not that the device has received the message. For error codes, see [SendMediaMessage Errors](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendMediaMessage.html#API_SendMediaMessage_Errors).

```
{
   "MessageId": "string"
}
```

**Note**  
Your MMS files must be stored in an Amazon S3 bucket in the same AWS account and AWS Region as your MMS-capable origination identity, and the sending identity must have read access to the bucket. For the steps to create a bucket, upload media, and get the Amazon S3 URI, see [Step 2: Store your media in Amazon S3](nx-mms-gsu-media.md).