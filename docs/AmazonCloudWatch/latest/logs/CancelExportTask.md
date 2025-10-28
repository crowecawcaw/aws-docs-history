# Cancel an export task

You can cancel an export task if it's in a `PENDING` or
`RUNNING` state.

###### To cancel an export task using the AWS CLI

At a command prompt, use the following [cancel-export-task](../../../cli/latest/reference/logs/cancel-export-task.md "../../../cli/latest/reference/logs/cancel-export-task.md")
command:

```
`aws logs --profile CWLExportUser cancel-export-task --task-id "`cda45419-90ea-4db5-9833-aade86253e66`"`
```

You can use the [describe-export-tasks](../../../cli/latest/reference/logs/describe-export-tasks.md "../../../cli/latest/reference/logs/describe-export-tasks.md") command to verify that the task was canceled
successfully.
