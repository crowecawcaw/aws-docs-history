

# Step 8: Create AWS DMS Source and Target Endpoints
<a name="chap-rdsoracle2aurora.steps.createsourcetargetendpoints"></a>

While your replication instance is being created, you can specify the source and target database endpoints using the [AWS Management Console](https://console.aws.amazon.com/). However, you can only test connectivity after the replication instance has been created, because the replication instance is used in the connection.

1. Specify your connection information for the source Oracle database and the target Amazon Aurora MySQL database. The following table describes the source settings.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter <code>Orasource</code> (the Amazon RDS for Oracle endpoint).</td></tr>
  <tr><td> <b>Source Engine</b> </td><td>Choose <b>oracle</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Provide the Oracle DB instance name. This is the <b>Server name</b> you used for AWS SCT, such as "do1xa4grferti8y.cqiw4tcs0mg7.us-west-2.rds.amazonaws.com".</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter <code>1521</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose <b>None</b>.</td></tr>
  <tr><td> <b>Username</b> </td><td>Enter <code>oraadmin</code>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the Oracle DB instance.</td></tr>
  <tr><td> <b>SID</b> </td><td>Provide the Oracle database name.</td></tr>
</tbody>
</table>


   The following table describes the target settings.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Endpoint Identifier</b> </td><td>Enter <code>Aurtarget</code> (the Amazon Aurora MySQL endpoint).</td></tr>
  <tr><td> <b>Target Engine</b> </td><td>Choose <b>aurora</b>.</td></tr>
  <tr><td> <b>Servername</b> </td><td>Provide the Aurora MySQL DB instance name. This is the <b>Server name</b> you used for AWS SCT, such as "dmsdemo-auroracluster-1u1oyqny35jwv.cluster-cqiw4tcs0mg7.us-west-2.rds.amazonaws.com".</td></tr>
  <tr><td> <b>Port</b> </td><td>Enter <code>3306</code>.</td></tr>
  <tr><td> <b>SSL mode</b> </td><td>Choose <b>None</b>.</td></tr>
  <tr><td> <b>Username</b> </td><td>Enter <code>auradmin</code>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the Aurora MySQL DB instance.</td></tr>
</tbody>
</table>


   The completed page should look like the following:  
![Advanced section](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora19.5.png)

1. In order to disable foreign key checks during the initial data load, you must add the following commands to the target Aurora MySQL DB instance. In the **Advanced** section, shown following, type the following commands for **Extra connection attributes**: `initstmt=SET FOREIGN_KEY_CHECKS=0;autocommit=1` 

   The first command disables foreign key checks during a load, and the second command commits the transactions that DMS executes.  
![Advanced section](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora20.png)

1. Choose **Next**.