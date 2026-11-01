

# Manage source servers after migration
<a name="server-post-migration"></a>

After you launch cutover instances, use the following actions to complete the migration and clean up your source servers in AWS Transform MGN. We recommend that you perform them in this order:

1. [Finalize cutover](#server-post-migration-finalize-cutover)

1. [Disconnect from AWS Transform MGN](#server-post-migration-disconnect)

1. [Archive the source server](#server-post-migration-archive) or [delete the source server](#server-post-migration-delete)

## Finalize cutover
<a name="server-post-migration-finalize-cutover"></a>

Finalize the cutover after you launch a cutover instance and confirm that it works as expected in AWS. Finalizing the cutover changes the server's **Migration lifecycle** status to **Cutover complete**, stops data replication, and discards all replicated data. AWS Transform MGN terminates all AWS resources used for data replication.

Finalizing the cutover also sends a command to the AWS Replication Agent to uninstall itself from the source server. Uninstalling typically takes up to 10 minutes.

To finalize a cutover:

1. Validate that the cutover instance functions correctly in AWS, for example, by testing connectivity and application behavior.

1. Open the AWS Transform MGN console and go to the **Source servers** page.

1. Select the checkbox next to one or more source servers in the **Cutover in progress** state.

1. Choose **Test and cutover**, then choose **Finalize cutover**.

1. In the **Finalize cutover for X servers** dialog box, choose **Finalize**.

After the cutover is finalized, the **Migration lifecycle** column shows **Cutover complete**, the **Data replication** column shows **Disconnected**, and the **Next step** column shows **Mark as archived**.

## Disconnect from AWS Transform MGN
<a name="server-post-migration-disconnect"></a>

After data replication is complete, you can disconnect the source server from AWS Transform MGN. Disconnecting uninstalls the AWS Replication Agent from the source server and stops data replication for the server. If you already finalized the cutover, the agent received a command to uninstall itself as part of finalizing.

**Warning**  
Do not disconnect the source server until you confirm that the cutover instance works correctly in AWS. If you discover issues after cutover, you might need to fall back to the source server.

To disconnect a source server:

1. Open the AWS Transform MGN console and go to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Disconnect from service**.

1. In the **Disconnect X server/s from service** dialog box, choose **Disconnect**.

**Important**  
To restart data replication for a disconnected server, you must reinstall the AWS Replication Agent. Disconnecting does not affect test or cutover instances that were launched for the server, but you can no longer identify which source server each Amazon EC2 instance corresponds to.

[Learn more about uninstalling the AWS Replication Agent](uninstalling-agent.md).

## Archive the source server
<a name="server-post-migration-archive"></a>

After a server is cut over, you can archive it. Archiving removes servers from the main **Source servers** list, which keeps the console organized after large migrations. Only archive servers for which you have already performed a cutover.

To archive a source server:

1. Open the AWS Transform MGN console and go to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Actions**, then choose **Mark as archived**.

1. In the **Archive X servers** dialog box, choose **Archive**.

To view archived servers, choose **Archived source servers** from the drop-down menu above the source servers table. To see your active servers again, choose **Active source servers**.

## Delete the source server
<a name="server-post-migration-delete"></a>

You can delete a source server to remove its record from AWS Transform MGN. You can delete one or more servers at a time. You can delete only servers that are not actively replicating.

To delete a source server:

1. Open the AWS Transform MGN console and go to the **Source servers** page.

1. Select the checkbox next to one or more source servers that are not actively replicating.

1. Choose **Actions**, then choose **Delete from service**.

1. Confirm the deletion in the dialog box.