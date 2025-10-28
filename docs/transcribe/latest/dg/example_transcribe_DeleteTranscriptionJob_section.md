# Use `DeleteTranscriptionJob` with an AWS SDK or CLI

The following code examples show how to use `DeleteTranscriptionJob`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Create and refine a custom vocabulary](example_transcribe_Scenario_CustomVocabulary_section.md "example_transcribe_Scenario_CustomVocabulary_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Transcribe#code-examples").

```

    /// <summary>
    /// Delete a transcription job. Also deletes the transcript associated with the job.
    /// </summary>
    /// <param name="jobName">Name of the transcription job to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteTranscriptionJob(string jobName)
    {
        var response = await _amazonTranscribeService.DeleteTranscriptionJobAsync(
            new DeleteTranscriptionJobRequest()
            {
                TranscriptionJobName = jobName
            });
        return response.HttpStatusCode == HttpStatusCode.OK;
    }



```

- For API details, see
  [DeleteTranscriptionJob](../../../goto/DotNetSDKV3/transcribe-2017-10-26/DeleteTranscriptionJob.md "../../../goto/DotNetSDKV3/transcribe-2017-10-26/DeleteTranscriptionJob.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To delete one of your transcription jobs**

The following `delete-transcription-job` example deletes one of your transcription jobs.

```
`aws transcribe delete-transcription-job \
 --transcription-job-name `your-transcription-job``

```

This command produces no output.

For more information, see [DeleteTranscriptionJob](API_DeleteTranscriptionJob.md "API_DeleteTranscriptionJob.md") in the _Amazon Transcribe Developer Guide_.

- For API details, see
  [DeleteTranscriptionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-transcription-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-transcription-job.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/transcribe#code-examples").

Delete a transcription job.

```
// Import the required AWS SDK clients and commands for Node.js
import { DeleteTranscriptionJobCommand } from "@aws-sdk/client-transcribe";
import { transcribeClient } from "./libs/transcribeClient.js";

// Set the parameters
export const params = {
  TranscriptionJobName: "JOB_NAME", // Required. For example, 'transciption_demo'
};

export const run = async () => {
  try {
    const data = await transcribeClient.send(
      new DeleteTranscriptionJobCommand(params),
    );
    console.log("Success - deleted");
    return data; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();



```

Create the client.

```
import { TranscribeClient } from "@aws-sdk/client-transcribe";
// Set the AWS Region.
const REGION = "REGION"; //e.g. "us-east-1"
// Create an Amazon Transcribe service client object.
const transcribeClient = new TranscribeClient({ region: REGION });
export { transcribeClient };


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/transcribe-examples-section.md#transcribe-delete-job "../../../sdk-for-javascript/v3/developer-guide/transcribe-examples-section.md#transcribe-delete-job").
- For API details, see
  [DeleteTranscriptionJob](../../../AWSJavaScriptSDK/v3/latest/client/transcribe/command/DeleteTranscriptionJobCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/transcribe/command/DeleteTranscriptionJobCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/transcribe#code-examples").

```
def delete_job(job_name, transcribe_client):
    """
    Deletes a transcription job. This also deletes the transcript associated with
    the job.

    :param job_name: The name of the job to delete.
    :param transcribe_client: The Boto3 Transcribe client.
    """
    try:
        transcribe_client.delete_transcription_job(TranscriptionJobName=job_name)
        logger.info("Deleted job %s.", job_name)
    except ClientError:
        logger.exception("Couldn't delete job %s.", job_name)
        raise




```

- For API details, see
  [DeleteTranscriptionJob](../../../goto/boto3/transcribe-2017-10-26/DeleteTranscriptionJob.md "../../../goto/boto3/transcribe-2017-10-26/DeleteTranscriptionJob.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](getting-started-sdk.md#sdk-general-information-section "getting-started-sdk.md#sdk-general-information-section").
This topic also includes information about getting started and details about previous SDK versions.
