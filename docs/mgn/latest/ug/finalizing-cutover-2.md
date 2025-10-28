NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Finalizing a cutover

If you are completely done with your migration and performed a successful cutover, you
can finalize the cutover. This changes your source servers' **Migration
lifecycle** status to **Cutover complete**, indicating
that the cutover is complete and that the migration has been performed successfully. In
addition, this stops data replication and causes all replicated data to be discarded. All AWS
resources used for data replication are terminated.

To finalize a cutover:

1. Check the box to the left of every source server that has a launched cutover instance
   you want to finalize.
2. Open the **Test and cutover** menu.
3. Under **Cutover**, choose **Finalize
   cutover**.
4. The **Finalize cutover for X servers** dialog appears.
   Choose **Finalize**. This changes your source servers' **Migration lifecycle** status to **Cutover
   complete**, indicating that the cutover is complete and that the migration has been
   performed successfully. In addition, this stops data replication and causes all replicated
   data to be discarded. All AWS resources used for data replication are terminated.

The AWS Application Migration Service console indicates **Cutover finalized**
when the cutover has completed successfully.

The AWS Application Migration Service console automatically stops data replication for the source servers
that were cutover in order to save resource costs. The selected source servers' **Migration lifecycle** column shows the **Cutover complete** status, the **Data replication**
status column shows **Disconnected**, and the **Next step** column shows **Mark as
archived**. The source servers have now been successfully migrated into
AWS. 5. You can now archive your source servers that have launched cutover instances.
Archiving removes these source servers from the main **Source
servers** page, allowing you to focus on source servers that have not yet been
cutover. You are still able to access the archived servers through filtering options.

To archive your cutover source servers:

    1. Check the box to the left of the of each source server for which the **Migration lifecycle** column states **Cutover
     complete**.
    2. Open the **Actions** menu and choose **Mark as archived**.
    3. When the **Archive X server** dialog appears,
     click **Archive**.
    4. To see your archived servers, open the **Preferences**
     menu by choosing the gear button.


    Toggle the **Show only archived servers** option and
     click **Confirm**.


    You are now be able to see all of your archived servers. Untoggle the **Show only archived servers** option to show non-archived servers.
