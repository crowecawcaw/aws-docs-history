NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Reverting a cutover

Once you have launched your cutover instances, open the Amazon EC2 console and SSH or RDP into
your cutover instances in order to ensure that they function correctly. Validate connectivity
and perform acceptance tests for your application.

###### Note

You should turn on Termination Protection after you have completed your testing and before
you are ready to finalize the cutover. Learn more about enabling termination protection in
[this Amazon EC2 article](../../../AWSEC2/latest/WindowsGuide/terminating-instances.md#Using_ChangingDisableAPITermination "../../../AWSEC2/latest/WindowsGuide/terminating-instances.md#Using_ChangingDisableAPITermination").

If you encounter any issues and want to launch new cutover instances, you can revert the
cutover. This reverts your source servers' **Migration
lifecycle** status to **Ready for cutover**, indicating
that these servers have not undergone cutover. During a revert, you also have the option
to delete your Cutover instances for cost-saving purposes.

To revert a cutover take the following steps:

1. Check the box to the left of every source server that has a launched cutover instance
   you want to revert.
2. Open the **Test and cutover** menu.
3. Under **Cutover**, choose **Revert to
   "ready for cutover"**.
4. This reverts your source servers' **Migration
   lifecycle** status to **Ready for cutover**,
   indicating that these servers have not undergone cutover.

When the **Revert cutover for X servers** dialog appears,
click **Revert**.
