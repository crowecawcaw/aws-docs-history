NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Starting a test

To launch a test instance for a single source server or multiple source servers:

1. Go to the **Source servers** page.
2. Check the box to the left of each server for which you want to launch a test
   instance.
3. Open the **Test and cutover** menu.
4. Under **Testing**, choose the **Launch
   test instances** option to launch a test instance for this server.
5. When the **Launch test instances for X servers** dialog
   appears, click **Launch** to begin the test.
   The AWS Application Migration Service console indicates **Launch job started**
   when the test has started.

Choose **View job details** on the dialog to view the specific
job for the test launch in the **Launch history** tab.

## Successful test launch indicators

You can tell that the test instance launch started successfully through several indicators
on the **Source servers** page.

1. The Alerts column shows the **Launched** status,
   indicating that a Test instance has been launched for this server.
2. The **Migration lifecycle** column shows **Test in progress**.
3. The **Next step** column shows **Complete testing and mark as 'Ready for cutover'**.
