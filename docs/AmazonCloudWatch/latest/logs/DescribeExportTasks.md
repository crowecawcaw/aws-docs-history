# Describe export tasks (CLI)

After you create an export task, you can get the current status of the task.

###### To describe export tasks using the AWS CLI

At a command prompt, use the following [describe-export-tasks](../../../cli/latest/reference/logs/describe-export-tasks.md "../../../cli/latest/reference/logs/describe-export-tasks.md")
command.

```
`aws logs --profile CWLExportUser describe-export-tasks --task-id "`cda45419-90ea-4db5-9833-aade86253e66`"`
```

The following is example output.

```
`{
 "exportTasks": [
 {
 "destination": "`my-exported-logs`",
 "destinationPrefix": "`export-task-output`",
 "executionInfo": {
 "creationTime": `1441495400000`
 },
 "from": `1441490400000`,
 "logGroupName": "`my-log-group`",
 "status": {
 "code": "RUNNING",
 "message": "Started Successfully"
 },
 "taskId": "`cda45419-90ea-4db5-9833-aade86253e66`",
 "taskName": "`my-log-group-09-10-2015`",
 "tTo": `1441494000000`
 }]
}`
```

You can use the `describe-export-tasks` command in three different
ways:

- Without any filters – Lists all of your
  export tasks, in reverse order of creation.
- Filter on task ID – Lists the export
  task, if one exists, with the specified ID.
- Filter on task status – Lists the export
  tasks with the specified status.
  For example, use the following command to filter on the `FAILED`
  status.

```
`aws logs --profile CWLExportUser describe-export-tasks --status-code "FAILED"`
```

The following is example output.

```
`{
 "exportTasks": [
 {
 "destination": "`my-exported-logs`",
 "destinationPrefix": "`export-task-output`",
 "executionInfo": {
 "completionTime": `1441498600000`
 "creationTime": `1441495400000`
 },
 "from": `1441490400000`,
 "logGroupName": "`my-log-group`",
 "status": {
 "code": "FAILED",
 "message": "FAILED"
 },
 "taskId": "`cda45419-90ea-4db5-9833-aade86253e66`",
 "taskName": "`my-log-group-09-10-2015`",
 "to": `1441494000000`
 }]
}`
```
