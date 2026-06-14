# ListJobs

The `ListJobs` operation retrieves a paginated list of jobs with
optional filtering capabilities. You can filter by job status and control the number
of results returned. The operation supports pagination through next tokens, allowing
you to retrieve large job lists efficiently.

For more information, see [ListJobs](../APIReference/API_geojobs_ListJobs.md "../APIReference/API_geojobs_ListJobs.md") in the
_Amazon Location Service API Reference_.

For example requests, responses, and CLI commands for this API, see [How
to list jobs](listing-jobs.md "listing-jobs.md").

## Use cases

- **Job inventory management:** Retrieve all
  jobs to audit processing history and track resource utilization across
  validation operations.
- **Status-based monitoring:** Filter jobs by
  status to identify running jobs requiring attention or completed jobs
  ready for result retrieval.
- **Operational reporting:** Generate reports
  on job execution patterns, success rates, and processing volumes for
  business analytics.
- **Troubleshooting and debugging:** List
  failed jobs to identify patterns in processing errors and diagnose
  systematic issues.

## Understand the request

The `ListJobs` request accepts optional parameters for filtering and
pagination. Without any parameters, the operation returns all jobs with default
pagination.

The request includes the following optional parameters:

**Filtering options**

Optional parameters to narrow the list of returned jobs.

- `Filter`: Object containing filter criteria.

  - `JobStatus`: Filter jobs by their current
    status. Valid values: `Pending`,
    `Running`, `Completed`,
    `Failed`, `Cancelling`, or
    `Cancelled`.

**Pagination controls**

Optional parameters to control result pagination.

- `MaxResults`: Maximum number of jobs to return in
  a single response. Use this to control page size for large
  result sets.
- `NextToken`: Pagination token from a previous
  `ListJobs` response. Include this token to
  retrieve the next page of results.

## Understand the response

The `ListJobs` response provides a paginated list of job summaries
with configuration and status information for each job. Use the next
token to retrieve additional pages when more results are available.

The response includes the following fields:

**Job list**

Array of job summaries matching the filter criteria.

- `Entries`: Array of job summaries, including:

  - `Action`: Action performed by the
    job.
  - `CreatedAt`: Job creation timestamp in ISO
    8601 format.
  - `EndedAt`: Job completion timestamp in ISO
    8601 format. Only present for jobs in terminal states
    (Completed, Failed, or Cancelled).
  - `ExecutionRoleArn`: IAM role used for
    execution.
  - `InputOptions`: Input configuration
    object.
  - `JobArn`: Amazon Resource Name (ARN) of
    the job.
  - `JobId`: Unique job identifier.
  - `Name`: Job name if provided during
    creation.
  - `OutputOptions`: Output configuration
    object.
  - `Status`: Current job status.
  - `UpdatedAt`: Last update timestamp in ISO
    8601 format.
  - `ActionOptions`: Additional features
    requested, if any.

**Pagination token**

Token for retrieving additional results.

- `NextToken`: Token to include in the next
  `ListJobs` request to retrieve the next page of
  results. This field is only present when more results are
  available. The absence of this field indicates you have
  retrieved the last page.

###### Note

Results maintain consistent ordering across pages. Use the
`NextToken` from each response in subsequent requests to
iterate through all pages of results.
