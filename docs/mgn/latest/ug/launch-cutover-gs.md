

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Launching a cutover instance
<a name="launch-cutover-gs"></a>

Once you have finalized the testing of all of your source servers, you are ready for cutover. You should perform the cutover at a set date and time. The cutover will migrate your source servers to the cutover instances on AWS. 

**Important**  
It is a best practice to perform a test at least two weeks before you plan to migrate your source servers. This time frame allows you to identify potential problems and solve them, before the actual migration takes place. After launching test instances, use either SSH (Linux) or RDP (Windows) to connect to your instance and ensure that everything is working correctly. 

You can cutover one source server at a time, or simultaneously cutover multiple source servers. For each source server, you will be informed of the success or failure of the cutover. For each new cutover, AWS Transform MGN first deletes any previously launched Test instance and dependent resources. Then, it launches a new cutover instance which reflects the most up-to-date state of the source server. After the cutover, data replication continues as before. The new and modified data on the source server is transferred to the Staging Area Subnet, and not to the cutover instances that were launched during the cutover.

## Ready for cutover indicators
<a name="ready-for-cutover-gs"></a>

Before launching a cutover instance, ensure that your source servers are ready for cutover by looking for the following indicators on the **Source Servers** page:

1. Under the **Migration lifecycle** column, the server should show **Ready for cutover** .

1. Under the **Data replication status** column, the server should show the **Healthy** status. 

1. Under the **Next step** column, the server should show **Terminate launched instance; Launch cutover instance** if you have not terminated your latest launched test instance.

1. Alternatively, the Next step column will show **Launch cutover instance** if you have terminated your latest launched test instance. 

## Starting a cutover
<a name="starting-cutover-gs"></a>

To launch a cutover instance for a single source server or multiple source servers, take the following steps:

1. Go to the **Source servers** page and check the box to the left of each server you want to cutover. 

1. Open the **Test and cutover** menu.

1. Under **Cutover**, choose the **Launch cutover instances** option.

1. When the **Launch cutover instances for X** servers dialog appears, choose **Launch** to begin the cutover. 

   On the **Source servers** page, the **Migration lifecycle** column will show **Cutover in progress** and the **Next step** column will show **Finalize cutover**. When the cutover starts, the Application Migration Service Console will indicate **Launch job started**.

1. Choose **View job details** on the dialog to view the specific Job for the cutover launch in the** Launch History** tab. 

### Successful cutover launch indicators
<a name="successful-cutover-gs"></a>

You can tell that the cutover instance launch was started successfully through several indicators on the **Source servers** page.



1. The **Alerts** column will state **Launched**. 

1. The **Migration lifecycle** column will state **Cutover in progress**.

1. The **Data replication status** will state **Healthy**.

1. The **Next step column** will state **Finalize cutover**.

## Reverting or finalizing a cutover
<a name="revert-finalize-cutover-gs"></a>

Once you have launched your cutover instances, open the Amazon EC2 Console and SSH or RDP into your cutover instances to ensure that they function correctly. Validate connectivity and perform acceptance tests for your application. 

**Note**  
You should turn on Termination Protection after you have completed your testing and before you are ready to finalize the cutover. Learn more about enabling termination protection in [this Amazon EC2 article ](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/terminating-instances.html#Using_ChangingDisableAPITermination).

### Reverting a cutover
<a name="reverting-cutover-gs"></a>

If you encounter any issues and want to launch new cutover instances, you can revert the cutover. This will revert your source servers' **Migration lifecycle** status to **Ready for cutover**, indicating that these servers have not undergone cutover. During a revert, you will also have the option to delete your Cutover instances for cost-saving purposes.

To revert a cutover:

1. Check the box to the left of every source server that has a launched cutover instance you want to revert.

1. Open the **Test and cutover** menu. 

1. Under **Cutover**, choose **Revert to "ready for cutover"**

1. This will revert your source servers' **Migration lifecycle** status to **Ready for cutover**, indicating that these servers have not undergone cutover. 

   When the **Revert cutover for X servers** dialog appears, choose **Revert**. 

### Finalizing a cutover
<a name="finalizing-cutover-gs"></a>

If you are completely done with your migration and performed a successful cutover, you can finalize the cutover. This will change your source servers' **Migration lifecycle** status to **Cutover complete**, indicating that the cutover is complete and that the migration has been performed successfully. In addition, this will stop data replication and cause all replicated data to be discarded. All AWS resources used for data replication will be terminated. 

To finalize a cutover:

1. Check the box to the left of every source server that has a launched cutover instance you want to finalize.

1. Open the **Test and cutover** menu. 

1. Under **Cutover**, choose **Finalize cutover**.

1. The **Finalize cutover for X servers** dialog will appear. Choose **Finalize**. This will change your source servers' **Migration lifecycle** status to **Cutover complete**, indicating that the cutover is complete and that the migration has been performed successfully. In addition, this will stop data replication and cause all replicated data to be discarded. All AWS resources used for data replication will be terminated. 

   The AWS Transform MGN console will indicate **Cutover finalized** when the cutover has completed successfully. 

   The AWS Transform MGN console will automatically stop data replication for the source servers that were cutover to save resource costs. The selected source servers' **Migration lifecycle** column will show the **Cutover complete** status, the **Data replication** status column will show **Disconnected**, and the **Next step** column will show **Mark as archived**. The source servers have now been successfully migrated into AWS.

1. You can now archive your source servers that have launched cutover instances. Archiving will remove these source servers from the main **Source servers** page, allowing you to focus on source servers that have not yet been cutover. You will still be able to access the archived servers through filtering options. 

   To archive your cutover source servers:

   1. Check the box to the left of each source server for which the **Migration lifecycle** column states **Cutover complete**. 

   1. Open the **Actions** menu and choose **Mark as archived**. 

   1. When the **Archive X server** dialog appears, choose **Archive**. 

   1. To see your archived servers, choose **Archived source servers** from the drop-down menu in the source servers view.

      You will now be able to see all of your archived servers. Use the same drop-down menu to see only **Active source servers** or **Discovered source servers**, according to your preferences.