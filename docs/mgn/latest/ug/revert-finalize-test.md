NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Reverting a test

After you have launched your test instances, open the Amazon EC2 console and SSH or RDP into your
test instances in order to ensure that they function correctly. Validate connectivity and
perform acceptance tests for your application.

If you encounter any issues and want to launch new Test instances, or if you are
performing a scheduled test and plan to perform additional tests prior to cutover, you can
revert the test. This reverts your source servers' **Migration
lifecycle** status to **Ready for testing** , indicating
that these servers still require additional testing before they are ready for cutover. During a
revert, you also have the option to delete your Test instances for cost-saving
purposes.

To revert a test:

1. Check the box to the left of every source server that has a launched Test instance for
   which you want to revert the test.
2. Open the **Test and cutover** menu.
3. Under **Testing**, choose **Revert to
   "ready for testing"**.
4. The **Revert testing for X servers** dialog appears.
   Select whether you want to terminate the launched instances used for testing. It is
   recommended to terminate these instances, as you will be charged for them even though you
   no longer need them. Check the **Yes, terminate launched instances
   (recommended)** box and choose **Revert**.

The AWS Application Migration Service console indicates that testing has been reverted. The selected source
servers' **Migration lifecycle** column shows the **Ready for testing** status, the **Next
step** column shows **Launch test instance** and
the launched Test instances are deleted if that option was selected.
