# Deleting EFS file systems

File system deletion is a destructive action that you can't undo. You lose the file
system and any data you have in it. Any data that you delete from a file system is gone, and
you can't restore the data. When users delete data from a file system, that data is
immediately rendered unusable. EFS force-overwrites the data in an eventual
manner.

###### Note

You cannot delete a file system that is part of a replication configuration. You must
delete the replication configuration first. For more information, see [Deleting replication configurations](delete-replications.md "delete-replications.md").

###### Important

You should always unmount a file system before you delete it.

###### To delete a file system

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Select the file system that you want to delete in the **File systems** page.
3. Choose **Delete**.
4. In the **Delete file system** dialog box, enter the file system ID shown, and
   choose **Confirm** to confirm the delete.

The console simplifies the file system deletion for you. First it deletes the associated
mount targets, and then it deletes the file system.
Before you can use the AWS CLI command to delete a file system, you must delete all of the
mount targets and access points that were created for the file system.

For example AWS CLI commands, see [Step 4: Clean up](wt1-getting-started.md#wt1-clean-up "wt1-getting-started.md#wt1-clean-up").
