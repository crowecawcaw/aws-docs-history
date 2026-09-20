

# Step 6: Create AWS DMS Source and Target Endpoints
<a name="chap-sqlserver2aurora.steps.createsourcetargetendpoints"></a>

While your replication instance is being created, you can specify the source and target database endpoints using the [AWS Management Console](https://console.aws.amazon.com/). However, you can test connectivity only after the replication instance has been created, because the replication instance is used in the connection.

1. In the AWS DMS console, specify your connection information for the source SQL Server database and the target Aurora MySQL database. The following table describes the source settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter a name, such as <code>SQLServerSource</code>.</td></tr>
  <tr><td> <b>Source Engine</b> </td><td>Choose <b>sqlserver</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Provide the SQL Server DB instance server name.</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter the port number of the database. The default for SQL Server is <code>1433</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose an SSL mode if you want to enable encryption for your connection’s traffic.</td></tr>
  <tr><td> <b>User name</b> </td><td>Enter the name of the user you want to use to connect to the source database.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the user.</td></tr>
  <tr><td> <b>Database name</b> </td><td>Provide the SQL Server database name.</td></tr>
</tbody>
</table>


   The following table describes the advanced source settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Extra connection attributes</b> </td><td>Extra parameters that you can set in an endpoint to add functionality or change the behavior of AWS DMS. A few of the most relevant attributes are listed here. Use a semicolon (;) to separate multiple entries.<ul><li>  <code>safeguardpolicy</code> - Changes the behavior of SQL Server by opening transactions to prevent the transaction log from being truncated while AWS DMS is reading the log. Valid values are <code>EXCLUSIVE_AUTOMATIC_TRUNCATION</code> or <code>RELY_ON_SQL_SERVER_REPLICATION_AGENT</code> (default). </li><li>  <code>useBCPFullLoad</code> - Directs AWS DMS to use BCP (bulk copy) for data loading. Valid values are <code>Y</code> or <code>N</code>. When the target table contains an identity column that does not exist in the source table, you must disable the use of BCP for loading the table by setting the parameter to <code>N</code>. </li><li>  <code>BCPPacketSize</code> - If BCP is enabled for data loads, then enter the maximum packet size used by BCP. Valid values are <code>1</code> – <code>100000</code> (default <code>16384</code>). </li><li>  <code>controlTablesFileGroup</code> - Specifies the file group to use for the control tables that the AWS DMS process creates in the database. </li></ul></td></tr>
  <tr><td> <b> KMS key </b> </td><td>Enter the KMS key if you choose to encrypt your replication instance’s storage.</td></tr>
</tbody>
</table>


   The following table describes the target settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter a name, such as <code>Auroratarget</code>.</td></tr>
  <tr><td> <b>Target Engine</b> </td><td>Choose <b>aurora</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Provide the Aurora MySQL DB server name for the primary instance.</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter the port number of the database. The default for Aurora MySQL is <code>3306</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose <b>None</b>.</td></tr>
  <tr><td> <b>User name</b> </td><td>Enter the name of the user that you want to use to connect to the target database.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the user.</td></tr>
</tbody>
</table>


   The following table describes the advanced target settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Extra connection attributes</b> </td><td>Extra parameters that you can set in an endpoint to add functionality or change the behavior of AWS DMS. A few of the most relevant attributes are listed here. Use a semicolon to separate multiple entries.<ul><li>  <code>targetDbType</code> - By default, AWS DMS creates a different database for each schema that is being migrated. If you want to combine several schemas into a single database, set this option to <code>targetDbType=SPECIFIC_DATABASE</code>. </li><li>  <code>initstmt</code> - Use this option to invoke the MySQL <code>initstmt</code> connection parameter and accept anything MySQL <code>initstmt</code> accepts. For an Aurora MySQL target, it’s often useful to disable foreign key checks by setting this option to <code>initstmt=SET FOREIGN_KEY_CHECKS=0</code>. </li></ul></td></tr>
  <tr><td> <b> KMS key </b> </td><td>Enter the KMS key if you choose to encrypt your replication instance’s storage.</td></tr>
</tbody>
</table>


   The following is an example of the completed page.  
![Completed Replication Task Page showing Replication instance created successfully](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsqlserver2aurora-dmsconnect.png)

   For information about extra connection attributes, see [Using Extra Connection Attributes](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).

1. After the endpoints and replication instance are created, test the endpoint connections by choosing **Run test** for the source and target endpoints.

1. Drop foreign key constraints and triggers on the target database.

   During the full load process, AWS DMS does not load tables in any particular order, so it might load the child table data before parent table data. As a result, foreign key constraints might be violated if they are enabled. Also, if triggers are present on the target database, they might change data loaded by AWS DMS in unexpected ways.

   ```
   ALTER TABLE 'table_name' DROP FOREIGN KEY 'fk_name';
   
   DROP TRIGGER 'trigger_name';
   ```

1. If you dropped foreign key constraints and triggers on the target database, generate a script that enables the foreign key constraints and triggers.

   Later, when you want to add them to your migrated database, you can just run this script.

1. (Optional) Drop secondary indexes on the target database.

   Secondary indexes (as with all indexes) can slow down the full load of data into tables because they must be maintained and updated during the loading process. Dropping them can improve the performance of your full load process. If you drop the indexes, you must to add them back later, after the full load is complete.

   ```
   ALTER TABLE 'table_name' DROP INDEX  'index_name';
   ```

1. Choose **Next**.