# EMR Serverless Job resiliency

EMR Serverless releases 7.1.0 and higher include support for job resiliency, so it automatically retries any failed jobs without any manual input from you. Another benefit of job resiliency
is that EMR Serverless moves job runs to different Availability Zone (AZ) should an AZ experience any issues.

To enable job resiliency for a job, set the retry policy for your job. A retry policy makes sure that EMR Serverless automatically restarts a job
if it fails at any point. Retry policies are supported for batch and streaming jobs, so customize job resiliency according to your use case. The following
table compares the behaviors and differences of job resiliency across batch and streaming jobs.

|                           | Batch jobs                                                                                      | Streaming jobs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default behavior          | Doesn't rerun the job.                                                                          | Always retries running the job as the application creates checkpoints while running the job.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Retry point               | Batch jobs don't have checkpoints, so EMR Serverless always re-runs the job from the beginning. | Streaming jobs support checkpoints, so configure the streaming query<br>to save runtime state and progress to a checkpoint location in Amazon S3. EMR Serverless resumes the job run from the checkpoint. For more information, refer to<br>[Recovering from failures with Checkpointing](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing") in the Apache Spark documentation. |
| Maximum of retry attempts | Allows for a maximum of 10 retries.                                                             | Streaming jobs have built-in thrash prevention control, so the application stops retrying jobs if they continue failing after one hour.<br>The default number of retries within one hour is five attempts. You can configure this<br>number of retries to be between 1 or 10. You can't customize the number of maximum attempts. A value of 1 indicates no retries.                                                                                                                                                                                                                      |

When EMR Serverless attempts to rerun a job, it also indexes the job with an attempt number, so track the lifecycle of a job across its attempts.

Use the EMR Serverless API operations or the AWS CLI to change job resiliency or access information related to job resiliency. For more information,
refer to the [EMR Serverless API guide](../../../emr-serverless/latest/APIReference/Welcome.md "../../../emr-serverless/latest/APIReference/Welcome.md").

By default, EMR Serverless doesn't rerun batch jobs. To enable retries for batch jobs, configure the `maxAttempts` parameter
when starting a batch job run. The `maxAttempts` parameter is applicable only to batch jobs. The default is 1, which means to not rerun the job.
Accepted values are 1 to 10, inclusive.

The following example demonstrates how to specify a max number of 10 attempts when starting a job run.

```
aws emr-serverless start-job-run
 --application-id `<APPLICATION_ID>` \
 --execution-role-arn `<JOB_EXECUTION_ROLE>` \
 --mode 'BATCH' \
 --retry-policy '{
    "maxAttempts": 10
 }' \
 --job-driver '{
    "sparkSubmit": {
         "entryPoint": "/usr/lib/spark/examples/jars/spark-examples-does-not-exist.jar",
         "entryPointArguments": ["1"],
         "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi"
     }
}'
```

EMR Serverless indefinitely retries streaming jobs if they fail. To prevent thrashing because of repeated unrecoverable failures,
use the `maxFailedAttemptsPerHour` to configure thrash prevention control for streaming job retries. This parameter lets you specify
the maximum number of failed attempts allowed with an hour before EMR Serverless stops retrying. The default is five. Accepted values are
1 to 10, inclusive.

```
aws emr-serverless start-job-run
 --application-id `<APPPLICATION_ID>` \
 --execution-role-arn `<JOB_EXECUTION_ROLE>` \
 --mode 'STREAMING' \
 --retry-policy '{
    "maxFailedAttemptsPerHour": 7
 }' \
 --job-driver '{
    "sparkSubmit": {
         "entryPoint": "/usr/lib/spark/examples/jars/spark-examples-does-not-exist.jar",
         "entryPointArguments": ["1"],
         "sparkSubmitParameters": "--class org.apache.spark.examples.SparkPi"
     }
}'
```

You can also use the other job run API operations get information about jobs. For example, use the
`attempt` parameter with the `GetJobRun` operation to get details about a specific job attempt. If you don't include the
`attempt` parameter, the operation returns information about the latest attempt.

```
aws emr-serverless get-job-run \
    --job-run-id `job-run-id` \
    --application-id `application-id` \
    --attempt 1
```

The `ListJobRunAttempts` operation returns information about all attempts related to a job run.

```
aws emr-serverless list-job-run-attempts \
  --application-id `application-id` \
  --job-run-id `job-run-id`
```

The `GetDashboardForJobRun` operation creates and returns a URL that use to access the application UIs for a job run. The `attempt`
parameter lets you get a URL for a specific attempt. If you don't include the
`attempt` parameter, the operation returns information about the latest attempt.

```
aws emr-serverless get-dashboard-for-job-run \
    --application-id `application-id` \
    --job-run-id `job-run-id` \
    --attempt 1
```

## Monitoring a job with a retry policy

Job resiliency support also adds the new event **EMR Serverless job run retry**. EMR Serverless publishes this event
on every retry of the job. You can use this notification to track retries of the job. For more information about events, refer to
[Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

## Logging with retry policy

Every time EMR Serverless retries a job, the attempt generates its own set of logs. To ensure that EMR Serverless can successfully
deliver these logs to Amazon S3 and Amazon CloudWatch without overwriting any, EMR Serverless adds a prefix to the format of the S3 log path and CloudWatch log stream name
to include the attempt number of the job.

The following is an example of what the format looks like.

```
'/applications/<applicationId>/jobs/<jobId>/attempts/<attemptNumber>/'.
```

This format ensures EMR Serverless publishes all of the logs for each attempt of the job to its own designated location in Amazon S3 and CloudWatch. For more details, refer to
[Storing logs](logging.md "logging.md").

###### Note

EMR Serverless only uses this prefix format with all streaming jobs and any batch jobs that have retry enabled.
