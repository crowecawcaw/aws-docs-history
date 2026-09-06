

# Deleting a file system
<a name="delete-file-system"></a>

You can delete an Amazon FSx for Lustre file system using the Amazon FSx console, the AWS CLI, and the Amazon FSx API. Before deleting an FSx for Lustre file system, you should [unmount](unmounting-fs.md) it from every connected Amazon EC2 instance. On S3-linked file systems, to ensure all of your data is written back to S3 before deleting your file system, you can either monitor for the [AgeOfOldestQueuedMessage](fs-metrics.md#auto-import-export-metrics) metric to be zero (if using automatic export) or you can run an [export data repository task](export-data-repo-task-dra.md). If you have automatic export enabled and want to use an export data repository task, you have to disable automatic export before executing the export data repository task.

To delete a file system after unmounting from every Amazon EC2 instance:
+ **Using the console** – Follow the procedure described in [Step 5: Clean up resources](getting-started.md#getting-started-step4).
+ **Using the API or CLI** – Use the the [DeleteFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteFileSystem.html) API operation or the [delete-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/delete-file-system.html) CLI command.