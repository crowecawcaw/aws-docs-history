# Identifying PHI in an audio file

Use
a batch transcription job to transcribe audio files and identify the personal health
information (PHI) within them. When you
activate Personal Health Information (PHI) Identification, Amazon Transcribe Medical labels the PHI that it
identified in the transcription results. For information about the PHI that Amazon Transcribe Medical can
identify, see [Identifying personal health information (PHI) in a
transcription](phi-id.md "phi-id.md").

You can start a batch transcription job using either the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API or the AWS Management Console.

To
use the AWS Management Console to transcribe a clinician-patient dialogue, create a
transcription job and choose **Conversation** for
**Audio input type**.

###### To

transcribe an audio file and identify its PHI
(AWS Management Console)

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, under Amazon Transcribe Medical, choose **Transcription
   jobs**.
3. Choose **Create job**.
4. On the **Specify job details** page, under
   **Job settings** , specify the following.
   1. **Name** – The name of the
      transcription job that is unique to your AWS account.
   2. **Audio input type** –
      **Conversation** or
      **Dictation**.

5. For the remaining fields, specify the Amazon S3 location of your
   audio file and where you want to store the output of your transcription
   job.
6. Choose **Next**.
7. Under **Audio settings**, choose **PHI
   Identification**.
8. Choose **Create**.

###### To transcribe an audio file and identify its PHI using a batch

transcription job (API)

- For the [`StartMedicalTranscriptionJob`](../APIReference/API_StartMedicalTranscriptionJob.md "../APIReference/API_StartMedicalTranscriptionJob.md") API, specify the following.
  1.  For `MedicalTranscriptionJobName`,
      specify
      a name that is unique to your AWS account.
  2.  For `LanguageCode`, specify the language code that
      corresponds to the language spoken in your audio file.
  3.  For the `MediaFileUri` parameter of the
      `Media` object, specify the name of the audio
      file that you want to transcribe.
  4.  For `Specialty`, specify the medical specialty of
      the clinician speaking in the audio file as
      `PRIMARYCARE`.
  5.  For `Type`, specify either
      `CONVERSATION` or `DICTATION`.
  6.  For `OutputBucketName`, specify the Amazon S3
      bucket where you want to store the transcription results.The following is an example request that uses the AWS SDK for Python (Boto3) to
      transcribe an audio file and identify the PHI of a patient.

```

from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe')
job_name = "`my-first-transcription-job`"
job_uri = "s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-audio-file`.`flac`"
transcribe.start_medical_transcription_job(
      MedicalTranscriptionJobName = job_name,
      Media = {'MediaFileUri': job_uri},
      LanguageCode = 'en-US',
      ContentIdentificationType = 'PHI',
      Specialty = 'PRIMARYCARE',
      Type = '`type`', # Specify 'CONVERSATION' for a medical conversation. Specify 'DICTATION' for a medical dictation.
      OutputBucketName = '`amzn-s3-demo-bucket`'
  )
while True:
    status = transcribe.get_medical_transcription_job(MedicalTranscriptionJobName = job_name)
    if status['MedicalTranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)

```

The following example code shows the transcription results with patient PHI
identified.

```

{
    "jobName": "my-medical-transcription-job-name",
    "accountId": "111122223333",
    "results": {
        "transcripts": [{
            "transcript": "The patient's name is Bertrand."
        }],
        "items": [{
                "id": 0,
            "start_time": "0.0",
            "end_time": "0.37",
            "alternatives": [{
                "confidence": "0.9993",
                "content": "The"
            }],
            "type": "pronunciation"
        }, {
                "id": 1,
            "start_time": "0.37",
            "end_time": "0.44",
            "alternatives": [{
                "confidence": "0.9981",
                "content": "patient's"
            }],
            "type": "pronunciation"
        }, {
                "id": 2,
            "start_time": "0.44",
            "end_time": "0.52",
            "alternatives": [{
                "confidence": "1.0",
                "content": "name"
            }],
            "type": "pronunciation"
        }, {
                "id": 3,
            "start_time": "0.52",
            "end_time": "0.92",
            "alternatives": [{
                "confidence": "1.0",
                "content": "is"
            }],
            "type": "pronunciation"
        }, {
                "id": 4,
            "start_time": "0.92",
            "end_time": "0.9989",
            "alternatives": [{
                "confidence": "1.0",
                "content": "Bertrand"
            }],
            "type": "pronunciation"
        }, {
                "id": 5,
            "alternatives": [{
                "confidence": "0.0",
                "content": "."
            }],
            "type": "punctuation"
        }],
        "entities": [{
            "content": "Bertrand",
            "category": "PHI*-Personal*",
            "startTime": 0.92,
            "endTime": 1.2,
            "confidence": 0.9989
        }],
        "audio_segments": [
            {
                "id": 0,
                "transcript": "The patient's name is Bertrand.",
                "start_time": "0.0",
                "end_time": "0.9989",
                "items": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                ]
            }
        ]
    },
    "status": "COMPLETED"
}


```

###### To transcribe an audio file and identify PHI using a batch transcription

job (AWS CLI)

- Run the
  following
  code.

```
aws transcribe start-medical-transcription-job \
--medical-transcription-job-name `my-medical-transcription-job-name`\
--language-code en-US \
--media MediaFileUri="s3://`amzn-s3-demo-bucket`/`my-input-files`/`my-audio-file`.`flac`" \
--output-bucket-name `amzn-s3-demo-bucket` \
--specialty PRIMARYCARE \
--type `type` \ # Choose `CONVERSATION` to transcribe a medical conversation. Choose `DICTATION` to transcribe a medical dictation.
--content-identification-type PHI


```
