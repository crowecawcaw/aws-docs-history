NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Launching a test instance

After you have added all of your source servers and configured their launch settings, you
are ready to launch a test instance. It is crucial to test the migration of your source servers
to AWS prior to initiating a cutover in order to verify that your source servers function
properly within the AWS environment.

###### Important

It is a best practice to perform a test at least two weeks before you plan to migrate your
source servers. This time frame allows you to identify potential problems and solve them,
before the actual cutover takes place. After launching test instances, use either SSH (Linux)
or RDP (Windows) to connect to your instance and ensure that everything is working correctly.

You can test one source server at a time, or simultaneously test multiple source servers.
For each source server, you will be informed of the success or failure of the test. You can test
your source server as many times as you want. Each new test first deletes any previously
launched test instance and dependent resources. Then, a new test instance is launched, which
reflects the most up-to-date state of the source server. After the test, data replication
continues as before. The new and modified data on the source server is transferred to the
staging area subnet and not to the test instances that were launched during the test.

###### Note

- When launching a test or cutover instance, you can launch up to 100 source servers in a
  single operation. Additional source servers can be launched in subsequent operations.
- Windows source servers need to have at least 2 GB of free space to successfully launch a
  test instance.
- Take into consideration that once a test instance is launched, actual resources will be
  used in your AWS account and you will be billed for these resources. You can terminate the
  operation of launched Test instances once you verify that they are working properly without
  impact in order to data replication.

## Ready for testing indicators

Prior to launching a Test instance, ensure that your source servers are ready for testing
by looking for the following indicators on the **Source servers**
page:

1. Under the **Migration lifecycle** column, the server should
   show **Ready for testing**.
2. Under the **Data replication status** column, the server
   should show the **Healthy** status.
3. Under the **Next step** column, the server should show
   **Launch test instance**.

## Starting a test

To launch a test instance for a single source server or multiple source servers, take the
following steps:

- Go to the **Source servers** page and check the box to the
  left of each server for which you want to launch a test instance.

- Open the **Test and cutover** menu.
- Under **Testing**, choose the **Launch
  test instances** option to launch a test instance for this server.
- When the **Launch test instances for X**
  **servers** dialog appears, choose **Launch** to begin the test.

The AWS Application Migration Service console will indicate **Launch job started**
when the test has started.

Choose **View job details** on the dialog to view the
specific Job for the test launch in the **Launch History** tab.

### Successful test launch indicators

You can tell that the Test instance launch started successfully through several
indicators on the **Source Servers** page.

1. The Alerts column will show the **Launched** status,
   indicating that a test instance has been launched for this server.
2. The **Migration lifecycle** column will show **Test in progress**.
3. The **Next step** column will show **Complete testing and mark as 'Ready for cutover'**.

## Reverting or finalizing a test

After you have launched your test instances, open the Amazon EC2 Console and SSH or RDP
into your test instances in order to ensure that they function correctly. Validate connectivity
and perform acceptance tests for your application.

### Reverting a test

If you encounter any issues and want to launch new test instances, or if you are
performing a scheduled test and plan to perform additional tests prior to cutover, you can
revert the test. This will revert your source servers' **Migration
lifecycle** status to **Ready for testing**, indicating
that these servers still require additional testing before they are ready for cutover. During
a revert, you will also have the option to delete your Test instances for cost-saving
purposes.

To revert a test:

1. Check the box to the left of every source server that has a launched test instance for
   which you want to revert the test.
2. Open the **Test and cutover** menu.
3. Under **Testing**, choose **Revert to
   "ready for testing"**
4. When the **Revert testing for X servers** dialog appears,
   select whether you want to terminate the launched instances used for testing. It is
   recommended to terminate these instances, as you will be charged for them even though you
   will no longer need them. Check the **Yes, terminate launched instances
   (recommended)** box and choose **Revert**.

The AWS Application Migration Service console will indicate that testing has been reverted. The selected source
servers' **Migration lifecycle** column will show the **Ready for testing** status, the **Next
step** column will show **Launch test instance** and
the launched Test instances will be deleted if that option was selected.

### Marking as Ready for cutover

If you are completely done with your testing and are ready for cutover, you can finalize
the test. This will change your source servers' **Migration
lifecycle** status to **Ready for cutover**, indicating
that all testing is complete and that these servers are now ready for cutover. You will also
have the option to delete your Test instances for cost saving purposes.

To finalize a test:

1. Check the box to the left of every source server that has a launched Test instance for
   which you want to finalize the test.
2. Open the **Test and Cutover** menu.
3. Under **Testing**, choose **Mark as
   "Ready for cutover"**
4. Mark X servers as "Ready for cutover" dialog will appear. Select whether you want to
   terminate the launched instances used for testing. It is recommended to terminate these
   instances, as you will be charged for them even though you will no longer need them. Check
   the **Yes, terminate launched instances (recommended)** box and
   choose **Continue**.
5. The AWS Application Migration Service console will confirm that the servers were marked as ready for cutover.

The console will indicate that testing has been finalized. The selected source servers'
**Migration lifecycle** column will show the **Ready for cutover** status and the launched test instances will be
deleted if that option was selected. The **Next step** column
will show **Terminate launched instance; Launch cutover
instance**. 6. You can now terminate the launched test instance directly from the Amazon EC2 Console
as that instance is no longer needed (if you have not done so already through the AWS MGN
Console). You can quickly access the Test instance by navigating to the specific servers >
**Server Details > Migration dashboard > Lifecycle > Launch
status** and choosing **View in EC2 Console.** 7. The Amazon EC2 Console will automatically search for and display the test instance.
Select the instance, open the **Instance state** menu, and
choose **Terminate instance**. When the confirmation dialogue
appears, click **Terminate**.
