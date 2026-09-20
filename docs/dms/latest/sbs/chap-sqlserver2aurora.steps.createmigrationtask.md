

# Step 7: Create and Run Your AWS DMS Migration Task
<a name="chap-sqlserver2aurora.steps.createmigrationtask"></a>

Using an AWS DMS task, you can specify what schema to migrate and the type of migration. You can migrate existing data, migrate existing data and replicate ongoing changes, or replicate data changes only.

1. In the AWS DMS console, on the **Create task** page, specify the task options. The following table describes the settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Task name</b> </td><td>Enter a name for the migration task.</td></tr>
  <tr><td> <b>Task description</b> </td><td>Enter a description for the task.</td></tr>
  <tr><td> <b>Source endpoint</b> </td><td>Shows the SQL Server source endpoint.<br />If you have more than one endpoint for the user, choose the correct endpoint from the list.</td></tr>
  <tr><td> <b>Target endpoint</b> </td><td>Shows the Aurora MySQL target endpoint.</td></tr>
  <tr><td> <b>Replication instance</b> </td><td>Shows the AWS DMS replication instance.</td></tr>
  <tr><td> <b>Migration type</b> </td><td>Choose an option.<ul><li>  <b>Migrate existing data</b> - AWS DMS migrates only your existing data. Changes to your source data aren’t captured and applied to your target. If you can afford to take an outage for the duration of the full load, then this is the simplest option. You can also use this option to create test copies of your database. If the source SQL Server database is an Amazon RDS database, you must choose this option. </li><li>  <b>Migrate existing data and replicate ongoing changes</b> - AWS DMS captures changes while migrating your existing data. AWS DMS continues to capture and apply changes even after the bulk data has been loaded. Eventually the source and target databases are in sync, allowing for a minimal downtime. </li><li>  <b>Replicate data changes only</b> - Bulk load data using a different method. This approach generally applies only to homogeneous migrations. </li></ul></td></tr>
  <tr><td> <b>Start task on create</b> </td><td>In most situations, you should choose this option. Sometimes, you might want to delay the start of a task, for example, if you want to change logging levels.</td></tr>
</tbody>
</table>


   The page should look similar to the following:  
![Create task page](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsqlserver2aurora-dmstask.png)

1. Under **Task settings**, specify the settings. The following table describes the settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Target table preparation mode</b> </td><td>Choose an option.<ul><li>  <b>Do nothing</b> - AWS DMS does nothing to prepare your tables. Your table structure remains the same, and any existing data remains in the table. You can use this method to consolidate data from multiple systems. </li><li>  <b>Drop tables on target</b> - AWS DMS creates your target tables for you. AWS DMS drops and re-creates the tables to migrate before migration. AWS DMS creates the table and a primary key only for heterogeneous migrations. </li><li>  <b>Truncate</b> - AWS DMS truncates a target table before loading it. If the target table doesn’t exist, then AWS DMS creates it. </li></ul> If the AWS Schema Conversion Tool already created the tables on the target, choose <b>Do nothing</b> or <b>Truncate</b>. </td></tr>
  <tr><td> <b>Include LOB columns in replication</b> </td><td>Choose an option.<ul><li>  <b>Don’t include LOB columns</b> - Do not migrate LOB data. </li><li>  <b>Full LOB mode</b> - AWS DMS migrates all LOBs (large objects) from the source to the target regardless of size. In this configuration, AWS DMS has no information about the maximum size of LOBs to expect. Thus, LOBs are migrated one at a time, piece by piece. Full LOB mode can be relatively slow. </li><li>  <b>Limited LOB mode</b> - You set a maximum size LOB that AWS DMS accepts. This option enables AWS DMS to pre-allocate memory and load the LOB data in bulk. LOBs that exceed the maximum LOB size are truncated, and a warning is issued to the log file. In limited LOB mode, you get significant performance gains over full LOB mode. We recommend that you use limited LOB mode whenever possible. </li></ul></td></tr>
  <tr><td> <b>Max LOB size (kb)</b> </td><td>When <b>Limited LOB mode</b> is selected, this option determines the maximum LOB size that AWS DMS accepts. Any LOBs that are larger than this value are truncated to this value.</td></tr>
  <tr><td> <b>Enable logging</b> </td><td>It’s best to select <b>Enable logging</b>. If you enable logging, you can see any errors or warnings that the task encounters, and you can troubleshoot those issues.</td></tr>
</tbody>
</table>


1. Leave the Advanced settings at their default values.

1. If you created and exported mapping rules with AWS SCT in the last step in [Step 4: Convert the SQL Server Schema to Aurora MySQL](chap-sqlserver2aurora.steps.convertschema.md), choose **Table mappings**, and select the **JSON** tab. Then select **Enable JSON editing**, and enter the table mappings you saved.

   If you did not create mapping rules, then proceed to the next step.

1. Choose **Create task**. The task starts immediately.

The **Tasks** section shows you the status of the migration task.

![Tasks section showing the source, target, type, and completion status for a task](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsqlserver2aurora-dmsmonitor.png)


If you chose **Enable logging** during setup, you can monitor your task. You can then view the Amazon CloudWatch metrics.

1. On the navigation pane, choose **Tasks**.

1. Choose your migration task.

1. Choose the **Task monitoring** tab, and monitor the task in progress on that tab.

   When the full load is complete and cached changes are applied, the task stops on its own.

1. On the target Aurora MySQL database, if you disabled foreign key constraints and triggers, enable them using the script that you saved previously.

1. On the target Aurora MySQL database, re-create the secondary indexes if you removed them previously.

1. If you chose to use AWS DMS to replicate changes, in the AWS DMS console, start the AWS DMS task by choosing **Start/Resume** for the task.

   Important replication instance metrics to monitor include the following:
   + CPU
   + FreeableMemory
   + DiskQueueDepth
   + CDCLatencySource
   + CDCLatencyTarget

   The AWS DMS task keeps the target Aurora MySQL database up to date with source database changes. AWS DMS keeps all the tables in the task up to date until it’s time to implement the application migration. The latency is zero, or close to zero, when the target has caught up to the source.

For more information, see [Monitoring DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html).