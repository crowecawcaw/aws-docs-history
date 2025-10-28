# Data repository tasks

By using import and export data repository tasks, you can manage the transfer of data and
metadata between your FSx for Lustre file system and any of its durable data repositories on Amazon S3.

_Data repository tasks_ optimize data and metadata transfers
between your FSx for Lustre file system and a data repository on S3. One way that they do this is by
tracking changes between your Amazon FSx file system and its linked data repository. They also do this
by using parallel transfer techniques to transfer data at speeds up to hundreds of GBps. You
create and view data repository tasks using the Amazon FSx console, the AWS CLI, and the Amazon FSx API.

Data repository tasks maintain the file system's Portable Operating System Interface (POSIX)
metadata, including ownership, permissions, and timestamps. Because the tasks maintain this
metadata, you can implement and maintain access controls between your FSx for Lustre file system and
its linked data repositories.

You can use a release data repository task to free up file system space for new files by
releasing files exported to Amazon S3. The released file's content is removed, but the metadata
of the released file remains on the file system. Users and applications can still access a
released file by reading the file again. When the user or application reads the released file,
FSx for Lustre transparently retrieves the file content from Amazon S3.

## Types of data repository tasks

There are three types of data repository tasks:

- **Export** data repository tasks export from
  your Lustre file system to a linked S3 bucket.
- **Import** data repository tasks import from
  a linked S3 bucket to your Lustre file system.
- **Release** data repository tasks release
  files exported to a linked S3 bucket from your Lustre file system.

For more information, see
[Creating a data repository task](creating-data-repo-task.md "creating-data-repo-task.md").

###### Topics

- [Understanding a task's status and details](data-repo-task-status.md "data-repo-task-status.md")
- [Using data repository tasks](managing-data-repo-task.md "managing-data-repo-task.md")
- [Working with task completion reports](task-completion-report.md "task-completion-report.md")
- [Troubleshooting data repository task failures](failed-tasks.md "failed-tasks.md")
