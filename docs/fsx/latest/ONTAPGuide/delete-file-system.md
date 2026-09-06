

# Deleting file systems
<a name="delete-file-system"></a>

You can delete an FSx for ONTAP file system using the Amazon FSx console, the AWS CLI, and the Amazon FSx API and SDKs.

**To delete a file system:**
+ **Using the console** – Follow the procedure described in [Cleaning up resources](getting-started.md#getting-started-step3).
+ **Using the CLI or API** – First delete all the volumes and SVMs on your file system. Then use the [delete-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/delete-file-system.html) CLI command or the [DeleteFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DeleteFileSystem.html) API operation.