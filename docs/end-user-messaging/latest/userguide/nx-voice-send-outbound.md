

# Outbound messaging
<a name="nx-voice-send-outbound"></a>

You place a voice call with the `SendVoiceMessage` operation. Use the AWS CLI to call from your application. The service converts text to speech with Amazon Polly, or plays an audio file that you reference with speech synthesis markup language (SSML). The example uses a phone pool as the origination identity, which is the recommended approach; you can also specify a single phone number instead.

**Note**  
While your account is in the sandbox, you can only place calls to verified destination phone numbers. Production accounts can call any valid number.

**To place a text-to-speech call**
+ Use the [send-voice-message](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/send-voice-message.html) command. Provide the spoken text in `--message-body`.

  ```
  aws pinpoint-sms-voice-v2 send-voice-message \\
      --destination-phone-number {{+12065550150}} \\
      --origination-identity {{pool-a1b2c3d4e5f6g7h8i}} \\
      --message-body {{"Hello. Your appointment is confirmed for tomorrow at 2 PM."}} \\
      --message-body-text-type {{TEXT}} \\
      --voice-id {{MATTHEW}} \\
      --configuration-set-name {{MyConfigurationSet}}
  ```

  In the preceding command, make the following changes:
  + Replace {{\+12065550150}} with the destination phone number, in E.164 format.
  + Replace {{pool-a1b2c3d4e5f6g7h8i}} with your origination identity. Using a phone pool is recommended; to call from a specific resource instead, provide a single phone number.
  + Replace the value of `--message-body` with the text to read out. For `TEXT`, the maximum length is 3,000 characters.
  + Set `--message-body-text-type` to `TEXT` for plain text, or `SSML` if the body contains speech synthesis markup language. The default is `TEXT`.
  + Set `--voice-id` to the Amazon Polly voice that reads the message. The default is `MATTHEW`. For supported values, see [SendVoiceMessage](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SendVoiceMessage.html#API_SendVoiceMessage_RequestSyntax) in the *AWS End User Messaging SMS and Voice V2 API Reference*.
  + Replace {{MyConfigurationSet}} with the name or ARN of the configuration set that captures events for this call.

If AWS End User Messaging accepts the request, it returns a `MessageId`. This means only that the request was accepted, not that the call has been answered.

To play audio that you supply instead of synthesized speech, set `--message-body-text-type` to `SSML` and reference your audio file with an SSML `audio` tag in the message body, for example `"<speak><audio src='https://example.com/audio/greeting.mp3'/></speak>"`. For the SSML tags that Amazon Polly supports, see [Supported SSML tags](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html) in the *Amazon Polly Developer Guide*.

**Note**  
[needs SME confirmation] Confirm the supported audio hosting and file-format requirements for AWS End User Messaging voice calls (for example, whether the audio must be reachable over HTTPS and the accepted codecs/bitrate). The API Reference documents `MessageBody` and `MessageBodyTextType` but does not restate Amazon Polly audio constraints.