

# GetJob
<a name="get-job-api"></a>

The `GetJob` operation retrieves information about a specific job, including its current status, configuration, timestamps, and any error information. Use this operation to monitor job progress and verify configuration details. For completed jobs, you can use this information to verify successful processing before accessing results.

For more information, see [GetJob](https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_GetJob.html) in the *Amazon Location Service API Reference*.

For example requests, responses, and CLI commands for this API, see [How to monitor job progress](https://docs.aws.amazon.com/location/latest/developerguide/monitoring-job-progress.html).

## Use cases
<a name="get-job-use-cases"></a>
+ **Job status and progress monitoring:** Track job lifecycle progression through pending, running, and completion states to determine when processing is complete and results are available for download. Monitor job status for workflow management and reporting.
+ **Error diagnosis:** Retrieve detailed error information when jobs fail, including specific error messages and failure reasons to troubleshoot processing issues.
+ **Configuration verification:** Confirm job configuration details including input/output locations, execution roles, and requested features before processing begins.

## Understand the request
<a name="get-job-request-parameters"></a>

The `GetJob` request requires only a single parameter to retrieve comprehensive information about a specific job. This simple request structure makes it easy to monitor job status and retrieve detailed configuration and processing information.

The request includes the following parameter:

**Job identification**  
Required parameter specifying which job to retrieve information about.  
+ `JobId`: The unique identifier of the job to retrieve. Must be 1-100 characters matching pattern `[-._\w]+`. This is the same identifier returned by the `StartJob` operation when the job was created.

## Understand the response
<a name="get-job-response-details"></a>

The `GetJob` response provides information about the specified job, including its current status, complete configuration, processing timestamps, and any error information. You can use this response to monitor job status and troubleshoot any errors that may arise.

The response includes the following fields:

**Job identification**  
Unique identifiers and basic job information.  
+ `JobId`: The unique job identifier used for monitoring and management operations.
+ `JobArn`: ARN that uniquely identifies the job within AWS.
+ `Name`: Human-readable job name if specified during job creation.

**Job status and lifecycle**  
Current job state and processing timeline information.  
+ `Status`: Current job status indicating processing state (Pending, Running, Completed, Failed, Cancelling, or Cancelled).
+ `CreatedAt`: Job creation timestamp in ISO 8601 format.
+ `UpdatedAt`: Last status update timestamp in ISO 8601 format.
+ `EndedAt`: Job completion timestamp in ISO 8601 format. Only present for jobs in terminal states.

**Job configuration**  
Complete job configuration as specified during creation.  
+ `Action`: The type of operation being performed (currently only `ValidateAddress` is supported).
+ `ExecutionRoleArn`: IAM role ARN used for accessing Amazon S3 buckets during job execution.
+ `InputOptions`: Input configuration including Amazon S3 location and data format.
+ `OutputOptions`: Output configuration including Amazon S3 destination and result format.
+ `ActionOptions`: Optional additional features requested for the job, such as `Position` or `CountrySpecificAttributes`.

**Error information**  
When a job fails, the response includes error details to help you diagnose and resolve the issue.  
+ `Error`: A `JobError` object containing details about the failure. This object includes the following fields:
  + `Code`: An error code that identifies the type of failure.
  + `Messages`: A list of human-readable messages that provide additional context for troubleshooting.