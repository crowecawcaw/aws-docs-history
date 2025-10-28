# Using a text file to create a medical

custom vocabulary

To create a custom vocabulary, you must have prepared a text file that contains a
collection a words or phrases. Amazon Transcribe Medical uses this text file to create a custom vocabulary
that you can use to improve the transcription accuracy of those words or phrases. You
can create a custom vocabulary using the [`CreateMedicalVocabulary`](../APIReference/API_CreateMedicalVocabulary.md "../APIReference/API_CreateMedicalVocabulary.md") API or the Amazon Transcribe Medical
console.

To use the AWS Management Console to create a custom vocabulary, you provide the Amazon S3 URI
of the text file containing your words or phrases.

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/").
2. In the navigation pane, under Amazon Transcribe Medical, choose **Custom
   vocabulary**.
3. For **Name**, under **Vocabulary
   settings**, choose a name for your custom
   vocabulary.
4. Specify the location of your audio file or video file in Amazon S3:
   - For **Vocabulary input file location on S3**
     under **Vocabulary settings**, specify the Amazon S3
     URI that identifies the text file you will use to create your
     custom vocabulary.
   - For **Vocabulary input file location in
     S3**, choose **Browse S3** to
     browse for the text file and choose it.

5. Choose **Create vocabulary**.
   You can see the processing status of your custom vocabulary in the
   AWS Management Console.

###### To create a medical custom vocabulary (API)

- For the [`StartTranscriptionJob`](../APIReference/API_StartTranscriptionJob.md "../APIReference/API_StartTranscriptionJob.md") API, specify the
  following.

      1. For `LanguageCode`, specify
       `en-US`.
      2. For `VocabularyFileUri`, specify the Amazon S3 location
       of the text file that you use to define your custom
       vocabulary.
      3. For `VocabularyName`, specify a name for your
       custom vocabulary. The name you specify must be unique within
       your AWS account.

  To see the processing status of your custom vocabulary, use the
  [`GetMedicalVocabulary`](../APIReference/API_GetMedicalVocabulary.md "../APIReference/API_GetMedicalVocabulary.md")
  API.

The following is an example request using the AWS SDK for Python (Boto3) to create a custom
vocabulary.

```

from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe', '`us-west-2`')
vocab_name = "`my-first-vocabulary`"
response = transcribe.create_medical_vocabulary(
    VocabularyName = job_name,
    VocabularyFileUri = 's3://`amzn-s3-demo-bucket`/`my-vocabularies`/`my-vocabulary-table`.txt'
    LanguageCode = 'en-US',
  )

while True:
    status = transcribe.get_medical_vocabulary(VocabularyName = vocab_name)
    if status['VocabularyState'] in ['READY', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)
```

###### To enable speaker partitioning in a batch transcription job

(AWS CLI)

- Run the following code.

```

aws transcribe create-medical-vocabulary \
--vocabulary-name `my-first-vocabulary` \
--vocabulary-file-uri s3://`amzn-s3-demo-bucket`/`my-vocabularies`/`my-vocabulary-file`.txt \
--language-code `en-US`
```
