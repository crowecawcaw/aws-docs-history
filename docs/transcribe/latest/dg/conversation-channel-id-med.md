# Transcribing multi-channel audio

If you have an audio file or stream that has multiple channels, you can use
_channel identification_ to transcribe the speech from each of
those channels. Amazon Transcribe Medical transcribes the speech from each channel separately. It combines
the separate transcriptions of each channel into a single transcription output.

Use channel identification to identify the separate channels in your audio and
transcribe the speech from each of those channels. Enable this in situations such as a
caller and agent scenario. Use this to distinguish a caller from an agent in recordings
or streams from contact centers that perform drug safety monitoring.

You can enable channel identification for both batch processing and real-time
streaming. The following list describes how to enable it for each method.

- Batch transcription – AWS Management Console and [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API
- Streaming transcription – WebSocket streaming and
  [`StartMedicalStreamTranscription`](../APIReference/API_streaming_StartMedicalStreamTranscription.md "../APIReference/API_streaming_StartMedicalStreamTranscription.md") API

## Transcribing multi-channel audio

files

When you transcribe an audio file, Amazon Transcribe Medical returns a list of
_items_ for each channel. An item is a transcribed word or
punctuation mark. Each word has a start time and an end time. If a person on one
channel speaks over a person on a separate channel, the start times and end times of
the items for each channel overlap while the individuals are speaking over each
other.

By default, you can transcribe audio files with two channels. You can request a
quota increase if you need to transcribe files that have more than two channels. For
information about requesting a quota increase, see [AWS service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

To transcribe multi-channel audio in a batch transcription job, use the AWS Management Console or the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API.

To use the AWS Management Console to enable channel identification in your batch
transcription job, you enable audio identification and then channel
identification. Channel identification is a subset of audio identification
in the AWS Management Console.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, under Amazon Transcribe Medical, choose
   **Transcription jobs**.
3. Choose **Create job**.
4. On the **Specify job details** page, provide
   information about your transcription job.
5. Choose **Next**.
6. Enable **Audio identification**.
7. For **Audio identification type**, choose
   **Channel identification**.
8. Choose **Create**.

###### To transcribe a multi-channel audio file (API)

- For the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API,
  specify the following.

      1. For `TranscriptionJobName`, specify a name
       unique to your AWS account.
      2. For `LanguageCode`, specify the language code
       that corresponds to the language spoken in the audio file.
       The valid value is `en-US`.
      3. For the `MediaFileUri` parameter of the
       `Media` object, specify the name of the media
       file that you want to transcribe.
      4. For the `Settings` object, set
       `ChannelIdentification` to
       `true`.

  The following is an example request using the AWS SDK for Python (Boto3).

```

from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe', '`us-west-2`')
job_name = "`my-first-transcription-job`"
job_name = "`my-first-med-transcription-job`"
job_uri = "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`"
transcribe.start_medical_transcription_job(
      MedicalTranscriptionJobName = job_name,
      Media = {
        'MediaFileUri': job_uri
      },
      OutputBucketName = '`amzn-s3-demo-bucket`',
      OutputKey = '`output-files`/',
      LanguageCode = 'en-US',
      Specialty = 'PRIMARYCARE',
      Type = 'CONVERSATION',
      Settings = {
        'ChannelIdentification': True
      }
)
while True:
    status = transcribe.get_transcription_job(MedicalTranscriptionJobName = job_name)
    if status['MedicalTranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)

```

###### To transcribe a multi-channel audio file using a batch transcription

job (AWS CLI)

- Run the following code.

```


aws transcribe start-medical-transcription-job \
--region `us-west-2` \
--cli-input-json file://`example-start-command`.json
```

The following is the code of
`example-start-command.json`.

```
{
      "MedicalTranscriptionJobName": "`my-first-med-transcription-job`",
      "Media": {
          "MediaFileUri": "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-audio-file`.`flac`"
      },
      "OutputBucketName": "`amzn-s3-demo-bucket`",
      "OutputKey": "`my-output-files`/",
      "LanguageCode": "en-US",
      "Specialty": "PRIMARYCARE",
      "Type": "CONVERSATION",

        "Settings":{
          "ChannelIdentification": true
        }
}
```

The following code shows the transcription output for an audio file that has a
conversation on two channels.

```

{
  "jobName": "`job id`",
  "accountId": "111122223333",
  "results": {
    "transcripts": [
      {
        "transcript": "When you try ... It seems to ..."
      }
    ],
    "channel_labels": {
      "channels": [
        {
          "channel_label": "ch_0",
          "items": [
            {
              "start_time": "12.282",
              "end_time": "12.592",
              "alternatives": [
                {
                  "confidence": "1.0000",
                  "content": "When"
                }
              ],
              "type": "pronunciation"
            },
            {
              "start_time": "12.592",
              "end_time": "12.692",
              "alternatives": [
                {
                  "confidence": "0.8787",
                  "content": "you"
                }
              ],
              "type": "pronunciation"
            },
            {
              "start_time": "12.702",
              "end_time": "13.252",
              "alternatives": [
                {
                  "confidence": "0.8318",
                  "content": "try"
                }
              ],
              "type": "pronunciation"
            },
            `...`
         ]
      },
      {
          "channel_label": "ch_1",
          "items": [
            {
              "start_time": "12.379",
              "end_time": "12.589",
              "alternatives": [
                {
                  "confidence": "0.5645",
                  "content": "It"
                }
              ],
              "type": "pronunciation"
            },
            {
              "start_time": "12.599",
              "end_time": "12.659",
              "alternatives": [
                {
                  "confidence": "0.2907",
                  "content": "seems"
                }
              ],
              "type": "pronunciation"
            },
            {
              "start_time": "12.669",
              "end_time": "13.029",
              "alternatives": [
                {
                  "confidence": "0.2497",
                  "content": "to"
                }
              ],
              "type": "pronunciation"
            },
            `...`
        ]
    }
}

```

## Transcribing multi-channel

audio streams

You can transcribe audio from separate channels in either HTTP/2 or WebSocket
streams using the [`StartMedicalStreamTranscription`](../APIReference/API_streaming_StartMedicalStreamTranscription.md "../APIReference/API_streaming_StartMedicalStreamTranscription.md") API.

By default, you can transcribe streams with two channels. You can request a quota
increase if you need to transcribe streams that have more than two channels. For
information about requesting a quota increase, see [AWS service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

### Transcribing

multi-channel audio in an HTTP/2 stream

To
transcribe multi-channel audio in an HTTP/2 stream, use the
[StartMedicalStreamTranscription](../APIReference/API_streaming_StartMedicalStreamTranscription.md "../APIReference/API_streaming_StartMedicalStreamTranscription.md") API
and specify the
following:

- `LanguageCode` – The language code of the audio. The valid
  value is `en-US`.
- `MediaEncoding` – The encoding of the audio. Valid values
  are `ogg-opus`, `flac`, and
  `pcm`.
- `EnableChannelIdentification` – `true`
- `NumberOfChannels` – the number of channels in your
  streaming audio.

For more information on setting up an HTTP/2 stream to transcribe a medical
conversation, see [Setting up an HTTP/2 stream](streaming-setting-up.md#streaming-http2 "streaming-setting-up.md#streaming-http2").

### Transcribing

multi-channel audio in a WebSocket stream

To partition speakers in WebSocket streams, use the following format to create
a pre-signed URI and start a WebSocket request. Specify
`enable-channel-identification` as `true` and the
number of channels in your stream in `number-of-channels`. A
pre-signed URI contains the information needed to set up bi-directional
communication between your application and Amazon Transcribe Medical.

```

GET wss://transcribestreaming.`us-west-2`.amazonaws.com:8443/medical-stream-transcription-websocket
?language-code=`languageCode`
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=`AKIAIOSFODNN7EXAMPLE`%2F`20220208`%2F`us-west-2`%2F`transcribe`%2Faws4_request
&X-Amz-Date=`20220208T235959Z`
&X-Amz-Expires=`300`
&X-Amz-Security-Token=`security-token`
&X-Amz-Signature=`Signature Version 4 signature`
&X-Amz-SignedHeaders=host
&media-encoding=`flac`
&sample-rate=`16000`
&session-id=`sessionId`
&enable-channel-identification=true
&number-of-channels=2

```

Parameter definitions can be found in the [API Reference](../APIReference/API_Reference.md "../APIReference/API_Reference.md"); parameters common to
all AWS API operations are listed in the [Common Parameters](../APIReference/CommonParameters.md "../APIReference/CommonParameters.md")
section.

For more information about WebSocket requests, see [Setting up a WebSocket stream](streaming-setting-up.md#streaming-websocket "streaming-setting-up.md#streaming-websocket").

### Multi-channel streaming output

The output of a streaming transcription is the same for HTTP/2 and WebSocket
requests. The following is an example output.

```
{
    "resultId": "XXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX",
    "startTime": 0.11,
    "endTime": 0.66,
    "isPartial": false,
    "alternatives": [
        {
            "transcript": "Left.",
            "items": [
                {
                    "startTime": 0.11,
                    "endTime": 0.45,
                    "type": "pronunciation",
                    "content": "Left",
                    "vocabularyFilterMatch": false
                },
                {
                    "startTime": 0.45,
                    "endTime": 0.45,
                    "type": "punctuation",
                    "content": ".",
                    "vocabularyFilterMatch": false
                }
            ]
        }
    ],
    "channelId": "ch_0"
}
```

For each speech segment, there is a `channelId` flag that indicates
which channel the speech belongs to.
