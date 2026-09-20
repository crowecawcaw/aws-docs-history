

# Step 7: Create an AWS DMS Replication Instance
<a name="chap-rdsoracle2aurora.steps.createreplicationinstance"></a>

After we validate the schema structure between source and target databases, as described preceding, we proceed to the core part of this walkthrough, which is the data migration. The following illustration shows a high-level view of the migration process.

![Migration process](https://docs.aws.amazon.com/dms/latest/sbs/images/datarep-conceptual2.png)


A DMS replication instance performs the actual data migration between source and target. The replication instance also caches the transaction logs during the migration. How much CPU and memory capacity a replication instance has influences the overall time required for the migration.

To create an AWS DMS replication instance, do the following:

1. Sign in to the AWS Management Console, select [AWS Database Migration Service](https://console.aws.amazon.com/dms/v2) (AWS DMS) and choose **Create replication instance**. If you are signed in as an AWS Identity and Access Management (IAM) user, you must have the appropriate permissions to access AWS DMS. For more information about the permissions required, see [IAM Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions).

1. On the **Create replication instance** page, specify your replication instance information as shown following.


<table>
<thead>
  <tr><th>For This Parameter</th><th>Do This</th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>Enter <code>DMSdemo-repserver</code>.</td></tr>
  <tr><td> <b>Descriptive Amazon Resource Name (ARN)</b> </td><td>Skip this optional field.</td></tr>
  <tr><td> <b>Description</b> </td><td>Enter a brief description, such as <code>DMS demo replication server</code>.</td></tr>
  <tr><td> <b>Instance class</b> </td><td>Choose <b>dms.t3.medium</b>. This instance class is large enough to migrate a small set of tables.</td></tr>
  <tr><td> <b>Engine version</b> </td><td>Choose <b>3.4.5</b>. This is the latest AWS DMS version, which includes all new features and enhancements.</td></tr>
  <tr><td> <b>Allocated storage (GiB)</b> </td><td>Choose <b>50</b>. This storage space is enough for your migration project.</td></tr>
  <tr><td> <b>VPC</b> </td><td>Choose <code>DMSDemoVPC</code>, which is the VPC that was created by the AWS CloudFormation stack.</td></tr>
  <tr><td> <b>Multi-AZ</b> </td><td>Choose <code>Dev or test workload (Single-AZ)</code>.</td></tr>
  <tr><td> <b>Publicly accessible</b> </td><td>Leave this item selected.</td></tr>
</tbody>
</table>


1. For the **Advanced**, **Maintenance**, and **Tags** sections, leave the default settings as they are, and choose **Create**.