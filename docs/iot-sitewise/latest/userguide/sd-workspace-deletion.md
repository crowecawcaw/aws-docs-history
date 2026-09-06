

# Appendix: Workspace deletion procedure
<a name="sd-workspace-deletion"></a>

**Important**  
Deleting a workspace and its associated resources is irreversible. Before starting, confirm that you no longer need the datasets, imported and enriched data, pipeline executions, pipelines, tasks, application, or time series.

Delete all resources within the workspace before deleting the workspace itself. For every `List*` operation, paginate through all results before proceeding to the next step.

## Step 1: Cancel or wait for enrichment jobs to finish
<a name="sd-deletion-step1"></a>

1. Call `ListEnrichmentJobs` for each dataset in the workspace.

1. For every ongoing enrichment job, call `CancelEnrichmentJob`.

1. Use `DescribeEnrichmentJob` to verify that each job reaches a terminal state (`COMPLETED`, `FAILED`, `TIMED_OUT`, or `CANCELLED`).

## Step 2: Wait for bulk import jobs to finish
<a name="sd-deletion-step2"></a>

1. Call `ListBulkImportJobs` for each dataset in the workspace.

1. Bulk import jobs do not have a cancellation operation. Wait for every ongoing bulk import job to reach a terminal state before continuing.

1. Use `DescribeBulkImportJob` to check job status when needed.

## Step 3: Delete pipeline executions, pipelines, and tasks
<a name="sd-deletion-step3"></a>

1. Call `ListPipelineExecutions` to identify pipeline executions in the workspace.

1. Delete each pipeline execution by calling `DeletePipelineExecution`.

1. Call `ListPipelines`, and delete each pipeline by calling `DeletePipeline`.

1. Call `ListTasks`, and delete each task by calling `DeleteTask`.

## Step 4: Delete curated datasets
<a name="sd-deletion-step4"></a>

1. Call `ListDatasets` to identify Curated Datasets.

1. For each Curated Dataset, call `ListDatasetDataSegments`.

1. Remove the data-segment associations by calling `BatchDisassociateDataSegmentsFromDataset`.

1. Delete the Curated Dataset by calling `DeleteDataset`.

## Step 5: Delete session datasets
<a name="sd-deletion-step5"></a>

1. Call `ListDatasets` to identify the remaining Session Datasets.

1. Verify that no ongoing enrichment or bulk import jobs reference each Session Dataset.

1. Delete each Session Dataset by calling `DeleteDataset`.

## Step 6: Delete time series
<a name="sd-deletion-step6"></a>

1. Call `ListTimeSeries` to identify time series in the workspace.

1. Remove any resource associations that prevent deletion.

1. Delete each time series by calling `DeleteTimeSeries`.

## Step 7: Delete the application
<a name="sd-deletion-step7"></a>

Each workspace currently supports at most one application. Delete the application by calling `DeleteApplication`.

## Step 8: Delete the workspace
<a name="sd-deletion-step8"></a>

1. Optionally, call `ListWorkspaces` to verify the workspace you want to delete.

1. Call `DeleteWorkspace` only after all associated resources have been deleted.

## Post-deletion behavior
<a name="sd-deletion-post"></a>

`DeleteWorkspace` is asynchronous. During the deletion workflow, the service automatically removes workspace-owned metadata and applied tags — no separate cleanup API is required. After the deletion workflow completes, the workspace no longer counts against the workspace quota for your account and AWS Region.