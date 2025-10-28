# Creating long audio files

You can use the Amazon Polly console to create long speeches using asynchronous
synthesis with the same functionality as you can use with the AWS CLI. This is
done using the **Text-to-Speech** tab much like any other
synthesis.

Console
The other asynchronous synthesis functionality is also available via the
console. The **S3 synthesis tasks** tab reflects the
`ListSpeechSynthesisTasks` functionality, displaying all
tasks saved to the S3 bucket and enabling you to filter them if you want.
Clicking on a specific single task shows its details, reflecting
`GetSpeechSynthesisTask` functionality.

###### To synthesize a large text using the Amazon Polly console

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Choose the **Text-to-Speech** tab. Select
   **Long Form** as the engine if
   appropriate.
3. With **SSML** on or off, type or paste your text
   into the input box.
4. Choose the language, region, and voice for your text.
5. Choose **Save to S3**.

###### Note

Both the **Download** and
**Listen** options are greyed out if the
text length is above the 3,000 character limit for the real-time
`SynthesizeSpeech` operation. 6. The console opens a form so that you can choose where to store the
output file.

    1. Fill in the name of the destination Amazon S3 bucket.
    2. Optionally, fill in the prefix key of the output.


    ###### Note

    The output S3 bucket must be writable.
    3. If you want to be notified when the synthesis task is
     complete, provide an optional SNS topic identifier.


    ###### Note

    The SNS must be open for publication by the current
     console user to use this option. For more information,
     see [Amazon
     Simple Notification Service (SNS)](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/")
    4. Choose **Save to S3**.

###### To retrieve information on your speech synthesis tasks

1. In the console, choose the **S3 Synthesis Tasks**
   tab.
2. The tasks are displayed in date order. To filter the tasks, by
   status, choose **All statuses** and then choose the
   status to use.
3. To view the details of a specific task, choose the linked
   **Task ID**.

AWS CLI
Amazon Polly _asynchronous synthesis_ functionality uses three
`SpeechSynthesisTask` APIs to work with large amounts of
text:

- `StartSpeechSynthesisTask`: starts a new synthesis
  task.
- `GetSpeechSynthesisTask`: returns details about a
  previously submitted synthesis task.
- `ListSpeechSynthesisTasks`: lists all submitted
  synthesis tasks.

**Synthesizing large amounts of text
(`StartSpeechSynthesisTask`)**

When you want to create an audio file larger than one that you can create
with the real-time `SynthesizeSpeech`, use the
`StartSpeechSynthesisTask` operation. In addition to the
arguments needed for the `SynthesizeSpeech` operation,
`StartSpeechSynthesisTask` also requires the name of an Amazon S3
bucket. Two other optional arguments are also available: a key prefix for
the output file and the ARN for an SNS Topic if you want to receive status
notification about the task.

- `OutputS3BucketName`: The name of the Amazon S3 bucket where
  the synthesis should be uploaded. This bucket should be in the same
  region as the Amazon Polly service. Additionally, the IAM user being used
  to make the call should have access to the bucket. [Required]
- `OutputS3KeyPrefix`: Key prefix for the output file.
  Use this parameter if you want to save the output speech file in a
  custom directory-like key in your bucket. [Optional]
- `SnsTopicArn`: The SNS topic ARN to use if you want to
  receive notifications about status of the task. This SNS topic
  should be in the same region as the Amazon Polly service. Additionally, the
  IAM user being used to make the call should have access to the
  topic. [Optional]

For example, the following example can be used to run the
`start-speech-synthesis-task` AWS CLI command in the US East
(Ohio) region:

The following AWS CLI example is formatted for Unix, Linux, and macOS.
For Windows, replace the backslash (\) Unix continuation character at the end of each line with a caret (^) and use full quotation marks (") around the input text with single quotes (') for interior tags.

```
aws polly start-speech-synthesis-task \
  --region `us-east-2` \
  --endpoint-url "`https://polly.us-east-2.amazonaws.com/`" \
  --output-format mp3 \
  --output-s3-bucket-name `your-bucket-name` \
  --output-s3-key-prefix `optional/prefix/path/file` \
  --voice-id Joanna \
  --text `file://text_file.txt`

```

This will result in a response that looks similar to this:

```
"SynthesisTask":
{
     "OutputFormat": "mp3",
     "OutputUri": "https://s3.us-east-2.amazonaws.com/your-bucket-name/optional/prefix/path/file.<task_id>.mp3",
     "TextType": "text",
     "CreationTime": [..],
     "RequestCharacters": [..],
     "TaskStatus": "scheduled",
     "TaskId": [task_id],
     "VoiceId": "Joanna"
 }
```

The `start-speech-synthesis-task` operation returns several new
fields:

- `OutputUri`: the location of your output speech file.
- `TaskId`: a unique identifier for the speech synthesis
  task generated by Amazon Polly.
- `CreationTime`: a timestamp for when the task was
  initially submitted.
- `RequestCharacters`: the number of billable characters
  in the task.
- `TaskStatus`: provides information on the status of the
  submitted task.

When your task is submitted, the initial status will show
`scheduled`. When Amazon Polly starts processing the task,
the status will change to `inProgress` and later, to
`completed` or `failed`. If the task
fails, an error message will be returned when calling either the
GetSpeechSynthesisTask or ListSpeechSynthesisTasks operation.

When the task is completed, the speech file is available at the location
specified in `OutputUri`.

**Retrieving information on your speech synthesis
task**

You can get information on a task, such as errors, status, and so on,
using the `GetSpeechSynthesisTask` operation. To do this, you
will need the `task-id` returned by the
`StartSpeechSynthesisTask`.

For example, the following example can be used to run the
`get-speech-synthesis-task` AWS CLI command:

```
aws polly get-speech-synthesis-task \
--region `us-east-2` \
--endpoint-url "`https:// polly.us-east-2.amazonaws.com/`" \
--task-id `task identifier`

```

You can also list all speech synthesis tasks that you've run in the
current region using the `ListSpeechSynthesisTasks` operation.

For example, the following example can be used to run the
`list-speech-synthesis-tasks` AWS CLI command:

```
aws polly list-speech-synthesis-tasks \
--region `us-east-2` \
--endpoint-url "`https:// polly.us-east-2.amazonaws.com/`"
```
