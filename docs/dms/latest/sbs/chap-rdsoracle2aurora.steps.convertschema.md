

# Step 5: Use the AWS Schema Conversion Tool to Convert the Oracle Schema to Aurora MySQL
<a name="chap-rdsoracle2aurora.steps.convertschema"></a>

Before you migrate data to Aurora MySQL, you convert the Oracle schema to an Aurora MySQL schema. [This video covers all the steps of this process](https://youtu.be/ClAJUNa1Ucc).

To convert an Oracle schema to an Aurora MySQL schema using AWS Schema Conversion Tool (AWS SCT), do the following:

1. Launch AWS SCT. In AWS SCT, choose **File**, then choose **New Project**. Create a new project named `DMSDemoProject`, specify the **Location** of the project folder, and then choose **OK**.

1. Choose **Add source** to add a source Oracle database to your project, then choose **Oracle**, and choose **Next**.

1. Enter the following information, and then choose **Test Connection**.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Connection name</b> </td><td>Enter <code> Amazon RDS for Oracle</code>. AWS SCT displays this name in the tree in the left panel.</td></tr>
  <tr><td> <b>Type</b> </td><td>Choose <b>SID</b>.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Use the <b>OracleJDBCConnectionString</b> value you used to connect to the Oracle DB instance, but remove the JDBC prefix information. For example, a sample connection string you use with SQL Workbench/J might be "jdbc:oracle:thin:@do1xa4grferti8y.cqiw4tcs0mg7.us-west-2.rds.amazonaws.com:1521:ORCL". For AWS SCT <b>Server name</b>, you remove "jdbc:oracle:thin:@//" and ":1521" to use just the server name: "do1xa4grferti8y.cqiw4tcs0mg7.us-west-2.rds.amazonaws.com"</td></tr>
  <tr><td> <b>Server port</b> </td><td>Enter <code>1521</code>.</td></tr>
  <tr><td> <b>Oracle SID</b> </td><td>Enter <code>ORCL</code>.</td></tr>
  <tr><td> <b>User name</b> </td><td>Enter <code>oraadmin</code>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Enter the password for the admin user that you assigned when creating the Oracle DB instance using the AWS CloudFormation template.</td></tr>
</tbody>
</table>
  
![Connecting to an Amazon RDS for Oracle DB instance](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora11.png)

1. Choose **OK** to close the alert box, then choose **Connect** to close the dialog box and to connect to the Oracle DB instance.

1. Choose **Add target** to add a target Amazon Aurora MySQL database to your project, then choose **Amazon Aurora (MySQL compatible)**, and choose **Next**.

1. Enter the following information and then choose **Test Connection**.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Connection name</b> </td><td>Enter <code>Aurora MySQL</code>. AWS SCT displays this name in the tree in the right panel.</td></tr>
  <tr><td> <b>Server name</b> </td><td>Use the <b>AuroraJDBCConnectionString</b> value you used to connect to the Aurora MySQL DB instance, but remove the JDBC prefix information and the port suffix. For example, a sample connection string you use with SQL Workbench/J might be "jdbc:mysql://dmsdemo-auroracluster-1u1ogdfg35v.cluster-cqiw4tcs0mg7.us-west-2.rds.amazonaws.com:3306". For AWS SCT <b>Server name</b>, you remove "jdbc:mysql://" and ":3306" to use just the server name: "dmsdemo-auroracluster-1u1ogdfg35v.cluster-cqiw4tcs0mg7.us-west-2.rds.amazonaws.com"</td></tr>
  <tr><td> <b>Server port</b> </td><td>Enter <code>3306</code>.</td></tr>
  <tr><td> <b>User name</b> </td><td>Enter <code>auradmin</code>.</td></tr>
  <tr><td> <b>Password</b> </td><td>Enter the password for the admin user that you assigned when creating the Oracle DB instance using the AWS CloudFormation template.</td></tr>
</tbody>
</table>


1. Choose **OK** to close the alert box, then choose **Connect** to connect to the Amazon Aurora MySQL DB instance.

1. In the tree in the left panel, select only the **HR** schema. In the tree in the right panel, select your target Aurora MySQL database. Choose **Create mapping**.  
![Creating a mapping rule](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora12.7.png)

1. Choose **Main view**. In the tree in the left panel, right-click the **HR** schema and choose **Create report**.

1. Check the report and the action items it suggests. The report discusses the type of objects that can be converted by using AWS SCT, along with potential migration issues and actions to resolve these issues. For this walkthrough, you should see something like the following:  
![Database migration report](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2aurora13.png)

   You can optionally save the report as .csv or .pdf format for later analysis.

1. Choose **Action Items**, and review any recommendations that you see.

1. In the tree in the left panel, right-click the **HR** schema and then choose **Convert schema**.

1. Choose **Yes** for the confirmation message. AWS SCT then converts your schema to the target database format.

1. In the tree in the right panel, choose the converted **hr** schema, and then choose **Apply to database** to apply the schema scripts to the target Aurora MySQL instance.

1. Choose the **hr** schema, and then choose **Refresh from Database** to refresh from the target database.

The database schema has now been converted and imported from source to target.