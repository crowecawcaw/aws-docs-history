

# Step 9: Create and Run Your AWS DMS Migration Task
<a name="chap-rdsoracle2aurora.steps.createmigrationtask"></a>

Using a AWS DMS task, you can specify what schema to migrate and the type of migration. You can migrate existing data, migrate existing data and replicate ongoing changes, or replicate data changes only. This walkthrough migrates existing data only.

1. On the **Create Task** page, specify the task options. The following table describes the settings.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Task name</b> </td><td>Enter <code>migratehrschema</code>.</td></tr>
  <tr><td> <b>Task description</b> </td><td>Enter a description for the task.</td></tr>
  <tr><td> <b>Source endpoint</b> </td><td>Shows <code>orasource</code> (the Amazon RDS for Oracle endpoint).</td></tr>
  <tr><td> <b>Target endpoint</b> </td><td>Shows <code>aurtarget</code> (the Amazon Aurora MySQL endpoint).</td></tr>
  <tr><td> <b>Replication instance</b> </td><td>Shows <code>DMSdemo-repserver</code> (the AWS DMS replication instance created in an earlier step).</td></tr>
  <tr><td> <b>Migration type</b> </td><td>Choose <b>Migrate existing data</b>.</td></tr>
  <tr><td> <b>Start task on create</b> </td><td>Select this option.</td></tr>
</tbody>
</table>


   The page should look like the following:  
![Create task page](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora23.png)

1. Under **Task Settings**, choose **Do nothing** for **Target table preparation mode**, because you have already created the tables through Schema Migration Tool. Because this migration doesn’t contain any LOBs, you can leave the LOB settings at their defaults.

   Optionally, you can select **Enable logging**. If you enable logging, you will incur additional Amazon CloudWatch charges for the creation of CloudWatch logs. For this walkthrough, logs are not necessary.  
![Task Settings section](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora24.png)

1. Leave the Advanced settings at their default values.

1. Choose **Table mappings**, choose **Default** for **Mapping method**, and then choose `HR` for **Schema to migrate**.

   The completed section should look like the following.  
![Completed Table mappings section](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora25.png)

1. Choose **Create task**. The task will begin immediately.

The Tasks section shows you the status of the migration task.

![Table statistics tab](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora25.5.png)


You can monitor your task if you choose **Enable logging** when you set up your task. You can then view the CloudWatch metrics by doing the following:

1. On the navigation pane, choose **Tasks**.

1. Choose your migration task (`migratehrschema`).

1. Choose the **Task monitoring** tab, and monitor the task in progress on that tab.