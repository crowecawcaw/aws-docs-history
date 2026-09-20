

# Creating a task
<a name="CHAP_Tasks.Creating"></a>

To create an AWS DMS migration task, you do the following:
+ Create a source endpoint, a target endpoint, and a replication instance before you create a migration task. 
+ Choose a migration method:
  + **Migrating data to the target database** – This process creates files or tables in the target database and automatically defines the metadata that is required at the target. It also populates the tables with data from the source. The data from the tables is loaded in parallel for improved efficiency. This process is the **Migrate existing data** option in the AWS Management Console and is called `Full Load` in the API.
  + **Capturing changes during migration** – This process captures changes to the source database that occur while the data is being migrated from the source to the target. When the migration of the originally requested data has completed, the change data capture (CDC) process then applies the captured changes to the target database. Changes are captured and applied as units of single committed transactions, and you can update several different target tables as a single source commit. This approach guarantees transactional integrity in the target database. This process is the **Migrate existing data and replicate ongoing changes** option in the console and is called `full-load-and-cdc` in the API.
  + **Replicating only data changes on the source database** – This process reads the recovery log file of the source database management system (DBMS) and groups together the entries for each transaction. In some cases, AWS DMS can't apply changes to the target within a reasonable time (for example, if the target isn't accessible). In these cases, AWS DMS buffers the changes on the replication server for as long as necessary. It doesn't reread the source DBMS logs, which can take a large amount of time. This process is the **Replicate data changes only** option in the AWS DMS console. 
+ Determine how the task should handle large binary objects (LOBs) on the source. For more information, see [Setting LOB support for source databases in an AWS DMS task](CHAP_Tasks.LOBSupport.md).
+ Specify migration task settings. These include setting up logging, specifying what data is written to the migration control table, how errors are handled, and other settings. For more information about task settings, see [Specifying task settings for AWS Database Migration Service tasks](CHAP_Tasks.CustomizingTasks.TaskSettings.md).
+ Set up table mapping to define rules to select and filter data that you are migrating. For more information about table mapping, see [Using table mapping to specify task settings](CHAP_Tasks.CustomizingTasks.TableMapping.md). Before you specify your mapping, make sure that you review the documentation section on data type mapping for your source and your target database. 
+ Enable and run premigration task assessments before you run the task. For more information about premigration assessments, see [Enabling and working with premigration assessments for a task](CHAP_Tasks.AssessmentReport.md).
+ Specify any required supplemental data for the task to migrate your data. For more information, see [Specifying supplemental data for task settings](CHAP_Tasks.TaskData.md).

You can choose to start a task as soon as you finish specifying information for that task on the **Create task** page. Alternatively, you can start the task from the Dashboard page later as well.

The following procedure assumes that you have already specified replication instance information and endpoints. For more information about setting up endpoints, see [Creating source and target endpoints](CHAP_Endpoints.Creating.md).

