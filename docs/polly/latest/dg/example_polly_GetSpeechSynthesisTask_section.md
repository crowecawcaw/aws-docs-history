# Use `GetSpeechSynthesisTask` with an AWS SDK or CLI

The following code examples show how to use `GetSpeechSynthesisTask`.

CLI

**AWS CLI**

**To get information about a speech synthesis task**

The following `get-speech-synthesis-task` example retrieves information about the specified speech synthesis task.

```
`aws polly get-speech-synthesis-task \
 --task-id `70b61c0f-57ce-4715-a247-cae8729dcce9``

```

Output:

```
{
    "SynthesisTask": {
        "TaskId": "70b61c0f-57ce-4715-a247-cae8729dcce9",
        "TaskStatus": "completed",
        "OutputUri": "https://s3.us-west-2.amazonaws.com/amzn-s3-demo-bucket/70b61c0f-57ce-4715-a247-cae8729dcce9.mp3",
        "CreationTime": 1603911042.689,
        "RequestCharacters": 1311,
        "OutputFormat": "mp3",
        "TextType": "text",
        "VoiceId": "Joanna"
    }
}
```

For more information, see [Creating long audio files](longer-cli.md "longer-cli.md") in the _Amazon Polly Developer Guide_.

- For API details, see
  [GetSpeechSynthesisTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-speech-synthesis-task.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-speech-synthesis-task.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples").

```
class PollyWrapper:
    """Encapsulates Amazon Polly functions."""

    def __init__(self, polly_client, s3_resource):
        """
        :param polly_client: A Boto3 Amazon Polly client.
        :param s3_resource: A Boto3 Amazon Simple Storage Service (Amazon S3) resource.
        """
        self.polly_client = polly_client
        self.s3_resource = s3_resource
        self.voice_metadata = None


    def get_speech_synthesis_task(self, task_id):
        """
        Gets metadata about an asynchronous speech synthesis task, such as its status.

        :param task_id: The ID of the task to retrieve.
        :return: Metadata about the task.
        """
        try:
            response = self.polly_client.get_speech_synthesis_task(TaskId=task_id)
            task = response["SynthesisTask"]
            logger.info("Got synthesis task. Status is %s.", task["TaskStatus"])
        except ClientError:
            logger.exception("Couldn't get synthesis task %s.", task_id)
            raise
        else:
            return task



```

- For API details, see
  [GetSpeechSynthesisTask](../../../goto/boto3/polly-2016-06-10/GetSpeechSynthesisTask.md "../../../goto/boto3/polly-2016-06-10/GetSpeechSynthesisTask.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Polly with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
