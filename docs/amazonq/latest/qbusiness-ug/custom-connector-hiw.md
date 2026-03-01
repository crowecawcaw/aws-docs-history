# Creating an Amazon Q custom connector

To use a custom data source, create an application environment that is responsible for updating
your Amazon Q index. The application environment depends on a crawler that you create.
The crawler reads the documents in your repository and determines which documents should
be sent to Amazon Q. Your application environment should perform the following steps:

1. Crawl your repository and make a list of the documents in your repository that
   are added, updated, or deleted.
2. Call the [StartDataSourceSyncJob](../api-reference/API_StartDataSourceSyncJob.md "../api-reference/API_StartDataSourceSyncJob.md") API operation to signal
   that a sync job is starting. You provide a data source ID to identify the data
   source that is synchronizing. Amazon Q returns an execution ID to
   identify a particular sync job.

###### Note

After you end a sync job, you can start a new sync job. There can be a
period of time before all of the submitted documents are added to the index.
To see the status of the sync job, use the [ListDataSourceSyncJobs](../api-reference/API_ListDataSourceSyncJobs.md "../api-reference/API_ListDataSourceSyncJobs.md") operation. If the
`Status` returned for the sync job is
`SYNCING_INDEXING`, some documents are still being indexed.
You can start a new sync job when the status of the previous job is
`FAILED` or `SUCCEEDED`. 3. To remove documents from the index, use the [BatchDeleteDocument](../api-reference/API_BatchDeleteDocument.md "../api-reference/API_BatchDeleteDocument.md") operation. You provide the
data source ID and execution ID to identify the data source that is
synchronizing and the job that this update is associated with. 4. To signal the end of the sync job, use the [StopDataSourceSyncJob](../api-reference/API_StopDataSourceSyncJob.md "../api-reference/API_StopDataSourceSyncJob.md") operation. After you call
the `StopDataSourceSyncJob` operation, the associated execution ID is
no longer valid.

###### Note

After you call the `StopDataSourceSyncJob` operation, you can't
use a sync job identifier in a call to the `BatchPutDocument` or
`BatchDeleteDocument` operations. If you do, all of the
documents submitted are returned in the `FailedDocuments`
response message from the API. 5. To list the sync jobs for the data source and to see metrics for the sync
jobs, use the [ListDataSourceSyncJobs](../api-reference/API_ListDataSourceSyncJobs.md "../api-reference/API_ListDataSourceSyncJobs.md") operation with the index
and data source identifiers.
