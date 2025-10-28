# Use `GetJobRun` with an AWS SDK or CLI

The following code examples show how to use `GetJobRun`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_glue_Scenario_GetStartedCrawlersJobs_section.md "example_glue_Scenario_GetStartedCrawlersJobs_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Glue#code-examples").

```
    /// <summary>
    /// Get information about a specific AWS Glue job run.
    /// </summary>
    /// <param name="jobName">The name of the job.</param>
    /// <param name="jobRunId">The Id of the job run.</param>
    /// <returns>A JobRun object with information about the job run.</returns>
    public async Task<JobRun> GetJobRunAsync(string jobName, string jobRunId)
    {
        var response = await _amazonGlue.GetJobRunAsync(new GetJobRunRequest { JobName = jobName, RunId = jobRunId });
        return response.JobRun;
    }



```

- For API details, see
  [GetJobRun](../../../goto/DotNetSDKV3/glue-2017-03-31/GetJobRun.md "../../../goto/DotNetSDKV3/glue-2017-03-31/GetJobRun.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/glue#code-examples").

```
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region in which the bucket was created (overrides config file).
        // clientConfig.region = "us-east-1";

    Aws::Glue::GlueClient client(clientConfig);

        Aws::Glue::Model::GetJobRunRequest jobRunRequest;
        jobRunRequest.SetJobName(jobName);
        jobRunRequest.SetRunId(jobRunID);

        Aws::Glue::Model::GetJobRunOutcome jobRunOutcome = client.GetJobRun(
                jobRunRequest);

        if (jobRunOutcome.IsSuccess()) {
            std::cout << "Displaying the job run JSON description." << std::endl;
            std::cout
                    << jobRunOutcome.GetResult().GetJobRun().Jsonize().View().WriteReadable()
                    << std::endl;
        }
        else {
            std::cerr << "Error get a job run. "
                      << jobRunOutcome.GetError().GetMessage()
                      << std::endl;
        }


```

