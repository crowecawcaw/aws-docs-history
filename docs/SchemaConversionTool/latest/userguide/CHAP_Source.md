# Connecting to Netezza with AWS Schema Conversion Tool

You can use AWS SCT to convert schemas, code objects, and application code from Netezza to Amazon Redshift.

## Privileges for Netezza as a

source

The following privileges are required for using Netezza as a source:

- select on system.definition_schema.system view
- select on system.definition_schema.system table
- select on system.definition_schema.management table
- list on `<database_name>`
- list on `<schema_name>`
- list on `<database_name>`.all.table
- list on `<database_name>`.all.external table
- list on `<database_name>`.all.view
- list on `<database_name>`.all.materialized view
- list on `<database_name>`.all.procedure
- list on `<database_name>`.all.sequence
- list on `<database_name>`.all.function
- list on `<database_name>`.all.aggregate

In the preceding example, replace placeholders as following:

- Replace `database_name` with
  the name of the source database.
- Replace `schema_name` with
  the name of the source schema.

AWS SCT requires access to the following system tables and views. You can grant
access to these objects instead of granting access to
`system.definition_schema.system view` and
`system.definition_schema.system tables` in the preceding list.

- select on system.definition_schema.\_t_aggregate
- select on system.definition_schema.\_t_class
- select on system.definition_schema.\_t_constraint
- select on system.definition_schema.\_t_const_relattr
- select on system.definition_schema.\_t_database
- select on system.definition_schema.\_t_grpobj_priv
- select on system.definition_schema.\_t_grpusr
- select on system.definition_schema.\_t_hist_config
- select on system.definition_schema.\_t_object
- select on system.definition_schema.\_t_object_classes
- select on system.definition_schema.\_t_proc
- select on system.definition_schema.\_t_type
- select on system.definition_schema.\_t_user
- select on system.definition_schema.\_t_usrobj_priv
- select on system.definition_schema.\_vt_sequence
- select on system.definition_schema.\_v_aggregate
- select on system.definition_schema.\_v_constraint_depends
- select on system.definition_schema.\_v_database
- select on system.definition_schema.\_v_datatype
- select on system.definition_schema.\_v_dslice
- select on system.definition_schema.\_v_function
- select on system.definition_schema.\_v_group
- select on system.definition_schema.\_v_obj_relation
- select on system.definition_schema.\_v_obj_relation_xdb
- select on system.definition_schema.\_v_procedure
- select on system.definition_schema.\_v_relation_column
- select on system.definition_schema.\_v_relation_keydata
- select on system.definition_schema.\_v_relobjclasses
- select on system.definition_schema.\_v_schema_xdb
- select on system.definition_schema.\_v_sequence
- select on system.definition_schema.\_v_synonym
- select on system.definition_schema.\_v_system_info
- select on system.definition_schema.\_v_sys_constraint
- select on system.definition_schema.\_v_sys_object_dslice_info
- select on system.definition_schema.\_v_sys_user
- select on system.definition_schema.\_v_table
- select on system.definition_schema.\_v_table_constraint
- select on system.definition_schema.\_v_table_dist_map
- select on system.definition_schema.\_v_table_organize_column
- select on system.definition_schema.\_v_table_storage_stat
- select on system.definition_schema.\_v_user
- select on system.definition_schema.\_v_view
- select on system.information_schema.\_v_relation_column
- select on system.information_schema.\_v_table
- select on $hist_column_access\_\*

## Connecting to Netezza as a

source

Use the following procedure to connect to your Netezza source database
with the AWS Schema Conversion Tool.

###### To connect to a Netezza source database

1. In the AWS Schema Conversion Tool, choose **Add source**.
2. Choose **Netezza**, then choose
   **Next**.

