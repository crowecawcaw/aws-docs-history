

# Step 8: Create AWS DMS Source and Target Endpoints
<a name="chap-rdsoracle2redshift.steps.createsourcetargetendpoints"></a>

While your replication instance is being created, you can specify the source and target database endpoints using the [AWS Management Console](https://console.aws.amazon.com/). However, you can only test connectivity after the replication instance has been created, because the replication instance is used in the connection.

1. Specify your connection information for the source Oracle database and the target Amazon Redshift database. The following table describes the source settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter <code>Orasource</code> (the Amazon RDS for Oracle endpoint).</td></tr>
  <tr><td> <b>Source Engine</b> </td><td>Choose <b>oracle</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Provide the Oracle DB instance name. This name is the <b>Server name</b> value that you used for AWS SCT, such as "abc123567.abc87654321.us-west-2.rds.amazonaws.com".</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter <code>1521</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose <b>None</b>.</td></tr>
  <tr><td> <b>Username</b> </td><td>Enter <code>oraadmin</code>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Enter <code>oraadmin123</code>.</td></tr>
  <tr><td> <b>SID</b> </td><td>Enter <code>ORCL</code>.</td></tr>
</tbody>
</table>


   The following table describes the target settings.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter <code>Redshifttarget</code> (the Amazon Redshift endpoint).</td></tr>
  <tr><td> <b>Target Engine</b> </td><td>Choose <b>redshift</b>.</td></tr>
  <tr><td> <b>Servername</b> </td><td>Provide the Amazon Redshift DB instance name. This name is the <b>Server name</b> value that you used for AWS SCT, such as <code>"oracletoredshiftdwusingdms-redshiftcluster-abc123567.abc87654321.us-west-2.redshift.amazonaws.com"</code>..</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter <code>5439</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose <b>None</b>.</td></tr>
  <tr><td> <b>Username</b> </td><td>Enter <code>redshiftadmin</code>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Enter <code>Redshift#123</code>.</td></tr>
  <tr><td> <b>Database name</b> </td><td>Enter <code>test</code>.</td></tr>
</tbody>
</table>


   The completed page should look like the following.  
![Advanced section](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2redshift19.5.png)

1. Wait for the status to say **Replication instance created successfully.**.

1. To test the source and target connections, choose **Run Test** for the source and target connections.

1. Choose **Next**.