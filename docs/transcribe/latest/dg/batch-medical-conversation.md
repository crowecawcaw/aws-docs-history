# Transcribing an audio file of a medical

conversation

Use a batch transcription job to transcribe audio files of medical conversations. You
can use this to transcribe a clinician-patient dialogue. You can start a batch
transcription job in either the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API or the AWS Management Console.

When you start a medical transcription job with the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API, you specify
`PRIMARYCARE` as the value of the `Specialty` parameter.

###### To transcribe a clinician-patient dialogue (AWS Management Console)

To use the AWS Management Console to transcribe a clinician-patient dialogue, create a
transcription job and choose **Conversation** for
**Audio input type**.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, under Amazon Transcribe Medical, choose **Transcription
   jobs**.
3. Choose **Create job**.
4. On the **Specify job details** page, under
   **Job settings** , specify the following.
   1. **Name** – the name of the
      transcription job.
   2. **Audio input type** –
      **Conversation**

5. For the remaining fields, specify the Amazon S3 location of your
   audio file and where you want to store the output of your transcription
   job.
6. Choose **Next**.
7. Choose **Create**.

###### To transcribe a medical conversation using a batch transcription job

(API)

- For the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API,
  specify the following.
  1.  For `MedicalTranscriptionJobName`, specify a name
      unique in your AWS account.
  2.  For `LanguageCode`, specify the language code that
      corresponds to the language spoken in your audio file and the
      language of your vocabulary filter.
  3.  For the `MediaFileUri` parameter of the
      `Media` object, specify the name of the audio
      file that you want to transcribe.
  4.  For `Specialty`, specify the medical specialty of
      the clinician speaking in the audio file as
      `PRIMARYCARE`.
  5.  For `Type`, specify
      `CONVERSATION`.
  6.  For `OutputBucketName`, specify the Amazon S3
      bucket to store the transcription results.The following is an example request that uses the AWS SDK for Python (Boto3) to
      transcribe a medical conversation of a clinician in the
      `PRIMARYCARE` specialty and a patient.

```

from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe', '`us-west-2`')
job_name = "`my-first-med-transcription-job`"
job_uri = "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-audio-file`.`flac`"
transcribe.start_medical_transcription_job(
      MedicalTranscriptionJobName = job_name,
      Media = {
        'MediaFileUri': job_uri
      },
      OutputBucketName = '`amzn-s3-demo-bucket`',
      OutputKey = '`output-files`/',
      LanguageCode = 'en-US',
      Specialty = 'PRIMARYCARE',
      Type = 'CONVERSATION'
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
clinician-patient conversation.

```

{
    "jobName": "conversation-medical-transcription-job",
    "accountId": "111122223333",
    "results": {
        "transcripts": [
            {
                "transcript": "... come for a follow up visit today..."
            }
        ],
        "items": [
            {
            `...`
                "start_time": "4.85",
                "end_time": "5.12",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "come"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "start_time": "5.12",
                "end_time": "5.29",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "for"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "start_time": "5.29",
                "end_time": "5.33",
                "alternatives": [
                    {
                        "confidence": "0.9955",
                        "content": "a"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "start_time": "5.33",
                "end_time": "5.66",
                "alternatives": [
                    {
                        "confidence": "0.9754",
                        "content": "follow"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "start_time": "5.66",
                "end_time": "5.75",
                "alternatives": [
                    {
                        "confidence": "0.9754",
                        "content": "up"
                    }
                ],
                "type": "pronunciation"
            },
            {
                "start_time": "5.75",
                "end_time": "6.02",
                "alternatives": [
                    {
                        "confidence": "1.0",
                        "content": "visit"
                    }
                ]
                `...`
    },
    "status": "COMPLETED"
}


```

###### To transcribe a medical conversation using a batch transcription job

(AWS CLI)

- Run the following code.

```


aws transcribe start-medical-transcription-job \
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
      "Type": "CONVERSATION"
  }
```