The **Add source** dialog box appears. 3. For **Connection name**, enter a name for your database.
AWS SCT displays this name in the tree in the left panel. 4. Use database credentials from AWS Secrets Manager or enter them manually:

    * To use database credentials from Secrets Manager, use the following
     instructions:




    	1. For **AWS Secret**, choose
    	 the name of the secret.
    	2. Choose **Populate** to automatically fill in
    	 all values in the database connection dialog box from Secrets Manager.
    For information about using database credentials from Secrets Manager, see [Configuring AWS Secrets Manager in the AWS Schema Conversion Tool](CHAP_UserInterface.md "CHAP_UserInterface.md").
    * To enter the Netezza source database connection
     information manually, use the following instructions:




    | Parameter | Action |
    | --- | --- |
    | **Server name** | Enter the Domain Name System (DNS) name or IP address of your source database server. |
    | **Server port** | Enter the port used to connect to your source database server. |
    | **User name*<br>• and **Password** | Enter the database credentials to connect to your source database server.<br>AWS SCT uses the password to connect to your source database<br>only when you choose to connect to your database in a project.<br>To guard against exposing the password for your source database,<br>AWS SCT doesn't store the password by default. If you close your<br>AWS SCT project and reopen it, you are prompted for the password<br>to connect to your source database as needed. |
    | **Store password** | AWS SCT creates a secure vault to store SSL certificates and database<br>passwords. By turning this option on, you can store the database password<br>and connect quickly to the database without having to enter the password. |
    | **Netezza driver path** | Enter the path to the driver to use to connect to the source database.<br>For more information, see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").<br>If you store the driver path in the global project settings,<br>the driver path doesn't appear on the connection dialog box.<br>For more information, see<br>[Storing driver paths in the global settings](CHAP_Installing.md#CHAP_Installing.JDBCDrivers.Settings "CHAP_Installing.md#CHAP_Installing.JDBCDrivers.Settings"). |

5. Choose **Test Connection** to verify
   that AWS SCT can connect to your source database.
6. Choose **Connect** to connect to your source database.

## Configuring ongoing data replication

After you convert your Netezza database schemas and apply them to your Amazon Redshift database,
you can migrate data with AWS SCT data extraction agents. The agent extracts your data
and uploads it to your Amazon S3 bucket. You can then use AWS SCT to copy the data from Amazon S3
to Amazon Redshift.

If data in your source database changes during the migration process, you can
capture ongoing changes with your AWS SCT data extraction agents. Then you can
replicate these ongoing changes in your target database after you complete the
initial data migration. This process is called ongoing data replication or
_change data capture_ (CDC).

###### To configure ongoing data replication for migrations from Netezza to Amazon Redshift

1. In your source database, create a history database. You can use the following
   code example in the Netezza command line interface (CLI).

```
nzhistcreatedb -d `history_database_name` -t query -v 1 -u `load_user` -o `histdb_owner` -p `your_password`
```

In the preceding example, replace `history_database_name`
with the name of your history database. Next, replace `load_user`
with the name of the user that you have defined to load history data to the database.
Then, replace `histdb_owner` with the name of the user that
you have defined as the owner of the history database. Make sure that you have
already created this user and granted the `CREATE DATABASE` permission.
Finally, replace `your_password` with a secure password. 2. Configure the history logging. To do so, use the following code example.

```
CREATE HISTORY CONFIGURATION `history_configuration_name` HISTTYPE QUERY
    DATABASE `history_database_name` USER `load_user` PASSWORD `your_password` COLLECT PLAN, COLUMN
    LOADINTERVAL 1 LOADMINTHRESHOLD 0 LOADMAXTHRESHOLD 0 STORAGELIMIT 25
    LOADRETRY 2 VERSION 1;
```

In the preceding example, replace `history_configuration_name`
and `history_database_name` with the names of your history
configuration and your history database. Next, replace `load_user`
with the name of the user that you have defined to load history data to the database.
Then, replace `your_password` with a secure password. 3. Grant read permissions for all tables in the history database. You can use the
following code example to grant the `SELECT` permission.

```
GRANT SELECT ON `history_database_name`.ALL.TABLE TO `your_user`;
```

