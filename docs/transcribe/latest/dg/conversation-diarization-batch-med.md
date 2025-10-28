# Enabling speaker partitioning in batch transcriptions

You can enable speaker partitioning in a batch transcription job using either
the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API or the AWS Management Console. This enables you to partition the text per speaker in a clinician-patient
conversation and determine who said what in the transcription output.

To use the AWS Management Console to enable speaker diarization in your
transcription job, you enable audio identification and then speaker
partitioning.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, under Amazon Transcribe Medical, choose
   **Transcription jobs**.
3. Choose **Create job**.
4. On the **Specify job details** page, provide
   information about your transcription job.
5. Choose **Next**.
6. Enable **Audio identification**.
7. For **Audio identification type**, choose
   **Speaker partitioning**.
8. For **Maximum number of speakers**, enter the
   maximum number of speakers that you think are speaking in your audio
   file.
9. Choose **Create**.

###### To enable speaker partitioning using a batch transcription job

(API)

- For the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API,
  specify the following.

      1. For `MedicalTranscriptionJobName`, specify a
       name that is unique in your AWS account.
      2. For `LanguageCode`, specify the language code
       that corresponds to the language spoken in the audio
       file.
      3. For the `MediaFileUri` parameter of the
       `Media` object, specify the name of the audio
       file that you want to transcribe.
      4. For `Specialty`, specify the medical specialty
       of the clinician speaking in the audio file.
      5. For `Type`, specify
       `CONVERSATION`.
      6. For `OutputBucketName`, specify the Amazon S3 bucket to store the transcription results.
      7. For the `Settings` object, specify the
       following.


      	1. `ShowSpeakerLabels` –
      	 `true`.
      	2. `MaxSpeakerLabels` – An integer between
      	 2 and 10 to indicate the number of speakers that you
      	 think are speaking in your audio.

  The following request uses the AWS SDK for Python (Boto3) to start a batch
  transcription job of a primary care clinician patient dialogue with speaker
  partitioning enabled.

```

from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe', '`us-west-2`')
job_name = "`my-first-transcription-job`"
job_uri = "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-media-file`.`flac`"
transcribe.start_medical_transcription_job(
    MedicalTranscriptionJobName = job_name,
    Media={
        'MediaFileUri': job_uri
    },
    OutputBucketName = '`amzn-s3-demo-bucket`',
    OutputKey = '`my-output-files`/',
    LanguageCode = 'en-US',
    Specialty = 'PRIMARYCARE',
    Type = 'CONVERSATION',
    OutputBucketName = '`amzn-s3-demo-bucket`',
Settings = {'ShowSpeakerLabels': True,
         'MaxSpeakerLabels': 2
         }
         )
while True:
    status = transcribe.get_medical_transcription_job(MedicalTranscriptionJobName = job_name)
    if status['MedicalTranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)


```

The following example code shows the transcription results of a
transcription job with speaker partitioning enabled.

```

{
    "jobName": "job ID",
    "accountId": "111122223333",
    "results": {
        "transcripts": [
            {
                "transcript": "Professional answer."
            }
        ],
        "speaker_labels": {
            "speakers": 1,
            "segments": [
                {
                    "start_time": "0.000000",
                    "speaker_label": "spk_0",
                    "end_time": "1.430",
                    "items": [
                        {
                            "start_time": "0.100",
                            "speaker_label": "spk_0",
                            "end_time": "0.690"
                        },
                        {
                            "start_time": "0.690",
                            "speaker_label": "spk_0",
                            "end_time": "1.210"
                        }
                    ]
                }
            ]
        },
        "items": [
            {
                "start_time": "0.100",
                "end_time": "0.690",
                "alternatives": [
                    {
                        "confidence": "0.8162",
                        "content": "Professional"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "start_time": "0.690",
                "end_time": "1.210",
                "alternatives": [
                    {
                        "confidence": "0.9939",
                        "content": "answer"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "alternatives": [
                    {
                        "content": "."
                    }
                ],
                "type": "punctuation"
            }
        ]
    },
    "status": "COMPLETED"
}


```

###### To transcribe an audio file of a conversation between a clinician

practicing primary care and a patient (AWS CLI)

- Run the following code.

```


aws transcribe start-transcription-job \
--region `us-west-2` \
--cli-input-json file://`example-start-command`.json

```

The following code shows the contents of
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
          "ShowSpeakerLabels": true,
          "MaxSpeakerLabels": 2
        }
}
```
