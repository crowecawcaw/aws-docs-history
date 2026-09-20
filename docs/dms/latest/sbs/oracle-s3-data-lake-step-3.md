

# Step 3: Create an AWS DMS Source Endpoint
<a name="oracle-s3-data-lake-step-3"></a>

In this step, we configure a source endpoint. AWS DMS uses this endpoint to connect to the source database to read data as well as changes to the data via transaction logs. You can use Extra Connection Attributes for the source endpoint to configure how AWS DMS captures changes to the data.

After you configure the AWS Database Migration Service (AWS DMS) replication instance and the source RDS for Oracle instance, ensure connectivity between these two instances. To ensure that the replication instance can access the server and the port for the database, make changes to the relevant security groups and network access control lists. For more information about your network configuration, see [Setting up a network for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html).

 AWS DMS can stream the changes to the data from `REDO` logs using either Logminer or Binary reader protocols. You can choose this protocol when you create your source endpoint. For detailed comparison on which mode to pickup for CDC replication, see [Using Oracle LogMiner or Binary Reader for CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC).

Logminer option is easier to set up. However, since our source Oracle database workload involves ETL jobs that result in high volume of transactions, we choose Binary Reader since it offers better performance for ongoing replication.

After you completed the network configurations, you can create a source endpoint.

 **To create a source endpoint** 

1. Sign in to the AWS Management Console, and open the [AWS DMS console](https://console.aws.amazon.com/dms/v2).

1. Choose **Endpoints**, then choose **Create endpoint**.

1. On the **Create endpoint** page, enter the following information.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint type</b> </td><td>Choose <b>Source endpoint</b>, turn on <b>Select RDS DB instance</b>, and choose an RDS for Oracle instance that you created for this walkthrough.</td></tr>
  <tr><td> <b>Endpoint identifier</b> </td><td>Enter <code>datalake-source-db</code>.</td></tr>
  <tr><td> <b>Source engine</b> </td><td>Choose <b>Oracle</b>.</td></tr>
  <tr><td> <b>Access to endpoint database</b> </td><td>Choose <b>Provide access information manually</b>. Alternatively, you can choose to provide a secret from AWS Secrets Manager that includes connection details.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Enter the database server name on Amazon RDS.</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter <code>1521</code>.</td></tr>
  <tr><td> <b>Secure Socket Layer (SSL) mode</b> </td><td>Choose <b>none</b>.</td></tr>
  <tr><td> <b>User name</b> </td><td>Enter the name of the user that you created for your RDS for Oracle database.</td></tr>
  <tr><td> <b>Password</b> </td><td>Enter the password that you created for your Oracle DB user.</td></tr>
  <tr><td> <b>SID/Service name</b> </td><td>Enter <code>SH</code>.</td></tr>
  <tr><td> <b>Endpoint settings - Extra connection attributes</b> </td><td>Enter <code>useLogminerReader=N;useBfile=Y;</code>.</td></tr>
</tbody>
</table>


1. Choose **Create endpoint**.