In the preceding example, replace `history_database_name` with
the name of your history database. Next, replace `your_user`
with the name of the user with minimal permissions to work with your Netezza database.
You use the credentials of this database user in AWS SCT. 4. Collect statistics for each table in your source schema to get the information
about the cardinality of columns. You can use the following command to generate
statistics in your history database.

```
GENERATE STATISTICS on "`schema_name`"."`table_name`";
```

In the preceding example, replace `schema_name` and
`table_name` with the name of your database schema and table. 5. Make sure that you completed the prerequisites by running the
following query:

```
SELECT COUNT(*) FROM `history_database_name`.`history_schema_name`."$hist_column_access_`N`";
```

In the preceding example, replace
`history_database_name` and
`history_schema_name` with the name of your
history database and schema. Next, replace `N`
with the the version number of your history database. For more information
about history database versions, see the [IBM Netezza Documentation](https://www.ibm.com/docs/en/netezza?topic=history-database-versions "https://www.ibm.com/docs/en/netezza?topic=history-database-versions"). 6. Install your data extraction agents. For more information, see [Installing extraction agents](agents.md#agents.Installing "agents.md#agents.Installing").

Make sure that the `{working.folder}` parameter in the `settings.properties` file
for all extractor instances points to the same folder. In this case, your extractors can coordinate the
CDC session and use a single transaction point for all subtasks. 7. Register your data extraction agent. For more information, see [Registering extraction agents with the AWS Schema Conversion Tool](agents.md#agents.Using "agents.md#agents.Using"). 8. Create your CDC task. For more information, see [Creating, running, and monitoring an AWS SCT task](agents.md#agents.Tasks "agents.md#agents.Tasks").

    1. Open your project in AWS SCT. In the left pane, choose your source table.
     Open the context (right-click) menu, and choose **Create local task**.
    2. For **Task name**, enter a descriptive name for your data migration task.
    3. For **Migration mode**, choose **Extract, upload, and copy**.
    4. Select **Enable CDC**.
    5. Choose the **CDC settings** tab and define
     the scope and the schedule of CDC sessions.
    6. Choose **Test task** to verify that you can connect to
     your working folder, Amazon S3 bucket, and Amazon Redshift data warehouse.
    7. Choose **Create** to create your task.
    8. Choose the **Tasks** tab, choose your task from the list,
     and choose **Start**.

9. The AWS SCT task maintains transactional consistency on the target
   database. The data extraction agent replicates transactions from the
   source in transaction ID order.

If you stop any of the migration sessions or if it fails, then the CDC
processing also stops.

## Netezza to Amazon Redshift conversion

settings

To edit Netezza to Amazon Redshift conversion settings, choose **Settings**
in AWS SCT, and then choose **Conversion settings**. From the upper
list, choose **Netezza**, and then choose **Netezza –
Amazon Redshift**. AWS SCT displays all available settings for Netezza to Amazon Redshift
conversion.

Netezza to Amazon Redshift conversion settings in AWS SCT include options for the
following:

- To limit the number of comments with action items in the converted
  code.

For **Add comments in the converted code for the action items of selected severity and higher**,
choose the severity of action items. AWS SCT adds comments in the converted code
for action items of the selected severity and higher.

For example, to minimize the number of comments in your converted code, choose
**Errors only**. To include comments for all action items in your
converted code, choose **All messages**.

- To set the maximum number of tables that AWS SCT can apply to your target Amazon Redshift cluster.

For **The maximum number of tables for the target Amazon Redshift cluster**,
choose the number of tables that AWS SCT can apply to your Amazon Redshift cluster.

Amazon Redshift has quotas that limit the use tables for different cluster node
types. If you choose **Auto**, AWS SCT determines the
number of tables to apply to your target Amazon Redshift cluster depending on the
node type. Optionally, choose the value manually. For more information,
see [Quotas and
limits in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-limits.md "../../../redshift/latest/mgmt/amazon-redshift-limits.md") in the
_Amazon Redshift Management Guide_.

AWS SCT converts all your source tables, even if this is more than your Amazon Redshift cluster can store.
AWS SCT stores the converted code in your project and doesn't apply it to the target database.
If you reach the Amazon Redshift cluster quota for the tables when you apply the converted code, then AWS SCT
displays a warning message. Also, AWS SCT applies tables to your target Amazon Redshift cluster until
the number of tables reaches the limit.

- To apply compression to Amazon Redshift table columns. To do so, select
  **Use compression encoding**.

AWS SCT assigns compression encoding to columns automatically using
the default Amazon Redshift algorithm. For more information, see [Compression
encodings](../../../redshift/latest/dg/c_Compression_encodings.md "../../../redshift/latest/dg/c_Compression_encodings.md") in the _Amazon Redshift Database Developer Guide_.

By default, Amazon Redshift doesn't apply compression to columns that are defined
as sort and distribution keys. You can change this behavior and apply
compression to these columns. To do so, select **Use compression
encoding for KEY columns**. You can select this option only
when you select the **Use compression encoding**
option.

## Netezza to Amazon Redshift conversion

optimization settings

To edit Netezza to Amazon Redshift conversion optimization settings, choose **Settings**
in AWS SCT, and then choose **Conversion settings**. From the upper list, choose
**Netezza**, and then choose **Netezza – Amazon Redshift**. In the
left pane, choose **Optimization strategies**. AWS SCT displays conversion
optimization settings for Netezza to Amazon Redshift conversion.

Netezza to Amazon Redshift conversion optimization settings in AWS SCT include options for the
following:

- To work with automatic table optimization. To do so, select
  **Use Amazon Redshift automatic table tuning**.

Automatic table optimization is a self-tuning process in Amazon Redshift that automatically
optimizes the design of tables. For more information, see [Working with automatic table optimization](../../../redshift/latest/dg/t_Creating_tables.md "../../../redshift/latest/dg/t_Creating_tables.md")
in the _Amazon Redshift Database Developer Guide_.

To rely only on the automatic table optimization, choose
**None** for **Initial key selection strategy**.

- To choose sort and distribution keys using your strategy.

You can choose sort and distribution keys using Amazon Redshift metadata, statistical information, or both these options.
For **Initial key selection strategy** on the **Optimization strategies** tab,
choose one of the following options:

    + Use metadata, ignore statistical information
    + Ignore metadata, use statistical information
    + Use metadata and statistical information

Depending on the option that you choose, you can select optimization
strategies. Then, for each strategy, enter the value (0–100). These
values define the weight of each strategy. Using these weight values,
AWS SCT defines how each rule influences on the choice of distribution
and sort keys. The default values are based on the AWS migration best
practices.

You can define the size of small tables for the **Find small
tables** strategy. For **Min table row
count** and **Max table row count**, enter
the minimum and maximum number of rows in a table to define it as a
small table. AWS SCT applies the `ALL` distribution style to
small tables. In this case, a copy of the entire table is distributed to
every node.

- To configure strategy details.

In addition to defining the weight for each optimization strategy, you can configure
the optimization settings. To do so, choose **Conversion optimization**.

    + For **Sort key columns limit**, enter the maximum number
     of columns in the sort key.
    + For **Skewed threshold value**, enter the percentage (0–100)
     of a skewed value for a column. AWS SCT excludes columns with the skew value greater than
     the threshold from the list of candidates for the distribution key. AWS SCT defines the
     skewed value for a column as the percentage ratio of the number of occurrences of the most
     common value to the total number of records.
    + For **Top N queries from the query history table**, enter
     the number (1–100) of the most frequently used queries to analyze.
    + For **Select statistics user**, choose the database user for which you want
     to analyze the query statistics.

Also, on the **Optimization strategies** tab, you can
define the size of small tables for the **Find small
tables** strategy. For **Min table row
count** and **Max table row count**, enter
the minimum and maximum number of rows in a table to consider it as a
small table. AWS SCT applies the `ALL` distribution style to
small tables. In this case, a copy of the entire table is distributed to
every node.
