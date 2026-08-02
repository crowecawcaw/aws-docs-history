# Appendix: Workspace deletion procedure

###### Important

Deleting a workspace and its associated resources is irreversible. Before starting,
confirm that you no longer need the datasets, imported and enriched data, pipeline
executions, pipelines, tasks, application, or time series.

Delete all resources within the workspace before deleting the workspace itself. For every
`List*` operation, paginate through all results before proceeding to the next
step.

## Step 1: Cancel or wait for enrichment jobs to finish

1. Call `ListEnrichmentJobs` for each dataset in the workspace.
2. For every ongoing enrichment job, call `CancelEnrichmentJob`.
3. Use `DescribeEnrichmentJob` to verify that each job reaches a terminal
   state (`COMPLETED`, `FAILED`, `TIMED_OUT`, or
   `CANCELLED`).

## Step 2: Wait for bulk import jobs to finish

1. Call `ListBulkImportJobs` for each dataset in the workspace.
2. Bulk import jobs do not have a cancellation operation. Wait for every ongoing bulk
   import job to reach a terminal state before continuing.
3. Use `DescribeBulkImportJob` to check job status when needed.

## Step 3: Delete pipeline executions, pipelines, and tasks

1. Call `ListPipelineExecutions` to identify pipeline executions in the
   workspace.
2. Delete each pipeline execution by calling
   `DeletePipelineExecution`.
3. Call `ListPipelines`, and delete each pipeline by calling
   `DeletePipeline`.
4. Call `ListTasks`, and delete each task by calling
   `DeleteTask`.

## Step 4: Delete curated datasets

1. Call `ListDatasets` to identify Curated Datasets.
2. For each Curated Dataset, call `ListDatasetDataSegments`.
3. Remove the data-segment associations by calling
   `BatchDisassociateDataSegmentsFromDataset`.
4. Delete the Curated Dataset by calling `DeleteDataset`.

## Step 5: Delete session datasets

1. Call `ListDatasets` to identify the remaining Session Datasets.
2. Verify that no ongoing enrichment or bulk import jobs reference each Session
   Dataset.
3. Delete each Session Dataset by calling `DeleteDataset`.

## Step 6: Delete time series

1. Call `ListTimeSeries` to identify time series in the workspace.
2. Remove any resource associations that prevent deletion.
3. Delete each time series by calling `DeleteTimeSeries`.

## Step 7: Delete the application

Each workspace currently supports at most one application. Delete the application by
calling `DeleteApplication`.

## Step 8: Delete the workspace

1. Optionally, call `ListWorkspaces` to verify the workspace you want to
   delete.
2. Call `DeleteWorkspace` only after all associated resources have been
   deleted.

## Post-deletion behavior

`DeleteWorkspace` is asynchronous. During the deletion workflow, the service
automatically removes workspace-owned metadata and applied tags — no separate cleanup API is
required. After the deletion workflow completes, the workspace no longer counts against the
workspace quota for your account and AWS Region.
