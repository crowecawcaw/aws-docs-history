

# Step 5: Create an AWS DMS Replication Instance
<a name="chap-rdsoracle2postgresql.steps.createreplicationinstance"></a>

After validating the schema structure between source and target databases, continue with the core part of this walkthrough, which is the data migration. The following illustration shows a high-level view of the migration process.

![Migration process](https://docs.aws.amazon.com/dms/latest/sbs/images/datarep-conceptual2.png)


An AWS DMS replication instance performs the actual data migration between source and target. The replication instance also caches the transaction logs during the migration. How much CPU and memory capacity a replication instance has influences the overall time required for the migration.

1. Sign in to the AWS Management Console, and select AWS DMS at https://console.aws.amazon.com/dms/v2/. Next, choose **Create Migration**. If you are signed in as an AWS Identity and Access Management (IAM) user, then you must have the appropriate permissions to access AWS DMS. For more information about the permissions required, see [IAM Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions).

1. Choose **Next** to start a database migration from the console’s Welcome page.

1. On the **Create replication instance** page, specify your replication instance information.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Name</b> </td><td>Select a name for your replication instance. If you will be using multiple replication servers or sharing an account, then choose a name that will help you quickly differentiate between the different servers.</td></tr>
  <tr><td> <b>Description</b> </td><td>Enter a brief description.</td></tr>
  <tr><td> <b>Instance class</b> </td><td>Select the type of replication server to create. Each size and type of instance class will have increasing CPU, memory, and I/O capacity. Generally, the <code>t2</code> instances are for lower load tasks, and the <code>c4</code> instances are for higher load and more tasks.</td></tr>
  <tr><td> <b>VPC</b> </td><td>Choose the VPC in which your replication instance will be launched. If possible, select the same VPC in which either your source or target database resides (or both).</td></tr>
  <tr><td> <b>Multi-AZ</b> </td><td>When <b>Yes</b> is selected, AWS DMS creates a second replication server in a different Availability Zone for failover if there is a problem with the primary replication server.</td></tr>
  <tr><td> <b>Publicly accessible</b> </td><td>If either your source or target database resides outside of the VPC in which your replication server resides, then you must make your replication server policy publicly accessible.</td></tr>
</tbody>
</table>


1. For the **Advanced** section, specify the following information.


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Allocated storage (GB)</b> </td><td>Amount of storage on the replication server for the AWS DMS task logs, including historical tasks logs. AWS DMS also uses disk storage to cache certain data while it replicates it from the source to the target. Additionally, more storage generally enables better IOPS on the server.</td></tr>
  <tr><td> <b>Replication Subnet Group</b> </td><td>If you are running in a Multi-AZ configuration, then you will need at least two subnet groups.</td></tr>
  <tr><td> <b>Availability zone</b> </td><td>Generally, performance is better if you locate your primary replication server in the same Availability Zone as your target database.</td></tr>
  <tr><td> <b>VPC Security Group(s)</b> </td><td>Security groups enable you to control ingress and egress to your VPC. AWS DMS allows you to associate one or more security groups with the VPC in which your replication server is launched.</td></tr>
  <tr><td> <b> KMS key </b> </td><td>With AWS DMS, all data is encrypted at rest using a KMS encryption key. By default, AWS DMS will create a new encryption key for your replication server. However, you may choose to use an existing key.</td></tr>
</tbody>
</table>


   For information about the KMS key, see [Setting an Encryption Key and Specifying KMS Permissions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.EncryptionKey.html).

1. Click **Next**.