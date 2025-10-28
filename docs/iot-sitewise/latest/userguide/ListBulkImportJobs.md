# List AWS IoT SiteWise bulk import jobs (AWS CLI)

Use the [ListBulkImportJobs](../APIReference/API_ListBulkImportJobss.md "../APIReference/API_ListBulkImportJobss.md") API operation to retrieve a list of summaries for bulk import
jobs in AWS IoT SiteWise. This operation provides an efficient way to monitor and manage your data
import processes. It returns the following key information for each job:

- Job ID. A unique identifier for each bulk import job
- Job name. The name you assigned to the job when creating it
- Current status. The job's current state (for example, COMPLETED, RUNNING,
  FAILED)
  ListBulkImportJobs is particularly useful for getting a comprehensive overview of all your
  bulk import jobs. This can help you track multiple data imports, identify any jobs that
  require attention, and maintain an organized workflow. The operation supports pagination,
  allowing you to retrieve large numbers of job summaries efficiently. You can use the job IDs
  returned by this operation with the [DescribeBulkImportJob](../APIReference/API_DescribeBulkImportJob.md "../APIReference/API_DescribeBulkImportJob.md")
  operation to retrieve more detailed information about specific jobs. This two-step process
  allows you to first get a high-level view of all jobs, and then drill down into the details of
  jobs of interest. When using `ListBulkImportJobs`, you can apply filters to narrow
  down the results. For example, you can filter jobs based on their status to retrieve only
  completed jobs or only running jobs. This feature helps you focus on the most relevant
  information for your current task. The operation also returns a `nextToken` if
  there are more results available. You can use this token in subsequent calls to retrieve the
  next set of job summaries, enabling you to iterate through all your bulk import jobs even if
  you have a large number of them. The following example demonstrates how to use
  `ListBulkImportJobs` with the AWS CLI to retrieve a list of completed jobs.

```
aws iotsitewise list-bulk-import-jobs --filter COMPLETED
```

###### Example Response for completed jobs filter

```
{
   "jobSummaries":[
      {
         "id":"bdbbfa52-d775-4952-b816-13ba1c7cb9da",
         "name":"myBulkImportJob",
         "status":"COMPLETED"
      },
      {
         "id":"15ffc641-dbd8-40c6-9983-5cb3b0bc3e6b",
         "name":"myBulkImportJob2",
         "status":"COMPLETED"
      }
   ]
}
```

This command demonstrates how to use `ListBulkImportJobs` to retrieve a list of
jobs that completed with failures. The maximum is set to 50 results and we're using a next
token for paginated results.

```
aws iotsitewise list-bulk-import-jobs --filter COMPLETED_WITH_FAILURES --max-results 50 --next-token "string"
```
