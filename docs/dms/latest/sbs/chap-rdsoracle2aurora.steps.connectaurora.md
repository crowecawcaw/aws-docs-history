

# Step 4: Test the Connectivity to the Aurora MySQL DB Instance
<a name="chap-rdsoracle2aurora.steps.connectaurora"></a>

Next, test your connection to your Aurora MySQL DB instance.

1. In SQL Workbench/J, choose **File**, then choose **Connect window**. Choose the Create a new connection profile icon. using the following information: Connect to the Aurora MySQL DB instance in SQL Workbench/J by using the information as shown following:


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>New profile</b> name</td><td>Enter <code>RDSAuroraConnection</code>.</td></tr>
  <tr><td> <b>Driver</b> </td><td>Choose <code>MySQL (com.mysql.jdbc.Driver)</code>.</td></tr>
  <tr><td> <b>URL</b> </td><td>Use the <b>AuroraJDBCConnectionString</b> value you recorded when you examined the output details of the DMSdemo stack in a previous step.</td></tr>
  <tr><td> <b>Username</b> </td><td>Enter <code>auradmin</code>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Provide the password for the admin user that you assigned when creating the Aurora MySQL DB instance using the AWS CloudFormation template.</td></tr>
</tbody>
</table>


1. Test the connection by choosing **Test**. Choose **OK** to close the dialog box, then choose OK to create the connection profile.  
![Connecting to the Aurora MySQL DB instance](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora10.png)
**Note**  
If your connection is unsuccessful, ensure that the IP address you assigned when creating the AWS CloudFormation template is the one you are attempting to connect from. This is the most common issue when trying to connect to an instance.

1. Log on to the Aurora MySQL instance by using the master admin credentials.

1. Verify your connectivity to the Aurora MySQL DB instance by running a sample SQL command, such as `SHOW DATABASES;`.  
![Connecting to the Aurora MySQL DB instance](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora10.5.png)