- For API details, see
  [GetJobRun](../../../goto/SdkForCpp/glue-2017-03-31/GetJobRun.md "../../../goto/SdkForCpp/glue-2017-03-31/GetJobRun.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To get information about a job run**

The following `get-job-run` example retrieves information about a job run.

```
`aws glue get-job-run \
 --job-name `"Combine legistators data"` \
 --run-id `jr_012e176506505074d94d761755e5c62538ee1aad6f17d39f527e9140cf0c9a5e``

```

Output:

```
{
    "JobRun": {
        "Id": "jr_012e176506505074d94d761755e5c62538ee1aad6f17d39f527e9140cf0c9a5e",
        "Attempt": 0,
        "JobName": "Combine legistators data",
        "StartedOn": 1602873931.255,
        "LastModifiedOn": 1602874075.985,
        "CompletedOn": 1602874075.985,
        "JobRunState": "SUCCEEDED",
        "Arguments": {
            "--enable-continuous-cloudwatch-log": "true",
            "--enable-metrics": "",
            "--enable-spark-ui": "true",
            "--job-bookmark-option": "job-bookmark-enable",
            "--spark-event-logs-path": "s3://aws-glue-assets-111122223333-us-east-1/sparkHistoryLogs/"
        },
        "PredecessorRuns": [],
        "AllocatedCapacity": 10,
        "ExecutionTime": 117,
        "Timeout": 2880,
        "MaxCapacity": 10.0,
        "WorkerType": "G.1X",
        "NumberOfWorkers": 10,
        "LogGroupName": "/aws-glue/jobs",
        "GlueVersion": "2.0"
    }
}
```

For more information, see [Job Runs](aws-glue-api-jobs-runs.md "aws-glue-api-jobs-runs.md") in the _AWS Glue Developer Guide_.

- For API details, see
  [GetJobRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-run.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-run.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/glue#code-examples").

```
const getJobRun = (jobName, jobRunId) => {
  const client = new GlueClient({});
  const command = new GetJobRunCommand({
    JobName: jobName,
    RunId: jobRunId,
  });

  return client.send(command);
};


```

- For API details, see
  [GetJobRun](../../../AWSJavaScriptSDK/v3/latest/client/glue/command/GetJobRunCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/glue/command/GetJobRunCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PHP

**SDK for PHP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/glue#code-examples").

```
        $jobName = 'test-job-' . $uniqid;

        $outputBucketUrl = "s3://$bucketName";
        $runId = $glueService->startJobRun($jobName, $databaseName, $tables, $outputBucketUrl)['JobRunId'];

        echo "waiting for job";
        do {
            $jobRun = $glueService->getJobRun($jobName, $runId);
            echo ".";
            sleep(10);
        } while (!array_intersect([$jobRun['JobRun']['JobRunState']], ['SUCCEEDED', 'STOPPED', 'FAILED', 'TIMEOUT']));
        echo "\n";

    public function getJobRun($jobName, $runId, $predecessorsIncluded = false): Result
    {
        return $this->glueClient->getJobRun([
            'JobName' => $jobName,
            'RunId' => $runId,
            'PredecessorsIncluded' => $predecessorsIncluded,
        ]);
    }


```

- For API details, see
  [GetJobRun](../../../goto/SdkForPHPV3/glue-2017-03-31/GetJobRun.md "../../../goto/SdkForPHPV3/glue-2017-03-31/GetJobRun.md")
  in _AWS SDK for PHP API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glue#code-examples").

```
class GlueWrapper:
    """Encapsulates AWS Glue actions."""

    def __init__(self, glue_client):
        """
        :param glue_client: A Boto3 Glue client.
        """
        self.glue_client = glue_client


    def get_job_run(self, name, run_id):
        """
        Gets information about a single job run.

        :param name: The name of the job definition for the run.
        :param run_id: The ID of the run.
        :return: Information about the run.
        """
        try:
            response = self.glue_client.get_job_run(JobName=name, RunId=run_id)
        except ClientError as err:
            logger.error(
                "Couldn't get job run %s/%s. Here's why: %s: %s",
                name,
                run_id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response["JobRun"]



```

- For API details, see
  [GetJobRun](../../../goto/boto3/glue-2017-03-31/GetJobRun.md "../../../goto/boto3/glue-2017-03-31/GetJobRun.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/glue#code-examples").

```

# The `GlueWrapper` class serves as a wrapper around the AWS Glue API, providing a simplified interface for common operations.
# It encapsulates the functionality of the AWS SDK for Glue and provides methods for interacting with Glue crawlers, databases, tables, jobs, and S3 resources.
# The class initializes with a Glue client and a logger, allowing it to make API calls and log any errors or informational messages.
class GlueWrapper
  def initialize(glue_client, logger)
    @glue_client = glue_client
    @logger = logger
  end

  # Retrieves data for a specific job run.
  #
  # @param job_name [String] The name of the job run to retrieve data for.
  # @return [Glue::Types::GetJobRunResponse]
  def get_job_run(job_name, run_id)
    @glue_client.get_job_run(job_name: job_name, run_id: run_id)
  rescue Aws::Glue::Errors::GlueException => e
    @logger.error("Glue could not get job runs: \n#{e.message}")
  end


```

- For API details, see
  [GetJobRun](../../../goto/SdkForRubyV3/glue-2017-03-31/GetJobRun.md "../../../goto/SdkForRubyV3/glue-2017-03-31/GetJobRun.md")
  in _AWS SDK for Ruby API Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/glue#code-examples").

```
        let get_job_run = || async {
            Ok::<JobRun, GlueMvpError>(
                glue.get_job_run()
                    .job_name(self.job())
                    .run_id(job_run_id.to_string())
                    .send()
                    .await
                    .map_err(GlueMvpError::from_glue_sdk)?
                    .job_run()
                    .ok_or_else(|| GlueMvpError::Unknown("Failed to get job_run".into()))?
                    .to_owned(),
            )
        };

        let mut job_run = get_job_run().await?;
        let mut state = job_run.job_run_state().unwrap_or(&unknown_state).to_owned();

        while matches!(
            state,
            JobRunState::Starting | JobRunState::Stopping | JobRunState::Running
        ) {
            info!(?state, "Waiting for job to finish");
            tokio::time::sleep(self.wait_delay).await;

            job_run = get_job_run().await?;
            state = job_run.job_run_state().unwrap_or(&unknown_state).to_owned();
        }


```

- For API details, see
  [GetJobRun](https://docs.rs/aws-sdk-glue/latest/aws_sdk_glue/client/struct.Client.html#method.get_job_run "https://docs.rs/aws-sdk-glue/latest/aws_sdk_glue/client/struct.Client.html#method.get_job_run")
  in _AWS SDK for Rust API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/glue#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/glue#code-examples").

```
import AWSClientRuntime
import AWSGlue

    /// Get information about a specific AWS Glue job run.
    ///
    /// - Parameters:
    ///   - glueClient: The AWS Glue client to use.
    ///   - jobName: The name of the job to return job run data for.
    ///   - id: The run ID of the specific job run to return.
    ///
    /// - Returns: A `GlueClientTypes.JobRun` object describing the state of
    ///   the job run, or `nil` if an error occurs.
    func getJobRun(glueClient: GlueClient, name jobName: String, id: String) async -> GlueClientTypes.JobRun? {
        do {
            let output = try await glueClient.getJobRun(
                input: GetJobRunInput(
                    jobName: jobName,
                    runId: id
                )
            )

            return output.jobRun
        } catch {
            return nil
        }
    }


```

- For API details, see
  [GetJobRun](<https://sdk.amazonaws.com/swift/api/awsglue/latest/documentation/awsglue/glueclient/getjobrun(input:)> "https://sdk.amazonaws.com/swift/api/awsglue/latest/documentation/awsglue/glueclient/getjobrun(input:)")
  in _AWS SDK for Swift API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
