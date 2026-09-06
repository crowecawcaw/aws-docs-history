

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Actions after migration
<a name="source-server-actions-post-migration"></a>

After a successful cutover, you can perform the following actions to complete the migration and clean up resources.

## Finalize cutover
<a name="source-server-actions-finalize-cutover"></a>

After confirming that the cutover instance is running correctly in AWS, finalize the cutover. This action marks the migration as complete for the source server and stops data replication.

To finalize a cutover:

1. Validate that the cutover instance is functioning correctly in AWS by testing connectivity and application behavior.

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Test and cutover**, then choose **Finalize cutover**.

1. Confirm the action by choosing **Finalize cutover** in the dialog.

**Important**  
Finalizing a cutover stops data replication and terminates the replication server in the staging area. This action cannot be undone. Do not finalize the cutover until you have confirmed that the cutover instance is working as expected.

## Disconnect from AWS Transform MGN
<a name="source-server-actions-disconnect"></a>

After finalizing the cutover, you can disconnect the source server from AWS Transform MGN. This action removes the server from active management in AWS Transform MGN and stops any remaining replication activity. The source server itself is not affected.

To disconnect a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Disconnect from service**.

1. Confirm the action in the dialog.

**Note**  
Do not disconnect the source server from AWS Transform MGN until the cutover instance in AWS is confirmed to be working correctly. You may need to revert to the source server if issues are discovered after cutover.

## Archive source server
<a name="source-server-actions-archive"></a>

After the migration is complete and the cutover instance is confirmed to be working correctly, you can archive the source server. Archiving removes the server from the active **Source servers** list and moves it to the archived view. This helps keep your console organized after large-scale migrations.

To archive a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Archive server**.

1. Confirm the action in the dialog.

**Note**  
Archived servers can be viewed by toggling the **Show archived servers** option in the **Preferences** menu on the Source servers page.

## Delete source server
<a name="source-server-actions-delete"></a>

You can permanently delete a source server from AWS Transform MGN. This removes all data associated with the server from the AWS Transform MGN console, including replication history and settings. This action does not affect the source server itself or any launched Amazon EC2 instances.

To delete a source server:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Delete server**.

1. Confirm the deletion by entering the server name in the confirmation dialog and choosing **Delete**.

**Important**  
Deleting a source server is a permanent action and cannot be undone. Ensure that the migration is complete and the cutover instance is working correctly before deleting the source server record from AWS Transform MGN.