

# Step 9: Create and Run Your AWS DMS Migration Task
<a name="chap-rdsoracle2redshift.steps.createmigrationtask"></a>

Using an AWS DMS task, you can specify what schema to migrate and the type of migration. You can migrate existing data, migrate existing data and replicate ongoing changes, or replicate data changes only. This walkthrough migrates existing data only.

1. On the **Create Task** page, specify the task options. The following table describes the settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Task name</b> </td><td>Enter <code>migrateSHschema</code>.</td></tr>
  <tr><td> <b>Replication instance</b> </td><td>Shows <code>DMSdemo-repserver</code> (the AWS DMS replication instance created in an earlier step).</td></tr>
  <tr><td> <b>Source endpoint</b> </td><td>Shows <code>orasource</code> (the Amazon RDS for Oracle endpoint).</td></tr>
  <tr><td> <b>Target endpoint</b> </td><td>Shows <code>redshifttarget</code> (the Amazon Redshift endpoint).</td></tr>
  <tr><td> <b>Migration type</b> </td><td>Choose <b>Migrate existing data</b>.</td></tr>
  <tr><td> <b>Start task on create</b> </td><td>Choose this option.</td></tr>
</tbody>
</table>


   The page should look like the following.  
![Create task page](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2redshift23.png)

1. On the **Task Settings** section, specify the settings as shown in the following table.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Target table preparation mode</b> </td><td>Choose <b>Do nothing</b>.</td></tr>
  <tr><td> <b>Include LOB columns in replication</b> </td><td>Choose <b>Limited LOB mode</b>.</td></tr>
  <tr><td> <b>Max LOB size (kb)</b> </td><td>Accept the default (32).</td></tr>
</tbody>
</table>


   The section should look like the following.  
![Create task page](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2redshift23.5.png)

1. In the **Selection rules** section, specify the settings as shown in the following table.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Schema name is</b> </td><td>Choose <code>Enter a schema</code>.</td></tr>
  <tr><td> <b>Schema name is like</b> </td><td>Enter <code>SH%</code>.</td></tr>
  <tr><td> <b>Table name is like</b> </td><td>Enter <b>%</b>.</td></tr>
  <tr><td> <b>Action</b> </td><td>Choose <code>Include</code>.</td></tr>
</tbody>
</table>


   The section should look like the following:  
![Add selection rule page](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2redshift24.png)

1. Choose **Add selection rule**.

1. Choose **Create task**. The task begins immediately. The **Tasks** section shows you the status of the migration task.

![Tasks page](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2redshift25.5.png)
