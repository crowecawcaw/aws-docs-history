# Understanding a task's status and details

A data repository task has descriptive information and a lifecycle status.

After a task is created, you can view the following detailed information for a data
repository task using the Amazon FSx console, CLI, or API:

- The task type:
  - `EXPORT_TO_REPOSITORY` indicates an export task.
  - `IMPORT_METADATA_FROM_REPOSITORY` indicates an import task.
  - `RELEASE_DATA_FROM_FILESYSTEM` indicates a release task.

- The file system that the task ran on.
- The task creation time.
- The task status.
- The total number of files that the task processed.
- The total number of files that the task successfully processed.
- The total number of files that the task failed to process. This value is greater than zero
  when the task status is FAILED. Detailed information about files that failed is available in a
  task completion report. For more information, see [Working with task completion reports](task-completion-report.md "task-completion-report.md").
- The time that the task started.
- The time that the task status was last updated. Task status is updated every 30
  seconds.
  A data repository task can have one of the following statuses:

- PENDING indicates that Amazon FSx has not started the task.
- EXECUTING indicates that Amazon FSx is processing the task.
- FAILED indicates that Amazon FSx didn't successfully process
  the task. For example, there might be files that the task failed to process. The task details
  provide more information about the failure. For more information about failed tasks, see [Troubleshooting data repository task failures](failed-tasks.md "failed-tasks.md").
- SUCCEEDED indicates that Amazon FSx completed the task successfully.
- CANCELED indicates that the task was canceled and not completed.
- CANCELING indicates that Amazon FSx is in the process of canceling
  the task.
  For more information about accessing existing data repository tasks, see [Accessing data repository tasks](view-data-repo-tasks.md "view-data-repo-tasks.md").
