# Checking the details and progress of an import task

You can use the [GetImportTask](../apiref/API_GetImportTask.md "../apiref/API_GetImportTask.md") API to track the progress and the status of your import task.

```
aws neptune-graph get-import-task --task-id <task-id>
```

An Import task can be in the following state:

- **INITIALIZING**: The task is preparing for import, including provisioning a graph when
  using the `CreateGraphUsingImportTask` API.
- **ANALYZING_DATA**: The task is taking an initial pass through the dataset to determine
  the optimal configuration for the graph.
- **IMPORTING**: The data is being loaded into the graph.
- **EXPORTING**: Data is being exported from the Neptune cluster or snapshot.
  This is only applicable when performing an import task with a source of Neptune and through the
  `CreateGraphUsingImportTask` API.
- **ROLLING_BACK**: The import task encountered an error. Refer to the
  [troubleshooting](bulk-import-troubleshooting.md "bulk-import-troubleshooting.md")
  section to investigate the errors. The import task will be rolled back and eventually marked as `FAILED`.
- **SUCCEEDED**: Graph creation and data loading have succeeded. Use the
  `get-graph` API to view details of the final graph.
- **REPROVISIONING**: A temporary state while the graph is being reconfigured during
  the import task.
- **FAILED**: Graph creation or data loading has failed. Refer to the
  [troubleshooting](bulk-import-troubleshooting.md "bulk-import-troubleshooting.md") section to understand the reason for the failure.
- **CANCELLING**: The user has cancelled the import task, and cancellation is in progress.
- **CANCELLED**: The import task has been cancelled, and all resources have been released.

Additionally, import task can be used to track the progress of the load, error count and graph summary.
