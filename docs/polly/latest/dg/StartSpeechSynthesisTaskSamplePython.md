# StartSpeechSynthesisTask

The following Python code example uses the AWS SDK for Python (Boto) to list the lexicons
in your account in the region specified in your local AWS configuration. For
information about creating the configuration file, see [Setting up the AWS CLI](setup-cli.md "setup-cli.md").

For more information, see the reference for [`StartSpeechSynthesisTask`](API_StartSpeechSynthesisTask.md "API_StartSpeechSynthesisTask.md") API.

```
import boto3
import time

polly_client = boto3.Session(
                aws_access_key_id='',
    aws_secret_access_key='',
    region_name='eu-west-2').client('polly')

response = polly_client.start_speech_synthesis_task(VoiceId='Joanna',
                OutputS3BucketName='synth-books-buckets',
                OutputS3KeyPrefix='key',
                OutputFormat='mp3',
                Text='This is a sample text to be synthesized.',
                Engine='neural')

taskId = response['SynthesisTask']['TaskId']

print( "Task id is {} ".format(taskId))

task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)

print(task_status)
```
