NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Marking as Ready for cutover

If you are completely done with your testing and are ready for cutover, you can finalize
the test. This changes your source servers' **Migration
lifecycle** status to **Ready for cutover**, indicating
that all testing is complete and that these servers are now ready for cutover. You also
have the option to delete your Test instances for cost saving purposes.

To finalize a test:

1. Check the box to the left of every source server that has a launched Test instance for
   which you want to finalize the test.
2. Open the **Test and cutover** menu.
3. Under **Testing**, choose **Mark as
   "Ready for cutover"**.
4. When the **Mark X servers as "Ready for cutover"** dialog
   appears, select whether you want to terminate the launched instances used for testing. It is
   recommended to terminate these instances, as you will be charged for them even though you
   no longer need them. Check the **Yes, terminate launched instances
   (recommended)** box and click **Continue**.

The AWS Application Migration Service console confirms that the servers were marked as ready for
cutover.

The AWS Application Migration Service console indicates that testing has been finalized. The selected source
servers' **Migration lifecycle** column shows the **Ready for cutover** status and the launched Test instances are
deleted if that option was selected. The **Next step** column
shows **Terminate launched instance; Launch cutover
instance**.

You can now terminate the launched Test instance directly from the Amazon EC2 console as that
instance is no longer needed (if you have not done so already through the AWS MGN console).
You can quickly access the Test instance by navigating to the specific servers > **Server details > Migration dashboard > Lifecycle > Launch status** and
choosing **view in EC2 console**.

The Amazon EC2 console automatically searches for and displays the Test instance. Select the
instance, open the **Instance state** menu, and choose **Terminate instance**.

Click **Terminate**.
