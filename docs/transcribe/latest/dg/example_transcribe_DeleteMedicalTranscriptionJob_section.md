# Use `DeleteMedicalTranscriptionJob` with an AWS SDK or CLI

The following code examples show how to use `DeleteMedicalTranscriptionJob`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Transcribe#code-examples").

```

    /// <summary>
    /// Delete a medical transcription job. Also deletes the transcript associated with the job.
    /// </summary>
    /// <param name="jobName">Name of the medical transcription job to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteMedicalTranscriptionJob(string jobName)
    {
        var response = await _amazonTranscribeService.DeleteMedicalTranscriptionJobAsync(
            new DeleteMedicalTranscriptionJobRequest()
            {
                MedicalTranscriptionJobName = jobName
            });
        return response.HttpStatusCode == HttpStatusCode.OK;
    }



```

- For API details, see
  [DeleteMedicalTranscriptionJob](../../../goto/DotNetSDKV3/transcribe-2017-10-26/DeleteMedicalTranscriptionJob.md "../../../goto/DotNetSDKV3/transcribe-2017-10-26/DeleteMedicalTranscriptionJob.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To delete a medical transcription job**

The following `delete-medical-transcription-job` example deletes a medical transcription job.

```
`aws transcribe delete-medical-transcription-job \
 --`medical-transcription-job-name` medical-transcription-job-name`

```

This command produces no output.

For more information, see [DeleteMedicalTranscriptionJob](API_DeleteMedicalTranscriptionJob.md "API_DeleteMedicalTranscriptionJob.md") in the _Amazon Transcribe Developer Guide_.

- For API details, see
  [DeleteMedicalTranscriptionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-medical-transcription-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-medical-transcription-job.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/transcribe#code-examples").

Create the client.

```
import { TranscribeClient } from "@aws-sdk/client-transcribe";
// Set the AWS Region.
const REGION = "REGION"; //e.g. "us-east-1"
// Create an Amazon Transcribe service client object.
const transcribeClient = new TranscribeClient({ region: REGION });
export { transcribeClient };


```

Delete a medical transcription job.

```
// Import the required AWS SDK clients and commands for Node.js
import { DeleteMedicalTranscriptionJobCommand } from "@aws-sdk/client-transcribe";
import { transcribeClient } from "./libs/transcribeClient.js";

// Set the parameters
export const params = {
  MedicalTranscriptionJobName: "MEDICAL_JOB_NAME", // For example, 'medical_transciption_demo'
};

export const run = async () => {
  try {
    const data = await transcribeClient.send(
      new DeleteMedicalTranscriptionJobCommand(params),
    );
    console.log("Success - deleted");
    return data; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();



```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/transcribe-medical-examples-section.md#transcribe-delete-medical-job "../../../sdk-for-javascript/v3/developer-guide/transcribe-medical-examples-section.md#transcribe-delete-medical-job").
- For API details, see
  [DeleteMedicalTranscriptionJob](../../../AWSJavaScriptSDK/v3/latest/client/transcribe/command/DeleteMedicalTranscriptionJobCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/transcribe/command/DeleteMedicalTranscriptionJobCommand.md")
  in _AWS SDK for JavaScript API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](getting-started-sdk.md#sdk-general-information-section "getting-started-sdk.md#sdk-general-information-section").
This topic also includes information about getting started and details about previous SDK versions.
