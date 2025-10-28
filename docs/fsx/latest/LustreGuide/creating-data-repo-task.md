# Creating a data repository task

You can create a data repository task by using the Amazon FSx console, CLI, or API. After you
create a task, you can view the task's progress and status by using the console, CLI, or
API.

You can create three types of data repository tasks:

- The **Export** data repository task exports from
  your Lustre file system to a linked S3 bucket. For more information, see
  [Using data repository tasks to export changes](export-data-repo-task-dra.md "export-data-repo-task-dra.md").
- The **Import** data repository task imports from
  a linked S3 bucket to your Lustre file system. For more information, see
  [Using data repository tasks to import changes](import-data-repo-task-dra.md "import-data-repo-task-dra.md").
- The **Release** data repository task releases
  files from your Lustre file system that have been exported to a linked S3 bucket.
  For more information, see [Using data repository tasks to release files](release-files-task.md "release-files-task.md").
