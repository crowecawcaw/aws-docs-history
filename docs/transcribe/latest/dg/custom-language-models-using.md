# Using a custom language model

Once you've created your custom language model, you can include it in your transcription requests;
refer to the following sections for examples.

The language of the model you're including in your request must match the language code you
specify for your media. If the languages don't match, your custom language model is not applied to your
transcription and there are no warnings or errors.

## Using a custom language model in a batch

transcription

To use a custom language model with a batch transcription, see the following for examples:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, choose **Transcription jobs**, then select
   **Create job** (top right). This opens the **Specify job details**
   page.
3. In the **Job settings** panel under **Model type**, select the
   **Custom language model** box.

![Amazon Transcribe console screenshot: the 'job settings' page.](images/clm-console.png)

You must also select an input language from the dropdown menu.

![Amazon Transcribe console screenshot: the 'job settings' page showing dropdown language menu.](images/clm-console-language.png) 4. Under **Custom model selection**, select an existing custom language
model from the dropdown menu or **Create a new one**.

Add the Amazon S3 location of your input file in the **Input data**
panel. 5. Select **Next** for additional configuration options.

Select **Create job** to run your transcription job.
This example uses the [start-transcription-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html") command and `ModelSettings` parameter with the `VocabularyName`
sub-parameter. For more information, see
[`StartTranscriptionJob`](../APIReference/API_StartTranscriptionJob.md "../APIReference/API_StartTranscriptionJob.md") and
[`ModelSettings`](../APIReference/API_ModelSettings.md "../APIReference/API_ModelSettings.md").

```
aws transcribe start-transcription-job \
--region `us-west-2` \
--transcription-job-name `my-first-transcription-job` \
--media MediaFileUri=s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac` \
--output-bucket-name `amzn-s3-demo-bucket` \
--output-key `my-output-files`/ \
--language-code `en-US` \
--model-settings LanguageModelName=`my-first-language-model`
```

Here's another example using the [start-transcription-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/start-transcription-job.html") command, and a request body that includes your
custom language model with that job.

```
aws transcribe start-transcription-job \
--region `us-west-2` \
--cli-input-json file://`my-first-model-job`.json
```

The file _my-first-model-job.json_ contains the following request body.

```
{
  "TranscriptionJobName": "`my-first-transcription-job`",
  "Media": {
        "MediaFileUri": "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`"
  },
  "OutputBucketName": "`amzn-s3-demo-bucket`",
  "OutputKey": "`my-output-files`/",
  "LanguageCode": "`en-US`",
  "ModelSettings": {
        "LanguageModelName": "`my-first-language-model`"
   }
}
```

This example uses the AWS SDK for Python (Boto3) to include a custom language model
using the `ModelSettings` argument for the
[start_transcription_job](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job") method. For more
information, see [`StartTranscriptionJob`](../APIReference/API_StartTranscriptionJob.md "../APIReference/API_StartTranscriptionJob.md") and
[`ModelSettings`](../APIReference/API_ModelSettings.md "../APIReference/API_ModelSettings.md").

For additional examples using the AWS SDKs, including feature-specific, scenario, and
cross-service examples, refer to the [Code examples for Amazon Transcribe using AWS SDKs](service_code_examples.md "service_code_examples.md") chapter.

```
from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe', '`us-west-2`')
job_name = "`my-first-transcription-job`"
job_uri = "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`"
transcribe.start_transcription_job(
    TranscriptionJobName = job_name,
    Media = {
        'MediaFileUri': job_uri
    },
    OutputBucketName = '`amzn-s3-demo-bucket`',
    OutputKey = '`my-output-files`/',
    LanguageCode = '`en-US`',
    ModelSettings = {
        'LanguageModelName': '`my-first-language-model`'
   }
)

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName = job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
```

## Using a custom language model in a streaming

transcription

To use a custom language model with a streaming transcription, see the following for examples:

1. Sign into the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, choose **Real-time transcription**. Scroll down to
   **Customizations** and expand this field if it is minimized.

![Amazon Transcribe console screenshot: the 'real-time transcription' page.](images/stream-main.png) 3. Toggle on **Custom language model** and select a model from the
dropdown menu.

![Amazon Transcribe console screenshot: the expanded 'customizations' panel.](images/model-stream2.png)

Include any other settings you want to apply to your stream. 4. You're now ready to transcribe your stream. Select **Start streaming**
and begin speaking. To end your dictation, select **Stop streaming**.
This example creates an HTTP/2 request that includes your custom language model. For more
information on using HTTP/2 streaming with Amazon Transcribe, see
[Setting up an HTTP/2 stream](streaming-setting-up.md#streaming-http2 "streaming-setting-up.md#streaming-http2"). For more detail on parameters
and headers specific to Amazon Transcribe, see [`StartStreamTranscription`](../APIReference/API_streaming_StartStreamTranscription.md "../APIReference/API_streaming_StartStreamTranscription.md").

```
POST /stream-transcription HTTP/2
host: transcribestreaming.`us-west-2`.amazonaws.com
X-Amz-Target: com.amazonaws.transcribe.Transcribe.`StartStreamTranscription`
Content-Type: application/vnd.amazon.eventstream
X-Amz-Content-Sha256: `string`
X-Amz-Date: `20220208`T`235959`Z
Authorization: AWS4-HMAC-SHA256 Credential=`access-key`/`20220208`/`us-west-2`/transcribe/aws4_request, SignedHeaders=content-type;host;x-amz-content-sha256;x-amz-date;x-amz-target;x-amz-security-token, Signature=`string`
x-amzn-transcribe-language-code: `en-US`
x-amzn-transcribe-media-encoding: `flac`
x-amzn-transcribe-sample-rate: `16000`
x-amzn-transcribe-language-model-name: `my-first-language-model`
transfer-encoding: chunked
```

Parameter definitions can be found in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to
all AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md")
section.

This example creates a presigned URL that applies your custom language model to a WebSocket
stream. Line breaks have been added for readability. For more information on using WebSocket
streams with Amazon Transcribe, see [Setting up a WebSocket stream](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket"). For more detail on parameters, see
[`StartStreamTranscription`](../APIReference/API_streaming_StartStreamTranscription.md "../APIReference/API_streaming_StartStreamTranscription.md").

```
GET wss://transcribestreaming.`us-west-2`.amazonaws.com:8443/stream-transcription-websocket?
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=`AKIAIOSFODNN7EXAMPLE`%2F`20220208`%2F`us-west-2`%2F`transcribe`%2Faws4_request
&X-Amz-Date=`20220208`T`235959`Z
&X-Amz-Expires=`300`
&X-Amz-Security-Token=`security-token`
&X-Amz-Signature=`string`
&X-Amz-SignedHeaders=content-type%3Bhost%3Bx-amz-date
&language-code=`en-US`
&media-encoding=`flac`
&sample-rate=`16000`
&language-model-name=`my-first-language-model`

```

Parameter definitions can be found in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to
all AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md")
section.
