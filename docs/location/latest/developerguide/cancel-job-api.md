# CancelJob

The `CancelJob` operation stops a running or pending job. Only jobs in
**Pending** or **Running** states can be cancelled. Cancellation is asynchronous, so
you should monitor the job status to confirm completion. Cancelled jobs may have
partial results in the output location depending on when cancellation occurs during
processing.

For more information, see [CancelJob](../APIReference/API_geojobs_CancelJob.md "../APIReference/API_geojobs_CancelJob.md") in the
_Amazon Location Service API Reference_.

For example requests, responses, and CLI commands for this API, see [How
to cancel a job](canceling-job.md "canceling-job.md").

## Use cases

- **Stop unnecessary processing:** Cancel jobs
  that were submitted with incorrect configuration, are no longer needed due to
  changed business requirements, or were started by mistake. This can prevent
  wasted resources and unnecessary charges.
- **Resource and cost optimization:** Free up
  processing capacity by cancelling lower-priority jobs when higher-priority
  tasks need to be processed.

## Understand the request

The `CancelJob` request requires only a single parameter to identify
which job to cancel. This simple request structure makes it easy to stop
processing for jobs that are no longer needed.

The request includes the following parameter:

**Job identification**

Required parameter that specifies which job to cancel.

- `JobId`: The unique identifier of the job to
  cancel. Must be 1-100 characters matching pattern
  `[-._\w]+`. This is the same identifier
  returned by the `StartJob` operation when the job
  was created. Only jobs in `Pending` or
  `Running` status can be cancelled.

## Understand the response

The `CancelJob` response confirms the cancellation request and
provides the job's updated status. Because cancellation is asynchronous, you
should use the `GetJob` operation to monitor the job until it reaches
the `Cancelled` status.

The response includes the following fields:

**Job identification**

Unique identifiers for the job being cancelled.

- `JobId`: The unique job identifier.
- `JobArn`: Amazon Resource Name (ARN) of the job
  being cancelled.

**Cancellation status**

Current job status after the cancellation request.

- `Status`: Job status immediately after the
  cancellation request. Typically `Cancelling` to
  indicate cancellation is in progress. The status transitions
  to `Cancelled` when cancellation completes. Use
  `GetJob` to monitor this transition.

###### Note

Cancelled jobs may have partial results in the output location depending on
when cancellation occurs during processing. Check the output location to
determine if any partial data was written before cancellation
completed. You are billed for the number of records that were processed and written to your output bucket before the job was cancelled.
