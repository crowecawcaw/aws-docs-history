

# Step 7: Create an AWS DMS Replication Instance
<a name="chap-rdsoracle2redshift.steps.createreplicationinstance"></a>

After we validate the schema structure between source and target databases, as described preceding, we proceed to the core part of this walkthrough, which is the data migration. The following illustration shows a high-level view of the migration process.

![migration process](https://docs.aws.amazon.com/dms/latest/sbs/images/sbs-rdsor2redshift-Step7-DMSOverview.png)


A DMS replication instance performs the actual data migration between source and target. The replication instance also caches the transaction logs during the migration. How much CPU and memory capacity a replication instance has influences the overall time required for the migration.

To create an AWS DMS replication instance, do the following:

1. Sign in to the AWS Management Console, open the AWS DMS console at https://console.aws.amazon.com/dms/v2/, and choose **Create Migration**. If you are signed in as an AWS Identity and Access Management (IAM) user, you must have the appropriate permissions to access AWS DMS. For more information about the permissions required, see [IAM Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions).

1. Choose **Create migration** to start a database migration.

1. On the **Welcome** page, choose **Next**.

1. On the **Create replication instance** page, specify your replication instance information as shown following.


<table>
<thead>
  <tr><th>Parameter</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>Enter <code>DMSdemo-repserver</code>.</td></tr>
  <tr><td> <b>Description</b> </td><td>Enter a brief description, such as <code>DMS demo replication server</code>.</td></tr>
  <tr><td> <b>Instance class</b> </td><td>Choose <b>dms.t2.medium</b>. This instance class is large enough to migrate a small set of tables.</td></tr>
  <tr><td> <b>VPC</b> </td><td>Choose <code>OracletoRedshiftusingDMS</code>, which is the VPC that was created by the AWS CloudFormation stack.</td></tr>
  <tr><td> <b>Multi-AZ</b> </td><td>Choose <code>No</code>.</td></tr>
  <tr><td> <b>Publicly accessible</b> </td><td>Leave this item selected.</td></tr>
</tbody>
</table>


1. For the **Advanced** section, leave the default settings as they are, and choose **Next**.