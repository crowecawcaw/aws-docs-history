

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Finalizing a cutover
<a name="finalizing-cutover-2"></a>

If you are completely done with your migration and performed a successful cutover, you can finalize the cutover. This changes your source servers' **Migration lifecycle** status to **Cutover complete**, indicating that the cutover is complete and that the migration has been performed successfully. In addition, this stops data replication and causes all replicated data to be discarded. All AWS resources used for data replication are terminated. 

To finalize a cutover:

1. Check the box to the left of every source server that has a launched cutover instance you want to finalize.

1. Open the **Test and cutover** menu.

1. Under **Cutover**, choose **Finalize cutover**.

1. The **Finalize cutover for X servers** dialog appears. Choose **Finalize**. This changes your source servers' **Migration lifecycle** status to **Cutover complete**, indicating that the cutover is complete and that the migration has been performed successfully. In addition, this stops data replication and causes all replicated data to be discarded. All AWS resources used for data replication are terminated. 

   The AWS Transform MGN console indicates **Cutover finalized** when the cutover has completed successfully. 

   The AWS Transform MGN console automatically stops data replication for the source servers that were cutover to save resource costs. The selected source servers' **Migration lifecycle** column shows the **Cutover complete** status, the **Data replication** status column shows **Disconnected**, and the **Next step** column shows **Mark as archived**. The source servers have now been successfully migrated into AWS.

1. You can now archive your source servers that have launched cutover instances. Archiving removes these source servers from the main **Source servers** page, allowing you to focus on source servers that have not yet been cutover. You are still able to access the archived servers through filtering options. 

   To archive your cutover source servers:

   1. Check the box to the left of each source server for which the **Migration lifecycle** column states **Cutover complete**.

   1. Open the **Actions** menu and choose **Mark as archived**.

   1. When the **Archive X server** dialog appears, choose **Archive**.

   1. To see your archived servers, open the **Preferences** menu by choosing the gear button.

      Toggle the **Show only archived servers** option and choose **Confirm**.

      You are now able to see all of your archived servers. Untoggle the **Show only archived servers** option to show non-archived servers. 