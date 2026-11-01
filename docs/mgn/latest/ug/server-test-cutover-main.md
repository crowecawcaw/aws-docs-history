

# Manage test and cutover instances
<a name="server-test-cutover-main"></a>

The **Test and cutover** menu allows you to manage your test and cutover instances. For a more in-depth step-by-step guide to launching test and cutover instances, see the [Launching test and cutover instances documentation](launching-test-servers.md).
+ **Launch test instances** – Choose this option to launch a test instance for this server.

  When the **Launch test instances for X** servers dialog appears, choose **Launch** to begin the test.

  The AWS Transform MGN console indicates **1 launch job complete** after the test has been completed successfully.
+ **Mark as "Ready for cutover"** – Use this option to finalize testing for this server after you have completed all of the necessary tests in preparation for cutover.

  When the **Mark X servers as "Ready for cutover"** dialog appears, select whether you want to terminate the launched instances used for testing. We recommend that you terminate these instances, as you will be charged for them even though you no longer need them. Check the **Yes, terminate launched instances (recommended)** box and choose **Continue**. 

  The AWS Transform MGN console indicates that testing has been finalized. The selected source servers' **Migration lifecycle** column shows the **Ready for cutover** status and the launched Test instances are deleted if that option was selected. 
+ **Revert to "ready for testing"** – Choose this option to revert a finalized test for this server if you want to run further tests prior to initiating a cutover.

  The **Revert testing for X servers** dialog appears. Select whether you want to terminate the launched instances used for testing. We recommend that you terminate these instances, as you will be charged for them even though you no longer need them. Check the **Yes, terminate launched instances (recommended)** box and choose **Revert**.

  The AWS Transform MGN console indicates that testing has been reverted. The selected source servers' **Migration lifecycle** column shows the **Ready for testing** status and the launched Test instances are deleted if that option was selected. 
+ **Launch cutover instances** – Choose this option to launch a cutover instance for this server after you have finalized all of your testing and are ready to initiate a cutover. 

  The **Launch cutover instances for X** **servers** dialog appears. Choose **Launch** to begin the cutover.

  The AWS Transform MGN console indicates **1 launch job complete** after the cutover has been completed successfully. 

  This changes your source servers' **Migration lifecycle** status to **Cutover in progress**, indicating that the cutover is in progress but has not yet been finalized.
+ **Finalize cutover** – Finalize the cutover for this server after you have successfully performed a cutover. This stops data replication and terminates the AWS resources used for replication. [Learn more about finalizing a cutover](server-post-migration.md#server-post-migration-finalize-cutover).
+ **Revert to "ready for cutover"** – Choose this option to revert a finalized cutover for this server if you encounter any issues or want to reverse the cutover for any reason.

  This reverts your source servers' **Migration lifecycle** to the **Ready for cutover** status, indicating that these servers have not undergone cutover. 

  The **Revert cutover for X servers** dialog appears. Choose **Revert**.
+ **Edit launch settings** – Use this option to edit the launch settings for this server. You are redirected to the **Edit launch settings** page. [Learn more about launch settings.](launching-target-servers.md)
+ **Edit post-launch settings** – Use this option to edit the post-launch settings for the selected source server or group of source servers. [Learn more about post-launch settings.](source-post-launch-settings.md)
+ **Terminate launched instance** – Choose this option if you want to delete your test or cutover instance for any reason at any time. It can only be selected for a server that has a launched test or cutover instance.

  When the **Terminate launched instance** dialog appears, choose **Terminate**.