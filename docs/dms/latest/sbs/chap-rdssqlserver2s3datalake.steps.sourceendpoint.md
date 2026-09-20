

# Step 3: Create an AWS DMS Source Endpoint
<a name="chap-rdssqlserver2s3datalake.steps.sourceendpoint"></a>

After you configured the AWS Database Migration Service (AWS DMS) replication instance and the source Amazon RDS for SQL Server instance, ensure connectivity between these two instances. To ensure that the replication instance can access the server and the port for the database, make changes to the relevant security groups and network access control lists. For more information about your network configuration, see [Setting up a network for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html).

After you completed the network configurations, you can create a source endpoint.

To create a source endpoint, do the following:

1. Open the AWS DMS console at https://console.aws.amazon.com/dms/v2/.

1. Choose **Endpoints**.

1. Choose **Create endpoint**.

1. On the **Create endpoint** page, enter the following information.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint type</b> </td><td>Choose <b>Source endpoint</b>, turn on <b>Select RDS DB instance</b>, and choose <code>datalake-source-db</code> RDS instance.</td></tr>
  <tr><td> <b>Endpoint identifier</b> </td><td>Enter <b>datalake-source-db</b>.</td></tr>
  <tr><td> <b>Source engine</b> </td><td>Choose <b>Microsoft SQL Server</b>.</td></tr>
  <tr><td> <b>Access to endpoint database</b> </td><td>Choose <b>Provide access information manually</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Enter the database server name on Amazon RDS.</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter <b>1433</b>.</td></tr>
  <tr><td> <b>Secure Socket Layer (SSL) mode</b> </td><td>Choose <b>none</b>.</td></tr>
  <tr><td> <b>User name</b> </td><td>Enter <b>dms_user</b>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Enter the password that you created for the <code>dms_user</code> user.</td></tr>
  <tr><td> <b>Database name</b> </td><td>Enter <b>AdventureWorks</b>.</td></tr>
</tbody>
</table>


1. Choose **Create endpoint**.

**Note**  
To migrate a Microsoft SQL Server Always On database, you need to use different configurations. For more information, see [Migrating a SQL Server Always On Database to Amazon Web Services](chap-manageddatabases.sqlserveralwayson.md).