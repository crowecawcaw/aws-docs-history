# Canceling an import task

You can cancel a running import task by using the
[CancelImportTask](../apiref/API_CancelImportTask.md "../apiref/API_CancelImportTask.md") API.

```
aws neptune-graph cancel-import-task \
--task-id <task-id>
```

The import task will will be canceled and all changes rolled back. The state of the import task will switch to
`CANCELING` after `cancel-import-task` API is called and eventually the state will be
`CANCELED` when rollback finishes. You can check the current state of your import task using the
[GetImportTask](bulk-import-checking-details.md "bulk-import-checking-details.md") API.

```
aws neptune-graph get-import-task \
--task-id <task-id>
```
