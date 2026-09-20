

# Step 6: Create AWS DMS Source and Target Endpoints
<a name="chap-rdsoracle2postgresql.steps.createsourcetargetendpoints"></a>

While your replication instance is being created, you can specify the source and target database endpoints using the [AWS Management Console](https://console.aws.amazon.com/). However, you can only test connectivity after the replication instance has been created, because the replication instance is used in the connection.

1. Sign in to the AWS Management Console, open the [AWS DMS console](https://console.aws.amazon.com/dms/v2), and then choose **Endpoints**.

1. Specify your connection information for the source Oracle database and the target PostgreSQL database. The following table describes the source settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter a name, such as <code>Orasource</code>.</td></tr>
  <tr><td> <b>Source Engine</b> </td><td>Choose <b>oracle</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Provide the Oracle DB instance server name.</td></tr>
  <tr><td> <b>Port</b> </td><td>The port of the database. The default for Oracle is <code>1521</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose an SSL mode if you want to enable encryption for your connection’s traffic.</td></tr>
  <tr><td> <b>Username</b> </td><td>The user you want to use to connect to the source database.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the user.</td></tr>
  <tr><td> <b>SID</b> </td><td>Provide the Oracle database name.</td></tr>
</tbody>
</table>


   The following table describes the advanced source settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Extra connection attributes</b> </td><td>Extra parameters that you can set in an endpoint to add functionality or change the behavior of AWS DMS. Some of the most common and convenient parameters to set for an Oracle source database are the following. Separate multiple entries from each other by using a semi-colon (;).<ul><li>  <code>addSupplementalLogging</code> - This parameter automatically configures supplemental logging when set to <code>Y</code>. </li><li>  <code>useLogminerReader</code> - By default, AWS DMS uses LogMiner on the Oracle database to capture all of the changes on the source database. The other mode is called Binary Reader. When using Binary Reader instead of LogMiner, AWS DMS copies the archived redo log from the source Oracle database to the replication server and reads the entire log in order to capture changes. The Binary Reader option is recommended if you are using ASM since it has performance advantages over LogMiner on ASM. If your source database is 12c, then the Binary Reader option is currently the only way to capture CDC changes in Oracle for LOB objects. </li></ul><br />To use LogMiner, enter the following: <code>useLogminerReader=Y</code> <br />To use Binary Reader, enter the following: <code>useLogminerReader=N; useBfile=Y</code>`</td></tr>
  <tr><td> <b> KMS key </b> </td><td>Enter the KMS key if you choose to encrypt your replication instance’s storage.</td></tr>
</tbody>
</table>


   For information about extra connection attributes, see [Using Extra Connection Attributes](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).

   The following table describes the target settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter a name, such as <code>Postgrestarget</code>.</td></tr>
  <tr><td> <b>Target Engine</b> </td><td>Choose <b>postgres</b>.</td></tr>
  <tr><td> <b>Servername</b> </td><td>Provide the PostgreSQL DB instance server name.</td></tr>
  <tr><td> <b>Port</b> </td><td>The port of the database. The default for PostgreSQL is <code>5432</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose <b>None</b>.</td></tr>
  <tr><td> <b>Username</b> </td><td>The user you want to use to connect to the target database.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the PostgreSQL DB instance.</td></tr>
</tbody>
</table>


   The following is an example of the completed page.  
![Completed replication task connections page](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2postgressql19.5.png)

1. After the endpoints and replication instance have been created, test each endpoint connection by choosing **Run test** for the source and target endpoints.

1. Drop foreign key constraints and triggers on the target database.

   During the full load process, AWS DMS does not load tables in any particular order, so it may load the child table data before parent table data. As a result, foreign key constraints might be violated if they are enabled. Also, if triggers are present on the target database, then it may change data loaded by AWS DMS in unexpected ways.

1. If you do not have one, then generate a script that enables the foreign key constraints and triggers.

   Later, when you want to add them to your migrated database, you can just run this script.

1. (Optional) Drop secondary indexes on the target database.

   Secondary indexes (as with all indexes) can slow down the full load of data into tables since they need to be maintained and updated during the loading process. Dropping them can improve the performance of your full load process. If you drop the indexes, then you will need to add them back later after the full load is complete.

1. Choose **Next**.