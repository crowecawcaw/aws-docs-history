

# Creating a custom voice

To create a custom voice, you provide recordings of one speaker, choose the language of the voice, and confirm the statements in [Your responsibilities](custom-voices.md#custom-voices-responsibilities).

## Recording requirements
<a name="creating-custom-voices-recordings"></a>

The recordings must meet the requirements in the following table.


| Requirement | Value | 
| --- | --- | 
| Number of recordings | 1–10 per voice | 
| Audio formats | WAV (wav), FLAC (flac), Ogg Vorbis (ogg\_vorbis), or MP3 (mp3). Set the Format field of each recording to the value that matches its audio. | 
| Length of each recording | 10 seconds to 15 minutes. If any recording is shorter or longer, voice creation fails and the voice status is failed. | 
| Total length | At most 15 minutes for all recordings together. If the total is longer, voice creation fails. | 
| Content | Speech by one speaker, in the language of the voice. Amazon Polly doesn't detect the language. | 
| Location | An Amazon Simple Storage Service (Amazon S3) object in the same Region as the Amazon Polly endpoint, or audio in the request. Audio in the request can be up to 5 MB per recording, before base64 encoding. | 

Amazon Polly accepts any sample rate, bit depth, and number of channels. The custom voice learns from everything in the recordings, including noise and echo. For the best result, follow these recommendations:
+ Record 2–10 minutes of natural speech, split into takes of up to a minute each. Several short takes work better than one long file.
+ Record one speaker in a quiet room, at the same distance from the microphone.
+ Don't use meeting apps or browser recorders. Their echo cancellation and noise suppression change the voice.
+ Speak in the style that you want the voice to have.
+ Convert each take to WAV, mono, 16-bit, 24 kHz before you upload it. At 24 kHz, a one-minute take is about 2.9 MB.

## Permissions for creating a custom voice
<a name="creating-custom-voices-permissions"></a>

To create a custom voice and check its status, you must have the following permissions:
+ The `polly:CreateVoice` permission.
+ The `polly:GetVoice` permission, to check the status of the voice. The `voice-active` waiter also uses `GetVoice`.
+ The `s3:GetObject` permission on each recording that you specify with an Amazon S3 URL. You don't need a bucket policy that grants access to Amazon Polly. If the objects are encrypted with an AWS KMS key (SSE-KMS), you also need the `kms:Decrypt` permission on that key.
+ The `polly:TagResource` permission, if you add tags to the voice when you create it.
+ The `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` permissions on the key, if you encrypt the voice with a customer managed key. For more information, see [Configuring permissions to use a customer managed key](encryption-at-rest.md#encryption-at-rest-key-permissions).

## Prerequisites
<a name="creating-custom-voices-prerequisites"></a>

Before you create a custom voice, make sure that you have the following:
+ Recordings that meet the [Recording requirements](#creating-custom-voices-recordings). If you use Amazon S3 URLs, upload the recordings to a bucket in the Region where you want to create the voice.
+ The permissions in [Permissions for creating a custom voice](#creating-custom-voices-permissions).
+ (Optional) A customer managed key that meets the [Key requirements](encryption-at-rest.md#encryption-at-rest-key-requirements), if you don't want Amazon Polly to use an AWS owned key.
+ For the AWS CLI, the latest version. If the AWS CLI doesn't recognize the `create-voice` command, update it. For more information, see [Setting up the AWS CLI](setup-cli.md).

## Creating a custom voice with the console or AWS CLI
<a name="creating-custom-voices-cli"></a>

**Note**  
During the preview, only approved AWS accounts can create custom voices, and only those accounts see the **Voice Cloning** tab in the Amazon Polly console. To get access, see [Availability, languages, and pricing](custom-voices.md#custom-voices-availability).

------
#### [ Console ]<a name="creating-custom-voices-console"></a>

**To create a custom voice (console)**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Voice Cloning** tab.

1. Choose **Create voice**.

1. Enter a name for the voice and choose its language. You can't change the name or the language after you create the voice.

1. In the **Choose Audio Recordings** section, add 1–10 recordings in WAV, FLAC, Ogg Vorbis, or MP3 format. Choose **Amazon S3 URIs** to use objects in an Amazon S3 bucket, or **Upload files** to upload files from your computer. Each uploaded file can be up to 5 MB. The recordings must meet the [Recording requirements](#creating-custom-voices-recordings).

1. (Optional) By default, Amazon Polly encrypts the voice with an AWS owned key. To use your own key, do the following:

   1. In the **Encryption** section, select **Customize encryption settings**.

   1. Choose a customer managed key. The key must be an enabled symmetric encryption key in the same Region as the voice.

1. In the **Consent** section, select both check boxes to accept the terms. For more information, see [Your responsibilities](custom-voices.md#custom-voices-responsibilities).

1. (Optional) Add a key and an optional value for each tag that you want to add to the voice. For more information, see [Tagging Amazon Polly resources](tagging.md).

1. Choose **Create voice**. The voice appears in `pending` status. When creation ends, the status changes to `active` or `failed`.

------
#### [ AWS CLI ]<a name="creating-custom-voices-cli-procedure"></a>

**To create a custom voice (AWS CLI)**

1. Upload your recordings to an Amazon S3 bucket in the Region where you want to create the voice.

1. Run the `create-voice` command. The `--terms-accepted` option sets `TermsAccepted` to `true`. Replace the voice name and the Amazon S3 URLs with your own values:

   ```
   aws polly create-voice \
   --region us-east-1 \
   --name {{MyVoice}} \
   --language-code en-US \
   --terms-accepted \
   --voice-creation-data '{
       "Recordings": [
           {"Format": "wav", "Data": {"S3Url": "{{s3://amzn-s3-demo-bucket/speaker-1.wav}}"}},
           {"Format": "wav", "Data": {"S3Url": "{{s3://amzn-s3-demo-bucket/speaker-2.wav}}"}}
       ]
   }'
   ```

   The response returns the voice in `pending` status with its `Id`. You use the ID in the next steps.

1. Wait until the voice is `active`. The following command checks the status every 15 seconds. It exits with return code 255 if voice creation fails or if the voice isn't active after 2 hours:

   ```
   aws polly wait voice-active \
   --region us-east-1 \
   --voice-id {{vc-9a8fa85dd3}}
   ```

1. Check the status of the voice.

   ```
   aws polly get-voice \
   --region us-east-1 \
   --voice-id {{vc-9a8fa85dd3}}
   ```

   If `Status` is `failed`, read `StatusReason`. Delete the voice, fix the problem, and create the voice again. Failed voices count toward your quota.

To send the audio in the request instead of an Amazon S3 URL, set `Bytes` with the `@=` operator and a `fileb://` path. The `@=` operator tells the AWS CLI to read the value from the file. For more information, see [Loading a file as a shorthand syntax value](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html#shorthand-files) in the *AWS CLI User Guide*.

```
aws polly create-voice \
--region us-east-1 \
--name {{MyVoice}} \
--language-code en-US \
--terms-accepted \
--voice-creation-data 'Recordings=[{Format=wav,Data={Bytes@=fileb://{{speaker-1.wav}}}}]'
```

------

## Options when you create a custom voice
<a name="creating-custom-voices-options"></a>

You can specify the following optional settings in a `CreateVoice` request.

Customer managed key  
To encrypt the voice with a customer managed key, specify the key ARN in the `KmsKeyArn` field of `CustomerManagedEncryption`. In the AWS CLI, use `--customer-managed-encryption '{"KmsKeyArn": "{{key-arn}}"}'`. The key must be a symmetric encryption key in the same Region as the voice. You can't change the key after you create the voice. For more information, see [Encryption at rest](encryption-at-rest.md).

Tags  
To add tags when you create the voice, specify them in `Tags`. For more information, see [Tagging Amazon Polly resources](tagging.md).

Client token  
If you don't specify a `ClientToken`, the AWS SDKs and the AWS CLI generate one. To retry a request that succeeded, use the same token and the same parameters. Amazon Polly then returns the voice from the first request and doesn't create another one. If you reuse a token with different parameters, the request fails with `ValidationException`.