**To create a migration task**

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/). 

   If you are signed in as an AWS Identity and Access Management (IAM) user, make sure that you have the appropriate permissions to access AWS DMS. For more information about the permissions required, see [IAM permissions needed to use AWS DMS](security-iam.md#CHAP_Security.IAMPermissions).

1. On the navigation pane, choose **Database migration tasks**, and then choose **Create task**.

1. On the **Create database migration task** page, in the **Task configuration** section, specify the task options. The following table describes the settings.  
![Create task](https://docs.aws.amazon.com/dms/latest/userguide/images/datarep-gs-wizard4.png)


<table>
<thead>
  <tr><th> For this option </th><th> Do this </th></tr>
</thead>
<tbody>
  <tr><td> <b>Task identifier</b> </td><td>Enter a name for the task.</td></tr>
  <tr><td> <b>Descriptive Amazon Resource Name (ARN) - <i>optional</i></b> </td><td>A friendly name to override the default AWS DMS ARN. You can't change this name after you create the task.</td></tr>
  <tr><td> <b>Replication instance</b> </td><td>Shows the replication instance to be used.</td></tr>
  <tr><td> <b>Source database endpoint</b> </td><td>Shows the source endpoint to be used.</td></tr>
  <tr><td> <b>Target database endpoint</b> </td><td>Shows the target endpoint to be used.</td></tr>
  <tr><td> <b>Migration type</b> </td><td>Choose the migration method you want to use. You can choose to have just the existing data migrated to the target database or have ongoing changes sent to the target database in addition to the migrated data.</td></tr>
</tbody>
</table>


1. In the **Task Settings** section, specify values for editing your task, target table preparation mode, stop task, LOB settings, validation, and logging.


<table>
<thead>
  <tr><th> For this option </th><th> Do this </th></tr>
</thead>
<tbody>
  <tr><td> <b>Editing mode</b> </td><td>Choose whether to use the Wizard or the JSON editor to specify your task settings. If you choose Wizard, the following options will be displayed. </td></tr>
  <tr><td> <b>CDC start mode for source transactions</b> </td><td>This setting is only visible if you choose <b>Replicate data changes only</b> for <b>Migration type</b> in the preceding section.<br /><b>Disable custom CDC start mode</b> – If you choose this option, you can start your task either automatically by using the <b>Automatically on create</b> option following, or manually by using the console.<br /><b>Enable custom CDC start mode</b> – If you choose this option, you can specify a custom UTC start time to start processing changes.</td></tr>
  <tr><td> <b>Target table preparation mode</b> </td><td>This setting is only visible if you choose <b>Migrate existing data</b> or <b>Migrate existing data and replicate ongoing changes</b> for <b>Migration type</b> in the preceding section.<br /><b>Do nothing</b> – In <b>Do nothing</b> mode, AWS DMS assumes that the target tables have been pre-created on the target. If the tables aren't empty, conflicts might occur during data migration and can result in a DMS task error. If the target table doesn't exist, DMS creates the table for you. Your table structure remains as is and any existing data is left in the table. <b>Do nothing</b> mode is appropriate for CDC-only tasks when the target tables have been backfilled from the source and ongoing replication is applied to keep the source and target in sync. To pre-create tables, you can use DMS Schema Conversion. For more information, see <a href="CHAP_SchemaConversion.md">Converting database schemas using DMS Schema Conversion</a>.<br /><b>Drop tables on target</b> – In <b>Drop tables on target</b> mode, AWS DMS drops the target tables and recreates them before starting the migration. This approach ensures that the target tables are empty when the migration starts. AWS DMS creates only the objects required to efficiently migrate the data: tables, primary keys, and in some cases, unique indexes. AWS DMS doesn't create secondary indexes, nonprimary key constraints, or column data defaults. If you are performing a full load plus CDC or CDC-only task, we recommend that you pause the migration at this point. Then, create secondary indexes that support filtering for update and delete statements.<br />You might need to perform some configuration on the target database when you use <b>Drop tables on target</b> mode. For example, for an Oracle target, AWS DMS can't create a schema (database user) for security reasons. In this case, you pre-create the schema user so AWS DMS can create the tables when the migration starts. For most other target types, AWS DMS creates the schema and all associated tables with the proper configuration parameters.<br /><b>Truncate</b> – In <b>Truncate</b> mode, AWS DMS truncates all target tables before the migration starts. If the target table doesn't exist, DMS creates the table for you. Your table structure remains as is but tables are truncated at the target. <b>Truncate</b> mode is appropriate for full load or full load plus CDC migrations where the target schema has been pre-created before the migration starts. To pre-create tables, you can use DMS Schema Conversion. For more information, see <a href="CHAP_SchemaConversion.md">Converting database schemas using DMS Schema Conversion</a>.If your target is MongoDB, <b>Truncate</b> mode doesn’t truncate tables at the target. Instead, it drops the collection and loses all the indices. Avoid <b>Truncate</b> mode when your target is MongoDB. </td></tr>
  <tr><td> <b>Stop task after full load completes</b> </td><td>This setting is only visible if you choose <b>Migrate existing data and replicate ongoing changes</b> for <b>Migration type</b> in the preceding section.<br /><b>Don't stop</b> – Don't stop the task but immediately apply cached changes and continue on.<br /><b>Stop before applying cached changes</b> – Stop the task before the application of cached changes. Using this approach, you can add secondary indexes that might speed the application of changes.<br /><b>Stop after applying cached changes</b> – Stop the task after cached changes have been applied. Using this approach, you can add foreign keys if you are using transactional apply.</td></tr>
  <tr><td> <b>Include LOB columns in replication</b> </td><td><b>Don't include LOB columns</b> – LOB columns are excluded from the migration.<br /><b>Full LOB mode</b> – Migrate complete LOBs regardless of size. AWS DMS migrates LOBs piecewise in chunks controlled by the <b>LOB Chunk size</b> parameter. This mode is slower than using Limited LOB mode.<br /><b>Limited LOB mode</b> – Truncate LOBs to the value of the <b>Max LOB size</b> parameter. This mode is faster than using Full LOB mode.</td></tr>
  <tr><td> <b>Maximum LOB size (kb)</b> </td><td>In <b>Limited LOB Mode</b>, LOB columns that exceed the setting of <b>Max LOB size</b> are truncated to the specified <b>Max LOB Size</b> value.</td></tr>
  <tr><td> <b>Enable validation</b> </td><td>Enables data validation, to verify that the data is migrated accurately from the source to the target. For more information, see <a href="CHAP_Validating.md">AWS DMS data validation</a>.</td></tr>
  <tr><td> <b>Enable CloudWatch logs</b> </td><td>Enables logging by Amazon CloudWatch.</td></tr>
</tbody>
</table>


1. In the **Premigration assessment** section, choose whether to run a premigration assessment. A premigration assessment warns you of potential migration issues before starting your database migration task. For more information, see [Enabling and working with premigration assessments](CHAP_Tasks.AssessmentReport.md). 

1. In the **Migration task startup configuration** section, specify whether to start the task automatically after creation.

1. In the **Tags** section, specify any tags you need to organize your task. You can use tags to manage your IAM roles and policies, and track your DMS costs. For more information, see [Tagging resources](CHAP_Tagging.md).

1. After you have finished with the task settings, choose **Create task**.