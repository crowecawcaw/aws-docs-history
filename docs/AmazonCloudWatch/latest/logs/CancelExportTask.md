

# Cancel an export task (CLI)
<a name="CancelExportTask"></a>

You can cancel an export task if it's in a `PENDING` or `RUNNING` state.

**To cancel an export task using the AWS CLI**  
At a command prompt, use the following [cancel-export-task](https://docs.aws.amazon.com/cli/latest/reference/logs/cancel-export-task.html) command:

```
aws logs --profile CWLExportUser cancel-export-task --task-id "{{cda45419-90ea-4db5-9833-aade86253e66}}"
```

You can use the [describe-export-tasks](https://docs.aws.amazon.com/cli/latest/reference/logs/describe-export-tasks.html) command to verify that the task was canceled successfully.